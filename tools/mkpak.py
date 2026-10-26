"""Crea un .pak de UE4 (versión 8, sin compresión ni cifrado) con un único archivo.

Uso: python tools/mkpak.py archivo ruta/dentro/del/pak salida.pak
"""
import struct, hashlib, sys

def fstr(s):
    b = (s + "\0").encode("ascii")
    return struct.pack("<i", len(b)) + b

def entry(offset, data):
    return (struct.pack("<qqqI", offset, len(data), len(data), 0)
            + hashlib.sha1(data).digest()
            + struct.pack("<BI", 0, 0))

def build(src, internal, out, mount="../../../"):
    data = open(src, "rb").read()
    hdr = entry(0, data)
    blob = hdr + data
    index = fstr(mount) + struct.pack("<i", 1) + fstr(internal) + entry(0, data)
    footer = (bytes(16) + b"\0" + struct.pack("<Ii", 0x5A6F12E1, 8)
              + struct.pack("<qq", len(blob), len(index))
              + hashlib.sha1(index).digest() + bytes(32 * 5))
    open(out, "wb").write(blob + index + footer)

def check(path):
    d = open(path, "rb").read()
    f = d[-221:]
    magic, ver = struct.unpack_from("<Ii", f, 17)
    off, size = struct.unpack_from("<qq", f, 25)
    idx = d[off:off + size]
    assert magic == 0x5A6F12E1 and ver == 8
    assert hashlib.sha1(idx).digest() == f[41:61]
    o = 0
    n = struct.unpack_from("<i", idx, o)[0]; o += 4
    mount = idx[o:o + n - 1].decode(); o += n
    cnt = struct.unpack_from("<i", idx, o)[0]; o += 4
    n = struct.unpack_from("<i", idx, o)[0]; o += 4
    name = idx[o:o + n - 1].decode(); o += n
    eo, es, eu, cm = struct.unpack_from("<qqqI", idx, o); o += 28
    h = idx[o:o + 20]
    data = d[eo + 53: eo + 53 + es]
    assert hashlib.sha1(data).digest() == h and es == eu and cm == 0
    return mount, cnt, name, es

if __name__ == "__main__":
    build(sys.argv[1], sys.argv[2], sys.argv[3])
    print(check(sys.argv[3]))
