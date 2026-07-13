Todas las preguntas abiertas están resueltas. Documento final completo y definitivo:

---

# Análisis Narrativo — Capítulo 2 (*Possessed*)
*(Cubre el contenido completo de `script_2.rpy`: subcapítulos internos 6 a 11 + secuencia de finales)*

---

## Objetivo del capítulo

Desarrollar la infección de Rodrigo como eje central: pasar de síntomas ambiguos y negación a una crisis visible que fractura al grupo y desemboca en una huida sin retorno. El capítulo transforma la amenaza externa (Galaxia, las criaturas) en una amenaza interna (la pérdida de humanidad de Rodrigo) y exige al jugador decidir qué tipo de persona es Rodrigo en el momento en que más importa. Cada subcapítulo añade una capa de degradación, hasta que el orfanato se incendia y los finales determinan quién sobrevive y en qué condición.

---

## Resumen

El capítulo abre con un flashback tres años atrás: la noche en que Luz se presentó ante el grupo como quien realmente es, con Rodrigo como su novio y único testigo previo. De vuelta al presente, Rodrigo regresa al grupo herido y con síntomas físicos inexplicables. El grupo decide si avanzar hacia el ala administrativa (ruta Nagi) o retroceder hacia la lavandería (ruta Cutipye); ambas rutas convergen en el Cap. 7, donde las luces se apagan y una voz de Galaxia habla directamente a Rodrigo. En el cuarto de una interna encuentran registros de laboratorio y una Biblia con el nombre real de Galaxia: Shio Katashi.

En el balcón, Rodrigo puede confesar la influencia al grupo o mantenerla en secreto; ambas ramas terminan con una gota de sustancia negra absorbida por su piel mientras Luz está presente.

Al amanecer (Cap. 8) el comportamiento de Rodrigo se vuelve preinimal: escanea alturas, camina sin ruido, reacciona a estímulos que los demás no perciben. El grupo descubre una rata mutante en el vestíbulo que ataca al personaje de menor afinidad. Rodrigo la elimina, y el nivel de `estado_mental` determina si el combate parece humano, sintetizado o brutal.

El Cap. 9 es un flashback completo a una fiesta universitaria donde Rodrigo bebió en exceso y probó marihuana por primera vez, tuvo una crisis cardíaca leve y fue salvado por el grupo. Azura coordinó el rescate desde el teléfono. Este pasado regresa al presente cuando Nagi confronta a Rodrigo en el Cap. 10 con ese recuerdo como arma.

En el Cap. 10, si la afinidad con Nagi es menor de 3, Nagi abandona al grupo en un estallido de rabia, es capturado por Galaxia y muere. El Huésped Cucaracha actúa como guardaespaldas de Galaxia y bloquea el pasillo. Si la afinidad es suficiente, Nagi permanece pero la fractura es visible.

En el Cap. 11, si la afinidad con Cutipye es menor de 4, ella ataca emocionalmente a Rodrigo con crueldad calculada. Si es suficiente, se quiebra ante el grupo y confiesa que fue idea suya entrar al orfanato. El capítulo termina con Galaxia bloqueando la salida. Azura identifica el fuego como herramienta; encuentran un encendedor y prenden el edificio.

La secuencia final es una huida con temporizador de 90 segundos y cinco QTEs. Si el tiempo se agota, todos mueren. Si Rodrigo tiene `estado_mental >= 16`, pierde el control y ataca al grupo (bad1 por transformación). Entre 11 y 15 desaparece en el humo (neutral). Por debajo de 11 retiene a Galaxia para que el grupo escape (good). El epílogo exterior varía según el ending. Los créditos y material post-juego se encuentran en `script_3.rpy`.

---

## Eventos importantes

