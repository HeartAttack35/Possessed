# DOC-MECANICAS.md — Possessed: Mecánicas de Juego

> **Nota de uso:** Este documento describe cómo funcionan las mecánicas para el jugador. No describe implementación técnica. Toda información está extraída directamente del código fuente del proyecto (`definitions.rpy`, `script.rpy`, `script_2.rpy`, `script_3.rpy`) y de aclaraciones directas del autor.
>
> Se distingue entre:
> - **[CONFIRMADA]** — extraída directamente del código o aclarada por el autor
> - **[INFERIDA]** — deducida del comportamiento del código sin confirmación explícita
> - **[PENDIENTE]** — información no disponible o no implementada aún

---

## 1. Sistema de Afinidad

### Objetivo
Rastrear la relación entre Rodrigo y cada uno de sus cuatro compañeros principales. Los valores acumulados determinan los epílogos individuales en los créditos finales y condicionan ciertos eventos durante la partida.

### Funcionamiento
El jugador acumula o pierde puntos de afinidad al elegir opciones en los menús de decisión. Los cambios son **invisibles durante el juego**: el jugador no recibe ninguna confirmación de cuándo sube o baja una afinidad.

### Variables

| Variable | Personaje | Valor inicial |
|---|---|---|
| `afinidad_luz` | Luz | 0 |
| `afinidad_azura` | Azura | 0 |
| `afinidad_cutipye` | Cutipye | 0 |
| `afinidad_nagi` | Nagi | 0 |

**[CONFIRMADA]** Cada decisión puede sumar 0, +1 o +2 puntos, o restar -1, dependiendo de la opción elegida. Una misma decisión puede afectar la afinidad de más de un personaje simultáneamente.

### Reglas
- El jugador nunca ve los números directamente en la partida normal.
- Los valores se acumulan a lo largo de toda la partida sin reiniciarse entre capítulos.
- No hay un umbral máximo declarado. **[CONFIRMADA por el autor]**

### Interacciones con otros sistemas

**Selección de objetivo en combate (cap_8):** El juego calcula qué personaje tiene la afinidad más baja al llegar a la confrontación con la rata mutante. Ese personaje es el atacado. En caso de empate, el orden de prioridad es: Nagi > Cutipye > Azura > Luz. **[CONFIRMADA]**

**Epílogos en créditos:** Se evalúa si cada afinidad es ≥ 5 al finalizar la partida.

| Afinidad final | Texto en epílogo |
|---|---|
| ≥ 5 | "Tu relación con [personaje] fue buena." |
| < 5 | "Tu relación con [personaje] fue distante." |

**Epílogo de Luz con `afinidad_luz < 5`:** El texto sugiere explícitamente que la distancia de Rodrigo contribuyó al destino trágico de Luz. **[CONFIRMADA]**

**Confesar la influencia (cap_7):** Elegir confesar suma +2 a todas las afinidades simultáneamente. **[CONFIRMADA]**

### Casos especiales
- Es posible que `afinidad_luz` quede baja si se elige burlarse del rumor del orfanato en cap_1 y no se reconforta a Luz en los momentos de crisis de cap_1 y cap_2.
- La afinidad con Nagi puede subir considerablemente si el jugador elige la ruta de la administración en cap_6 y admite estar mal cuando Nagi lo pregunta.

### Pendientes
- No está declarado un umbral máximo para las afinidades. **[CONFIRMADA: no existe techo]**
- No está disponible el detalle de todas las decisiones de afinidad de los capítulos 9 en adelante. **[PENDIENTE]**

---

## 2. Sistema de Estado Mental

### Objetivo
Rastrear el deterioro psicológico de Rodrigo como consecuencia de los eventos traumáticos y de la influencia creciente de Galaxia. Afecta directamente el comportamiento de Rodrigo en combate y su interpretación de los eventos del entorno.

### Funcionamiento
La variable `estado_mental` sube al tomar decisiones temerosas, al presenciar eventos traumáticos, o al ocultar información al grupo. Puede bajar ligeramente con decisiones racionales o reconfortantes. El jugador **nunca ve el valor** durante la partida normal.

