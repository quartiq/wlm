# -*- coding: utf-8 -*-
# Copyright (c) 2015-2020 Robert Jördens <rj@quartiq.de>. All rights reserved.
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import print_function, unicode_literals

import logging
import asyncio
import time

from aiozmq import rpc
import docopt

import wlm_constants

logger = logging.getLogger(__name__)


__doc__ = """
Highfinesse Wavelength Meter WS* logger

Usage:
    wlm_log <host> <interval> <dbhost> <dbport> <name>
"""


@asyncio.coroutine
def log(idb, host, dt, name):
    dev = yield from rpc.connect_rpc(connect="tcp://%s:6881" % host)
    keys = yield from dev.call.keys()
    logger.info("have: %s", [wlm_constants.cmi_rev.get(k, k) for k in keys])
    keys = "Pressure Temperature".split()
    keys += ["Wavelength%i" % i for i in range(1, 9)]
    while True:
        dati = yield from dev.call.get_many(keys)
        t0 = time.time()
        dat = {k.lower(): d for k, (t, m, i, d) in dati.items()
               if d >= 0 and t > t0 - dt}
        if dat:
            logger.info("%s", dat)
            idb.write_row(name, **dat)
        yield from asyncio.sleep(dt)


if __name__ == "__main__":
    logging.basicConfig(level=logging.WARNING)
    args = docopt.docopt(__doc__)

    loop = asyncio.get_event_loop()
    from qc import influxdb
    idb = influxdb.InfluxdbUDP(args["<dbhost>"], int(args["<dbport>"]))
    loop.run_until_complete(log(idb, args["<host>"],
                                float(args["<interval>"]), args["<name>"]))
