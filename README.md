<div align="center">

# 📡 Voices of the Void — Traducción al castellano

**Traducción completa al castellano de España de _Voices of the Void_**
Menús, ajustes, tienda, objetos, correos del Dr. Bao, notas, tutorial y ayuda.

![Versión del juego](https://img.shields.io/badge/VotV-Alpha%200.9.0n-8b0000?style=flat-square)
![Idioma](https://img.shields.io/badge/idioma-castellano%20(España)-c60b1e?style=flat-square)
![Textos](https://img.shields.io/badge/textos-19.263%20claves-2b7a0b?style=flat-square)
![Licencia](https://img.shields.io/badge/herramientas-MIT-blue?style=flat-square)

</div>

---

## ✨ Qué es esto

_Voices of the Void_ trae una opción de español, pero apenas cubre unas 350 frases, en español latino y con fallos. Todo lo demás sale en inglés, menú principal incluido.

Este mod sustituye ese archivo de idioma por una **traducción completa al castellano de España**:

| | |
|---|---|
| 🗂️ **Textos del juego** | 19.263 claves (5.807 frases distintas) |
| 🇪🇸 **Variante** | Castellano de España: *patata*, *gambas*, *ordenador*, *pulsa*… |
| 🧑‍🔬 **Tono** | Interfaz clara, Bao burocrático y borde, notas inquietantes, humor intacto |
| 🛡️ **Seguridad** | Todas las variables `{a}`, etiquetas de color, iconos y comandos de terminal comprobados automáticamente |
| ♻️ **Reversible** | Es un único archivo `.pak`: lo borras y el juego vuelve a estar como antes |

---

## 📥 Instalación

1. Descarga **[`VotV-WindowsNoEditor_ES_P.pak`](dist/VotV-WindowsNoEditor_ES_P.pak)** (o desde la pestaña *Releases*).
2. Cópialo en la carpeta `Paks` del juego, **junto al pak grande** (no lo sustituyas):
   ```
   WindowsNoEditor\VotV\Content\Paks\VotV-WindowsNoEditor_ES_P.pak
   ```
3. Abre el juego → **Settings** → **Language** → elige **17. Spagnola**.
4. Si el menú sigue en inglés, cierra el juego del todo y vuelve a abrirlo.

> 💡 El idioma se guarda en `%LOCALAPPDATA%\VotV\Saved\Config\WindowsNoEditor\GameUserSettings.ini` como `Language=es`.

### Desinstalar

Borra `VotV-WindowsNoEditor_ES_P.pak` de la carpeta `Paks`. Ya está.

### Compatibilidad

- Probado en **Alpha 0.9.0 (build a090n)**.
- Funciona junto a mods de UE4SS y LogicMods, porque solo sustituye el archivo de idioma.
- En otras versiones del juego puede funcionar a medias: los textos nuevos o cambiados saldrán en inglés. Mira [Actualizar a una versión nueva](#-actualizar-a-una-versión-nueva-del-juego).

---

## 🧭 Criterios de traducción

La guía completa está en **[`docs/GLOSARIO.md`](docs/GLOSARIO.md)**. Lo principal:

- **Castellano de España** y **tuteo** en toda la interfaz. El Dr. Bao también tutea a Kel, con su tono de jefe impaciente.
- **Términos técnicos fijos:** *disco de datos* (drive), *acimut / elevación*, *código hash*, *nivel de procesamiento*, *rack de servidores*, *campo solar*, *quad* (ATV)…
- **No se traduce:** nombres propios (Dr. Bao, Dr. Kel, Ariral, Kerfur, Rozital…), antenas con alfabeto OTAN (Romeo, Sierra, Tango…) ni comandos de terminal (`sv.ping`, `sd.calall`, `sv.target`…).
- **Se recrean las erratas y gritos intencionados** del original, igual que los chistes y tacos, adaptados al humor de aquí.

### Lo que se queda en inglés a propósito

Textos en latín, la nota en alemán, el idioma alienígena, los textos corruptos con mensajes ocultos, nombres de emisoras de radio, nombres de archivo y códigos internos (`channel_00`, `data_block_999`…).

---

## 🛠️ Para desarrolladores

### Estructura

```
votv-castellano/
├── dist/
│   ├── VotV-WindowsNoEditor_ES_P.pak   ← mod listo para instalar
│   └── Game.locres                     ← archivo de idioma suelto
├── traduccion/
│   └── es.json                         ← LA traducción (editable)
├── tools/
│   ├── build.py        ← genera locres + pak desde es.json
│   ├── pendientes.py   ← exporta/importa textos nuevos al actualizar el juego
│   ├── validar.py      ← comprueba variables, etiquetas y saltos de línea
│   ├── locres.py       ← lector/escritor de .locres (UE4, versión 3)
│   └── mkpak.py        ← empaquetador .pak mínimo (UE4, versión 8)
└── docs/
    └── GLOSARIO.md     ← guía de estilo y glosario
```

### Formato de `traduccion/es.json`

```json
{
  "_": {
    "161F6B204C6753DC7863C38AE18DFC17": {
      "h": 880654254,
      "es": "Paquete de gambas vacío"
    }
  }
}
```

- El primer nivel es el *namespace* de Unreal (`_` = namespace vacío).
- La clave es el identificador del texto en el juego.
- `h` es el hash del texto **inglés** original. Sirve para detectar si el desarrollador ha cambiado ese texto en una versión nueva.
- `es` es la traducción.

Al ir por clave y no por frase, una misma palabra inglesa puede tener traducciones distintas según dónde aparezca.

### Requisitos

- **Python 3.8+** (sin dependencias externas).
- **[FModel](https://fmodel.app/)**, para extraer el `Game.locres` inglés de tu juego. Este repositorio **no incluye archivos originales del juego**.

### Generar el mod

1. En FModel, abre `VotV\Content\Paks` (motor *UE4.27*) y exporta en bruto:
   `VotV/Content/Localization/Game/en/Game.locres`
2. Ejecuta:
   ```bash
   python tools/build.py ruta/al/en/Game.locres
   ```
3. El resultado se guarda en `dist/`. Si hay textos con problemas, se dejan en inglés y se listan en `dist/avisos.txt`.

### 🔄 Actualizar a una versión nueva del juego

```bash
# 1. Exporta los textos nuevos o cambiados
python tools/pendientes.py exportar ruta/al/en/Game.locres pendientes.json

# 2. Traduce los valores de pendientes.json (respeta {variables}, <etiquetas> y saltos de línea)

# 3. Impórtalos (se validan automáticamente)
python tools/pendientes.py importar ruta/al/en/Game.locres pendientes.json

# 4. Regenera el mod
python tools/build.py ruta/al/en/Game.locres
```

### Cómo funciona por dentro

- El juego guarda los textos en `Content/Localization/Game/<idioma>/Game.locres`, dentro del pak principal.
- Unreal carga con **prioridad los paks cuyo nombre termina en `_P`**. Este mod es un pak pequeño (versión 8, sin compresión) con un único archivo: `VotV/Content/Localization/Game/es/Game.locres`, montado en `../../../`. El juego lo usa en lugar del suyo para el idioma `es`.
- `build.py` parte de la tabla de claves del locres inglés, pone la traducción de cada clave y deduplica las cadenas. Cualquier texto que no pase `validar.py` se queda en inglés para no romper nada en el juego.

---

## 🙏 Créditos

- **_Voices of the Void_**: MrDrNose y su equipo. Todo el contenido del juego es suyo.
- Parte de los textos parten de la **traducción al español de la comunidad** que ya venía en el juego, revisada y adaptada al castellano.
- **[FModel](https://github.com/4sval/FModel)**, para extraer los archivos del juego.

## ⚖️ Aviso

Traducción **no oficial** hecha por fans y sin ánimo de lucro. No tiene relación con los desarrolladores del juego ni está respaldada por ellos. No incluye archivos del juego: para usar este mod necesitas tu propia copia de _Voices of the Void_. Si los desarrolladores lo piden, se retirará.

Las herramientas de `tools/` se publican bajo licencia [MIT](LICENSE).