1. **Flashback Cap. 6**: Tres años atrás, Luz se presenta ante el grupo como quien realmente es. Rodrigo ya lo sabía; su reacción de orgullo y ternura establece la profundidad del vínculo.
2. **Síntomas de Rodrigo al inicio del Cap. 6**: Sabor dulce-metálico, herida que sana anormalmente rápido, partículas oscuras en los dedos, pupila que se contrae de forma no reconocida, sensación de latido ajeno.
3. **Voz de Galaxia (primera vez en Cap. 6)**: Rodrigo escucha "Casi... casi mía..." en el cuarto de máquinas. El grupo no la oye.
4. **Elección de ruta (Cap. 6)**: El jugador decide entre ir al ala administrativa (Nagi) o retroceder (Cutipye). Afecta afinidades, `estado_mental` y la escena inicial del Cap. 7.
5. **Lights out (Cap. 7)**: Las luces se apagan; Galaxia habla directamente a Rodrigo en la oscuridad.
6. **Cuarto de la interna (Cap. 7)**: El grupo encuentra la Entrada 09 del experimento, la Biblia con el nombre Shio Katashi, un cuaderno infantil y el versículo subrayado de Jeremías 12:9. Galaxia interpreta el versículo para Rodrigo.
7. **Escena del balcón (Cap. 7)**: Rodrigo puede confesar o callar su estado. Independientemente de la elección, una gota de sustancia negra se absorbe a través de su piel ante los ojos de Luz.
8. **Amanecer y comportamiento preinimal (Cap. 8)**: Rodrigo despierta con reflejos e instintos que no reconoce como suyos. El sistema calcula quién tiene menor afinidad; esa persona es el objetivo de la rata mutante.
9. **Combate contra la rata mutante (Cap. 8)**: Rodrigo la elimina. El nivel de `estado_mental` cambia el registro visual y narrativo: humano, sintetizado o depredador. El grupo queda en shock.
10. **Flashback de la fiesta (Cap. 9)**: Rodrigo bebe, fuma marihuana, tiene una crisis cardíaca leve. Azura coordina el rescate. Luz llega y reacciona según la elección del jugador.
11. **Muerte de Luz (Cap. 9)**: Ocurre siempre, sin excepción. Es consecuencia directa de la crisis de control de Rodrigo; sus últimas palabras varían según la afinidad acumulada.
12. **Confrontación de Nagi (Cap. 10)**: Nagi usa el flashback de la fiesta como argumento. Si la afinidad es baja, abandona al grupo; Galaxia lo captura y lo mata. Si es suficiente, permanece pero la fractura es visible.
13. **Aparición del Huésped Cucaracha (solo en rama traición Nagi)**: Un huésped mutado con exoesqueleto de cucaracha actúa como guardaespaldas de Galaxia y bloquea el pasillo mientras ella arrastra a Nagi.
14. **Quiebre de Cutipye (Cap. 11)**: Dependiendo de la afinidad, Cutipye ataca a Rodrigo verbalmente o se derrumba confesando su culpa. En la ruta alta, el grupo procesa colectivamente la responsabilidad.
15. **Incendio**: Azura y Cutipye/Rodrigo prenden el edificio. Los Huéspedes huyen por instinto; el control territorial de Galaxia se fractura.
16. **Persecución con temporizador**: Cinco QTEs en 90 segundos. Cada decisión resta tiempo.
17. **Confrontación final con Galaxia**: No huye del fuego. Reacciona con curiosidad genuina cuando el grupo ejecuta el plan.
18. **Los finales**: Tres posibles estados para Rodrigo (good, neutral, bad1) según `estado_mental` y tiempo restante. Destino del grupo varía según `nagi_dead` y `cuty_dead`.

---

## Personajes

**Rodrigo** — La infección avanza de síntomas imperceptibles a crisis manifiesta. Sus instintos se vuelven predatorios, sus percepciones se agudizan y sus impulsos físicos superan su voluntad en momentos de tensión alta. La elección de confesar o callar define el tono de sus relaciones en los capítulos siguientes. En el ending good retiene a Galaxia para salvar al grupo; en el bad1 los ataca; en el neutral desaparece en el humo.

**Luz** — Presente como soporte emocional y testigo del deterioro de Rodrigo. Es la primera en estar físicamente cerca cuando la sustancia negra se absorbe por la piel de Rodrigo. Muere en el Cap. 9 en todas las rutas; solo sus últimas palabras varían según la afinidad. Su lealtad es incondicional e independiente de las decisiones del jugador.

**Nagi** — Su arco en este capítulo es el más dinámico del grupo: pasa de una contención genuinamente protectora en los Caps. 6 y 7 a una explosión en el Cap. 10. Si la afinidad es baja, muere capturado por Galaxia. Si es alta, permanece aunque no recupera del todo su registro habitual.

**Cutipye** — Mantiene su mecanismo de humor como escudo hasta el Cap. 11, donde se quiebra y confiesa que entrar al orfanato fue idea suya. Su lealtad o su crueldad en ese punto dependen de la afinidad acumulada.

