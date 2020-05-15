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

* If the proprietary Highfinesse TCP server is being used, but with limited API and no support for pub-sub: https://github.com/quartiq/highfinesse-net/
* Some integration into ARTIQ, smaller API coverage: https://github.com/dnadlinger/highfinesse-lsa-server
