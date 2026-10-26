#!/usr/bin/env python3
"""Ayuda a mantener la traducción cuando sale una versión nueva del juego.

Exportar lo que falta (claves nuevas o cuyo texto inglés ha cambiado):
    python tools/pendientes.py exportar ruta/al/en/Game.locres pendientes.json

    -> pendientes.json = { "ns/clave": "texto en inglés", ... }
       (las claves que comparten el mismo texto se agrupan con " | ")

Traduce los valores (respetando {variables}, <etiquetas> y saltos de línea) y luego:
    python tools/pendientes.py importar ruta/al/en/Game.locres pendientes.json
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from locres import read  # noqa: E402
from validar import problems  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ES = os.path.join(ROOT, "traduccion", "es.json")


def load_en(path):
    en = read(path)
    out = {}
    for _, ns, keys in en["namespaces"]:
        for _, key, sh, idx in keys:
            out[(ns or "_", key)] = (sh, en["strings"][idx][0])
    return out


def exportar(en_path, out_path):
    en = load_en(en_path)
    tr = json.load(open(ES, encoding="utf-8"))
    groups = {}
    for (ns, key), (sh, src) in en.items():
        e = tr.get(ns, {}).get(key)
        if e is None or e["h"] != sh:
            if any(c.isalpha() for c in src):
                groups.setdefault(src, []).append(f"{ns}/{key}")
    data = {" | ".join(ks): src for src, ks in groups.items()}
    json.dump(data, open(out_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"{len(data)} textos pendientes ({sum(len(k) for k in groups.values())} claves) -> {out_path}")


def importar(en_path, in_path):
    en = load_en(en_path)
    tr = json.load(open(ES, encoding="utf-8"))
    data = json.load(open(in_path, encoding="utf-8"))
    ok = bad = 0
    for ks, t in data.items():
        for k in ks.split(" | "):
            ns, key = k.split("/", 1)
            sh, src = en[(ns, key)]
            if t == src:
                continue
            p = problems(src, t)
            if p:
                print("RECHAZADA", k, p); bad += 1; continue
            tr.setdefault(ns, {})[key] = {"h": sh, "es": t}
            ok += 1
    json.dump(tr, open(ES, "w", encoding="utf-8"), ensure_ascii=False, indent=1, sort_keys=True)
    print(f"Importadas {ok} claves, rechazadas {bad}")


if __name__ == "__main__":
    if len(sys.argv) != 4 or sys.argv[1] not in ("exportar", "importar"):
        sys.exit(__doc__)
    (exportar if sys.argv[1] == "exportar" else importar)(sys.argv[2], sys.argv[3])