### Variable

| Variable | Valor inicial | Mínimo | Máximo |
|---|---|---|---|
| `estado_mental` | 0 | 0 (no baja de 0) | Sin techo |

**[CONFIRMADA por el autor]** El valor no puede descender por debajo de 0 y no tiene un límite superior.

### Reglas
- Sube principalmente con eventos de miedo, trauma y ocultamiento.
- Puede bajar en -1 con algunas decisiones racionales o de control.
- Algunos eventos lo incrementan automáticamente sin importar la decisión tomada.

### Umbrales y estados

**Comportamiento en exploración (cap_8, al amanecer):** **[CONFIRMADA]**

| Valor | Reacción de Rodrigo al percibir sonidos |
|---|---|
| < 4 | Lo racionaliza como fatiga o viento. No lo reconoce como señal. |
| 4–10 | Reconoce que escucha algo pero lo mezcla con sensaciones confusas. |
| ≥ 11 | Lo percibe con claridad sobrenatural. Lo describe con vocabulario de depredador. |

**Tipo de combate contra la rata mutante (cap_8):** **[CONFIRMADA]**

| Valor | Comportamiento en combate |
|---|---|
| < 10 | Combate humano: torpe, desesperado, con miedo visible. |
| 10–14 | Combate sintetizado: movimientos ágiles y antinaturales, parcialmente disociado. |
| ≥ 15 | Combate predador: brutal, preciso, sin emoción reconocible. Los compañeros lo observan con miedo. |

**Reacción del grupo en cap_6 (post-herida de Rodrigo):** **[CONFIRMADA]**

| Valor | Reacción |
|---|---|
| ≥ 6 | Nagi y Cutipye reaccionan con preocupación activa, lo interpelan directamente. |
| < 6 | Reaccionan con ligereza, lo tranquilizan como a alguien que tuvo un susto. |

### Resumen en créditos

| Valor final | Texto mostrado |
|---|---|
| ≤ 10 | "Rodrigo mantuvo la calma." |
| 11–15 | "Rodrigo estuvo bajo presión." |
| ≥ 16 | "Rodrigo sucumbió al estrés." |

**[CONFIRMADA]**

### Interacciones con otros sistemas
- La elección de **ocultar la influencia** en cap_7 suma +2. La de **confesar** no lo modifica. **[CONFIRMADA]**
- La elección de "Mantenerlo en secreto" suma +2; la de "Tengo miedo, Cutipye" suma +1. **[CONFIRMADA]**
- El amanecer del cap_8 suma +1 automáticamente, sin decisión del jugador. **[CONFIRMADA]**

### Casos especiales
- Si el jugador elige sistemáticamente las opciones de pánico o derrumbe emocional, el valor puede alcanzar rangos altos antes del cap_8, forzando el combate predador incluso si las afinidades son equilibradas.

### Pendientes
- Impacto de `estado_mental` en los capítulos 9 en adelante: no disponible. **[PENDIENTE]**

---

## 3. Sistema de Game Over

### Objetivo
Terminar la partida de forma no canónica cuando el jugador toma una decisión fatal o falla una secuencia de tiempo limitado. Presenta una pantalla de game over con opciones para continuar.

### Funcionamiento
Determinadas opciones en los menús de elección, o el fallo de secuencias QTE, llevan directamente a etiquetas de game over. La narración describe la muerte antes de mostrar la pantalla de fin.

Tras el game over, el jugador puede elegir entre:
- **Cargar partida** (va a la pantalla de carga).
- **Volver al menú principal**.

**[CONFIRMADA]** No hay game over automático por acumulación de variables; todos son consecuencia directa de una elección o de no reaccionar a tiempo en un QTE.

### Game overs confirmados en los archivos disponibles

| Nombre | Capítulo | Causa |
|---|---|---|
| `game_over_spdr` | Cap_1 | Insistir en atacar a la criatura-araña en lugar de huir. |
| `game_over_mnts_1` | Cap_2 | Acercarse a investigar la criatura-mantis. |
| `game_over_mnts_2` | Cap_2 | Esconderse bajo la cama durante el encuentro con la mantis. |
| `game_over_ladder` | Cap_4 | No reaccionar a la escalera dentro del tiempo límite del QTE. |
| `game_over_wasp` | Cap_5 | Fallar cualquiera de las tres fases del QTE contra el zángano. |

