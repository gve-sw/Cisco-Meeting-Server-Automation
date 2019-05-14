import socket
import struct

from et.codecs import encode


def phone_home(host, port, data, format=2):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    e_data = encode(data, format)
    return s.sendto(e_data, (host, port))


if __name__ == "__main__":      # pragma: no cover
    import sys

    def _local_ip():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 53))
        return s.getsockname()[0]

    host, port = "", 2233

    data_objs = [
        "",

        {
            "test": "data"
        },

        {
            "local_ip": _local_ip(),
            "sys.platform": sys.platform,
            "sys.version_info": list(sys.version_info),
            "version": "1.2.3rc4",
        },
    ]


    for data in data_objs:
        for format in (1, 2):
            phone_home(host, port, format=format, data=data)
