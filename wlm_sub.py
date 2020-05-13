# -*- coding: utf-8 -*-
# Copyright (c) 2015-2020 Robert Jördens <rj@quartiq.de>. All rights reserved.
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import print_function, unicode_literals

import logging
import asyncio

from aiozmq import rpc
import docopt

logger = logging.getLogger(__name__)


__doc__ = """
Highfinesse Wavelength Meter WS* subscriber

Usage:
    wlm_sub <host>
"""


@asyncio.coroutine
def log(host):
    class Sub(rpc.AttrHandler):
        @rpc.method
        def update(self, mode, data):
            logger.info((mode, data))
    sub = Sub()
    yield from rpc.serve_pubsub(sub, subscribe="",  # any
                                connect="tcp://%s:6882" % host)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    args = docopt.docopt(__doc__)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(log(args["<host>"]))
    loop.run_forever()
