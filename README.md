# Highfinesse wavemeter network server

This comes from an older codebase but may well work with current libraries and
wavemeters. The modules paths may need some adjustment.

It provides:

* Wavemeter API shim for Python using ctypes
* a RPC and PUB-SUB network interface (ZMQ through aiozmq) to pretty much all
the wavemeter functionality
* a generic subscription client for the PUB-SUB protocol
* a UDP logger for influxdb

## Alternatives

* For the proprietary Highfinesse TCP server (unlikely to be released), but with very limited API and no support for pub-sub: https://github.com/quartiq/highfinesse-net/
* Some integration into ARTIQ, smaller API coverage: https://github.com/dnadlinger/highfinesse-lsa-server
* Modern web based frontend: https://github.com/galwiner/WLMpage
* With labrad: https://github.com/nelsond/hfwlm and https://github.com/nelsond/labrad-hfwavemeter-server
* In some Uni-Ulm code: https://github.com/Ulm-IQO/qudi/blob/master/hardware/high_finesse_wavemeter.py