### Casos especiales
- El game over de la araña incluye un juicio narrativo explícito: *"Rodrigo murió como un idiota..."*. **[CONFIRMADA]**
- La única opción que evita los dos game overs de la mantis es esconderse *detrás del armario*. **[CONFIRMADA]**
- El game over de la escalera es el único donde la descripción visual de la muerte incluye diálogo de Galaxia. **[CONFIRMADA]**
- El game over del zángano muestra la muerte de Azura, no de Rodrigo. Es el único game over confirmado donde muere un personaje secundario en lugar del protagonista. **[CONFIRMADA]**

### Pendientes
- Número total de game overs en la partida completa. **[PENDIENTE]**

---

## 4. Sistema de Endings

### Objetivo
Determinar el desenlace final de la historia y los epílogos de cada personaje según las decisiones acumuladas durante la partida.

### Variable

| Variable | Valor por defecto | Valores posibles |
|---|---|---|
| `ending_type` | `"good"` | `"good"`, `"bad1"`, `"bad2"`, `"neutral1"`, `"neutral2"` |

### Funcionamiento
Al llegar a los créditos, el juego evalúa `ending_type` para mostrar el epílogo general y los epílogos individuales de cada personaje. Adicionalmente muestra un resumen de la partida basado en las afinidades finales y el `estado_mental`.

**[CONFIRMADA por el autor]** El valor de `ending_type` es asignado en `label cap_12`, antes de los créditos, en función de las decisiones acumuladas por el jugador.

### Tipos de ending y sus epílogos

**[CONFIRMADA]**

| Tipo | Descripción del epílogo general |
|---|---|
| `bad1` | Nadie sobrevive. El orfanato arde durante la madrugada. Todos los personajes son listados como desaparecidos. Se sugiere que algo sigue vivo entre los restos calcinados. |
| `bad2` | Solo Azura sobrevive. Vive con el trauma sin poder superarlo. Se pregunta si realmente escapó del lugar. |
| `neutral1` | Algunos sobrevivientes. Cargan el trauma de por vida. Se marchan antes de que lleguen los servicios de emergencia. |
| `neutral2` | Tres sobrevivientes. El incendio es atribuido oficialmente a un accidente. Los sobrevivientes nunca corrigen la versión oficial. |
| `good` | Azura, Nagi y Cutipye sobreviven. Alguien se queda atrás. Se escuchan alas entre las llamas, sugiriendo que algo protege el lugar. |

### Epílogos individuales por personaje

Los epílogos de cada personaje en los créditos también varían según `ending_type` y las flags de muerte individuales.

**Rodrigo:**
- Si `ending_type == "bad1"`: su familia acepta su desaparición en silencio y nadie lo busca.
- En cualquier otro ending: su familia no inicia investigación, pero sus amigos conocen la verdad.

**Luz:**
- Si `ending_type == "bad1"`: las autoridades cierran el caso sin pruebas.
- Si `afinidad_luz >= 5`: texto neutro sobre la investigación familiar.
- Si `afinidad_luz < 5`: el texto sugiere que la relación distante de Rodrigo contribuyó a su destino.

**Azura:**
- Si `ending_type == "bad1"`: desaparecida, la familia espera su regreso.
- Si `ending_type == "bad2"`: sobrevive pero asiste a terapia sin superar el trauma.
- En otros endings: supera el trauma con apoyo familiar y de amigos.

**Nagi:**
- Si `ending_type == "bad1"`: la familia no encuentra cuerpo ni pistas.
- Si `nagi_dead == True` (y no es bad1): la familia busca pero no lo encuentra.
- En otros casos: sobrevive pero nunca vuelve a ser el mismo.

**Cutipye:**
- Si `ending_type == "bad1"`: desaparición con hermetismo familiar; se mudan de la ciudad.
- Si `cuty_dead == True` (y no es bad1): funeral privado sin investigación formal.
- En otros casos: sobrevive pero se vuelve retraída y se muda para escapar de los recuerdos.

