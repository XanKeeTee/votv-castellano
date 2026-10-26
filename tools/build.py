#!/usr/bin/env python3
"""Genera el Game.locres en castellano y el .pak listo para instalar.

Uso:
    python tools/build.py ruta/al/en/Game.locres

Necesitas el Game.locres INGLÉS de tu versión del juego (se extrae con FModel de
VotV/Content/Localization/Game/en/Game.locres). Este repositorio no incluye los
textos originales del juego, solo la traducción.

Salida:
    dist/Game.locres                       (locres español)
    dist/VotV-WindowsNoEditor_ES_P.pak     (pak para Content/Paks)
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from locres import read, write  # noqa: E402
from mkpak import build as build_pak, check as check_pak  # noqa: E402
from validar import problems  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAK_PATH = "VotV/Content/Localization/Game/es/Game.locres"


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    en = read(sys.argv[1])
    tr = json.load(open(os.path.join(ROOT, "traduccion", "es.json"), encoding="utf-8"))

    strings, index = [], {}
    def intern(s):
        if s not in index:
            index[s] = len(strings)
            strings.append([s, 0])
        return index[s]

    stats = {"traducidas": 0, "sin_traducir": 0, "desactualizadas": 0, "con_errores": 0}
    avisos = []
    namespaces = []
    for nh, ns, keys in en["namespaces"]:
        table = tr.get(ns or "_", {})
        nkeys = []
        for kh, key, sh, idx in keys:
            src = en["strings"][idx][0]
            t = src
            e = table.get(key)
            if e is None:
                stats["sin_traducir"] += 1
            elif e["h"] != sh:
                stats["desactualizadas"] += 1
                avisos.append(("texto original cambiado", ns, key, src))
            elif problems(src, e["es"]):
                stats["con_errores"] += 1
                avisos.append(("variables/saltos no coinciden", ns, key, src))
            else:
                t = e["es"]
                stats["traducidas"] += 1
            j = intern(t)
            strings[j][1] += 1
            nkeys.append([kh, key, sh, j])
        namespaces.append([nh, ns, nkeys])

    os.makedirs(os.path.join(ROOT, "dist"), exist_ok=True)
    loc = os.path.join(ROOT, "dist", "Game.locres")
    pak = os.path.join(ROOT, "dist", "VotV-WindowsNoEditor_ES_P.pak")
    write(loc, {"entries": en["entries"], "namespaces": namespaces, "strings": strings})
    build_pak(loc, PAK_PATH, pak)
    check_pak(pak)

    print("Claves:", sum(len(n[2]) for n in namespaces))
    for k, v in stats.items():
        print(f"  {k}: {v}")
    if avisos:
        with open(os.path.join(ROOT, "dist", "avisos.txt"), "w", encoding="utf-8") as f:
            for a in avisos:
                f.write(f"[{a[0]}] {a[1] or '_'}/{a[2]}: {a[3]!r}\n")
        print(f"  -> {len(avisos)} avisos en dist/avisos.txt (se dejan en inglés)")
    print("Listo:", pak)


if __name__ == "__main__":
    main()
