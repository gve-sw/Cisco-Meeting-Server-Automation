#!/usr/bin/env python

import logging
import socket

from et.codecs import decode


bufsize = 16384
_logger = logging.getLogger(__name__)


def listen(host, port, handler):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))
    _logger.info("Listening on {h}:{p}".format(
        h="localhost" if host == "" else host,
        p=port))

    while True:
        payload, addr = s.recvfrom(bufsize)
        assert len(payload) < bufsize, "May have exceeded buffer size"
        data, format = decode(payload)
        _logger.info("Received {n} bytes from {addr} in format {f}".format(
            n=len(payload), addr=addr, f=format))
        handler(data, addr)


if __name__ == "__main__":      #  pragma: no cover
    logging.basicConfig(level=logging.INFO)

    def handler(data, addr):
        print(data)

    listen("", 2233, handler)