**[CONFIRMADA]**

### Flags de muerte individuales

| Variable | Descripción |
|---|---|
| `nagi_dead` | Registra si Nagi murió durante la partida. |
| `cuty_dead` | Registra si Cutipye murió durante la partida. |

**[CONFIRMADA por el autor]** Estas flags serán activadas principalmente en los capítulos 10 y 11, con la posibilidad de incorporar eventos en capítulos previos mediante modificaciones futuras al script.

### Casos especiales
- La infección de Rodrigo es permanente en todos los finales. **[CONFIRMADA por el autor]** Ningún ending contempla una reversión de la posesión.

### Pendientes
- Las condiciones exactas que derivan en cada `ending_type` no están en los archivos disponibles. **[PENDIENTE — se resolverá en `cap_12`]**
- Condiciones específicas que activan `nagi_dead` y `cuty_dead` en capítulos previos al 10. **[PENDIENTE — implementación futura]**

---

## 5. Sistema de QTE (Quick Time Events)

### Objetivo
Introducir secuencias de tiempo limitado en las que el jugador debe reaccionar con un botón visible en pantalla antes de que expire un contador. El fallo conduce directamente a un game over.

### Funcionamiento
El juego muestra una pantalla modal con un texto de instrucción parpadeante, un botón de acción y un temporizador invisible que corre en segundo plano. Si el jugador pulsa el botón antes de que expire el tiempo, la secuencia continúa. Si el tiempo se agota sin acción, salta automáticamente al game over correspondiente.

### Reglas
- El botón de acción usa un estilo visual distinto (fondo rojo, texto grande, bordes negros) para destacarlo como urgente. **[CONFIRMADA]**
- El tiempo disponible disminuye en cada fase consecutiva de un mismo QTE. **[CONFIRMADA]**
- Mientras el QTE está activo, el jugador no puede interactuar con ningún otro elemento de la pantalla (pantalla modal). **[CONFIRMADA]**
- No hay segundo intento dentro de la misma fase; el fallo es inmediato.

### QTEs confirmados en los archivos disponibles

**QTE de la escalera (cap_4)**

| Fase | Tiempo | Acción | Éxito | Fallo |
|---|---|---|---|---|
| Única | 3 segundos | Botón "TREPAR" | Continúa la huida | `game_over_ladder` |

**QTE del zángano (cap_5) — tres fases encadenadas**

| Fase | Tiempo | Personaje | Acción del botón | Fallo global |
|---|---|---|---|---|
| Fase 1 | 3 segundos | Cutipye | "LANZAR EXTINTOR" | `game_over_wasp` |
| Fase 2 | 2.5 segundos | Nagi | "BATEAR" | `game_over_wasp` |
| Fase 3 | 2 segundos | Luz | "¡GOLPEA!" | `game_over_wasp` |

**[CONFIRMADA]** Fallar cualquiera de las tres fases lleva al mismo game over. No hay recuperación entre fases.

### Casos especiales
- En el QTE del zángano, cada fase tiene un botón posicionado en un lugar distinto de la pantalla (izquierda, derecha, centro), obligando al jugador a adaptar la posición del cursor o el foco visual en cada transición. **[CONFIRMADA]**

### Pendientes
- Número total de QTEs en la partida completa. **[PENDIENTE]**
- Si existen QTEs con más de tres fases en capítulos posteriores. **[PENDIENTE]**

---

## 6. Sistema de Progresión por Capítulos

### Objetivo
Dividir la historia en segmentos con puntos de guardado opcionales al final de cada capítulo, y guardados automáticos en encuentros clave.

### Funcionamiento
Al completar un capítulo, el juego pausa la música, muestra el nombre del capítulo completado y ofrece al jugador guardar antes de continuar.

### Reglas
- El guardado al finalizar capítulo es **opcional**. **[CONFIRMADA]**
- El guardado usa el slot `"1-1"` con el nombre del capítulo como etiqueta. **[CONFIRMADA]**
- Existen guardados automáticos en puntos clave dentro de los capítulos (antes de encuentros con criaturas). **[CONFIRMADA]**

