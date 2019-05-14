import logging
import json
import struct
import zlib

codecs = {
    1: {
        "description": "JSON codec",
        "encoder": lambda d: json.dumps(d).encode("UTF-8"),
        "decoder": lambda p: json.loads(p.decode("UTF-8")),
    },
    2: {
        "description": "zlib-compressed JSON codec",
        "encoder": lambda d: zlib.compress(json.dumps(d).encode("UTF-8")),
        "decoder": lambda p: json.loads(zlib.decompress(p).decode("UTF-8")),
    },
}

_logger = logging.getLogger(__name__)

sfmt = "!H"
sfmt_sz = struct.calcsize(sfmt)


def encode(data, format):
    encoder = codecs[format]["encoder"]
    e_format = struct.pack(sfmt, format)
    e_data = encoder(data)
    payload = e_format + e_data
    return payload


def decode(payload):
    e_format, e_data = payload[0:sfmt_sz], payload[sfmt_sz:]
    format = struct.unpack(sfmt, e_format)[0]
    decoder = codecs[format]["decoder"]
    return decoder(e_data), format
