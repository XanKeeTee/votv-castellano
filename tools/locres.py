"""Lector/escritor mínimo de .locres de UE4 (versión 3, Optimized_CityHash64_UTF16)."""
import struct, sys, json

MAGIC = bytes.fromhex("0e147475674a03fc4a15909dc3377f1b")


def rstr(d, o):
    n = struct.unpack_from("<i", d, o)[0]; o += 4
    if n == 0:
        return "", o
    if n < 0:
        n = -n
        s = d[o:o + 2 * n].decode("utf-16-le"); o += 2 * n
    else:
        s = d[o:o + n].decode("latin-1"); o += n
    return s[:-1] if s.endswith("\0") else s, o


def wstr(s):
    if s == "":
        return struct.pack("<i", 0)
    try:
        b = (s + "\0").encode("ascii")
        return struct.pack("<i", len(b)) + b
    except UnicodeEncodeError:
        b = (s + "\0").encode("utf-16-le")
        return struct.pack("<i", -(len(b) // 2)) + b


def read(path):
    d = open(path, "rb").read()
    assert d[:16] == MAGIC
    ver = d[16]; assert ver == 3, ver
    stroff, = struct.unpack_from("<q", d, 17)
    o = 25
    entries, nns = struct.unpack_from("<ii", d, o); o += 8
    # tabla de cadenas
    so = stroff
    nstr, = struct.unpack_from("<i", d, so); so += 4
    strings = []
    for _ in range(nstr):
        s, so = rstr(d, so)
        rc, = struct.unpack_from("<i", d, so); so += 4
        strings.append([s, rc])
    nss = []
    for _ in range(nns):
        nh, = struct.unpack_from("<I", d, o); o += 4
        ns, o = rstr(d, o)
        nk, = struct.unpack_from("<i", d, o); o += 4
        keys = []
        for _ in range(nk):
            kh, = struct.unpack_from("<I", d, o); o += 4
            k, o = rstr(d, o)
            sh, idx = struct.unpack_from("<Ii", d, o); o += 8
            keys.append([kh, k, sh, idx])
        nss.append([nh, ns, keys])
    return {"entries": entries, "namespaces": nss, "strings": strings}


def write(path, data):
    body = bytearray()
    body += struct.pack("<ii", data["entries"], len(data["namespaces"]))
    for nh, ns, keys in data["namespaces"]:
        body += struct.pack("<I", nh) + wstr(ns) + struct.pack("<i", len(keys))
        for kh, k, sh, idx in keys:
            body += struct.pack("<I", kh) + wstr(k) + struct.pack("<Ii", sh, idx)
    stroff = 16 + 1 + 8 + len(body)
    tail = bytearray(struct.pack("<i", len(data["strings"])))
    for s, rc in data["strings"]:
        tail += wstr(s) + struct.pack("<i", rc)
    out = MAGIC + bytes([3]) + struct.pack("<q", stroff) + bytes(body) + bytes(tail)
    open(path, "wb").write(out)


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "dump":
        data = read(sys.argv[2])
        json.dump(data, open(sys.argv[3], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    elif cmd == "build":
        data = json.load(open(sys.argv[2], encoding="utf-8"))
        write(sys.argv[3], data)