### Capítulos identificados en los archivos disponibles

| Capítulo | Contenido principal | Archivos |
|---|---|---|
| Cap_1 | Llegada al orfanato. Encuentro con la araña. Separación del grupo. Descubrimiento de la mochila de Cutipye. | `script.rpy` |
| Cap_2 | Sótano y laboratorio. Lectura de la bitácora H-127. Encuentro con el Sujeto y revelación del nombre "Galaxia". Encuentro con la mantis. Reunión con Luz y pasaje secreto. | `script.rpy` |
| Cap_3 | Flashback: infancia de Rodrigo, primer encuentro con Luz en la escuela. | `script.rpy` |
| Cap_4 | Rodrigo solo en el sótano. Primer encuentro directo con Galaxia. Descubrimiento de que las balas no la matan. QTE de la escalera. Rodrigo herido y encerrado. | `script.rpy` |
| Cap_5 | Perspectiva del grupo buscando a Rodrigo. Encuentro con las larvas y la Avispa Nodriza. QTE del zángano (tres fases). Reunión con Rodrigo. | `script.rpy` |
| Cap_6 | Flashback: presentación de Luz al grupo hace tres años. Presente: Rodrigo herido, primeros síntomas visibles de la infección. Decisión de ruta (administración vs. retroceder). | `script_2.rpy` |
| Cap_7 | Oscuridad total. Voz de Galaxia en la mente de Rodrigo. Decisión: confesar o esconder la infección. Escena del balcón con Luz. | `script_2.rpy` |
| Cap_8 | Amanecer. Comportamiento alterado de Rodrigo. Combate contra la rata mutante (varía según `estado_mental`). | `script_2.rpy` |
| Cap_9 | Flashback: fiesta. *(Contenido parcial en los archivos disponibles.)* | `script_2.rpy` |
| Cap_10 | **[PENDIENTE]** No disponible en los archivos actuales. | — |
| Cap_11 | **[PENDIENTE]** No disponible en los archivos actuales. | — |
| Cap_12 | **[PENDIENTE]** Asignación de `ending_type` y transición a créditos. | — |

### Pendientes
- Contenido de los capítulos 9 (completo), 10, 11 y 12. **[PENDIENTE]**
- Número total definitivo de capítulos. **[PENDIENTE]**

---

## 7. Mecánica de Influencia / Infección (Galaxia)

### Objetivo
Representar la posesión progresiva de Rodrigo por parte de Galaxia. No es un medidor independiente; se manifiesta a través del sistema de `estado_mental`, de eventos narrativos y de cambios de comportamiento visibles para el jugador.

### Funcionamiento
A medida que `estado_mental` sube, la influencia de Galaxia se hace más presente. La voz de Galaxia aparece en texto de color morado (`#390169`) en la interfaz de diálogo, diferenciándola del pensamiento interno de Rodrigo, que aparece entre paréntesis. Los síntomas físicos son descritos narrativamente.

### Reglas
- El jugador no puede curar ni revertir la infección en ningún punto de la partida. **[CONFIRMADA por el autor]**
- Las decisiones de confesar u ocultar la infección afectan las afinidades y el `estado_mental`, pero no detienen el avance de la posesión. **[CONFIRMADA]**
- La infección se asume como permanente en todos los finales. **[CONFIRMADA por el autor]**

### Síntomas observables desde el punto de vista del jugador

| Fase | Señales narrativas |
|---|---|
| Temprana | Sabor dulce/metálico. Manchas oscuras en manos que desaparecen al frotarlas. Sensación de latido ajeno que "no es suyo". |
| Media | Voz de Galaxia audible en momentos de tensión. Impulsos de subir a lugares elevados y vigilar. Sensación de que el espacio es "seguro arriba". |
| Avanzada | Rodrigo actúa como depredador sin reconocerlo. Pupilas que cambian. Los compañeros lo observan con miedo después del combate. |

**[CONFIRMADA]**

