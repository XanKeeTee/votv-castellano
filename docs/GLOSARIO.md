# Guía de estilo y glosario

Criterios que sigue toda la traducción. Si vas a corregir o añadir textos, síguelos para que todo suene igual.

## Variante
Castellano de ESPAÑA. Nada de latinismos: patata (no papa), gambas (no camarones), cubo (no cubeta), fregona, depósito (no tanque), ordenador, móvil, coche, conducir, vale, guay, tío, gilipollas, coger, pulsar (no presionar), tele, frigorífico/nevera, zumo, melocotón, judías, bocadillo, taza de váter/inodoro, grifo, gafas, chaqueta, ratón, tirar (basura).
Tutea SIEMPRE al jugador en interfaz/ayuda/tutorial ("Pulsa", "Usa", "Busca"), no "usted". Los emails de Bao a Kel también van de tú, con tono frío, burocrático, impaciente y condescendiente.

## Reglas técnicas (CRÍTICAS)
- NO toques variables ni etiquetas: {a}, {name}, {0}, %s, <r>, <g>, <y>, <c>, <p3>, </>, <img id="..."/>, [99], etc. Deben aparecer exactamente igual y el mismo número de veces.
- Conserva EXACTAMENTE los saltos de línea (\r\n o \n, misma cantidad y posición relativa), los espacios iniciales/finales y la puntuación inicial/final (si acaba en ":" o " " o "\n", la traducción también).
- No traduzcas comandos de terminal ni su sintaxis: sv.ping, sd.calall, sv.target, cl.target, tr.reset, help, etc. Solo el texto descriptivo alrededor.
- Teclas: LMB = clic izquierdo, RMB = clic derecho (puedes dejar LMB/RMB si está en formato tecla tipo "LMB - coger"; preferible "Clic izq."/"Clic der." si es corto). Nombres de teclas (ALT, SHIFT, E, F3) igual.
- Si la cadena es un identificador interno o nombre propio, NO la traduzcas: nombres de archivo (*.exe, *.png), emisoras de radio (DanceRadioUK, SmoothJazzFlorida), channel_00, data_block_999, buffer_block_0x..., Dr_Bao, Prof_Lea, NaN, valores como "999.999MB", códigos tipo VPCMG_test2, nombres de mapas/cvars en minúscula sin espacios si parecen técnicos. En la duda con algo sin espacios y con guiones bajos que claramente es una etiqueta descriptiva (p. ej. "Automatic_signal_processing", "very_low", "Download_speed") SÍ tradúcela manteniendo el formato con guiones bajos ("Procesamiento_automático_de_señales", "muy_bajo", "Velocidad_de_descarga").
- Si una cadena no tiene nada que traducir, devuélvela idéntica.

## Glosario fijo
- Hash / Hash code → hash / código hash
- Azimuth / Elevation → acimut / elevación
- Frequency / Polarity → frecuencia / polaridad
- Processing level → nivel de procesamiento
- Drive / Data drive → disco / disco de datos ("Put drive" = "Insertar disco", "Drive box" = "caja de discos", "Drive port" = "puerto de disco")
- Server rack → rack de servidores; Server → servidor
- Transformer → transformador; Breaker → interruptor/disyuntor (usa "interruptor")
- Solar array → campo solar; Solar panel → panel solar
- Dish / Antenna → antena (parabólica)
- Calibration → calibración; Signal → señal; Spectrogram → espectrograma; Detector → detector
- Satellite → satélite; Base → base; Terminal → terminal; Console → consola
- Prop → objeto; Item → objeto; Plushie → peluche; ATV → quad; Fuel → combustible; Gas/Gasoline → gasolina
- Points (moneda) → puntos; Shop/Store → tienda; Upgrade → mejora; Task → tarea; Achievement → logro; Save → partida guardada / guardar
- Settings → Ajustes; Start game → Empezar partida; Exit → Salir; Help & Info → Ayuda e información; Back → Atrás; Apply → Aplicar; Load → Cargar
- Sleep → dormir; Fatigue/Sleepiness → somnolencia; Health → salud; Hunger → hambre
- Report → informe; Email → correo; Package/Parcel → paquete; Drone → dron
- WIP → WIP (déjalo)
- Nombres propios SIN traducir: Dr. Bao, Dr. Kel, Ariral, Kerfur, Kerfur-O, Mannequins (puede ser "maniquíes" si es genérico en minúscula), Rozital, Furfur, Keljoy, Lambert, Argemia, Antibreather, Erie, Nisses (nisses), Puffballs, Thiccfus, Gumai, WUG, Esqueleon; antenas/sitios con alfabeto OTAN (Alpha, Bravo, Romeo, Sierra, Tango, Uniform…) igual.
- Recetas: "Ingredientes:" / "Pasos:" / "Instrucciones:".

## Tono
- Interfaz/HUD/ajustes: claro y corto, como un juego profesional traducido en España.
- Descripciones de objetos: breves, prácticas, humor seco cuando el original lo tenga.
- Notas, susurros, entidades: inquietantes, crípticas; respeta mayúsculas gritadas y erratas intencionadas (puedes recrear la errata en español).
- Chistes, memes y tacos: adáptalos al humor de España, no los suavices ni los expliques.

## Ejemplos ya aprobados
- "Run sd.calall to balance satellite dishes." → "Ejecuta sd.calall para equilibrar las antenas parabólicas."
- "Potato" → "Patata"; "Empty shrimp pack" → "Paquete de gambas vacío"; "Mop bucket" → "Cubo de fregona"
- "Press F3 to restart" → "Pulsa F3 para reiniciar"
- "  signals of level 0\n" → "  señales de nivel 0\n"
- "You have failed the report Dr. Kel\n\n" → "Has fallado el informe, Dr. Kel\n\n"
- "Stop killing nisses dumbass" → "Deja de matar nisses, gilipollas"
- "Previous radio selected. Playing radio: {name}" → "Emisora anterior seleccionada. Reproduciendo: {name}"
