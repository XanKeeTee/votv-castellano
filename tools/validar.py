"""Comprobaciones de seguridad: variables, etiquetas, saltos de línea y comandos.

Uso: python tools/validar.py original.json traduccion.json
"""
import json, re, sys

PH = re.compile(r"\{[^}]*\}|%[sdif]|<[^>]*>|\[\d+\]")
CMD = re.compile(r"\b(?:sv|sd|tr|cl|sm|dr|kf)\.\w+")

def problems(o, t):
    p = []
    if sorted(PH.findall(o)) != sorted(PH.findall(t)): p.append("etiquetas/variables")
    if o.count("\r\n") != t.count("\r\n") or o.count("\n") != t.count("\n"): p.append("saltos de línea")
    lw = lambda s: s[:len(s) - len(s.lstrip())]
    tw = lambda s: s[len(s.rstrip()):]
    if lw(o) != lw(t) or tw(o) != tw(t): p.append("espacios inicio/fin")
    for c in CMD.findall(o):
        if c not in t: p.append("comando " + c)
    if t.strip() == "" and o.strip() != "": p.append("vacía")
    return p

if __name__ == "__main__":
    src = json.load(open(sys.argv[1], encoding="utf-8"))
    out = json.load(open(sys.argv[2], encoding="utf-8"))
    bad = 0
    for k, o in src.items():
        if k not in out:
            print(k, "FALTA"); bad += 1; continue
        p = problems(o, out[k])
        if p: print(k, p); bad += 1
    extra = set(out) - set(src)
    if extra: print("claves sobrantes:", sorted(extra)[:10])
    print("total", len(src), "problemas", bad)
