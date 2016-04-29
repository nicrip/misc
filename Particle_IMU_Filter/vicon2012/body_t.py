"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

import cStringIO as StringIO
import struct

class body_t(object):
    __slots__ = ["utime", "pos", "orientation"]

    def __init__(self):
        self.utime = 0
        self.pos = [ 0.0 for dim0 in range(3) ]
        self.orientation = [ 0.0 for dim0 in range(4) ]

    def encode(self):
        buf = StringIO.StringIO()
        buf.write(body_t._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">q", self.utime))
        buf.write(struct.pack('>3d', *self.pos[:3]))
        buf.write(struct.pack('>4d', *self.orientation[:4]))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = StringIO.StringIO(data)
        if buf.read(8) != body_t._get_packed_fingerprint():
            raise ValueError("Decode error")
        return body_t._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = body_t()
        self.utime = struct.unpack(">q", buf.read(8))[0]
        self.pos = struct.unpack('>3d', buf.read(24))
        self.orientation = struct.unpack('>4d', buf.read(32))
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if body_t in parents: return 0
        tmphash = (0xf77fdd2b875cd533) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if body_t._packed_fingerprint is None:
            body_t._packed_fingerprint = struct.pack(">Q", body_t._get_hash_recursive([]))
        return body_t._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