**Azura** — Rol operativo y de mediación. Coordina el rescate en el flashback de la fiesta. Media entre Nagi y Rodrigo en el Cap. 11. Identifica el fuego como herramienta y ejecuta el plan con precisión. Es el personaje que más consistentemente sobrevive.

**Galaxia / Shio Katashi** — Su nombre real aparece en la Biblia. Interpreta el versículo de Jeremías como la historia de su propia transformación. No huye del fuego en los finales; reacciona con curiosidad genuina ante el plan del grupo. En el ending good pronuncia su propio nombre por primera vez en quince años, en un momento de reconocimiento de sí misma, no dirigido a Rodrigo.

**El Huésped Cucaracha** — Huésped mutado con exoesqueleto quitinoso que actúa como guardaespaldas de Galaxia en la rama de traición de Nagi. Su dureza física le permite bloquear el pasillo mientras Galaxia arrastra a Nagi. Solo aparece si `afinidad_nagi < 3`.

---

## Revelaciones

1. **Nombre real de Galaxia**: Shio Katashi. Estaba en la Biblia junto al cuaderno infantil. Era una interna del orfanato.
2. **Entrada 09 del laboratorio**: Cinco sujetos alcanzaron compatibilidad parcial con el patógeno ("Huéspedes Activos"). Mutación adaptativa: masa muscular aumentada, endurecimiento dérmico, cambios oculares. También: comportamiento errático, violento, territorial.
3. **Versículo de Jeremías 12:9 y su reinterpretación por Galaxia**: Ella subrayó el texto repetidamente. Lo usa para narrar su propia transformación: rezó para ser salvada y el patógeno la convirtió en el depredador del versículo. La hiena que todos deben devorar se convirtió en la que devora.
4. **La sustancia negra es parte activa del proceso de infección**: Una gota se absorbe directamente por la piel de Rodrigo en el balcón, ante los ojos de Luz. No deja marca visible, pero el movimiento es deliberado.
5. **`estado_mental` determina cualitativamente la experiencia de Rodrigo**: No es solo mecánica de puntos; condiciona si Rodrigo racionaliza sus síntomas, los acepta con ambigüedad, o los encuentra placenteros. Tiene implicaciones narrativas directas en el combate y en el ending.
6. **Cutipye fue quien propuso visitar el orfanato**: Confirmado en el Cap. 11 (ruta alta). Es el origen de toda la cadena de eventos.
7. **`riesgo_salud` aplica un multiplicador de 1.25 a `estado_mental`**: Si Rodrigo aceptó los vicios en el flashback de la fiesta (`riesgo_salud = True`), la variable representa un historial de salud deteriorada que amplifica el avance de la infección en capítulos posteriores.

---

## Foreshadowing

- La herida que sana "demasiado rápido" en la escena de apertura es el primer indicio físico de que la compatibilidad de Rodrigo con el patógeno ya está activa.
- La pupila que "se contrae de una forma que no reconoció" prefigura la pérdida progresiva de control sobre su cuerpo.
- El comportamiento de Rodrigo al amanecer (escanear alturas, pasos silenciosos, pensamientos de "sentinela") anticipa el ending bad1.
- El versículo de Jeremías en boca de Galaxia enmarca a Rodrigo como posible sucesor del rol de "hiena". "¿Lo ves ahora, Rodrigo? Siempre estuvo escrito" opera como profecía sobre su arco final.
- La rata mutante del Cap. 8 actúa como espejo: lo que Rodrigo le hace a esa criatura es lo que podría hacerle al grupo en el ending bad1.
- Nagi usa el flashback de la fiesta como argumento en el Cap. 10; ese mismo recuerdo resignifica el ending good, donde Nagi finalmente se niega a "largar" a Rodrigo.
- Azura identifica el fuego como herramienta antes de que se necesite; el incendio final no es improvisado.
- La última imagen del Cap. 11 —Galaxia bloqueando la salida con brazos cruzados, sin correr, sin amenazar— anticipa su comportamiento en el ending good: no es una bestia, es algo que eligió quedarse.

---

## Cambios emocionales

**Rodrigo** — Abre en estado de shock funcional. Pasa por negación activa, introspección forzada por los otros personajes, quiebre en el flashback de la fiesta, y aceleración de síntomas hasta la crisis del Cap. 10. En el Cap. 11 llora en silencio cuando Cutipye (ruta baja) lo destruye verbalmente sin que él se defienda. El Rodrigo que llega al incendio final no es el mismo que entró al orfanato.

