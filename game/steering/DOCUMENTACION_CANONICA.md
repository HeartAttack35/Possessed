# DOCUMENTACIÓN CANÓNICA - POSSESSED

**Proyecto:** Possessed
**Engine:** Ren'Py (Python 3.12)
**Género:** Horror / Visual Novel
**Resolución:** 1920x1080
**Versión del documento:** 1.0
**Fecha de generación:** 2026-07-08
**Estado general:** Trabajo en progreso

---

> **NOTA METODOLÓGICA:** Este documento contiene únicamente información extraída del código fuente y archivos del proyecto. Las secciones marcadas como **[PENDIENTE]** indican información ausente en los archivos revisados o en desarrollo. Las secciones marcadas como **[INFERIDO]** indican información deducida del contexto, no declarada explícitamente. Las **[CONTRADICCIONES]** detectadas se enumeran tal cual, sin elegir una versión.

---

## ÍNDICE

1. [Resumen del Proyecto](#1-resumen-del-proyecto)
2. [Estructura Técnica](#2-estructura-técnica)
3. [Personajes](#3-personajes)
4. [Sistema de Juego](#4-sistema-de-juego)
5. [Narrativa y Historia](#5-narrativa-y-historia)
6. [Audio](#6-audio)
7. [Recursos Visuales](#7-recursos-visuales)
8. [Archivos Pendientes de Revisión](#8-archivos-pendientes-de-revisión)
9. [Créditos](#9-créditos)

---

## 1. RESUMEN DEL PROYECTO

**Possessed** es una novela visual de terror psicológico. Un grupo de cinco amigos entra a un orfanato abandonado que ocultaba experimentos ilegales, y desencadena una serie de eventos de horror y supervivencia. El jugador controla a Rodrigo, cuyas decisiones afectan las relaciones con sus compañeros y determinan quién sobrevive.

### Características confirmadas en código

- Protagonista controlable con relaciones variables con 4 personajes
- Sistema de afinidad numérico por personaje
- Sistema de estado mental (rastreador de cordura/transformación)
- 5 endings distintos (bad1, bad2, neutral1, neutral2, good)
- Muertes permanentes de personajes secundarios (Nagi, Cutipye)
- Secuencias de persecución y QTE
- Flashbacks de la historia previa del grupo

### Contenido maduro (confirmado explícitamente en código)

Violencia explícita, gore, lenguaje fuerte, personaje transgénero, referencias a tortura, experimentos en menores, abuso de sustancias.

---

## 2. ESTRUCTURA TÉCNICA

### 2.1 Archivos de código fuente

| Archivo | Contenido |
|---|---|
| `script.rpy` | Capítulos 1–5 |
| `script_2.rpy` | Capítulos 6–11 + créditos |
| `script_3.rpy` | Pantalla de créditos finales |
| `definitions.rpy` | Personajes, variables, imágenes, transforms, HUD |
| `options.rpy` | Configuración de Ren'Py, audio, build |
| `screens.rpy` | Pantallas UI (menú, guardado, preferencias) |
| `gui.rpy` | Estilos visuales (no analizado en detalle) |

### 2.2 Configuración del proyecto (confirmada en `options.rpy`)

```
config.name = "Possessed"
config.version = "1.0"
build.name = "Possessed"
config.save_directory = "Possessed-1753492026"
config.window_icon = "gui/window_icon.png"
preferences.text_cps = 40
preferences.afm_time = 15
```

### 2.3 Canales de audio (confirmados en `options.rpy`)

```python
renpy.music.register_channel("ambient", mixer="ambient", loop=True)
```

Canales activos: `music`, `sound`, `voice`, `ambient`

### 2.4 Capítulos implementados

| Capítulo | Archivo | Estado |
|---|---|---|
| Capítulo 1 | script.rpy | Completo |
| Capítulo 2 | script.rpy | Completo |
| Capítulo 3 | script.rpy | Completo |
| Capítulo 4 | script.rpy | Completo |
| Capítulo 5 | script.rpy | Completo |
| Capítulo 6 | script_2.rpy | Completo (2 rutas) |
| Capítulo 7 | script_2.rpy | Completo (2 rutas) |
| Capítulo 8 | script_2.rpy | Completo |
| Capítulo 9 | script_2.rpy | Completo |
| Capítulo 10 | script_2.rpy | Completo (2 rutas) |
| Capítulo 11 | script_2.rpy | Parcial (rama de afinidad alta sin terminar) |
| Capítulo 12 | script_2.rpy | **Solo contiene `return`** |
| Créditos | script_3.rpy | Completo |

**Nota:** El juego planea 10–12 capítulos según el desarrollador. Solo 1–11 están parcialmente implementados.

---

## 3. PERSONAJES

### 3.1 Protagonista

#### Rodrigo
- **Variable:** `r`
- **Color de texto:** `#0c0472` (azul oscuro)
- **Descripción narrativa:** Joven introvertido, callado, con tendencia a la distancia emocional. Pareja de Luz. Carga una navaja desde el inicio.
- **Rol mecánico:** Punto de vista del jugador. Sus decisiones controlan todas las variables del juego.
- **Arco narrativo:** Se infecta progresivamente con el patógeno de Galaxia, transformándose en un ser híbrido humano-cuervo. Lucha por retener su humanidad.
- **Relación familiar [confirmada en créditos]:** Padre que lo da por fugado; madre que no habla del tema; ninguno busca investigar su desaparición.

**Expresiones implementadas en código** (todas actualmente son placeholder — mismo archivo PNG):

`neutral`, `soft`, `molesto`, `serio`, `frustrado`, `nervioso`, `sorprendido`, `pain`, `scared`, `worried`, `alert`, `linterna`, `shocked`, `aim_gun`, `injured`, `shock_state`, `bleeding_wall`, `casual_young_shy`, `casual_young_blush`, `move_slow` (animado), `run_panic` (animado), `dead` (efecto TintMatrix negro)

---

### 3.2 Personajes principales

#### Luz
- **Nombre anterior:** Lucien
- **Variables:** `l` (presente), `ln` (flashback)
- **Color de texto:** `#fd5353` (rojo/rosa)
- **Descripción narrativa:** Mujer trans. Novia de Rodrigo desde la adolescencia. Empática, cálida, protectora. Fue quien inició la amistad con Rodrigo cuando eran niños. La escena de su presentación como Luz ocurre en el Cap 6 (flashback "tres años atrás").
- **Variable de afinidad:** `afinidad_luz`
- **Threshold de créditos:** ≥5 = "relación buena"; <5 = "relación distante"
- **Estado en endings:** Muerta en bad1. En endings restantes, fallecida (funeral mencionado).

**Expresiones:** `smile`, `scared`, `worry`, `sad`, `angry`, `neutral`, `serious`, `surprised`, `determined`, `tired`, `pre_transition_shy`, `pre_transition_smile_tears`, `dead`

---

#### Azura
- **Variable:** `a`
- **Color de texto:** `#0f8028` (verde oscuro)
- **Descripción narrativa:** Mediadora del grupo. Optimista incluso bajo presión. Tiene conocimientos básicos de primeros auxilios.
- **Variable de afinidad:** `afinidad_azura`
- **Estado en endings:** Única sobreviviente en bad2. Sobrevive en neutral y good.

**Expresiones:** `neutral`, `smile`, `temblor`, `emocion`, `scared`, `worried`, `shocked`, `tired`, `casual_young`, `casual_young_smile`, `dead`

---

#### Cutipye
- **Variable:** `c`
- **Color de texto:** `#2dff5a` (verde brillante)
- **Descripción narrativa:** Bromista, enérgica, pertenece a una familia adinerada. Puede volverse hostil si la relación con Rodrigo se deteriora.
- **Variable de afinidad:** `afinidad_cutipye`
- **Threshold de traición:** `afinidad_cutipye < 4` activa escena de traición en Cap 11
- **Variable de muerte:** `cuty_dead`
- **Estado en endings:** Muerta (cuty_dead=True) si afinidad < 4. Sobrevive traumatizada en ending neutro/good si survives.

**Expresiones:** `neutral`, `smile`, `smile_nervous`, `determined`, `serious`, `soft`, `scared`, `shocked`, `tired`, `disgust`, `casual_young`, `throw`, `worried`, `dead`

---

#### Nagi
- **Apellido:** Katashi
- **Variable:** `n`
- **Color de texto:** `#7b2cbf` (morado)
- **Descripción narrativa:** Extrovertido, líder social, bromista. Tiene un lado empático profundo que emerge en momentos críticos.
- **Variable de afinidad:** `afinidad_nagi`
- **Threshold de abandono:** `afinidad_nagi < 3` activa traición y muerte en Cap 10
- **Variable de muerte:** `nagi_dead`
- **Estado en endings:** Muerto (nagi_dead=True) si afinidad < 3. Sobrevive en good (aunque "nunca volvió a ser el mismo").

**Expresiones:** `neutral`, `smug`, `smile`, `serio`, `soft`, `tired`, `angry`, `annoyed`, `worried`, `shocked`, `surprised`, `scared`, `casual_young`, `casual_young_molesto`, `casual_young_shock`, `dead`

---

### 3.3 Antagonistas

#### Galaxia (Shio Katashi)
- **Variable:** `g`
- **Color de texto:** `#390169` (morado muy oscuro)
- **Font especial:** `fonts/HelpMe.ttf`
- **Descripción narrativa:** Única Huésped Activa con consciencia plena. Ex-huérfana del orfanato "Luz y Esperanza", infectada con el Patógeno H-127. Apariencia híbrida humano-felino (orejas de gato, garras, dientes afilados). Juguetona y sádica. Obsesionada con Rodrigo.
- **Habilidades confirmadas en código:**
  - Regeneración celular rápida (balas no la matan permanentemente)
  - Agilidad y velocidad sobrehumanas (corre por paredes y techo)
  - Transmisión del patógeno mediante contacto directo
  - Manipulación psicológica, comunicación telepática con infectados
- **Nombre real:** Confirmado en Cap 7 mediante una Biblia con su nombre inscrito
- **Versículo relevante [Cap 7]:** Jeremías 12:9 — "hiena manchada"

**Expresiones:** `walk_creepy`, `smile`, `half_smile`, `shadow_eyes`, `laugh`, `regen`, `healed`, `headshot`

---

#### Criaturas Huésped (ex-huérfanos mutados por H-127)

Estas criaturas actúan por instinto animal. Solo Galaxia posee consciencia plena.

| Criatura | Aparición | Características |
|---|---|---|
| **Araña-Huésped** | Cap 1 | Se mueve por techos, primera criatura encontrada |
| **Mantis-Huésped** | Cap 2 | Hojas afiladas, caza en oscuridad por olfato/olfato |
| **Avispa-Nodriza** | Cap 5 | Protege larvas humanoides en la cocina |
| **Avispa-Zángano** | Cap 5 | Versión de combate; se enfrenta al grupo en pasillo |
| **Rata-Huésped** | Cap 8 | Piel estirada, espinazos expuestos, ojos rojos; ataca al personaje con menor afinidad |
| **Cucaracha-Guardián** | Cap 10 | Caparazón grueso, bloquea el pasillo cuando Nagi es capturado |

---

### 3.4 Personajes secundarios

#### Dr. Édgar L. Montané
- **Rol:** Director del Proyecto H-127
- **Fuente:** Bitácora encontrada en Cap 2 (sala H-127)
- **Estado actual:** [PENDIENTE] No se indica si aparece en persona

#### Sujeto Herido
- **Variable:** `sujeto`
- **Aparición:** Cap 2 (sala H-127)
- **Rol:** Expone el nombre de Galaxia antes de morir; advierte al grupo
- **Nota [INFERIDO]:** Su sprite usa el modelo de Nagi con efecto negro. Probablemente placeholder.

#### Lucien (joven)
- **Aparición:** Flashbacks de infancia (Cap 3) y adolescencia (Cap 6)
- **Contexto:** Lucien es el nombre anterior de Luz. Los flashbacks muestran su historia con Rodrigo.

---

## 4. SISTEMA DE JUEGO

### 4.1 Variables de estado global

```python
# definitions.rpy
default afinidad_luz = 0
default afinidad_azura = 0
default afinidad_cutipye = 0
default afinidad_nagi = 0
default estado_mental = 0
default tiempo_escape = 0         # Declarada; uso en código no visible en archivos revisados
default nombre_capitulo = ""
default mostrar_hud = True        # SOLO DEBUG
default label_nagi = False        # True si se siguió ruta de Nagi en Cap 6
default _distortion_active = False
default _heavy_distortion_active = False
default nagi_dead = False
default cuty_dead = False
default persistent.credits_seen = False
default ending_type = "good"
```

---

### 4.2 Sistema de afinidad

Cada decisión del jugador puede incrementar o decrementar la afinidad con un personaje. Las afinidades afectan:
- Diálogos y reacciones de los personajes
- Si Nagi traiciona o permanece leal (Cap 10)
- Si Cutipye traiciona o permanece leal (Cap 11)
- El epílogo de Luz en los créditos
- Qué personaje ataca la Rata-Huésped (el de menor afinidad)

**Thresholds confirmados en código:**

| Personaje | Threshold | Efecto |
|---|---|---|
| Nagi | < 3 | Traición + muerte en Cap 10 |
| Cutipye | < 4 | Traición + posible muerte en Cap 11 |
| Luz | ≥ 5 | Epílogo "bueno" en créditos |

**[PENDIENTE]** Valores máximos de afinidad alcanzables no están definidos explícitamente en el código. Los thresholds de porcentaje (~30% del máximo) están planificados pero no implementados.

---

### 4.3 Sistema de estado mental

`estado_mental` rastrea la transformación psicológica de Rodrigo.

**Eventos que incrementan `estado_mental` (conteo en código revisado):**

| Evento | Capítulo | Variación |
|---|---|---|
| Respuesta "Intentas atacar criatura" | Cap 1 | +2 |
| Respuesta "Sales corriendo" | Cap 1 | +3 |
| Respuesta "Te muestras incómodo" (tortura) | Cap 1 | +1 |
| Opción "Cuestionar a Luz" | Cap 2 | +2 |
| Subir al final del cap 2 | Cap 2 | +1 |
| Diversas respuestas paranoicas | Cap 5–10 | +1 por evento |
| Pensamientos predadores en Cap 8 | Cap 8 | +1, +2 |
| Amanecer (automático) | Cap 8 | +1 |

**Eventos que decrementan `estado_mental`:**

| Evento | Capítulo | Variación |
|---|---|---|
| Respuesta "Piensas en opciones" | Cap 1 | -1 |
| Respuesta "Abrazarla sin pensar" | Cap 2 | -1 |
| Respuestas de racionalización | Cap 6+ | -1 |

**Rangos de efecto confirmados:**

| Rango | Efecto en combate (Cap 8) | Evaluación en créditos |
|---|---|---|
| estado_mental < 4 | Respuesta racional | — |
| estado_mental < 10 | Sensación mixta; combate humano | "Rodrigo mantuvo la calma" |
| estado_mental < 11 | Sensación de capacidad expandida | — |
| estado_mental < 15 | Combate sintetizado (instintos de cuervo) | "Rodrigo estuvo bajo presión" |
| estado_mental ≥ 15 | Combate brutal/predatorio | "Rodrigo sucumbió al estrés" |

**[PENDIENTE]** No existe un valor máximo de estado_mental definido en el código.

---

### 4.4 Tipos de final

Definidos en `definitions.rpy`:
```python
default ending_type = "good"  # Valores posibles:
# "bad1", "bad2", "neutral1", "neutral2", "good"
```

**Descripción de cada final (confirmada en `script_3.rpy`):**

| Ending | Descripción del epílogo |
|---|---|
| **bad1** | Incendio total; todos desaparecen; ningún sobreviviente. El orfanato en ruinas. |
| **bad2** | Azura es la única sobreviviente. Incapaz de dormir. En terapia pero traumatizada. |
| **neutral1** | Varios sobrevivientes. La historia es demasiado horrible para contarla. |
| **neutral2** | Tres sobrevivientes. Atribuyen la tragedia a un accidente. Nadie les creería. |
| **good** | Azura, Nagi y Cutipye sobreviven. Rodrigo se queda atrás. Se escucha el eco de unas alas en las llamas. |

**[PENDIENTE]** La lógica exacta que asigna el `ending_type` no está visible en los capítulos disponibles (cap 12 y posteriores están sin implementar).

---

### 4.5 HUD de desarrollo (Debug)

```python
# screen hud_stats() en definitions.rpy
```

Visible solo cuando `mostrar_hud = True`. Muestra:
- Afinidades con Luz, Azura, Cutipye, Nagi (en sus colores respectivos)
- Estado Mental

**Para activar/desactivar en juego:** Consola (`Shift+O`) → `mostrar_hud = True/False`

---

### 4.6 Quick Time Events (QTE)

#### QTE Escalera (Cap 4)
- **Contexto:** Rodrigo huye de Galaxia hacia una escotilla
- **Tiempo:** 3 segundos
- **Pantalla:** `screen qte_escalera`
- **Fallo:** `label game_over_ladder` → Game Over

#### QTE Avispa Zángano (Cap 5) — 3 fases
- **Fase 1:** `screen qte_wasp_1` — Cutipye lanza extintor
- **Fase 2:** `screen qte_wasp_2` — Nagi golpea con bate
- **Fase 3:** `screen qte_wasp_3` — Luz remata
- **Éxito:** `label combate_ganado`

---

### 4.7 Sistema de checkpoints

El juego guarda manualmente en "encuentros" numerados:

```python
# Todos usan slot "1-1"
$ renpy.save("1-1", "Encuentro 1")   # Cap 1 — criatura araña
$ renpy.save("1-1", "Encuentro 2")   # Cap 2 — sujeto herido
$ renpy.save("1-1", "Encuentro 3")   # Cap 3 — Galaxia en ventana
$ renpy.save("1-1", "Encuentro 4")   # Cap 4 — persecución sótano
$ renpy.save("1-1", "Encuentro 5")   # Cap 5 — nido de avispas
```

Además, `label chapter_complete(nombre)` ofrece guardar al terminar cada capítulo con el nombre del capítulo como etiqueta.

---

### 4.8 Transformación de Rodrigo (efectos visuales)

| Transform | Trigger | Efecto |
|---|---|---|
| `distortion_light` | Estado medio | Saturación +40%, zoom suave, oscilación |
| `distortion_heavy` | Estado alto | Saturación +80%, glitch de color, zoom agresivo |
| `sepia_filter` | Flashbacks | SepiaMatrix() |
| `blanco_y_negro` | Pantalla de advertencia | SaturationMatrix(0.0) |
| `oscuro` | Escenas oscuras | BrightnessMatrix(-0.5) |


---

## 5. NARRATIVA Y HISTORIA

### 5.1 Sinopsis general

Un grupo de cinco amigos —Rodrigo, Luz, Azura, Cutipye y Nagi— deciden explorar un orfanato abandonado en medio del bosque, rumoreado haber sido centro de tortura durante la dictadura. Al entrar, desatan una serie de encuentros mortales con criaturas mutadas —ex-huérfanos transformados por el Patógeno H-127— y con Galaxia, la única con consciencia humana que orquesta una "cacería" psicológica.

Rodrigo, tras contacto físico con Galaxia, comienza una transformación lenta en un Huésped híbrido humano-cuervo. A medida que su humanidad se erosiona, debe liderar al grupo hacia la salida mientras lucha contra instintos predadores y la pérdida de control.

---

### 5.2 Proyecto H-127 (Contexto lore)

**Fuente confirmada:** Bitácora del Dr. Édgar L. Montané (Cap 2)

El Proyecto H-127 era un programa clandestino de investigación biológica ubicado en el orfanato "Luz y Esperanza" durante la dictadura. Se seleccionaron niños huérfanos sin lazos familiares para integrarles el Patógeno H-127 —un agente biológico destinado a inducir "simbiosis controlada" entre humano y criatura.

**Hallazgos confirmados en bitácora:**
- Entrada 01 (Día 0): Selección de sujetos "prescindibles"
- Entrada 04 (Día 11): 60% de mortalidad; mutaciones inestables; colapso tisular
- Entrada 09 (Día 28): Identificación de "Huéspedes Activos" —sujetos con tolerancia al patógeno; muestran aumento muscular, endurecimiento dérmico, cambios oculares
- Comportamiento observado: Violencia territorial; uno de los sujetos arrancó el rostro de un investigador por contacto visual prolongado

**Estado actual del proyecto:** [PENDIENTE] No se menciona qué ocurrió al final del experimento ni el paradero del Dr. Montané.

---

### 5.3 Mapa de capítulos implementados

| Cap | Título | Eventos principales | Decisiones clave |
|---|---|---|---|
| **1** | Exploración inicial | Encuentro con criatura araña; decisión de atacar o huir | Primera elección de afinidad (Cutipye/Azura) |
| **2** | El sótano | Descubrimiento del laboratorio H-127; sujeto herido advierte sobre Galaxia | Cómo reconfortar a Luz (+afinidad) |
| **3** | Flashback infantil | Recuerdo de Rodrigo y Lucien (Luz) de niños; caída de Rodrigo al sótano | Decisiones no impactan variables |
| **4** | Persecución | Galaxia persigue a Rodrigo; Rodrigo descubre que balas no la matan; QTE de escalera | QTE determina game over o supervivencia |
| **5** | Reunión | Grupo se reencuentra; combate contra avispas; Rodrigo es herido | QTE de 3 fases con grupo (extintor, bate, barra) |
| **6** | División | Flashback de Luz revelando su identidad trans; Nagi y Cuty suben o buscan info | Ruta Nagi vs ruta Cutipye; decisión de buscar info o retroceder |
| **7** | Confesión | Rodrigo confiesa infección o la oculta; Biblia con nombre de Galaxia encontrada | Confesar infección (+afinidad todos) vs ocultarlo |
| **8** | Transformación | Flashback de fiesta (sobredosis); combate con rata-huésped; manifestación de instintos predadores | Estado_mental determina estilo de combate |
| **9** | **[PARCIAL]** | Flashback completo de Lucien/Luz en fiesta; manifestación física de plumas en Rodrigo | Respuestas con Luz tras sobredosis |
| **10** | Traición Nagi | Nagi traiciona (afinidad < 3) o permanece leal; combate con cucaracha-guardián | Determina si Nagi muere (nagi_dead = True) |
| **11** | Traición Cutipye | Cutipye traiciona (afinidad < 4) o permanece leal; Galaxia captura/mata a Cutipye si traiciona | Determina si Cutipye muere (cuty_dead = True) |
| **12** | **[SIN IMPLEMENTAR]** | Solo contiene `return` | — |

---

### 5.4 Flashbacks y estructura temporal

La historia alterna entre presente (exploración del orfanato) y flashbacks del pasado del grupo.

**Flashbacks confirmados:**

| Capítulo | Título flashback | Personajes | Tema |
|---|---|---|---|
| Cap 3 | Patio escolar (infancia) | Lucien (niño) y Rodrigo (niño) | Origen de la amistad; Lucien ofrece una manzana a Rodrigo aislado |
| Cap 6 | Casa de Cutipye (3 años atrás) | Grupo adolescente | Lucien revela su identidad como Luz y presenta a Rodrigo como su novio |
| Cap 8 | Fiesta de Nagi (juventud) | Rodrigo, Nagi, Cutipye, Azura | Rodrigo bebe y fuma por presión; sobredosis; Azura lo salva por teléfono; Luz lo cuida |
| Cap 9 | Continuación de fiesta | Rodrigo y Luz | Rodrigo despierta en casa de Luz tras sobredosis |

**[INFERIDO]** Los flashbacks están distribuidos para humanizar a Rodrigo antes de que pierda su humanidad por completo.

---

### 5.5 Escenas de muerte

#### Game Over por Araña-Huésped (Cap 1)
- **Trigger:** Elegir "Insistes en atacar"
- **Resultado:** Rodrigo muere mientras ataca a la criatura
- **Pantalla:** `scene spdr1` (imagen específica), luego `gameover_screen`

#### Game Over por Mantis-Huésped (Cap 2)
- **Trigger (opción 1):** "Te acercas a comprobar"
- **Trigger (opción 2):** "Te escondes bajo una de las camas"
- **Resultado:** Muerte instantánea; la Mantis atraviesa a Rodrigo con sus hojas
- **Pantallas:** `scene death_mnts_1`, `scene death_mnts_2` (opción 1); `scene death_mnts_3` (opción 2)

#### Game Over por Escalera (Cap 4)
- **Trigger:** No presionar botón QTE en 3 segundos
- **Resultado:** Galaxia atrapa a Rodrigo; lo mata en el suelo
- **Pantalla:** `scene death_glx_1`

#### Muerte de Nagi (Cap 10)
- **Trigger:** `afinidad_nagi < 3`
- **Resultado:** Nagi abandona al grupo; Galaxia lo captura; el grupo escucha gritos; Nagi no reaparece; `nagi_dead = True`
- **Nota:** Esta muerte es permanente para la partida

#### Muerte de Cutipye (Cap 11)
- **Trigger:** `afinidad_cutipye < 4`
- **Resultado:** Cutipye traiciona emocionalmente a Rodrigo; se va sola; Galaxia la atrapa en una habitación limpia; muere tras vaciar su pistola en Galaxia sin éxito; `cuty_dead = True`
- **Pantalla:** `scene death_cutipye` con efecto `blood_splash`
- **Nota:** Esta muerte es permanente para la partida

---

## 6. AUDIO

### 6.1 Música de fondo (definidas en `definitions.rpy`)

| Variable | Archivo | Loop point | Uso en código |
|---|---|---|---|
| `audio.main_menu` | `music/menu.ogg` | 28.25s | Menú principal; escenas reflexivas |
| `audio.forest` | `music/bosque.mp3` | — | Inicio del juego (bosque) |
| `audio.melody` | `music/melodia.ogg` | — | Escenas de tensión ligera |
| `audio.story` | `music/historia.ogg` | 41.53s | Escenas de lectura (bitácoras) |
| `audio.curse` | `music/maldicion.ogg` | — | Game Over; momentos de horror |
| `audio.chase` | `music/persecucion.ogg` | 62.8s | Persecuciones generales |
| `audio.chase1` | `music/persecucion (galaxia).ogg` | 34.5s | Persecución de Galaxia |
| `audio.flashback` | `music/flashback.ogg` | 28.00s | Flashbacks con filtro sepia |
| `audio.credits` | `music/creditos.mp3` | — | Pantalla de créditos finales |
| `audio.rodtheme` | `music/rodtheme.mp3` | **[PENDIENTE]** | Tema de Rodrigo (loop no definido) |
| `audio.ambiental` | `music/ambiental.mp3` | **[PENDIENTE]** | Ambientación general (loop no definido) |

---

### 6.2 Efectos de sonido (definidos en `definitions.rpy`)

| Variable | Archivo | Uso narrativo |
|---|---|---|
| `shock` | `sfx/shock.mp3` | Momentos de sorpresa |
| `slash` | `sfx/slash.mp3` | Ataques con armas cortantes |
| `run` | `sfx/run.mp3` | Carreras |
| `flies` | `sfx/flies.mp3` | Ambientación de cadáveres |
| `crack` | `sfx/crack-and-crunch.mp3` | Ruidos de huesos/estructuras |
| `walk0` | `sfx/walking_intro.mp3` | Pasos introductorios |
| `break_glass` | `sfx/break-glass.mp3` | Rotura de ventanas |
| `break_wood` | `sfx/break-wood.mp3` | Rotura de madera |
| `wood_creak` | `sfx/wood-creak.mp3` | Crujidos de piso |
| `door_break` | `sfx/door-break.mp3` | Puerta derribada (volumen 0.6) |
| `door_slam` | `sfx/door-slam.mp3` | Puerta cerrada con fuerza |
| `thud` | `sfx/thud.mp3` | Impactos pesados |
| `door_open` | `sfx/door-open.mp3` | Puerta abriéndose |
| `door_close` | `sfx/door-close.mp3` | Puerta cerrándose |
| `scream1` | `sfx/scream-echo.mp3` | Gritos con eco (Luz) |
| `chptr_cmplt` | `sfx/chapter-clear.mp3` | Completar capítulo |
| `glx_laugh` | `sfx/laugh.mp3` | Risa de Galaxia |
| `paper_flip` | `sfx/paper-flip.mp3` | Pasar páginas |
| `alarm` | `sfx/alarm.mp3` | Alarma (volumen 0.7) |
| `gunshot` | `sfx/gunshot.mp3` | Disparos |
| `walk` | `sfx/walking.mp3` | Pasos normales |
| `land` | `sfx/land.mp3` | Aterrizaje tras salto |
| `objfall` | `sfx/object-fall.mp3` | Objetos cayendo |
| `nailtap` | `sfx/nails-tapping.mp3` | Garras sobre superficie |
| `larvcry` | `sfx/larvae_cry.mp3` | Llanto de larvas humanoides |

---

### 6.3 Archivos de audio para revisión

Los siguientes archivos de audio están referenciados en los scripts pero **NO aparecen** en la estructura de carpetas `/audio` proporcionada. Requieren revisión manual para determinar si son placeholders temporales, faltan por añadir, o deben eliminarse del código.

#### Archivos con ruta no estándar o no encontrados

| Archivo referenciado | Línea en código | Contexto |
|---|---|---|
| `"pasos_susurro.ogg"` | script.rpy:137 | `play sound` — Rodrigo escucha pasos sutiles |
| `"ambiente_tenso.ogg"` | script.rpy:306 | `play music` — Sala de espera abandonada |
| `"daga_desenvainada.ogg"` | script.rpy:388 | `play sound` — Rodrigo saca su daga |
| `"dust_and_echo.ogg"` | script.rpy:1259 | `play ambient` — Caída de Rodrigo |
| `"sfx/goteo_lento.wav"` | script.rpy:913 | `play music` — Pasillo oscuro (transición Cap 3) |
| `"audio/ambience/pasillo_tenso.ogg"` | script_2.rpy:2221, 2566 | `play music` — Pasillo administrativo (Cap 10) |
| `"bgm/nostalgic_party.mp3"` | script_2.rpy:1666 | `play ambient` — Flashback fiesta |
| `"audio/sfx/pasos_lejanos_fade.ogg"` | script_2.rpy:2383 | `play sound fadeout` — Nagi se aleja |
| `"audio/sfx/grito_nagi.ogg"` | script_2.rpy:2395 | `play sound` — Grito de Nagi capturado |
| `"audio/sfx/golpe_pared.ogg"` | script_2.rpy:2398 | `play sound` — Impacto de Nagi contra pared |
| `"audio/sfx/arrastre_humedo.ogg"` | script_2.rpy:2410 | `play sound` — Galaxia arrastra a Nagi |
| `"audio/sfx/grito_desgarrador_nagi.ogg"` | script_2.rpy:2429 | `play sound` — Segundo grito de Nagi |
| `"audio/sfx/golpe_pared_fuerte.ogg"` | script_2.rpy:2434 | `play sound` — Impacto fuerte |
| `"audio/sfx/levantado_suelo_humedo.ogg"` | script_2.rpy:2445 | `play sound` — Galaxia levanta a Nagi |
| `"audio/sfx/caida_techo_pesado.ogg"` | script_2.rpy:2486 | `play sound` — Cucaracha-Guardián cae del techo |
| `"audio/sfx/chasquido_antenas.ogg"` | script_2.rpy:2500 | `play sound` — Sonido de cucaracha |
| `"audio/sfx/golpe_galaxia.ogg"` | script_2.rpy:2514 | `play sound` — Galaxia golpea a Nagi |
| `"audio/sfx/embestida_concreto.ogg"` | script_2.rpy:2521 | `play sound` — Guardián embiste a Rodrigo |
| `"audio/sfx/puerta_metallica_cerrar.ogg"` | script_2.rpy:2530 | `play sound` — Cierre de puerta metálica |
| `"sfx/glass_clink.mp3"` | script_2.rpy:15 | `play sound` — Vasos en fiesta |
| `"sfx/doorbell.mp3"` | script_2.rpy:34 | `play sound` — Timbre |
| `"sfx/door_open.mp3"` | script_2.rpy:82 | `play sound` — Puerta abriéndose (fiesta) |
| `"sfx/wet_whisper.mp3"` | script_2.rpy:165, script.rpy:1417 | `play ambient`/`sound` — Susurro de Galaxia |
| `"sfx/low_drone.mp3"` | script_2.rpy:679 | `play ambient` — Zumbido de tensión |
| `"sfx/metal_impact.mp3"` | script_2.rpy:719 | `play sound` — Golpe metálico |
| `"sfx/ringing.mp3"` | script_2.rpy:729 | `play ambient` — Tinnitus / luces apagadas |
| `"sfx/lights_back.mp3"` | script_2.rpy:752 | `play sound` — Luces encendiéndose |
| `"sfx/room_tone.mp3"` | script_2.rpy:811 | `play ambient` — Habitación abandonada |
| `"sfx/drip_distant.mp3"` | script_2.rpy:1155, 1302 | `play sound` — Gota cayendo (infección) |
| `"sfx/heart_slow.mp3"` | script_2.rpy:1262 | `play sound` loop — Latido lento |
| `"sfx/distant_scratch.mp3"` | script_2.rpy:1463 | `play sound` — Arañazo lejano |
| `"sfx/scratch_wood.mp3"` | script_2.rpy:1535 | `play sound` — Garras sobre madera |
| `"sfx/human_scream.mp3"` | script_2.rpy:1567 | `play sound` — Grito humano (combate) |
| `"sfx/beast_growl.mp3"` | script_2.rpy:1583 | `play sound` — Gruñido animal |
| `"sfx/slash_rough.mp3"` | script_2.rpy:1595 | `play sound` — Corte con daga |
| `"sfx/primal_screech.mp3"` | script_2.rpy:1601 | `play sound` — Chillido salvaje |
| `"sfx/impact_heavy.mp3"` | script_2.rpy:1612 | `play sound` — Impacto pesado |
| `"sfx/stab_repeated.mp3"` | script_2.rpy:1614 | `play sound` — Puñaladas repetidas |
| `"sfx/heavy_breathing.mp3"` | script_2.rpy:1620 | `play ambient` loop — Respiración agitada |
| `"sfx/voices_overlapping.mp3"` | script_2.rpy:2034 | `play sound` — Voces distorsionadas |
| `"sfx/crying.mp3"` | script_2.rpy:2195 | `play sound` — Rodrigo llorando |
| `"sfx/land.mp3"` | script.rpy:111 | `play sound` — Caída al orfanato |
| `"sfx/claw_drag_concrete.mp3"` | script.rpy:605, 791, 820, 1318 | `play sound` — Garras arrastrándose |
| `"sfx/ultimo_aliento.wav"` | script.rpy:830 | `play sound` — Último aliento (muerte) |
| `"sfx/susurro_cercano.wav"` | script.rpy:1163 | `play ambient` — Galaxia susurrando |
| `"sfx/bang_window.mp3"` | script.rpy:1177 | `play sound` — Golpe en ventana |
| `"sfx/heavy_breathing.ogg"` | script.rpy:1276 | `play sound` loop — Respiración de Rodrigo herido |
| `"sfx/monster_parkour.ogg"` | script.rpy:1352 | `play sound` — Galaxia rebotando en paredes |
| `"sfx/glass_break_footsteps.mp3"` | script.rpy:1359 | `play sound` — Pasos en cristales |
| `"sfx/thud.mp3"` | script.rpy:1397 | `play sound` — Galaxia cae tras disparo |
| `"sfx/body_fall_glass.mp3"` | script.rpy:1401 | `play sound` — Cuerpo cayendo en vidrio |
| `"sfx/blood_drip.mp3"` | script.rpy:1439 | `play sound` — Sangre goteando |
| `"sfx/flesh_bubble.mp3"` | script.rpy:1442 | `play sound` — Regeneración de Galaxia |
| `"sfx/heavy_bang.mp3"` | script.rpy:1460, 1504, 1508 | `play sound` — Golpes pesados |
| `"sfx/brick_throw.mp3"` | script.rpy:1466 | `play sound` — Ladrillo lanzado |
| `"sfx/gal_pain_scream.mp3"` | script.rpy:1495 | `play sound` — Grito de dolor de Galaxia |
| `"sfx/hatch_slam_lock.mp3"` | script.rpy:1500 | `play sound` — Escotilla cerrada |
| `"sfx/bone_crack.mp3"` | script.rpy:1563 | `play sound` — Huesos quebrándose |
| `"sfx/bite_crunch.mp3"` | script.rpy:1571 | `play sound` — Mordida fatal |
| `"sfx/rocks_falling_echo.mp3"` | script.rpy:1600 | `play sound` — Piedras cayendo |
| `"sfx/wasp_wings.mp3"` | script.rpy:1652 | `play sound` loop — Aleteo de avispas |
| `"sfx/wasp_screech_attack.mp3"` | script.rpy:1697 | `play sound` — Chillido de avispa |

**Total de archivos para revisión:** 60+

**Recomendación:** Verificar cada línea de código enumerada arriba para determinar si el archivo debe:
1. Ser añadido al proyecto
2. Tener su referencia eliminada del código
3. Ser reemplazado con un archivo existente


---

## 7. RECURSOS VISUALES

### 7.1 Sprites de personajes

**ADVERTENCIA CRÍTICA:** Todos los sprites de personajes definidos en `definitions.rpy` apuntan al **mismo archivo PNG por personaje**, independientemente de la expresión. Por ejemplo:

```python
image rodrigo neutral = "images/sprites/Rodri.png"
image rodrigo molesto = "images/sprites/Rodri.png"
image rodrigo serio = "images/sprites/Rodri.png"
```

**Estado confirmado por el desarrollador:** Estos son **placeholders**. Las variantes de expresión están pendientes de implementación.

#### Sprites definidos (todos placeholders)

- **Rodrigo:** 24 expresiones → `Rodri.png`
- **Luz:** 13 expresiones → `Luz.png`
- **Azura:** 10 expresiones → `Azura.png`
- **Cutipye:** 12 expresiones → `Cutipye.png`
- **Nagi:** 14 expresiones → `Nagi.png`
- **Galaxia:** 8 expresiones → `Galaxia.png`
- **Sujeto herido:** 1 sprite → `Nagi.png` con `TintMatrix("#000000")` (reutilización)
- **Avispa zángano:** 2 expresiones → `avispa_zangano.png`

---

### 7.2 Fondos (backgrounds)

#### Fondos confirmados en `definitions.rpy`

| Variable | Archivo | Uso |
|---|---|---|
| `mainmenubg` | `bg/main_menu.png` | Menú principal |
| `gameover_screen` | `bg/game_over.jpg` | Game Over |
| `foreboding_1` | `bg/pasillo_oscuro.jpg` | Pasillo oscuro |
| `escape_1` | `bg/pasillo_corriendo.jpg` | Pasillo de huida |
| `puerta_abierta_sotano` | `bg/puerta_oxidada.png` | Puerta al sótano |
| `pasillo_lab` | `bg/pasillo_abandonado.jpg` | Laboratorio abandonado |
| `sala_h127_1` | `bg/sala_h127.jpg` | Sala H-127 |
| `puerta_cerrandose` | `bg/puerta_h127.jpg` | Puerta de H-127 |
| `pasillo_huida` | `bg/pasillo_corriendo.jpg` | Pasillo de escape |
| `corredor_amplio` | `bg/pasillo_corriendo.jpg` | Corredor amplio (reutilización) |
| `chase1_1` | `bg/bg_bodega_pan.jpg` | Bodega (persecución) |
| `bg_pasillo_escombros` | `bg/pasillo_corriendo.jpg` | Pasillo bloqueado |
| `bg_cuarto_maquinas` | `bg/puerta_oxidada.png` | Cuarto de máquinas (reutilización) |
| `pasillo_servicio` | `bg/pasillo_oscuro.jpg` | Pasillo de servicio |
| `cocina_puerta` | `bg/puerta_oxidada.png` | Puerta de cocina |
| `cuarto_maquinas_puerta` | `bg/bg_bodega_pan.jpg` | Puerta cuarto máquinas |
| `pistola_primer_plano` | `objects/obj-gun.png` | Pistola encontrada |
| `pasillo_servicio_lucha` | `bg/pasillo_oscuro.jpg` | Combate vs avispa |
| `pasillo_lab_close` | `bg/pasillo_corriendo.jpg` | Pasillo laboratorio (cerca) |
| `pasillo_intermedio` | `bg/pasillo_corriendo.jpg` | Pasillo intermedio |
| `pasillo_dawn` | `bg/pasillo_corriendo.jpg` | Pasillo al amanecer |
| `habitacion_abandonada_dawn` | `bg/habitacion_abandonada.jpg` | Habitación abandonada (amanecer) |
| `vestibulo_dawn` | `bg/vestibulo.jpg` | Vestíbulo principal |
| `ending` | `bg/ending.jpeg` | Pantalla de final |
| `pasillo_oscuridad` | `bg/pasillo_corriendo.jpg` + `BrightnessMatrix(-0.5)` | Pasillo muy oscuro (con filtro) |

**[NOTA DE OPTIMIZACIÓN]** Muchos fondos reutilizan el mismo archivo (`pasillo_corriendo.jpg`, `pasillo_oscuro.jpg`, `puerta_oxidada.png`). Esto puede ser intencional (economía de assets) o placeholder.

---

### 7.3 Objetos

| Variable | Archivo | Uso |
|---|---|---|
| `cuaderno_bitacora` | `images/objects/obj_cuaderno.png` | Bitácora del Dr. Montané |
| `item_gun` | `images/objects/obj-gun.png` | Pistola encontrada en Cap 3 |

---

### 7.4 Muertes (Game Over)

| Variable | Archivo | Contexto |
|---|---|---|
| `spdr1` | `game_over/death_spdr_1.png` | Muerte por araña-huésped |
| `death_mnts_1` | [No definida explícitamente] | Muerte por mantis (opción 1) |
| `death_mnts_2` | [No definida explícitamente] | Muerte por mantis (opción 1 final) |
| `death_mnts_3` | [No definida explícitamente] | Muerte por mantis (opción 2) |
| `death_glx_1` | [No definida explícitamente] | Muerte por Galaxia (escalera) |
| `death_cutipye` | [No definida explícitamente] | Muerte de Cutipye (con efecto `blood_splash`) |

**[PENDIENTE]** Las imágenes de muerte no araña no están definidas en `definitions.rpy`, pero se usan en el código. Requieren confirmación de ubicación de archivos.

---

### 7.5 Escenas especiales

| Referencia en código | Descripción | Estado |
|---|---|---|
| `scene bosque_tarde` | Inicio del juego | [PENDIENTE] ruta de archivo no definida |
| `scene orfanato_exterior1` | Exterior del orfanato | [PENDIENTE] |
| `scene orfanato_exterior2` | Exterior (cerca ventana) | [PENDIENTE] |
| `scene lavanderia_abandonada` | Lavandería | [PENDIENTE] |
| `scene habitacion_cadaver` | Habitación con cadáver | [PENDIENTE] |
| `scene_spdr` | Araña-huésped en techo | [PENDIENTE] |
| `scene sotano_inicial` | Entrada al sótano | [PENDIENTE] |
| `scene sala_proyector` | Sala con proyector | [PENDIENTE] |
| `scene puerta_h127` | Puerta H-127 | [PENDIENTE] |
| `scene sala_h127` | Interior H-127 | [PENDIENTE] |
| `scene escombros_bloqueo` | Pasillo bloqueado | [PENDIENTE] |
| `scene foreboding_2` | Escondite de Rodrigo | [PENDIENTE] |
| `scene habitacion_mantis` | Mantis cazando | [PENDIENTE] |
| `scene pasaje_secreto` | Pasaje oculto | [PENDIENTE] |
| `scene luzdrigo_fb_1` a `_6` | Flashback infancia (6 escenas) | [PENDIENTE] |
| `scene pasillo_dawn` | Pasillo al amanecer | [PENDIENTE] |
| `scene bodega_dark` | Bodega oscura | [PENDIENTE] |
| `scene rodrigo_grab_pistol` | Rodrigo recoge pistola | [PENDIENTE] |
| `scene bg_bodega_pan` | Bodega panorámica | [PENDIENTE] |
| `scene bodega_gal_shadow` | Galaxia acechando | [PENDIENTE] |
| `scene bg_almacen_medico` | Almacén médico | [PENDIENTE] |
| `scene gal_dead_floor` | Galaxia "muerta" en suelo | [PENDIENTE] |
| `scene chase1_reprise` | Galaxia regenerándose | [PENDIENTE] |
| `scene escalera_mano_1`, `_2` | QTE escalera | [PENDIENTE] |
| `scene sala_espera_abandonada` | Sala de espera | [PENDIENTE] |
| `scene pasillo_abandonado` | Pasillo estándar | [PENDIENTE] |
| `scene pasillo_oscuro` | Pasillo oscuro general | [PENDIENTE] |
| `scene orfanato_exterior1` | Exterior 1 | [PENDIENTE] |
| `scene escaleras_con_sombra` | Escaleras al 2do piso | [PENDIENTE] |
| `scene habitacion_intacta` | Habitación del cuidador | [PENDIENTE] |
| `scene galaxia_ventana` | Galaxia en ventana | [PENDIENTE] |
| `scene pasillo_servicio` | Pasillo de servicio | [PENDIENTE] |
| `scene cocina_infestada` | Cocina con larvas | [PENDIENTE] |
| `scene avispa_guardia` | Avispa nodriza | [PENDIENTE] |
| `scene cocina_puerta`, `_2` | Puerta cocina 1 y 2 | [PENDIENTE] |
| `scene fiesta_flashback1` a `_3` | Flashback fiesta (3 escenas) | [PENDIENTE] |
| `scene bg_fiesta_borrosa` | Fiesta distorsionada | [PENDIENTE] |
| `scene bg_habitacion_luz`, `_1` | Cuarto de Luz (2 escenas) | [PENDIENTE] |
| `scene rodrigo_cig_balcony`, `_2` | Balcón con Rodrigo (2 escenas) | [PENDIENTE] |
| `scene balcon_abandonado_night` | Balcón nocturno | [PENDIENTE] |
| `scene habitacion_abandonada_dawn` | Habitación al amanecer | [PENDIENTE] |
| `scene vestibulo_dawn` | Vestíbulo al amanecer | [PENDIENTE] |
| `scene vestibulo_fight_normal` | Combate humano | [PENDIENTE] |
| `scene vestibulo_fight_saturated` | Combate sintetizado | [PENDIENTE] |
| `scene vestibulo_fight_glitch` | Combate brutal | [PENDIENTE] |
| `scene vestibulo_aftermath` | Post-combate | [PENDIENTE] |
| `scene bg pasillo_derruido` | Pasillo derrumbado (Cap 10) | [PENDIENTE] |
| `scene bg_enfermeria_abandonada` | Enfermería (Cap 11) | [PENDIENTE] |
| `scene bg_habitacion_limpia` | Habitación de Galaxia | [PENDIENTE] |

**[CONFIRMADO]** Hay 80+ referencias a escenas en el código sin definición de ruta en `definitions.rpy`. Requieren confirmación de existencia de archivos o creación de assets pendientes.

---

### 7.6 Transforms (efectos visuales)

Ver sección 4.8 del documento para transforms de distorsión.

#### Transforms adicionales relevantes

| Transform | Efecto | Uso |
|---|---|---|
| `slow_scroll` | Scroll vertical lento (130s) | Pasillo largo |
| `fadein_center` | Fade in con zoom (1.5s) | Textos de advertencia |
| `heartbeat` | Zoom pulsante | Latidos; tensión |
| `transform_blink` | Parpadeo (alpha) | Luces parpadeantes |
| `shaking` | Sacudida ligera | Personaje temblando |
| `vjump` | Salto vertical | Sobresalto |
| `slight_zoom` | Zoom 1.05 | Énfasis sutil |
| `credit_sprite_left` | Posición 0.25, 0.5 | Créditos finales |
| `credit_text_right` | Posición 0.75, 0.5 | Créditos finales |
| `centro_izquierda` | xalign 0.35 | Personaje izquierda-centro |
| `centro_derecha` | xalign 0.65 | Personaje derecha-centro |

---


---

## 8. ARCHIVOS PENDIENTES DE REVISIÓN

### 8.1 Música con parámetros sin definir

Los siguientes archivos de música están en la carpeta `/audio/music/` y tienen código definido, pero **faltan parámetros importantes**:

```python
define audio.rodtheme = "music/rodtheme.mp3"   # PENDIENTE: definir loop y convertir a .ogg
define audio.ambiental = "music/ambiental.mp3"  # PENDIENTE: definir loop y convertir a .ogg
```

**Nota del código:** Ambos están marcados en el propio código con comentarios `# DEFINIR LOOP, CAMBIAR A OGG`.

---

### 8.2 Imágenes no definidas en `definitions.rpy` pero usadas en scripts

Se detectaron referencias a escenas e imágenes en los scripts que **no están definidas en `definitions.rpy`**. Ver listado completo en sección 7.5.

---

### 8.3 Ramas de código sin terminar

| Ubicación | Descripción |
|---|---|
| `script_2.rpy: cap_11` (línea ~2720) | Rama `afinidad_cutipye >= 4` (alta) solo tiene `return`; placeholder |
| `script_2.rpy: cap_12` | Solo contiene `return`; sin implementar |
| `script_2.rpy: cap_9` | Hay referencia a `$ riesgo_salud` pero no se usa en el resto del código visible |

---

### 8.4 Contradicciones detectadas

**Contradicción 1: Orfanato "Luz y Esperanza" vs nombre real**
- En la bitácora (Cap 2): el orfanato se llama **"Luz y Esperanza"**
- No hay mención de este nombre en ningún otro lugar del código visible
- El nombre del personaje "Luz" coincide con el nombre del orfanato; **no está claro si es intencional o coincidencia**

**Contradicción 2: Dos versiones de la reacción de Nagi en Cap 10**
El código de `traicion_nagi` contiene dos descripiciones del mismo momento:

- Primera versión (línea ~2369): `"Un grito desgarrador cortó el aire."` seguido del grupo descubriendo que Nagi fue capturado por Galaxia en pasillo.
- Segunda versión (línea ~2428): `"Un grito desgarrador rompe el aire."` con diálogos adicionales de Nagi y Galaxia antes de la captura.

Ambas versiones están bajo la misma `label traicion_nagi` y se ejecutan secuencialmente. Puede ser un error de duplicación pendiente de limpiar.

**Contradicción 3: Instrucción del Dr. Montané en Entrada 09**
La bitácora del Dr. Montané en Cap 2 describe solo 5 Huéspedes Activos ("Cinco sujetos han mostrado tolerancia parcial"). Sin embargo, en la historia se encuentran al menos 6 tipos distintos de criaturas. Si todos los mutantes provienen de H-127, el número no cuadra. Puede ser que el Dr. no contara a todos.

**Contradicción 4: variable `riesgo_salud`**
En Cap 9 se declara `$ riesgo_salud = True/False` según si Rodrigo fuma. Esta variable no aparece usada en ninguna otra parte del código disponible.

---

### 8.5 Labels de carga/guardado

Se referencia `label load_screen` en múltiples pantallas de Game Over:
```python
"Cargar partida":
    jump load_screen
```

Este label no está definido en ninguno de los archivos analizados. **[PENDIENTE]** Puede estar en `screens.rpy` o ser un label built-in de Ren'Py.

---

## 9. CRÉDITOS

**Confirmados en `script_3.rpy` (créditos finales del juego):**

| Rol | Nombre(s) |
|---|---|
| Historia y Dirección | HeartAttack51 |
| Programación | HeartAttack51 |
| Música | Human Entertainment, Capcom, Renegade Kid LLC, @Jambus8550, ryuka |
| Efectos de sonido | Renegade Kid LLC, HeartAttack51, Artistas libres de derechos |
| Ilustraciones | Uraku, Vins2099, Artistas libres de derechos |
| Diseño de personajes: Azura | AlliTati |
| Diseño de personajes: Cutipye | Uraku |
| Diseño de personajes: Dr. Edgar | HeartAttack51 |
| Diseño de personajes: Galaxia | HeartAttack51 |
| Diseño de personajes: Luz | Michi_tamagotchi |
| Diseño de personajes: Nagi | HeartAttack51 |
| Diseño de personajes: Rodrigo | HeartAttack51 |

**Agradecimientos especiales confirmados en código:**
> "La gente que fue parte del proyecto. Canela la perrita. A todos los que no atacaron a la primera criatura."

---

## APÉNDICE: ETIQUETAS (LABELS) PRINCIPALES

Lista de todas las etiquetas de historia identificadas en los scripts:

```
label start
label intro
label splashscreen
label chapter_complete(nombre)
label before_main_menu
label creditos

# Capítulos
label cap_2 → cap_3 → cap_4 → cap_5 → cap_6 → cap_7 → cap_8 → cap_9 → cap_10 → cap_11 → cap_12

# Rutas
label ir_administracion         # Ruta Nagi en Cap 6
label volver_afuera             # Ruta Cutipye en Cap 6
label traicion_nagi             # Nagi abandona (afinidad < 3)
label nagi_no_traiciona         # Nagi permanece leal
label confesion_rodrigo         # Rodrigo confiesa infección
label ocultar_influencia        # Rodrigo oculta infección
label escena_luz_balcon_confesion
label escena_luz_balcon_oculta
label escena_traicion_cutipye   # Galaxia caza a Cutipye

# Secuencias de escape
label escapar_araña
label escape_mnts
label continue_escape_ladder

# Game Over
label game_over_spdr
label game_over_mnts_1
label game_over_mnts_2
label game_over_ladder
```

---

*Fin del documento. Versión generada automáticamente a partir del código fuente en fecha 2026-07-08.*
