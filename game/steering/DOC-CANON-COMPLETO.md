# DOCUMENTACIÓN CANÓNICA — POSSESSED
## Documento de referencia oficial para NotebookLM

> **Metodología de clasificación:**
> - ✅ **Confirmado** — explícito en el código fuente o declarado directamente por el autor
> - 🔶 **Inferido** — deducible del contexto sin declaración explícita
> - ⬜ **Pendiente** — información ausente, no implementada o sin resolver
> - ⚠️ **Contradicción** — dos fuentes del proyecto dan versiones incompatibles
>
> Este documento **no inventa información**. Si una sección carece de datos suficientes, se marca como Pendiente.
> Generado a partir de: `script.rpy`, `script_2.rpy`, `script_3.rpy`, `definitions.rpy`,
> `DOC-universo-canonico.md`, `DOC-mecanicas.md`, `DOC-Cronologia.md`, `DOC-script1.md`,
> `DOC-script2.md`, y fichas de personajes `FICHA-*.md`.
> **Última actualización:** sesión del autor, 2026-07-13.

---

## ÍNDICE

1. [Resumen del proyecto](#1-resumen-del-proyecto)
2. [Estructura técnica](#2-estructura-técnica)
3. [El universo — mundo y lore](#3-el-universo--mundo-y-lore)
4. [Personajes](#4-personajes)
5. [Las criaturas](#5-las-criaturas)
6. [Sistema de juego y mecánicas](#6-sistema-de-juego-y-mecánicas)
7. [Capítulos implementados](#7-capítulos-implementados)
8. [Finales y epílogos](#8-finales-y-epílogos)
9. [Audio](#9-audio)
10. [Recursos visuales](#10-recursos-visuales)
11. [Cronología canónica](#11-cronología-canónica)
12. [Contradicciones detectadas](#12-contradicciones-detectadas)
13. [Pendientes globales](#13-pendientes-globales)
14. [Ideas propuestas compatibles con el lore](#14-ideas-propuestas-compatibles-con-el-lore)

---

## 1. RESUMEN DEL PROYECTO

✅ **Possessed** es una novela visual de horror psicológico desarrollada en Ren'Py. Un grupo de cinco amigos entra a un orfanato abandonado que ocultaba experimentos biológicos ilegales sobre niños, y desencadena una noche de supervivencia y transformación. El jugador controla a Rodrigo, cuyas decisiones afectan las relaciones del grupo y determinan quién sobrevive.

### Datos técnicos confirmados

| Campo | Valor | Fuente |
|---|---|---|
| Motor | Ren'Py | `definitions.rpy` |
| Python | 3.12 | `cache/bytecode-312.rpyb` |
| Resolución nativa | 1920×1080 | steering/tech.md |
| Nombre interno | "Possessed" | `options.rpy` |
| Directorio de guardado | "Possessed-1753492026" | `options.rpy` |
| Icono de ventana | `gui/window_icon.png` | `options.rpy` |
| Velocidad de texto (CPS) | 40 | `options.rpy` |
| Idioma narrativo | Español | scripts |

### Contenido maduro ✅

Violencia explícita, gore, lenguaje fuerte, personaje transgénero, experimentos en menores, abuso de sustancias, muerte de personajes secundarios.

### Créditos de diseño de personajes ✅ (`script_3.rpy`)

| Personaje | Diseñador/a |
|---|---|
| Rodrigo, Nagi, Galaxia | HeartAttack51 |
| Luz | Michi_tamagotchi |
| Cutipye | Uraku |
| Azura | AlliTati |

---

## 2. ESTRUCTURA TÉCNICA

### 2.1 Archivos fuente ✅

| Archivo | Contenido |
|---|---|
| `script.rpy` | Capítulos 1–5 |
| `script_2.rpy` | Capítulos 6–11 + créditos |
| `script_3.rpy` | Pantalla de créditos finales |
| `definitions.rpy` | Personajes, variables, imágenes, transforms, HUD |
| `options.rpy` | Configuración de Ren'Py, audio, build |
| `screens.rpy` | Pantallas UI (menú, guardado, preferencias) |
| `gui.rpy` | Estilos visuales |

### 2.2 Canales de audio ✅

```python
renpy.music.register_channel("ambient", mixer="ambient", loop=True)
```

Canales activos: `music`, `sound`, `voice`, `ambient`

### 2.3 Estado de implementación por capítulo ✅

| Capítulo | Archivo | Estado |
|---|---|---|
| 1–5 | `script.rpy` | Completo |
| 6–9 | `script_2.rpy` | Completo |
| 10 | `script_2.rpy` | Completo (2 rutas) |
| 11 | `script_2.rpy` | Parcial (rama alta sin terminar) |
| 12 | `script_2.rpy` | Solo contiene `return` |
| Créditos | `script_3.rpy` | Completo |

---

## 3. EL UNIVERSO — MUNDO Y LORE

### 3.1 El orfanato "Luz y Esperanza"

✅ Existe un orfanato abandonado llamado **"Luz y Esperanza"**, ubicado en un bosque kilómetros más allá de una autopista. El nombre está confirmado en el encabezado de la Bitácora del Dr. Montané.

✅ El edificio tiene al menos dos plantas, un sótano y un subsuelo. Espacios identificados: lavandería, pasillos con habitaciones numeradas, sala del proyector, sala H-127, vestíbulo principal, ala administrativa, ala de servicio, cocina industrial, cuarto de máquinas, habitaciones de literas, balcón oxidado en el segundo piso, oficina administrativa con mapa en la pared.

✅ El orfanato fue desalojado antes de los eventos de la historia. No hay habitantes humanos cuando el grupo entra.

🔶 Azura menciona el rumor de que fue usado como centro de tortura durante una dictadura. La bitácora del Dr. Montané no menciona ninguna dictadura. Este dato es **información de personaje**, no hecho verificado en ninguna fuente primaria.

✅ Los cambios en la estructura del edificio entre capítulos (rutas bloqueadas, nuevos derrumbes) responden al deterioro físico acumulado de la construcción, **no a ningún fenómeno activo**. Confirmado por el autor.

✅ En todos los finales posibles, el orfanato arde y queda destruido. El fuego es el único elemento que confirma la muerte definitiva de Galaxia.

### 3.2 El Centro de Investigación Subterráneo

✅ Bajo el orfanato existe un **Centro de Investigación Subterráneo**, denominado así en la Bitácora del Dr. Montané. Fue el escenario del Proyecto H-127.

✅ El laboratorio tiene salas numeradas con puertas metálicas. Al menos una sala está identificada como **H-127**. En el vestíbulo hay una sala con proyector, escritorios, archivos húmedos y fotografías clínicas de niños con "la piel incorrecta".

### 3.3 La Fundación Connor

✅ La **Fundación Connor** era una corporación internacional dedicada públicamente a investigación biomédica, farmacéutica y genética.

✅ En secreto poseía el **Departamento H**, responsable del desarrollo de agentes biológicos experimentales con potencial militar y médico. El símbolo grabado en la caja que contenía la bitácora corresponde a este departamento.

✅ Los objetivos declarados internamente del H-127: regeneración de tejidos, adaptación extrema del cuerpo humano, creación de combatientes capaces de sobrevivir en ambientes hostiles.

✅ Tras el incidente de contención, la Fundación ejecutó el **Protocolo de Contingencia Hades**: eliminación de especímenes posibles, destrucción parcial de instalaciones, eliminación de registros. El proyecto fue declarado oficialmente cancelado por "riesgos biológicos inaceptables".

✅ **La Fundación Connor sigue activa en el presente de la historia.** Sus conexiones con el orfanato fueron eliminadas. Ninguna otra división es relevante para los eventos de la historia. Confirmado por el autor.

### 3.4 El Patógeno H-127

✅ Es un **patógeno bioingenierizado**: un virus modificado que edita genes embrionarios y altera la regulación celular. Microorganismos simbióticos aceleran la regeneración, aumentan densidad muscular y ósea, e inhiben la muerte celular.

✅ **Resultado mayoritario:** Mutaciones descontroladas y deterioro neurológico. El 60% de los primeros sujetos murió (Bitácora, Entrada 04). Los tejidos colapsan, los huesos se expanden sin orden, los sistemas vitales no resisten. Algunos cuerpos continuaron respirando durante horas tras el colapso.

✅ **Huéspedes Activos:** En el Día 28, cinco sujetos mostraron tolerancia parcial. Características: aumento de masa muscular, endurecimiento dérmico, cambios oculares, comportamientos erráticos y territoriales. Uno arrancó el rostro de un investigador por contacto visual prolongado.

✅ **Compatibilidad excepcional:** Tipo de respuesta rara en que el huésped obtiene estabilidad y capacidades superiores. Galaxia es el único caso confirmado que completó el proceso dentro del proyecto. Rodrigo posee la misma compatibilidad excepcional.

✅ **Mente colmena:** Galaxia comanda a los demás Huéspedes mediante el patógeno. Esta misma conexión la enlaza con Rodrigo tras la infección. A partir de cierto punto, el vínculo es bidireccional: Galaxia puede percibir los pensamientos de Rodrigo.

✅ **Adaptación continua:** El H-127 se adapta a cada huésped. Cada infección es única.

✅ **Vector de infección de Rodrigo:** Las garras de Galaxia en el costado durante la persecución del Capítulo 4. ⬜ El vector exacto (arañazo, saliva u otra vía) no está confirmado explícitamente en el script.

✅ **Fuego:** El único método confirmado de matar a Galaxia de forma definitiva. En el Capítulo 12, el fuego también rompe el control de mente colmena sobre los demás Huéspedes.

✅ **Balas:** No matan a Galaxia. Sí son efectivas contra otras criaturas.

### 3.5 Contexto temporal de la historia

✅ Los eventos principales ocurren en **una sola noche y la mañana siguiente.** El Capítulo 8 comienza con: *"El amanecer se filtró a través de las ventanas rotas como un velo gris."*

✅ La estación es **otoño.** La apertura describe "una fría tarde de otoño."

✅ El flashback del Capítulo 6 está anclado explícitamente **"tres años atrás"** respecto al presente.

---

## 4. PERSONAJES

---

### 4.1 Rodrigo — Protagonista

| Campo | Dato | Fuente |
|---|---|---|
| Nombre | Rodrigo | ✅ código |
| Apellido | No será mencionado en la historia | ✅ autor |
| Apodo | "Rodri" | ✅ código |
| Edad | 21 años | ✅ autor |
| Variable | `r` | ✅ código |
| Color de texto | `#0c0472` (azul índigo oscuro) | ✅ código |
| Altura | 1.68 m | ✅ autor |
| Complexión | Delgada | ✅ autor |
| Cabello | Castaño, desordenado | ✅ autor + código |
| Ojos | Café chocolate | ✅ autor |
| Ropa (presente) | Camiseta blanca, polo negro, jeans azules rasgados, zapatillas deportivas negras | ✅ autor |

**Personalidad:** Introvertido y callado. Humor seco e irónico. Protector silencioso. Se carga el peso solo. Racional bajo presión hasta que no puede serlo. Sus confesiones emocionales salen inaudibles.

**Arco narrativo:** Se infecta progresivamente con el H-127, transformándose en un ser híbrido humano-cuervo. Lucha por retener su humanidad mientras lidera al grupo hacia la salida.

**Síntomas post-infección confirmados en código:**
sabor dulce-metálico en la boca; motas oscuras en los dedos; herida que no duele como debería; contracción de pupila no reconocida; impulsos de buscar altura; instintos predatorios progresivos; voz interna identificada como Galaxia; una gota negra y móvil que penetra bajo su piel (Cap 7); dedos que se curvan como garras de forma refleja; plumas negras en el cuello bajo estrés extremo que se retraen.

**Destino por ending:** ✅

| Ending | Destino |
|---|---|
| `bad1` | Completa la transformación. Ataca a sus amigos. Muere transformado. |
| `bad2` | Muere transformado. Azura es la única sobreviviente. |
| `neutral1` / `neutral2` | Desaparece en el incendio. |
| `good` | Retiene a Galaxia en el incendio mientras sus amigas escapan. Muere. Los supervivientes escuchan *"el eco de unas alas agitándose entre las llamas."* |

**Relación familiar (en créditos):** El padre lo da por fugado. La madre no habla del tema. Nadie lo busca.

---

### 4.2 Luz — Protagonista secundaria

| Campo | Dato | Fuente |
|---|---|---|
| Nombre | Luz | ✅ código |
| Nombre previo | Lucien | ✅ código |
| Apellido | ⬜ No aparece en ningún archivo | — |
| Edad | 19 años | ✅ autor |
| Variable | `l` / `ln` (flashback) | ✅ código |
| Color de texto | `#fd5353` (rojo-coral) | ✅ código |
| Cabello | Pelirrojo natural | ✅ código |
| Ojos | Celestes | ✅ código |
| Rol | Mujer trans. Novia de Rodrigo. Ancla emocional del protagonista. | ✅ código |

**Personalidad:** Directa sin ser brusca. Empática pero no condescendiente. Valiente bajo presión. Humor natural y afectuoso. Estabilizadora del grupo.

**Muere en todos los endings sin excepción.** ✅

**Últimas palabras según `afinidad_luz`:** ✅

| Afinidad | Línea |
|---|---|
| 0–2 | *"Rodrigo... duele... ¿por qué?"* |
| 3 | *"No... fue un accidente... lo sé..."* |
| 4 | *"Rodrigo, no te culpes... fuiste fuerte por nosotros."* |
| 5 | *"Te... aprecio tanto... no dejes que esto te destruya."* |
| 6 | *"Rodri... Amor... siempre estaré contigo en espíritu."* |
| 7+ | *"Te quiero... Rodrigo. No olvides nuestros momentos... vive por mí."* |

---

### 4.3 Azura — Personaje secundario principal

| Campo | Dato | Fuente |
|---|---|---|
| Nombre | Azura | ✅ código |
| Apellido | Honey | ✅ autor |
| Apodo | "Zu-chan" | ✅ código |
| Edad | 22 años | ✅ autor |
| Variable | `a` | ✅ código |
| Color de texto | `#0f8028` (verde oscuro) | ✅ código |
| Cabello | Castaño claro | ✅ autor |
| Ojos | Esmeralda | ✅ autor + código |

**Personalidad:** Desarmante y cálida. Mediadora del grupo. Serena bajo presión (con esfuerzo). Internaliza información difícil sin compartirla. Optimismo funcional como estrategia de supervivencia.

**Rol único:** Es el único personaje que puede ser la **única superviviente** en el ending `bad2`. En el ending `good` supera el trauma con apoyo familiar.

**Nota:** Azura lee la Entrada 09 (Huéspedes Activos) en el Cap 7, la dobla en silencio y la guarda en el bolsillo sin decir nada al grupo. ✅

---

### 4.4 Cutipye — Personaje secundario principal

| Campo | Dato | Fuente |
|---|---|---|
| Nombre | Cutipye | ✅ código |
| Apellido | Hayashi | ✅ autor |
| Apodo | "Cuty" | ✅ código |
| Edad | 20 años | ✅ autor |
| Variable | `c` | ✅ código |
| Color de texto | `#2dff5a` (verde brillante) | ✅ código |
| Cabello | Castaño claro | ✅ autor |
| Ojos | Verde menta | ✅ autor |
| Altura | 1.60 m | ✅ autor |

**Personalidad:** Humor como mecanismo de aguante. Directa sin rodeos. Pragmatismo en crisis. Afecto real conviviendo con miedo real en la misma frase. Se rompe cuando ya no puede sostener más.

**Dato importante:** Cutipye fue **quien propuso visitar el orfanato**. Confirmado en el Cap 11, ruta alta. ✅

**Umbral de traición:** `afinidad_cutipye < 4` → Cap 11, ataque verbal a Rodrigo, muerte a manos de Galaxia. `cuty_dead = True`. ✅

---

### 4.5 Nagi — Personaje secundario principal

| Campo | Dato | Fuente |
|---|---|---|
| Nombre | Nagi | ✅ código |
| Apellido | Katashi | ✅ código (`script_3.rpy`) |
| Edad | 22 años | ✅ autor |
| Variable | `n` | ✅ código |
| Color de texto | `#7b2cbf` (púrpura medio) | ✅ código |
| Cabello | Negro opaco | ✅ autor |
| Ojos | Púrpura | ✅ autor |
| Altura | 1.75 m | ✅ autor |
| Pareja romántica | Cutipye | ✅ autor |

**Personalidad:** Extrovertido y ruidoso por diseño. Lee a Rodrigo con precisión. Impulsivo y directo. Protector ambiguo (salvó a Rodrigo en la fiesta y también lo puso en riesgo esa misma noche). Cobardía disfrazada de rabia en el momento crítico.

**Umbral de traición:** `afinidad_nagi < 3` → Cap 10, abandona al grupo, Galaxia lo captura. `nagi_dead = True`. ✅

**Post-supervivencia (ending good):** "Nunca volvió a ser el mismo." Deja de ser impulsivo para convertirse en alguien temeroso y precavido. ✅

**Conexión familiar con Galaxia:** ✅ **Confirmado por el autor.**
Nagi Katashi y Shio Katashi (Galaxia) son **primos lejanos**, ambos descendientes de una familia de inmigrantes. La conexión es intencionalmente ambigua para su desarrollo en una eventual secuela.

---

### 4.6 Galaxia (Shio Katashi) — Antagonista principal

| Campo | Dato | Fuente |
|---|---|---|
| Nombre adoptado | Galaxia | ✅ código |
| Nombre real | Shio Katashi | ✅ código (Biblia, Cap 7) |
| Apellido | Katashi | ✅ código |
| Edad aproximada | ~24–25 años (inoculada a los 9–10, lleva 15 años en el orfanato) | ✅ autor |
| Variable | `g` | ✅ código |
| Color de texto | `#390169` (púrpura muy oscuro) | ✅ código |
| Fuente especial | `fonts/HelpMe.ttf` (exclusiva de este personaje) | ✅ código |
| Música diferenciada | `audio.chase1` — persecución específica de Galaxia | ✅ código |

**Origen:** Huérfana interna del orfanato. Inoculada con H-127 como parte del Proyecto. Desarrolló compatibilidad excepcional — el mismo tipo que posee Rodrigo.

**Apariencia post-mutación:** Postura encorvada como hiena. Ojos luminiscentes heterocromáticos (originalmente negros). Orejas felinas. Cola. Dientes afilados. Garras largas. ✅ (autor + código)

**Capacidades confirmadas:**
- Regeneración de disparos directos. Las balas no la matan.
- Movimiento por paredes y techo.
- Fuerza y agilidad sobrehumanas.
- Comunicación telepática con Rodrigo (vía H-127).
- Comando telepático de los demás Huéspedes.
- Voz proyectada a distancia sin presencia física.

**Biblia personal:** Jeremías 12:9 subrayado repetidamente hasta rasgar el papel. Sus propias palabras: *"Yo también recé… Pedí ser salvada. Pero Él me convirtió en la hiena."* ✅

**Último acto conocido (ending good):** Dice *"Shio"* — su propio nombre previo. Primera vez que lo pronuncia en quince años. ✅ (autor)

**Muerte:** Solo el fuego la mata definitivamente. Muere en todos los endings. ✅

**Relación con el grupo en general:** Son presas con función instrumental para presionar a Rodrigo. Captura a Nagi (Cap 10) y a Cutipye (Cap 11) inmediatamente después de que el grupo se fractura.

**Nota sobre el cuaderno (easter egg):** ⬜ Existe un objeto planeado — un cuaderno pequeño y cubierto de polvo sin título — que documenta la disolución de Shio y el nacimiento de Galaxia. Accesible solo en una ruta easter egg. No implementado en el script actual.

---

### 4.7 Personajes secundarios

#### Dr. Édgar L. Montané
✅ Director registrado del Proyecto H-127. Único investigador nombrado en la bitácora. ⬜ No aparece en persona en ningún capítulo implementado.

#### El Sujeto Herido
✅ Sin nombre. Agonizante en la sala H-127. Nombra a Galaxia y advierte al grupo antes de morir. Sus últimas palabras: *"No se puede huir de ella."*

---

## 5. LAS CRIATURAS

Todas son ex-huérfanos del orfanato transformados por el H-127. ✅

### 5.1 Araña-Huésped
✅ Primera criatura sobrenatural. Colgada del techo, desafía la gravedad. Descrita como "algo que alguna vez fue humano." Uno de los cinco Huéspedes Activos del Proyecto.

### 5.2 Mantis-Huésped
✅ Antenas que detectan el miedo. Hojas afiladas en los brazos. Seis ojos visibles. Método metódico de caza. Aparece en Cap 2; una alarma la distrae y la hace abandonar la búsqueda de Rodrigo. Uno de los cinco Huéspedes Activos.

### 5.3 Avispa Nodriza
✅ Cuida un nido en la cocina industrial. Reacciona con instinto materno/asesino cuando las larvas son perturbadas. Uno de los cinco Huéspedes Activos.

### 5.4 Avispa Zángano
✅ Combate de tres fases QTE en el pasillo del ala de servicio (Cap 5): Cutipye lanza extintor → Nagi golpea con bate → Luz remata con barra. Uno de los cinco Huéspedes Activos.

### 5.5 Huésped-Rata
✅ Vestíbulo principal (Cap 8). Piel estirada, espinazos expuestos, ojos de "rubí podrido." Patas traseras demasiado largas para su torso. Ataca al personaje con menor afinidad en el grupo. Orden de prioridad: `nagi (0) > cutipye (1) > azura (2) > luz (3)`. ✅ (código Python, `script_2.rpy`)

### 5.6 El Parásito (Cucaracha-Guardián)
✅ Cap 10, bloquea el pasillo solo cuando Nagi es capturado (`afinidad_nagi < 3`). Apariencia: humano mitad cucaracha, caparazón brillante, brazos con garras de cucaracha, ojos como brasas. Comportamiento: se esconde, se alimenta de carne en descomposición, huye cuando es perturbado, solo ataca si está acorralado. Resistencia excepcional. Uno de los Huéspedes del Proyecto H-127.

### 5.7 Larvas humanoides
✅ En la cocina industrial. Tamaño de perros grandes. Pálidas, húmedas. Pequeñas manos atrofiadas y rostros humanos a medio formar que boquean en silencio. Sujetos del H-127 que no sobrevivieron la mutación completa.

---

## 6. SISTEMA DE JUEGO Y MECÁNICAS

### 6.1 Variables globales ✅ (`definitions.rpy`)

```python
default afinidad_luz = 0
default afinidad_azura = 0
default afinidad_cutipye = 0
default afinidad_nagi = 0
default estado_mental = 0
default tiempo_escape = 0      # timer de escape del Cap 12
default mostrar_hud = True     # solo debug — eliminado en producción
default label_nagi = False     # True si se siguió ruta de Nagi en Cap 6
default nagi_dead = False
default cuty_dead = False
default riesgo_salud = False   # True si Rodrigo aceptó los vicios en el flashback de Cap 9
default ending_type = "good"   # valor por defecto intencional
```

### 6.2 Sistema de afinidad ✅

Cuatro variables independientes (una por personaje). Los cambios son **invisibles durante el juego**. Afectan: diálogos, rutas de traición/lealtad, combate de la Rata (objetivo = afinidad más baja), epílogos en créditos.

**Thresholds confirmados:**

| Personaje | Threshold | Consecuencia |
|---|---|---|
| Nagi | < 3 | Traición y muerte en Cap 10 |
| Cutipye | < 4 | Traición y muerte en Cap 11 |
| Luz | ≥ 5 | Epílogo positivo en créditos |

⬜ No existe un valor máximo de afinidad definido en el código.

### 6.3 Sistema de estado mental ✅

`estado_mental` rastrea el deterioro psicológico y la transformación de Rodrigo.

**Reglas:** Sube con decisiones de pánico, ocultamiento y trauma. Baja con decisiones racionales (−1). No puede descender de 0. No tiene límite superior.

**Umbrales y efectos:**

| Valor | Efecto en combate (Cap 8) | Evaluación en créditos |
|---|---|---|
| < 10 | Combate humano: torpe, desesperado | "Rodrigo mantuvo la calma" |
| 10–14 | Combate sintetizado: agilidad antinatural, instintos de cuervo | "Rodrigo estuvo bajo presión" |
| ≥ 15 | Combate predador: brutal, preciso, sin emoción | "Rodrigo sucumbió al estrés" |

**Amanecer del Cap 8:** +1 automático, sin decisión del jugador. ✅

**Multiplicador `riesgo_salud`:** Si `riesgo_salud = True` (Rodrigo aceptó los vicios en el flashback del Cap 9), un multiplicador de 1.25 amplifica el avance de la infección en capítulos posteriores. ✅

### 6.4 Sistema de QTE ✅

Modal. Botón visible con temporizador invisible. El tiempo disminuye en cada fase consecutiva. No hay segundo intento.

**QTEs confirmados:**

| QTE | Capítulo | Fases | Tiempo | Fallo |
|---|---|---|---|---|
| Escalera | 4 | 1 | 3 seg | `game_over_ladder` |
| Avispa Zángano | 5 | 3 | 3 / 2.5 / 2 seg | `game_over_wasp` |
| Escape final | 12 | 5 | 90 seg globales | ending `bad1` |

⬜ Número total de QTEs en la partida completa: pendiente.

### 6.5 Game overs confirmados ✅

| ID | Capítulo | Causa |
|---|---|---|
| `game_over_spdr` | 1 | Insistir en atacar a la Araña |
| `game_over_mnts_1` | 2 | Acercarse a la Mantis |
| `game_over_mnts_2` | 2 | Esconderse bajo la cama |
| `game_over_ladder` | 4 | No completar QTE en 3 seg |
| `game_over_wasp` | 5 | Fallar cualquier fase del QTE del Zángano |

⬜ Número total de game overs: pendiente.

**Nota:** El game over del Zángano muestra la muerte de Azura, no de Rodrigo. Es el único game over confirmado donde muere un personaje secundario en lugar del protagonista. ✅

### 6.6 Sistema de guardado ✅

Slot único: `"1-1"`. Los guardados automáticos (encuentros) usan el mismo slot que el guardado manual al fin de capítulo.

| Etiqueta | Ubicación |
|---|---|
| "Encuentro 1" | Antes de la Araña (Cap 1) |
| "Encuentro 2" | Antes de la Mantis (Cap 2) |
| "Encuentro 3" | Antes de Galaxia en ventana (Cap 3) |
| "Encuentro 4" | Antes de la persecución del sótano (Cap 4) |
| "Encuentro 5" | Antes de las Avispas (Cap 5) |

### 6.7 HUD de desarrollo ✅

Controlado por `mostrar_hud`. Muestra afinidades y `estado_mental` en tiempo real. **Será eliminado en versión de producción.** Confirmado por el autor.

---

## 7. CAPÍTULOS IMPLEMENTADOS

### Cap 1 — Exploración inicial (`script.rpy`)
✅ El grupo entra al orfanato por una ventana rota. Nagi la rompe con el bate. Se dispersan en la lavandería. Rodrigo escucha pasos pequeños y busca a sus compañeras. Encuentra a Luz pálida, descubren la Araña-Huésped en el techo, huyen. Encuentran la mochila de Cutipye con manchas de sangre. Rodrigo oculta al grupo la Entrada 04 de la bitácora (60% de muertes). Galaxia aparece en ventana. El piso cede y Rodrigo cae al subsuelo.
**Decisiones clave:** atacar/huir de la araña, reconfortar a Luz, reacción al rumor de dictadura.

### Cap 2 — El sótano (`script.rpy`)
✅ Rodrigo y Luz bajan al laboratorio. Leen la Bitácora del Dr. Montané (Entradas 01 y objetivo). Encuentran al Sujeto Herido que nombra a Galaxia y advierte antes de morir. Galaxia cierra una puerta y anuncia el juego. Rodrigo se esconde de la Mantis-Huésped. Una alarma lejana la distrae. Luz descubre un pasadizo secreto al ala sur.
**Decisiones clave:** cómo reaccionar a Luz tras la Araña, tres opciones ante la Mantis (solo "armario" es segura).

### Cap 3 — Flashback de infancia (`script.rpy`)
✅ Flashback: patio escolar, Lucien (niño) se sienta junto a Rodrigo (niño aislado). Rodrigo dice su nombre por primera vez. Regreso al presente: el grupo se reúne con Azura. Luz encuentra una pistola en una habitación intacta del segundo piso. El suelo cede, Rodrigo cae al subsuelo. Nagi y Cutipye lo ven desde arriba.
**Nota:** Las decisions de este capítulo no impactan variables de afinidad o estado mental.

### Cap 4 — Persecución (`script.rpy`)
✅ Rodrigo solo en el subsuelo. Primer encuentro directo con Galaxia. Le dispara en la frente: ella se regenera. Nueva persecución. QTE de la escalera (3 seg). Rodrigo dispara a Galaxia en el abdomen a quemarropa. Escapa herido. **Momento de la infección del H-127:** las garras de Galaxia en su costado.

### Cap 5 — Reunión (`script.rpy`)
✅ El grupo busca a Rodrigo. Descubren el nido de Avispas en la cocina. Combate contra la Avispa Zángano (QTE 3 fases). Luz remata a la criatura con la barra metálica y no la suelta cuando deja de moverse. El grupo la observa. Nadie dice nada. Se reúnen con Rodrigo en el cuarto de máquinas.

### Cap 6 — División (`script_2.rpy`)
✅ Flashback: casa de Cutipye, "tres años atrás." Luz se presenta como ella misma ante el grupo. Rodrigo ya lo sabía. De vuelta al presente: Rodrigo herido con síntomas (sabor dulce-metálico, marcas oscuras, pupila contraída). Voz de Galaxia: *"Casi… casi mía…"*. Debate Nagi (ala administrativa) vs. Cutipye (retroceder). Rodrigo decide.
**Dos rutas:** `ir_administracion` (Nagi) / `volver_afuera` (Cutipye). Ambas confluyen en Cap 7.

### Cap 7 — Oscuridad y confesión (`script_2.rpy`)
✅ Las luces se apagan. Galaxia habla directamente a Rodrigo. El grupo encuentra la Biblia con el nombre "Shio Katashi" y el versículo de Jeremías 12:9. Azura guarda la Entrada 09 en silencio. Rodrigo sale al balcón oxidado. Escucha un latido que no es el suyo. Decisión clave: confesar la influencia o mantenerla en secreto. Independientemente de la elección, una gota de sustancia negra se absorbe por su piel.
**Ruta confesión:** +2 a todas las afinidades. **Ruta secreto:** +2 a estado_mental.

### Cap 8 — Amanecer (`script_2.rpy`)
✅ El amanecer. Rodrigo despierta con impulsos de buscar altura. Pensamientos predatorios que no reconoce como suyos. La Rata-Huésped ataca al personaje de menor afinidad. Rodrigo interviene. El estilo del combate varía según `estado_mental` (humano / sintetizado / predador). El grupo lo observa con miedo.
**Evento automático:** +1 a `estado_mental` sin decisión del jugador.

### Cap 9 — Flashback de fiesta / Muerte de Luz (`script_2.rpy`)
✅ Flashback completo: fiesta organizada por Nagi. Rodrigo bebe, Nagi le ofrece cannabis por primera vez. Rodrigo colapsa. Nagi lo sostiene. Azura coordina el rescate por teléfono desde fuera. Rodrigo despierta en casa de Luz. De vuelta al presente: en el vestíbulo, la influencia de Galaxia se activa sobre Rodrigo. Luz da un paso hacia él y extiende la mano. Rodrigo reacciona al contacto como ante una amenaza. **Luz muere.** La risa de Galaxia no vuelve. *"El silencio es peor."*

### Cap 10 — Traición o lealtad de Nagi (`script_2.rpy`)
✅ Nagi confronta a Rodrigo. Dos rutas según `afinidad_nagi`:
- **< 3:** Nagi abandona al grupo, Galaxia lo captura. El Huésped Cucaracha bloquea el pasillo. `nagi_dead = True`.
- **≥ 3:** Nagi explota pero no cruza la puerta. Acepta la mediación de Azura. El grupo sigue unido.

### Cap 11 — Traición o mea culpa de Cutipye (`script_2.rpy`)
✅ Dos rutas según `afinidad_cutipye`:
- **< 4:** Cutipye ataca verbalmente a Rodrigo con crueldad calculada. Sale sola. Galaxia la intercepta en una habitación impecable. Cutipye dispara la pistola cuatro veces. Galaxia se regenera. `cuty_dead = True`.
- **≥ 4:** ⬜ Cutipye asume la responsabilidad de haber traído al grupo. Escena planeada, sin implementación completa en el script actual.

✅ Azura identifica el fuego como herramienta. El incendio comienza.

### Cap 12 — Sin implementar
⬜ El label `cap_12` solo contiene `return`. No hay narrativa.

---

## 8. FINALES Y EPÍLOGOS

### 8.1 Variable y lógica ✅

```python
default ending_type = "good"  # valor por defecto intencional
```

La asignación de `ending_type` ocurre en Cap 12 (sin implementar). El valor por defecto `"good"` es intencional: el ending bueno es el estado base, modificado por las decisiones del jugador.

**Lógica confirmada (Cap 12, según DOC-script2.md):**
- Si `tiempo_escape` llega a 0: ending `bad1`
- Si el grupo escapa y `estado_mental >= 16`: ending `bad1` (Rodrigo ataca al grupo)
- Si `estado_mental >= 11`: ending neutral (Rodrigo desaparece en el humo)
- Si `estado_mental < 11`: ending `good` (Rodrigo retiene a Galaxia)

### 8.2 Descripción de cada ending ✅ (`script_3.rpy`)

**`bad1` — El incendio consume a todos**
El orfanato arde durante la madrugada. Cuando llegan las autoridades no hay sobrevivientes. Todos son listados como desaparecidos. *"Algunos vecinos aseguran que, en las noches más silenciosas, aún pueden oír algo moviéndose entre los restos calcinados."*

**`bad2` — Solo Azura sobrevive**
Azura escapa. Semanas después apenas puede dormir. Se pregunta si realmente escapó. Asiste a terapia sin superar el trauma. Usa la experiencia como motor para su música.

**`neutral1` — Varios sobrevivientes, historia enterrada**
Varios sobrevivientes observan el incendio desde la distancia. Cuando llegan las sirenas, ya se habían marchado. *"Algunas historias son demasiado horribles para contarlas."*

**`neutral2` — Tres sobrevivientes, versión oficial falsa**
El incendio es atribuido a un accidente. Los tres sobrevivientes nunca corrigen esa versión. *"Después de lo que vieron aquella noche, sabían que nadie les creería."*

**`good` — Rodrigo retiene a Galaxia**
Azura, Nagi y Cutipye sobreviven. Rodrigo retiene físicamente a Galaxia en el incendio. Su último acto es humano. *"A veces, cuando el viento sopla fuerte entre los árboles, juran escuchar el eco de unas alas agitándose entre las llamas. Como si algo aún protegiera aquel lugar."*

### 8.3 Epílogos individuales por ending ✅ (`script_3.rpy`)

**Rodrigo:**
- `bad1`: La familia acepta su desaparición en silencio. Nadie lo busca.
- Otros endings: La familia no investiga, pero sus amigos conocen la verdad.

**Luz:** Muere en todos los endings.
- `bad1`: Caso cerrado por falta de pruebas.
- `afinidad_luz >= 5`: Investigación familiar abierta. Los sobrevivientes asisten al funeral.
- `afinidad_luz < 5`: El epílogo sugiere que la relación distante de Rodrigo contribuyó a su destino.

**Azura:**
- `bad1`: Familia espera su regreso.
- `bad2`: Sobrevive; trauma sin superar; usa la experiencia como motor musical.
- Otros endings: Supera el trauma con apoyo de familia y amigos.

**Nagi:**
- `bad1`: Sin cuerpo ni pistas. Habitación intacta.
- `nagi_dead = True` (y no bad1): Búsqueda familiar sin resultado.
- Sobrevive: "Nunca volvió a ser el mismo."

**Cutipye:**
- `bad1`: Hermetismo absoluto. Familia se muda de la ciudad.
- `cuty_dead = True` (y no bad1): Funeral privado, sin investigación.
- Sobrevive: Se vuelve retraída y distante. Se muda para alejarse de los recuerdos.

---

## 9. AUDIO

### 9.1 Música de fondo ✅ (`definitions.rpy`)

| Variable | Archivo | Loop point | Uso narrativo |
|---|---|---|---|
| `audio.main_menu` | `music/menu.ogg` | 28.25s | Menú principal, escenas reflexivas |
| `audio.forest` | `music/bosque.mp3` | — | Inicio (bosque) |
| `audio.melody` | `music/melodia.ogg` | — | Tensión ligera |
| `audio.story` | `music/historia.ogg` | 41.53s | Lectura de bitácoras |
| `audio.curse` | `music/maldicion.ogg` | — | Game over, momentos de horror |
| `audio.chase` | `music/persecucion.ogg` | 62.8s | Persecuciones generales |
| `audio.chase1` | `music/persecucion (galaxia).ogg` | 34.5s | Persecución específica de Galaxia |
| `audio.flashback` | `music/flashback.ogg` | 28.00s | Flashbacks con filtro sepia |
| `audio.credits` | `music/creditos.mp3` | — | Créditos finales |
| `audio.rodtheme` | `music/rodtheme.mp3` | ⬜ Sin definir | Tema de Rodrigo, momentos introspectivos |
| `audio.ambiental` | `music/ambiental.mp3` | ⬜ Sin definir | Ambientación general |

⬜ `rodtheme` y `ambiental` están marcados en el código como pendientes de conversión a `.ogg` y definición de loop.

### 9.2 Efectos de sonido definidos ✅

Los siguientes SFX están definidos en `definitions.rpy` y tienen archivos existentes en `/audio/sfx/`:

`shock`, `slash`, `run`, `flies`, `crack`, `walk0`, `break_glass`, `break_wood`, `wood_creak`, `door_break`, `door_slam`, `thud`, `door_open`, `door_close`, `scream1`, `chptr_cmplt`, `glx_laugh`, `paper_flip`, `alarm`, `gunshot`, `walk`, `land`, `objfall`, `nailtap`, `larvcry`

### 9.3 Audio referenciado en scripts pero no encontrado en `/audio` ⬜

Los siguientes archivos aparecen en los scripts pero no están en la carpeta `/audio/sfx/`. Requieren revisión manual:

`pasos_susurro.ogg`, `ambiente_tenso.ogg`, `daga_desenvainada.ogg`, `wet_whisper.mp3`, `low_drone.mp3`, `metal_impact.mp3`, `ringing.mp3`, `lights_back.mp3`, `room_tone.mp3`, `drip_distant.mp3`, `heart_slow.mp3`, `distant_scratch.mp3`, `scratch_wood.mp3`, `human_scream.mp3`, `beast_growl.mp3`, `slash_rough.mp3`, `primal_screech.mp3`, `impact_heavy.mp3`, `stab_repeated.mp3`, `heavy_breathing.mp3`, `voices_overlapping.mp3`, `crying.mp3`, `claw_drag_concrete.mp3`, `ultimo_aliento.wav`, `susurro_cercano.wav`, `bang_window.mp3`, `heavy_breathing.ogg`, `monster_parkour.ogg`, `flesh_bubble.mp3`, `gal_pain_scream.mp3`, `hatch_slam_lock.mp3`, y una lista extensa de efectos para los caps 10–11 con rutas `audio/sfx/` que no coinciden con la estructura actual.

*(Lista completa en `DOCUMENTACION_CANONICA.md`, sección 6.3)*

---

## 10. RECURSOS VISUALES

### 10.1 Sprites — estado actual ⬜

Todos los personajes usan actualmente el **mismo archivo PNG placeholder** por personaje. No hay sprites diferenciados por expresión.

| Personaje | Archivo placeholder |
|---|---|
| Rodrigo | `images/sprites/Rodri.png` |
| Luz | `images/sprites/Luz.png` |
| Azura | `images/sprites/Azura.png` |
| Cutipye | `images/sprites/Cutipye.png` |
| Nagi | `images/sprites/Nagi.png` |
| Galaxia | `images/sprites/Galaxia.png` |

### 10.2 Sprites de estado "muerto" ✅

Todos los personajes principales tienen un sprite `dead` implementado mediante `TintMatrix("#000000")` sobre el sprite base.

### 10.3 Discrepancias de sprites pendientes ⬜

- `galaxia sentada_sonriendo` — usado en Cap 11 pero **no está definido** en `definitions.rpy`. Debe añadirse.
- `galaxia headshot` — definido en `definitions.rpy` pero reemplazado narrativamente por `gal_dead_floor`. Candidato a eliminar.
- Cutipye Cap 11: expresiones `media_sonrisa`, `mirada_reojo`, `sorpresa_fingida`, `seria`, `fria`, `cansada` — usadas en script pero **no definidas** en `definitions.rpy`.

### 10.4 Transforms visuales ✅ (`definitions.rpy`)

| Transform | Efecto |
|---|---|
| `distortion_light` | Saturación +40%, zoom y oscilación suave |
| `distortion_heavy` | Saturación +80%, glitch de color, zoom agresivo |
| `sepia_filter` | Flashbacks (SepiaMatrix) |
| `blanco_y_negro` | Pantalla de advertencia (SaturationMatrix 0.0) |
| `oscuro` | Escenas oscuras (BrightnessMatrix −0.5) |
| `heartbeat` | Efecto de latido pulsante |
| `shaking` | Temblor de sprite |
| `vjump` | Salto vertical breve |
| `slow_scroll` | Desplazamiento lento vertical (130 segundos) |

---

## 11. CRONOLOGÍA CANÓNICA

*(Solo hechos confirmados ✅ o inferidos 🔶. Sin fechas absolutas: toda la cronología es relativa.)*

### Pasado remoto — El experimento

**E-01** ✅ El Dr. Montané inicia el Proyecto H-127. Niños huérfanos son seleccionados como "prescindibles."

**E-02** ✅ Día 11. El 60% de los sujetos muere. Mutaciones inestables, colapso tisular, cámaras frías saturadas.

**E-03** ✅ Día 28. Cinco sujetos muestran tolerancia parcial. Son llamados "Huéspedes Activos." Uno arranca el rostro de un investigador por contacto visual prolongado.

**E-04** ✅ Incidente de contención. La Fundación Connor ejecuta el Protocolo Hades. El proyecto es clausurado y declarado fracasado.

**E-05** 🔶 Algunos especímenes sobreviven. Parte de la investigación queda dispersa por el edificio. Galaxia permanece en el orfanato.

**E-06** 🔶 Shio Katashi abandona su identidad. Se autodenomina Galaxia. El orfanato se convierte en su territorio exclusivo. Permanece ahí **15 años**. ✅ (autor)

---

### Pasado medio — Infancia de los protagonistas

**E-07** ✅ En el patio de una escuela, Lucien (niño) encuentra a Rodrigo (niño aislado). Semanas después, Rodrigo pronuncia su nombre por primera vez. Lucien responde: *"Ya lo sabía. Pero me alegra oírlo de ti."*

---

### Pasado reciente — Adolescencia

**E-08** 🔶 El grupo se forma durante la secundaria. Azura y Cutipye son el núcleo fundador. Nagi llega a través de Cutipye. Rodrigo y Luz llegan después.

**E-09** ✅ **"Tres años atrás"** (texto explícito del Cap 6): En la casa de Cutipye, Lucien se presenta públicamente como Luz. Rodrigo ya lo sabía. Le dice: *"Te ves hermosa, Luz."*

**E-10** 🔶 En una fiesta organizada por Nagi, Rodrigo bebe en exceso y consume cannabis por primera vez. Colapsa. Nagi lo sostiene. Azura coordina el rescate por teléfono. Rodrigo despierta en casa de Luz.

---

### Presente — La noche en el orfanato

*(Una sola noche y la mañana siguiente — confirmado por el amanecer explícito del Cap 8)* ✅

**E-11** ✅ Tarde de otoño. El grupo entra al orfanato por una ventanilla rota. Rodrigo es el único escéptico.

**E-12** ✅ El grupo se dispersa. Rodrigo escucha pasos pequeños, busca a sus amigas, encuentra a Luz pálida. Descubren la Araña-Huésped. Huyen. *(Cap 1)*

**E-13** ✅ Rodrigo y Luz bajan al sótano. Leen la Bitácora del Dr. Montané. Encuentran al Sujeto Herido, quien nombra a Galaxia y muere. Galaxia cierra una puerta y anuncia el juego. *(Cap 2)*

**E-14** ✅ Rodrigo se esconde de la Mantis tras el armario. Una alarma lejana la distrae. Rodrigo y Luz se reúnen. Luz descubrió un pasadizo secreto. *(Cap 2)*

**E-15** ✅ El grupo se reúne con Azura. Luz encuentra la pistola. Rodrigo lee la Entrada 04 y la oculta. Galaxia aparece en ventana. El piso cede. Rodrigo cae al subsuelo. *(Cap 3)*

**E-16** ✅ Rodrigo dispara a Galaxia en la frente. Ella se regenera. **Momento de la infección:** garras de Galaxia en el costado de Rodrigo al escapar por la escotilla. *(Cap 4)*

**E-17** ✅ El grupo atraviesa la cocina-nido. Combate QTE contra la Avispa Zángano. Luz golpea a la criatura con la barra más veces de las necesarias. Nadie lo comenta. Se reúnen con Rodrigo en el cuarto de máquinas. *(Cap 5)*

**E-18** ✅ Flashback: Luz se presenta como ella misma ("tres años atrás"). Presente: Rodrigo muestra síntomas. Debate de ruta. Rodrigo decide. *(Cap 6)*

**E-19** ✅ Las luces se apagan. Voz de Galaxia. Descubren la Biblia con "Shio Katashi." Azura guarda la Entrada 09 en silencio. Rodrigo fuma solo en el balcón: elige confesar o callar. La gota negra se absorbe bajo su piel. *(Cap 7)*

**E-20** ✅ El amanecer. Rodrigo despierta con impulsos predatorios. La Rata-Huésped ataca al personaje de menor afinidad. Rodrigo la mata. El grupo lo observa con miedo. *(Cap 8)*

**E-21** ✅ Flashback completo de la fiesta y la sobredosis. Presente: en el vestíbulo, Galaxia influye sobre Rodrigo. Luz extiende la mano. Rodrigo reacciona como ante una amenaza. **Luz muere.** *(Cap 9)*

**E-22** ✅ Nagi traiciona o permanece según `afinidad_nagi`. Si traiciona: Galaxia lo captura, el Huésped Cucaracha bloquea el pasillo. `nagi_dead = True`. *(Cap 10)*

**E-23** ✅ Cutipye traiciona o asume su responsabilidad según `afinidad_cutipye`. Si traiciona: Galaxia la intercepta en una habitación impecable. `cuty_dead = True`. Azura identifica el fuego como herramienta. El incendio comienza. *(Cap 11)*

**E-24** ⬜ Persecución final. Cinco QTEs. Timer de 90 segundos. Confrontación con Galaxia. Los finales se bifurcan. *(Cap 12 — sin implementar)*

---

### Desenlace — Post-incendio

✅ El orfanato queda destruido. Galaxia muere en todos los endings. Las investigaciones familiares y silencios varían según qué personajes sobreviven.

---

## 12. CONTRADICCIONES DETECTADAS

### C-01 — Azura en la fiesta: presencia física ambigua ⚠️

**Fuentes:** `script_2.rpy` (Cap 9) vs. FICHA-Azura.md (confirmado por autor).

El Cap 9 menciona que Rodrigo "olvidó a Azura" mientras la fiesta lo arrastraba, lo que implica que estaba en el lugar. La ficha de Azura afirma que "no estaba presente físicamente" en el momento del colapso y fue "la voz al teléfono."

Las dos afirmaciones son inconsistentes pero no irreconciliables: Azura pudo estar en la fiesta pero no en la habitación específica del colapso. El script no lo resuelve con claridad.

---

### C-02 — Duplicación del flashback de la sobredosis ⚠️

**Fuentes:** `script_2.rpy` (Cap 8) y `script_2.rpy` (Cap 9).

El Cap 8 incluye una referencia breve a la sobredosis en el contexto del combate con la Rata. El Cap 9 abre con el mismo evento como flashback jugable completo. No hay contradicción sobre los hechos, pero sí una redundancia narrativa cuya intencionalidad no queda clara en el código.

---

### C-03 — "Dictadura" como contexto: rumor vs. fuentes primarias ⚠️

**Fuentes:** `script.rpy` (Azura, apertura) vs. Bitácora del Dr. Montané.

Azura menciona el rumor del orfanato como centro de tortura durante una dictadura. La bitácora confirma el experimento H-127 pero no menciona ninguna dictadura ni contexto político. La conexión entre el proyecto y un régimen político no tiene respaldo en ninguna fuente primaria del proyecto.

---

### C-04 — Mochila de Cutipye: hueco narrativo sin cerrar ⚠️

**Fuentes:** `script.rpy` (Cap 1) vs. FICHA-Cutipye.md.

En el Cap 1, Rodrigo encuentra la mochila de Cutipye en el pasillo con manchas de sangre. En el Cap 3, Cutipye aparece en el segundo piso junto a Nagi, sin heridas descritas. El script actual no implementa la escena de separación que explicaría cómo llegó del lugar donde perdió la mochila al segundo piso. **No es contradicción interna del script, pero es un hueco narrativo no cerrado.**

---

## 13. PENDIENTES GLOBALES

| # | Pendiente | Área |
|---|---|---|
| 1 | Contenido completo del Cap 12 | Narrativa / código |
| 2 | Escena de mea culpa de Cutipye (Cap 11, afinidad alta) | Narrativa / código |
| 3 | Escena de separación de Cutipye en Cap 1/2 (enfrentamiento con Huésped-Rata) | Narrativa / código |
| 4 | Diseño visual final de sprites para todos los personajes | Arte |
| 5 | Sprites de Cutipye (Cap 11): `media_sonrisa`, `mirada_reojo`, `sorpresa_fingida`, `seria`, `fria`, `cansada` | Arte / código |
| 6 | Sprite `galaxia sentada_sonriendo` (usado en Cap 11, no definido en `definitions.rpy`) | Arte / código |
| 7 | Loop y conversión a `.ogg` de `rodtheme.mp3` y `ambiental.mp3` | Audio |
| 8 | Archivos de audio referenciados en scripts pero ausentes en `/audio` | Audio |
| 9 | Cuaderno de Galaxia (easter egg) | Narrativa |
| 10 | Conexión bíblica del nombre "Galaxia" (solo accesible en ruta específica) | Narrativa |
| 11 | Escena ampliada del momento de infección (rutas alternas) | Narrativa |
| 12 | Confesión final de Luz planificada para el cap de cierre | Narrativa |
| 13 | ¿La herida de Cutipye en Cap 1 fue infección por H-127? (canon pendiente de secuela) | Lore |
| 14 | Punto exacto en que el vínculo de mente colmena se vuelve bidireccional (umbral no definido numéricamente) | Mecánica / lore |
| 15 | Destino de los otros cuatro Huéspedes Activos | Lore |
| 16 | Qué siente Galaxia hacia el Dr. Montané y los investigadores | Personaje |
| 17 | Destino del Dr. Montané en el presente | Lore |
| 18 | Color exacto de los ojos heterocromáticos de Galaxia post-mutación | Arte |
| 19 | Apellido de Luz | Personaje |
| 20 | Tema musical propio de Luz | Audio |
| 21 | HUD `mostrar_hud` — eliminación completa antes de build de producción | Código |

---

## 14. IDEAS PROPUESTAS COMPATIBLES CON EL LORE

> **Reglas de esta sección:**
> - Cada idea se basa **únicamente** en información existente en el proyecto.
> - No modifica el canon establecido.
> - Se indica claramente qué lore sirve como base.
> - El nivel de compatibilidad es una evaluación, no una aprobación.

---

### IDEA 01 — El cuaderno de Cutipye como detonante del incendio

**Descripción:** El cuaderno de dibujos de Cutipye (encontrado en su mochila en Cap 1) sirve como pieza clave en la planificación del incendio final. El cuaderno puede tener páginas arrancadas que Azura usa para encender el fuego de forma controlada, o un boceto del edificio que les permite identificar dónde quemar para que el fuego se propague sin vías de escape para Galaxia.

**Problema que resuelve:** Cierra el arco del cuaderno (mencionado en Cap 1 como detalle de caracterización pero sin función narrativa concretada) y da a Azura un objeto tangible para justificar su rol como "quien identifica el fuego como herramienta."

**Ventajas:**
- Usa un elemento ya confirmado en el proyecto (el cuaderno existe en Cap 1).
- Conecta el arco de Cutipye con el clímax narrativo.
- Da al personaje de Azura una escena activa con objeto físico.

**Desventajas:**
- Añade complejidad al Cap 11/12, que ya tiene muchas variables de estado.
- Si el cuaderno fue quemado o perdido en el orfanato antes del Cap 11, la continuidad requiere explicación.

**Posibles contradicciones:** Ninguna detectada. La confirmación del autor de que el cuaderno "es una pieza clave en la planificación del incendio" hace de esta idea una **continuación directa de un dato ya confirmado**, no una adición nueva.

**Impacto en la historia:** Añade un hilo narrativo desde el Cap 1 hasta el clímax. Transforma un detalle de caracterización en un elemento funcional de la trama.

**Impacto en gameplay:** El cuaderno podría convertirse en un ítem que el jugador debe recuperar o usar activamente en Cap 11/12, añadiendo una micro-mecánica de inventario.

**Compatibilidad:** ✅ Alta — ya confirmada parcialmente por el autor.

---

### IDEA 02 — La conexión Nagi-Galaxia como revelación en el ending good

**Descripción:** En el ending `good`, en el momento en que Rodrigo retiene a Galaxia en el incendio, Galaxia dice *"Shio"* por primera vez. En ese instante, si Nagi está vivo y cerca, él reconoce el nombre. Una sola línea: *"...¿Shio?"* — sin explicación. El jugador que haya prestado atención a los apellidos lo entendería.

**Problema que resuelve:** Introduce de forma orgánica la conexión familiar Nagi-Galaxia (confirmada por el autor) sin necesidad de exponerla explícitamente. Recompensa la atención del jugador. Planta la semilla de la secuela.

**Ventajas:**
- No altera el canon. Usa solo información confirmada.
- No requiere implementar escenas nuevas complejas — es una sola línea de diálogo.
- Amplía el peso emocional del ending `good` sin cambiar su estructura.
- El "nunca volvió a ser el mismo" del epílogo de Nagi adquiere una capa adicional.

**Desventajas:**
- Requiere que Nagi haya sobrevivido (solo activo en el ending `good`).
- Un jugador que no conecte los apellidos no entenderá la referencia, lo que puede generar confusión o pasar desapercibido.

**Posibles contradicciones:** Ninguna. La conexión ya está confirmada. Solo la forma de revelarla es nueva.

**Impacto en la historia:** Añade una capa de significado a la relación Rodrigo-Galaxia-Nagi. El sacrificio de Rodrigo también protege indirectamente a un primo lejano de la persona que está muriendo.

**Impacto en gameplay:** Ninguno directo. Es un momento narrativo pasivo.

**Compatibilidad:** ✅ Alta.

---

### IDEA 03 — La Entrada 09 guardada por Azura como herramienta de negociación

**Descripción:** Azura guarda la Entrada 09 (descripción de los Huéspedes Activos) en su bolsillo en Cap 7 sin decirle nada al grupo. En una posible secuela o en un capítulo alternativo, ese papel podría usarse como evidencia frente a la Fundación Connor, que sigue activa en el presente. Un personaje sobreviviente (Azura es la más probable) podría entregarlo a un periodista o a las autoridades, desencadenando consecuencias para la Fundación.

**Problema que resuelve:** Cierra el arco de ese ítem (fue recogido deliberadamente y nunca mencionado) y activa el único villain institucional confirmado del universo que sigue activo después del incendio.

**Ventajas:**
- Usa elementos 100% confirmados: la Entrada 09 existe, Azura la tiene, la Fundación Connor sigue activa.
- Abre una línea de trama realista para una secuela sin requerir elementos sobrenaturales nuevos.
- Justifica retroactivamente por qué Azura guardó el papel en silencio.

**Desventajas:**
- Para ser jugable requeriría un Cap 12 o secuela implementados.
- Si la Fundación destruyó todas las evidencias (confirmado), un solo papel puede no ser suficiente — requeriría explicación de por qué esta evidencia sobrevivió.

**Posibles contradicciones:** El canon establece que la Fundación destruyó la mayoría de las evidencias. El papel sobrevivió porque estaba en el orfanato, no en las instalaciones de la Fundación — lo que es consistente. Sin contradicción directa.

**Impacto en la historia:** Transforma el horror contenido en el orfanato en una historia con ramificaciones institucionales. Da a Azura un arco de agencia post-supervivencia más allá de la terapia y la música.

**Impacto en gameplay:** Requeriría un sistema de ítems o una decisión al final del juego sobre qué hacer con el papel.

**Compatibilidad:** 🔶 Media — narrativamente sólida, pero requiere implementación significativa.

---

### IDEA 04 — La herida de Cutipye como infección latente (semilla de secuela)

**Descripción:** La herida de Cutipye en Cap 1 (cuyo origen no es aclarado dentro de la historia) podría ser un arañazo del Huésped-Rata durante la separación del grupo. Esto la convertiría en portadora latente del H-127, con una compatibilidad muy baja — no suficiente para desarrollar Huésped Activo, pero sí para manifestar síntomas años después.

**Problema que resuelve:** Cierra el hueco narrativo de la mochila y la herida (C-04 en la sección de contradicciones). Da a Cutipye un arco de post-supervivencia más oscuro que el actual ("se vuelve retraída y se muda").

**Ventajas:**
- La herida ya existe en el canon como pendiente explícito.
- El H-127 se adapta a cada huésped — una manifestación distinta es coherente.
- El "trauma" descrito en el epílogo de Cutipye podría reinterpretarse parcialmente como síntomas físicos.

**Desventajas:**
- Añade implicaciones graves a un personaje que ya tiene un arco emocional complejo.
- Podría contradecir la percepción del jugador si los síntomas físicos no se siembran antes en el script.

**Posibles contradicciones:** El canon actual marca la herida de Cutipye como "pendiente de planificación futura" y "relevante para una posible secuela." Esta idea es consistente con esa declaración.

**Impacto en la historia:** En la historia actual, ninguno. En una secuela, Cutipye podría ser el punto de entrada a una nueva infección fuera del orfanato, con la Fundación Connor como actor interesado.

**Impacto en gameplay:** En la historia actual, ninguno. En una secuela, podría ser mecánica central.

**Compatibilidad:** 🔶 Media — confirmada como posibilidad por el autor, pero sin implementación planificada.

---

### IDEA 05 — El apellido de Luz como vínculo al contexto político del orfanato

**Descripción:** El apellido de Luz está marcado como pendiente. Si se elige un apellido con historia documentada de desaparición forzada durante la dictadura mencionada por Azura, se sembraría la posibilidad de que la familia de Luz tuviera una conexión previa con el orfanato — sin hacer la conexión explícita dentro del juego actual.

**Problema que resuelve:** Usa el único elemento del lore político sin respaldo (el rumor de la dictadura, C-03) de forma narrativamente sugestiva sin afirmar ni negar el canon.

**Ventajas:**
- No altera ningún hecho confirmado.
- Es un detalle de caracterización, no una modificación de la trama.
- Añade capas de lectura para jugadores que presten atención.

**Desventajas:**
- Requiere que el rumor de la dictadura sea más que un rumor — lo que no está confirmado.
- Puede sentirse forzado si el apellido no encaja orgánicamente con el tono del personaje.

**Posibles contradicciones:** El canon no confirma ni niega la dictadura. Esta idea solo añade implicación, no afirmación. Compatible como subtexto.

**Impacto en la historia:** Mínimo en la historia actual. Significativo como elemento de worldbuilding en una lectura profunda.

**Impacto en gameplay:** Ninguno.

**Compatibilidad:** 🔶 Media — depende de una decisión previa sobre el rumor de la dictadura.

---

### IDEA 06 — La música de Azura como testigo del trauma (ending bad2)

**Descripción:** En el ending `bad2`, el epílogo confirma que Azura usa la experiencia del orfanato como motor para su música. Si Azura es músico con guitarra acústica y composición propia (confirmado por el autor), sus canciones podrían ser el único registro "humano" de lo que ocurrió — no evidencia forense, sino memoria emocional. Una de sus canciones podría contener el nombre "Shio" o referencias veladas al orfanato que nadie entendería sin haber estado allí.

**Problema que resuelve:** Conecta el detalle de la guitarra (confirmado pero sin función narrativa directa) con el epílogo del ending `bad2`. Da consistencia al arco emocional de Azura.

**Ventajas:**
- Todos los elementos ya existen: la guitarra, el trauma, la música como motor, el nombre Shio.
- Añade profundidad emocional al ending `bad2` sin cambiar su estructura.
- Es internamente coherente con la personalidad de Azura.

**Desventajas:**
- Solo aplica al ending `bad2`. En otros endings, Azura sobrevive con apoyo y tiene rutas de recuperación distintas.
- Implementar esto requeriría añadir una escena al epílogo del ending `bad2`.

**Posibles contradicciones:** Ninguna.

**Impacto en la historia:** Añade resonancia emocional al único ending donde Azura carga sola con todo.

**Impacto en gameplay:** Solo en el epílogo. No altera mecánicas.

**Compatibilidad:** ✅ Alta.

---

*Documento generado a partir exclusivamente de los archivos fuente del proyecto.*
*No se ha añadido información externa ni inventada.*
*Las ideas de la sección 14 son propuestas, no canon. Solo el autor puede confirmarlas.*