**Luz** — Soporte estable hasta su muerte en el Cap. 9. Sus últimas palabras se mueven siempre hacia Rodrigo, no alejándose. Lealtad incondicional.

**Nagi** — Cambio más dramático del capítulo. Ternura contenida en los Caps. 6 y 7; explosión en el Cap. 10. Si la afinidad es suficiente, el estallido no lo rompe del todo. Si no, actúa sobre él con consecuencias fatales.

**Cutipye** — Mantiene el escudo de humor hasta el Cap. 11. El cuaderno de bocetos es el detonante de su quiebre en la ruta alta. En la ruta baja convierte el miedo en crueldad y abandona la habitación.

**Azura** — Contención y mediación a lo largo del capítulo. Su quiebre emocional es más contenido que el de los demás; en la rama de traición de Nagi se la ve suplicar antes de ser apartada.

---

## Variables modificadas

| Variable | Qué la modifica | Rango posible de cambio en Cap. 2 |
|---|---|---|
| `afinidad_luz` | Elecciones en Caps. 6, 7, 9; confesión del balcón (+2 en ruta confesión) | +1 a +8 adicionales |
| `afinidad_nagi` | Elecciones en Caps. 6, 7 (ruta admin), oficina de Nagi; variantes de diálogo | +1 a +4 adicionales |
| `afinidad_cutipye` | Elecciones en Cap. 6 (retroceso), Cap. 7, Cap. 10 rama traición-Nagi | +1 a +3 adicionales |
| `afinidad_azura` | Confesión del balcón (+2 solo en ruta confesión) | 0 a +2 adicionales |
| `estado_mental` | Múltiples puntos de elección, despertar Cap. 8, registro del combate | Variable; sube y baja según ruta |
| `nagi_dead` | Cap. 10, rama traición si `afinidad_nagi < 3` | False → True |
| `cuty_dead` | QTEs de combate en ending bad1 | False → True |
| `ending_type` | Determinado por `estado_mental` al final y desempeño en QTEs; "good" por defecto (intencional) | "good", "neutral1", "neutral2", "bad1" |
| `tiempo_escape` | Decrementado por cada QTE durante la huida | 0 a 90 |
| `riesgo_salud` | Cap. 9, fiesta: True si Rodrigo aceptó los vicios | True / False |
| `ruta_anterior` | Flag interno para ramificar el Cap. 7 | "nagi" / "cuty" |

---

## Consecuencias futuras

- Si `nagi_dead = True`, la estructura del grupo cambia permanentemente. Nagi no puede aparecer en eventos futuros dentro del juego en curso.
- Si `cuty_dead = True` (solo en bad1), lo mismo aplica para Cutipye. La rama "[ CUTIPYE CORRE ]" en el QTE de combate es un placeholder; se implementará una ruta en la que ella sobreviva durante la huida.
- Luz muere en el Cap. 9 en todas las rutas. Su ausencia es una constante narrativa a partir de aquí.
- El nivel final de `estado_mental` determina el ending. Si `riesgo_salud = True`, un multiplicador de 1.25 amplifica su valor en capítulos posteriores, reflejando el historial de salud deteriorada de Rodrigo.
- La revelación de que Cutipye propuso visitar el orfanato (Cap. 11, ruta alta) tiene peso moral para su arco en capítulos siguientes o en una posible secuela.
- El nombre real de Galaxia (Shio Katashi) está ahora en posesión del grupo. Puede usarse para interactuar con ella de forma distinta en un encuentro futuro.
- En el ending good, Galaxia pronuncia su propio nombre por primera vez en quince años. El acto de Rodrigo de retenerla reactivó algo de quien ella fue antes. Las implicaciones para una posible secuela son significativas.
- El incendio destruye el laboratorio subterráneo y toda la evidencia física del H-127. Cualquier información sobre el patógeno en adelante depende de lo que el grupo lleva en la memoria o en papel.
- Los créditos y el material post-juego (información desbloqueable) se encuentran en `script_3.rpy`, que no continúa la narrativa desde el epílogo.
- El valor por defecto `ending_type = "good"` es intencional: el ending bueno es el estado base, modificado progresivamente por las decisiones del jugador a lo largo del juego.