### Interacciones con otros sistemas
- La voz de Galaxia tiene conocimiento del estado interno de Rodrigo y lo usa para provocarlo o empujarlo a actuar. **[CONFIRMADA]**
- En cap_7, una gota de sustancia negra penetra la piel de Rodrigo. Este evento ocurre independientemente de si confesó u ocultó la infección. **[CONFIRMADA]**
- Si el jugador oculta la infección, Galaxia comenta el engaño directamente en la narración. **[CONFIRMADA]**

### Pendientes
- Qué desencadena el primer contacto físico de Galaxia con Rodrigo (en qué capítulo y bajo qué condición exacta). **[PENDIENTE]**
- Si la progresión de la infección tiene puntos de no retorno más allá del `estado_mental`. **[PENDIENTE]**

---

## 8. Sistema de Guardado

### Objetivo
Permitir al jugador conservar su progreso y retomar la partida desde puntos anteriores.

### Funcionamiento
El guardado puede ocurrir de dos formas: automático en momentos clave del script, y manual al final de cada capítulo.

### Reglas
- Los guardados automáticos usan el slot `"1-1"` con una etiqueta descriptiva del momento. **[CONFIRMADA]**
- El guardado manual al final de capítulo también usa el slot `"1-1"`. **[CONFIRMADA — inferida: ambos usan el mismo slot, lo que significa que el guardado automático puede sobreescribirse con el manual del capítulo siguiente]**
- El jugador tiene acceso a guardado rápido (`Q.Save`) y carga rápida (`Q.Load`) desde el menú rápido durante la partida. **[CONFIRMADA]**
- Los datos persistentes (como `persistent.credits_seen`) se conservan entre sesiones y no se borran al cargar una partida. **[CONFIRMADA]**

### Guardados automáticos identificados

| Etiqueta | Ubicación |
|---|---|
| "Encuentro 1" | Antes del encuentro con la araña (cap_1) |
| "Encuentro 2" | Antes del encuentro con la mantis (cap_2) |
| "Encuentro 4" | Antes de la primera aparición de Galaxia (cap_4) |
| "Encuentro 5" | Antes del encuentro con las avispas (cap_5) |

**[CONFIRMADA]**

### Pendientes
- Si existe un "Encuentro 3". No hay evidencia de este guardado en los archivos disponibles. **[PENDIENTE]**

---

## 9. HUD de Estadísticas

### Objetivo
Herramienta de desarrollo. Muestra en tiempo real los valores de las variables de juego durante las pruebas.

### Funcionamiento
Se muestra en la esquina superior izquierda de la pantalla. Controlado por la variable `mostrar_hud`, que por defecto está activa en la build de desarrollo.

### Variables mostradas

| Variable | Color |
|---|---|
| Afinidad Luz | Rojo (`#fd5353`) |
| Afinidad Azura | Verde (`#0f8028`) |
| Afinidad Cutipye | Verde claro (`#2dff5a`) |
| Afinidad Nagi | Morado (`#7b2cbf`) |
| Estado Mental | Naranja (`#ffaa00`) |

### Reglas
- **[CONFIRMADA por el autor]** El HUD será eliminado por completo en la versión de producción. No es una función destinada al jugador final.
- Durante el desarrollo puede activarse o desactivarse desde la consola con `mostrar_hud = True` / `mostrar_hud = False`.

---

## Pendientes globales

1. Condiciones exactas de asignación de `ending_type` (se implementan en `cap_12`, aún no disponible).
2. Condiciones que activan `nagi_dead` y `cuty_dead` en capítulos previos al 10 (implementación futura).
3. Contenido completo de cap_9, cap_10, cap_11 y cap_12.
4. Sprites diferenciados por expresión para todos los personajes (actualmente todos usan el mismo archivo `.png` como placeholder).
5. Archivos de audio referenciados en el script pero aún no implementados formalmente (ej. `pasos_susurro.ogg`, `ambiente_tenso.ogg`, `daga_desenvainada.ogg`).
6. Número total de game overs y QTEs en la partida completa.
7. Si existe un "Encuentro 3" con guardado automático.
8. Impacto de `estado_mental` en los capítulos 9 en adelante.