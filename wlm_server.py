# -*- coding: utf-8 -*-
# Copyright (c) 2015-2020 Robert Jördens <rj@quartiq.de>. All rights reserved.
# SPDX-License-Identifier: GPL-3.0-or-later

import logging
import time

import asyncio
import zmq
from aiozmq import rpc

import wlm

logger = logging.getLogger(__name__)


class Wlm(rpc.AttrHandler):
    def __init__(self, pub, loop=None):
        self.status = {}
        if loop is None:
            loop = asyncio.get_event_loop()
        self.loop = loop
        self.pub = pub

    def cb(self, mode, i, d):
        data = time.time(), mode, i, d
        try:
            mode = wlm.cmi_rev[mode][0]
        except KeyError:
            pass
        logger.debug("%s %s", mode, data)
        self.status[mode] = data
        self.loop.call_soon_threadsafe(
            asyncio.async, self.pub.publish(str(mode)).update(mode, data))

    @rpc.method
    def get(self, mode):
        return self.status[mode]

    @rpc.method
    def get_many(self, modes):
        return {mode: self.status[mode] for mode in modes
                if mode in self.status}

    @rpc.method
    def keys(self):
        return list(self.status.keys())

    @rpc.method
    def all(self):
        return self.status


@asyncio.coroutine
def go():
    pub = yield from rpc.connect_pubsub(bind="tcp://*:6882")
    pub.transport.setsockopt(zmq.SNDHWM, 128)
    w = Wlm(pub=pub)
    serv = yield from rpc.serve_rpc(w, bind="tcp://*:6881")
    serv.transport.setsockopt(zmq.SNDHWM, 128)
    w.cbc = wlm.CallbackProc(w.cb)  # keep from being gc-ed
    if wlm.lib.Instantiate(wlm.cInstCheckForWLM, 1, 0, 0):
        wlm.lib.Instantiate(wlm.cInstNotification, wlm.cNotifyInstallCallback,
                            w.cbc, 0)
    logger.info("listening")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(go())
    loop.run_forever()
