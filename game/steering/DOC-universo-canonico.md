# Documento Canónico del Universo — POSSESSED

> **Metodología:** Toda la información proviene exclusivamente de los archivos del proyecto:
> `script.rpy`, `script_2.rpy`, `script_3.rpy`, `definitions.rpy`, `DOC-script1.md` y `DOC-Cronologia.md`,
> complementada con las declaraciones directas del autor registradas en sesión.
>
> Cada dato está clasificado como:
> - ✅ **Confirmado** — explícito en el código o confirmado directamente por el autor
> - 🔶 **Inferido** — deducible del contexto sin declaración explícita
> - ⬜ **Pendiente** — información ausente, sin resolver o sin implementar

---

## 1. Historia del mundo

### El orfanato "Luz y Esperanza"

✅ Existe un orfanato abandonado llamado **"Luz y Esperanza"**, ubicado en un bosque kilómetros más allá de una autopista.
Nombre confirmado en el encabezado de la Bitácora del Dr. Montané.

✅ El edificio tiene al menos dos plantas, más un sótano y un subsuelo.
Espacios identificados en el código: lavandería, pasillos con habitaciones numeradas,
sala del proyector, sala H-127, vestíbulo principal, ala administrativa, ala de servicio,
cocina industrial, cuarto de máquinas, habitaciones de literas, balcón oxidado en el segundo piso,
oficina administrativa con mapa en la pared, y una habitación intacta en el segundo piso.

✅ El orfanato fue desalojado antes de los eventos de la historia. No hay habitantes humanos cuando el grupo entra.

🔶 El rumor de que fue usado como centro de tortura durante una dictadura es mencionado por Azura.
No está confirmado por ninguna fuente primaria dentro del proyecto.
Es información de personaje, no verificada.

✅ Bajo el orfanato existe un **Centro de Investigación Subterráneo**, denominado así en la Bitácora del Dr. Montané.
Este laboratorio clandestino fue el escenario del Proyecto H-127.

✅ El deterioro físico del edificio (escombros, derrumbes, pasillos bloqueados o liberados)
responde a la vejez de la estructura y no a ningún fenómeno sobrenatural activo.
**Confirmado por el autor.** Lo que el Capítulo 7 narra como reorganización del edificio
corresponde a nuevos derrumbes y vías bloqueadas por la edad de la construcción.

---

### El contexto temporal

✅ Los eventos principales de la historia ocurren en **una sola noche y la mañana siguiente.**
El Capítulo 8 abre explícitamente con: *"El amanecer se filtró a través de las ventanas rotas como un velo gris."*

✅ La estación es **otoño.** La apertura del juego la describe como una "fría tarde de otoño."

✅ El flashback del Capítulo 6 está anclado explícitamente **"tres años atrás"** respecto al presente.

🔶 La infancia de Rodrigo y Lucien (Luz) en la escuela ocurre años antes del presente.
No hay edades ni fechas concretas en el código.

🔶 La fiesta donde Rodrigo sufre la sobredosis ocurre en la adolescencia tardía, antes del presente.
No hay marcador temporal preciso.

---

### El incendio del orfanato

✅ En todos los finales posibles, el orfanato arde y queda destruido.
El fuego es el único elemento que confirma la muerte definitiva de Galaxia.

✅ La secuencia del incendio está implementada en el Capítulo 12 (`label cap_12`, líneas 2974–3694 de `script_2.rpy`).
Incluye una persecución con cinco QTEs temporizados (90 segundos globales) y bifurca según `estado_mental` al salir.

✅ Los cinco finales posibles, según las variables `ending_type`, `nagi_dead`, `cuty_dead` y `estado_mental`:
- **bad1:** nadie sobrevive (o Rodrigo sucumbe y ataca al grupo).
- **bad2:** solo Azura sobrevive.
- **neutral1:** varios sobrevivientes (≥3), historia enterrada.
- **neutral2:** dos o menos sobrevivientes, versión oficial falsa.
- **good:** Rodrigo retiene a Galaxia en el incendio; Azura, Nagi y Cutipye escapan.

✅ El final `bad2` está confirmado en el código: Azura es la única que escapa.
Asiste a terapia sin superar el trauma. Usa la experiencia como motor para su música.


---

## 2. Organizaciones

### La Fundación Connor

✅ La **Fundación Connor** era una corporación internacional dedicada públicamente a investigación biomédica, farmacéutica y genética. **Confirmado por el autor.**

✅ En secreto, poseía una división denominada **Departamento H**, responsable del desarrollo de agentes biológicos experimentales con potencial militar y médico.

✅ El Proyecto H-127 era un programa del Departamento H.

✅ Los objetivos declarados internamente para el H-127 eran:
regeneración de tejidos; adaptación extrema del cuerpo humano;
creación de combatientes capaces de sobrevivir en ambientes hostiles.

✅ El símbolo grabado en la caja metálica sellada que contenía la Bitácora del Dr. Montané
corresponde al **Departamento H.** Esta división nunca fue reconocida públicamente.

✅ Tras el incidente de contención (ver Eventos Históricos), la Fundación Connor negó cualquier vínculo con el proyecto y destruyó la mayoría de las evidencias.

✅ **La Fundación Connor sigue activa en el presente de la historia.**
Sus conexiones con el incidente del orfanato fueron completamente abandonadas y eliminadas.
Ninguna otra división de la Fundación es relevante para los eventos de la historia. **Confirmado por el autor.**

---

### Proyecto H-127 / Centro de Investigación Subterráneo

✅ **Director registrado:** Dr. Édgar L. Montané. Es el único nombre de investigador mencionado en la bitácora.

✅ **Nombre oficial:** Proyecto H-127. El objetivo declarado en la bitácora es *"inducir una simbiosis controlada"* con el Patógeno H-127.

✅ **Sujetos:** Niños huérfanos sin lazos familiares, seleccionados por considerarse "prescindibles" (Bitácora, Entrada 01).

✅ **Ubicación:** Centro de Investigación Subterráneo del Orfanato "Luz y Esperanza."

✅ El laboratorio tiene salas numeradas con puertas metálicas. Al menos una sala está identificada como **H-127.**
En el vestíbulo hay una sala con proyector, escritorios, archivos húmedos y fotografías clínicas de niños con "la piel incorrecta."

✅ **Cierre:** El proyecto fue clausurado por la Fundación Connor tras el incidente de contención
mediante el **Protocolo de Contingencia Hades** (ver Eventos Históricos). **Confirmado por el autor.**

✅ **Declaración oficial:** El proyecto fue declarado un fracaso y cancelado por "riesgos biológicos inaceptables."


---

## 3. Tecnología

### Patógeno H-127

✅ Es un **patógeno bioingenierizado**: un virus modificado que edita genes embrionarios y altera la regulación celular.
Microorganismos simbióticos aceleran la regeneración, aumentan densidad muscular y ósea,
e inhiben la muerte celular. *(Descripción confirmada por el autor en DOC-script1.md)*

✅ **Resultado mayoritario:** En la mayoría de los casos produce mutaciones descontroladas y deterioro neurológico.
El 60% de los primeros sujetos murió (Bitácora, Entrada 04, Capítulo 3).
Los tejidos colapsan, los huesos se expanden sin orden, los sistemas vitales no resisten.
Algunos cuerpos continuaron respirando durante horas tras el colapso.

✅ **Huéspedes Activos:** En el Día 28, cinco sujetos mostraron tolerancia parcial al patógeno.
Designados "Huéspedes Activos" en la Entrada 09 (Capítulo 7).
Características: aumento de masa muscular, endurecimiento dérmico, cambios oculares,
comportamientos erráticos, violentos y territoriales.
Uno arrancó el rostro de un investigador por contacto visual prolongado.

✅ Los demás Huéspedes Activos (distintos de Shio Katashi) son las demás criaturas del orfanato.
**Confirmado por el autor.**

✅ **Compatibilidad excepcional:** Existe un tipo de respuesta rara en la que el huésped
no se deteriora sino que obtiene estabilidad y capacidades superiores.
Galaxia es el único caso confirmado de este tipo que completó el proceso dentro del proyecto.
Rodrigo posee la misma compatibilidad excepcional.

✅ **Mente colmena:** Galaxia comanda a los demás Huéspedes mediante el patógeno,
en una especie de vínculo de mente colmena. Esta misma conexión es la que enlaza a Galaxia con Rodrigo
tras la infección. **Confirmado por el autor.**
En el Capítulo 12, cuando el edificio arde, las criaturas dejan de responder a sus órdenes
y reaccionan por instinto de supervivencia propio: *"El control territorial de Galaxia se fracturaba."*

✅ **Alcance del vínculo con Rodrigo:** A partir del punto en que los sentidos de Rodrigo
comienzan a distorsionarse, la conexión es bidireccional: Galaxia puede percibir sus pensamientos.
Este hecho no es explícito para el jugador dentro de la narrativa. **Confirmado por el autor.**

✅ **Adaptación continua:** El H-127 se adapta continuamente. Cada infección es única.

✅ **Vector de infección de Rodrigo:** Las garras de Galaxia en el costado de Rodrigo
durante la persecución del Capítulo 4. Confirmado en DOC-script1.md.

✅ **Síntomas de Rodrigo post-infección** (confirmados en código):
sabor dulce-metálico en la boca; motas oscuras en los dedos que desaparecen al frotar;
herida que no duele como debería; contracción de pupila que él mismo no reconoce;
impulsos de buscar altura; instintos predatorios progresivos; voz interna identificada como Galaxia;
una gota negra y móvil que penetra bajo su piel en el balcón del Capítulo 7.

✅ **Balas:** No matan a Galaxia. Rodrigo la dispara en la frente y en el abdomen;
en ambos casos ella se regenera. Las balas sí son efectivas contra otras criaturas del orfanato.

✅ **Fuego:** El único método confirmado de matar a Galaxia de forma definitiva.

---

### Armas e instrumentos del grupo

✅ **Navaja/daga de Rodrigo:** portada desde el inicio, oculta en el cinturón. Usada en combate durante toda la historia.

✅ **Bate de béisbol de Nagi:** usado para forzar la entrada rompiendo la ventanilla.

✅ **Pistola:** encontrada por Luz en el segundo piso, envuelta en un pañuelo, aceitada a pesar de su antigüedad, con una caja de balas.
Rodrigo la recoge del subsuelo tras el derrumbe. Tiene balas limitadas.
En el Capítulo 11, Cutipye la vacía disparando contra Galaxia (cuatro tiros, todos cicatrizados).

✅ **Encendedor de Rodrigo:** mencionado en el Capítulo 12. Lo usaba para ver en cuartos sin linterna.
Es el elemento que inicia el incendio en la ruta en que Cutipye ya está muerta.

✅ **Extintor:** usado por Cutipye en el combate QTE contra la Avispa Zángano (Capítulo 5).

✅ **Barra metálica:** usada por Luz en el combate QTE contra la Avispa Zángano (Capítulo 5).
Luz continúa golpeando después de que la criatura deja de moverse.


---

## 4. Sobrenatural

### Galaxia (Shio Katashi)

✅ **Nombre real:** Shio Katashi. Inscrito en una Biblia encontrada en el Capítulo 7.

✅ **Nombre autoimpuesto:** Galaxia.

✅ **Origen:** Fue una de las niñas internas del orfanato "Luz y Esperanza." Es huérfana.
Fue inoculada con el H-127 como parte del Proyecto H-127.
Desarrolló compatibilidad excepcional y se convirtió en Huésped Activa estable.

✅ **Biblia personal:** Tenía una Biblia con Jeremías 12:9 (*"¿Es mi heredad para mí como hiena manchada?"*)
subrayado repetidamente hasta rasgar el papel.
Sus propias palabras, como susurros telepáticos en el juego:
*"Yo también recé… Pedí ser salvada. Pero Él me convirtió en la hiena."*

✅ **Apariencia descrita en el código:** Camina erguida pero con postura encorvada. Ojos luminiscentes.
Dientes afilados. "Orejas de gato" (Capítulo 3, ventana del segundo piso).

✅ **Capacidades confirmadas en código:**
- Regeneración de disparos directos (tiro en frente y abdomen, Capítulo 4).
- Movimiento por paredes y techo.
- Fuerza superior a la humana.
- Comunicación que llega a Rodrigo como susurros internos (vínculo de mente colmena con el H-127).
- Comando de los demás Huéspedes del orfanato.

✅ **Comportamiento:** Es consciente. Usa el nombre de Rodrigo.
Trata la cacería como un juego personal.
El sujeto herido la distingue de las otras criaturas: *"Ella no es como los otros... Ella lo disfruta."*
En el Capítulo 12, ante la perspectiva del incendio, su postura cambia: un instinto de alerta
que hasta ese momento no había mostrado.

✅ **Última palabra conocida antes de morir (ending good):**
Dice *"Shio"* — su propio nombre previo. Primera vez que lo pronuncia en quince años.

✅ **Muerte:** Solo el fuego la mata de forma definitiva. Muere en todos los finales.
En el ending good, Rodrigo la retiene físicamente mientras el incendio los cubre a ambos.

✅ **Duración en el orfanato:** 15 años. Confirmado por el autor en documentación interna.

✅ **Conexión con Rodrigo:** Comparten la misma compatibilidad excepcional al H-127.
Según DOC-script1.md, de niña Galaxia tenía una personalidad similar a la de Rodrigo en el presente.
Ella ve en él un reflejo de lo que fue antes de la transformación.

---

### La Araña-Huésped

✅ Primera criatura sobrenatural. Colgada del techo en una habitación del primer piso.
Descrita como "algo que alguna vez fue humano." Desafía la gravedad.

✅ Es uno de los cinco Huéspedes Activos del Proyecto H-127. **Confirmado por el autor.**

---

### La Mantis-Huésped

✅ Criatura con antenas que detectan el miedo. Posee hojas afiladas en los brazos.
Busca a Rodrigo en una habitación de literas (Capítulo 2).
Una alarma lejana la distrae y la hace abandonar la búsqueda.
Tiene seis ojos visibles (mencionados en la muerte alternativa `game_over_mnts_1`).

✅ Es uno de los cinco Huéspedes Activos del Proyecto H-127. **Confirmado por el autor.**

---

### Las Avispas (Nodriza y Zángano)

✅ Criaturas mitad humano, mitad insecto. Piernas largas y quitinosas, abdomen con aguijón, antenas, alas.

✅ La **Avispa Nodriza** cuida un nido en la cocina industrial. Cuida a las larvas con sus antenas.
Reacciona con instinto materno/asesino cuando las larvas son perturbadas.

✅ El **Avispa Zángano** es derrotado en el pasillo del ala de servicio (Capítulo 5).
Combate de tres fases QTE: Cutipye lanza un extintor → Nagi golpea con el bate → Luz remata con la barra.

✅ Son Huéspedes Activos del Proyecto H-127. **Confirmado por el autor.**

---

### Las larvas humanoides

✅ Están en la cocina industrial. Tamaño de perros grandes. Pálidas, húmedas.
Tienen pequeñas manos atrofiadas y rostros humanos a medio formar que boquean en silencio.

✅ Son sujetos del H-127 que no sobrevivieron la mutación completa.

---

### El Huésped-Rata

✅ Aparece en el vestíbulo principal (Capítulo 8). Piel estirada, espinazos expuestos, ojos de "rubí podrido."
Patas traseras demasiado largas para su torso.
Ataca al personaje con menor afinidad en el grupo.

✅ Es un Huésped del Proyecto H-127. **Confirmado por el autor.**

---

### El Parásito (Cucaracha-Guardián)

✅ Aparece en el Capítulo 10, bloqueando un pasillo. Confirmado en DOC-Cronologia.md.

✅ **Nombre de criatura:** El Parásito. **Confirmado por el autor.**

✅ **Apariencia:** Humano mitad cucaracha. Tiene un caparazón brillante que cubre parcialmente su espalda.
Su cuerpo emite un hedor nauseabundo. Sus brazos terminan en garras con forma de patas de cucaracha.
Sus ojos son pequeños y brillan como brasas.

✅ **Comportamiento:** Suele esconderse en la basura o lugares infestados.
Se alimenta de carne en descomposición. Huye cuando es perturbado.
Solo ataca usando los dientes si se siente acorralado.
Emite un silbido para asustar a depredadores o desprende sustancias de olor desagradable como defensa.

✅ **Resistencia:** Es increíblemente resistente, capaz de soportar ataques que matarían a otros Huéspedes.

✅ Es un Huésped del Proyecto H-127. **Confirmado por el autor.**


---

## 5. Reglas del universo

### Sobre el H-127 y las criaturas

✅ Las balas no matan a Galaxia, pero sí causan daño temporal y dolor.

✅ Las balas sí son efectivas contra otras criaturas del orfanato.

✅ El fuego mata a Galaxia de forma definitiva. Es el único método confirmado.

✅ El fuego rompe el control de mente colmena de Galaxia sobre los Huéspedes:
en el Capítulo 12, ante el incendio, las criaturas dejan de obedecer y reaccionan por instinto propio.

✅ Las criaturas conservan comportamientos vinculados a su origen humano:
la Nodriza cuida a sus larvas; la Mantis busca a su presa de forma metódica;
Galaxia juega con sus víctimas en lugar de matarlas directamente.

✅ La infección del H-127 no es instantánea. Rodrigo muestra síntomas progresivos
a lo largo de varios capítulos tras el momento de infección.

✅ La progresión de la infección en Rodrigo está vinculada mecánicamente a la variable `estado_mental`.
A mayor valor, más evidentes los rasgos no humanos en su comportamiento, percepción y combate.
El Capítulo 8 muestra tres niveles de combate distintos según el valor acumulado:
humano/torpe (bajo), agilidad antinatural con instintos de cuervo (medio), ejecución predatoria sin rastro de humanidad (alto).

✅ En el ending `bad1`, si `estado_mental >= 16` al salir del orfanato,
Rodrigo ya no reconoce a sus compañeros como aliados y los ataca.

### Sobre el orfanato

✅ Los cambios en la estructura del edificio entre capítulos
(rutas bloqueadas, pasillos nuevamente accesibles)
responden al deterioro físico acumulado de la construcción, no a ningún fenómeno activo.
**Confirmado por el autor.**

### Sobre el final

✅ La secuencia de escape final (Capítulo 12) es un timer global de 90 segundos.
Cada QTE resta tiempo según la elección. Si `tiempo_escape` llega a 0, el ending es `bad1`.

✅ Si el grupo escapa antes de agotar el tiempo, el ending se bifurca según `estado_mental`:
- `estado_mental >= 16` → ending `bad1` (Rodrigo ataca al grupo).
- `estado_mental >= 11` → ending neutral (Rodrigo se pierde en el humo).
- `estado_mental < 11` → ending good (Rodrigo elige retener a Galaxia).


---

## 6. Eventos históricos

*(Ordenados del más antiguo al más reciente. Solo hechos confirmados o inferidos del código y del autor.)*

---

### Pasado remoto — El experimento y su clausura

**E-01** ✅ El Dr. Édgar L. Montané inicia el Proyecto H-127 en el Centro de Investigación Subterráneo
del orfanato "Luz y Esperanza," bajo el patrocinio del Departamento H de la Fundación Connor.
Niños huérfanos son seleccionados como sujetos.

**E-02** ✅ Día 11. El 60% de los primeros sujetos muere. Las cámaras frías quedan saturadas.
Se incrementa la dosis de estabilizadores.

**E-03** ✅ Día 28. Cinco sujetos muestran tolerancia parcial al patógeno. Son designados "Huéspedes Activos."
Presentan mutación adaptativa y comportamientos violentos. Uno arranca el rostro de un investigador.

**E-04** ✅ En algún momento de las pruebas finales, ocurre un **incidente de contención.**
Un brote interno provoca la muerte de gran parte del personal y la pérdida del control de varios sujetos.
La Fundación Connor ejecuta el **Protocolo de Contingencia Hades**:
eliminación de los especímenes posibles; destrucción parcial de instalaciones mediante explosivos e incendio;
eliminación de registros digitales y físicos; clasificación de la información restante.
El proyecto es declarado oficialmente cancelado por "riesgos biológicos inaceptables."
**Confirmado por el autor.**

**E-04b** ✅ La investigación recuperada tras el Protocolo Hades se encuentra dispersa
a lo largo del orfanato. Algunos registros son accesibles al jugador durante el gameplay.
**Confirmado por el autor.**

**E-05** 🔶 La realidad post-clausura: algunos especímenes sobrevivieron.
Parte de la investigación fue recuperada. El H-127 no desapareció por completo.
La Fundación Connor negó cualquier vínculo con el proyecto y destruyó la mayoría de evidencias.

**E-06** 🔶 Shio Katashi, uno de los Huéspedes Activos, completa su transformación durante los años posteriores.
Se autodenomina Galaxia. Su Biblia personal documenta el proceso.
El orfanato se convierte en su territorio exclusivo. Permanece ahí durante 15 años.

---

### Pasado medio — Infancia de los protagonistas

**E-07** ✅ En el patio de una escuela, Lucien (nombre previo de Luz) se acerca a Rodrigo,
que no hablaba con nadie. Semanas después, Rodrigo le dice su nombre por primera vez.
Es su primer amigo. *(Flashback, Capítulo 3)*

---

### Pasado reciente — Adolescencia

**E-08** 🔶 El grupo de amigos se forma durante la secundaria.
El equilibrio entre Nagi y Rodrigo existe "desde la secundaria" (narrador, Capítulo 6).

**E-09** ✅ **"Tres años atrás"** (texto explícito, apertura del Capítulo 6):
En la casa de Cutipye, Lucien se presenta públicamente como Luz ante sus amigos.
Rodrigo ya lo sabía. Le dice: *"Te ves hermosa, Luz."*

**E-10** 🔶 En una fiesta organizada por Nagi, Rodrigo bebe en exceso y consume cannabis por primera vez.
Colapsa. Nagi lo sostiene para que no se ahogue. Azura coordina la atención por teléfono.
Rodrigo despierta en la habitación de Luz.
*(Flashback completo, Capítulo 9; referenciado brevemente en Capítulo 8)*

---

### Presente — La noche en el orfanato

**E-11** ✅ Tarde de otoño. El grupo entra al orfanato. Nagi rompe una ventanilla con el bate.
Caen al interior por la lavandería.

**E-12** ✅ El grupo se dispersa. Rodrigo escucha pasos pequeños y busca a sus amigas.
Escucha el grito de Luz, derriba una puerta oxidada y la encuentra pálida.
Ambos descubren la Araña-Huésped en el techo y huyen. *(Capítulo 1)*

**E-13** ✅ En el sótano, Rodrigo y Luz leen la Bitácora del Dr. Montané.
Comprenden el origen del Proyecto H-127.
Encuentran al sujeto herido, quien nombra a Galaxia y advierte que no deja escapar a nadie. Muere. *(Capítulo 2)*

**E-14** ✅ Rodrigo se esconde de la Mantis-Huésped tras un armario.
Una alarma lejana distrae a la criatura. Rodrigo y Luz se reencuentran.
Luz descubrió un pasadizo secreto hacia el ala sur. *(Capítulo 2)*

**E-15** ✅ El grupo se reúne con Azura en el vestíbulo. En el segundo piso, Luz encuentra la pistola.
Rodrigo lee la Entrada 04 (60% de muertes) y la oculta al grupo. *(Capítulo 3)*

**E-16** ✅ Galaxia aparece en la ventana del segundo piso.
El piso cede y Rodrigo cae al subsuelo. *(Capítulo 3)*

**E-17** ✅ Rodrigo le dispara a Galaxia en la frente. Ella se regenera.
Durante el escape por la escotilla, las garras de Galaxia le abren el costado.
Rodrigo dispara en el abdomen a quemarropa. Cierra la escotilla. Queda herido.
**Este es el momento de la infección del H-127.** *(Capítulo 4)*

**E-18** ✅ El grupo atraviesa la cocina-nido. Combate contra la Avispa Zángano.
Luz golpea a la criatura con la barra metálica más veces de las necesarias. Nadie lo comenta. *(Capítulo 5)*

**E-19** ✅ El grupo encuentra a Rodrigo en el cuarto de máquinas en estado de shock.
Rodrigo empieza a notar los primeros síntomas de la infección. *(Capítulos 5–6)*

**E-20** ✅ El grupo debate. El jugador elige entre ir al ala administrativa o retroceder. *(Capítulo 6)*
En ambas rutas, Rodrigo deja marcas oscuras sobre superficies que otros personajes notan pero no verbalizan.

**E-21** ✅ El grupo encuentra la Biblia con el nombre "Shio Katashi" y el versículo subrayado.
Azura encuentra y guarda en silencio la Entrada 09. *(Capítulo 7)*

**E-22** ✅ En el balcón, Rodrigo elige entre confesar o ocultar que siente la influencia del H-127.
Una gota negra y móvil penetra bajo su piel. *(Capítulo 7)*

**E-23** ✅ Amanecer. Rodrigo despierta con impulsos de buscar altura.
La Rata-Huésped ataca al personaje de menor afinidad. Rodrigo la mata.
El estilo del combate varía según el nivel de infección acumulado. *(Capítulo 8)*

**E-24** ✅ Luz muere. *(Capítulo 9)*

**E-25** ✅ Nagi puede traicionar o permanecer leal según `afinidad_nagi`. *(Capítulo 10)*
Si `afinidad_nagi < 3`: Galaxia lo captura. `nagi_dead = True`.

**E-26** ✅ Cutipye puede morir o asumir su responsabilidad según `afinidad_cutipye`. *(Capítulo 11)*
Si `afinidad_cutipye < 4`: Cutipye dispara cuatro veces a Galaxia; ella se regenera y mata a Cutipye.
`cuty_dead = True`.

**E-27** ✅ El grupo llega al pasillo de salida del orfanato. Galaxia bloquea la puerta. *(Capítulo 12)*
El incendio se inicia. Las criaturas dejan de obedecer a Galaxia y huyen por instinto.
Secuencia de escape con cinco QTEs temporizados. El final se bifurca según `estado_mental`.

---

### Desenlace — Post-incendio

**E-28** ✅ El orfanato queda destruido por el fuego. Galaxia muere en todos los finales.

**E-29** ✅ Familia de Luz: inicia una investigación que sigue abierta. Los sobrevivientes asisten al funeral.

**E-30** ✅ Familia de Rodrigo: el padre lo atribuye a desaparición voluntaria. La madre no habla del tema.
Nadie investiga. (En bad1: silencio total.)

**E-31** ✅ Familia de Nagi: si murió en Capítulo 10, la familia inicia búsqueda sin resultado.
Si murió en bad1: sin cuerpo, habitación intacta.

**E-32** ✅ Familia de Cutipye: si murió en Capítulo 11, funeral privado sin investigación formal.
Si murió en bad1: hermetismo, familia se muda de la ciudad.


---

## 7. Preguntas pendientes

Estas preguntas no tienen respuesta definitiva en los archivos del proyecto:

1. ⬜ **¿La herida de Cutipye en el Capítulo 1 fue infección por H-127?**
El origen de la herida no es aclarado dentro de la historia. Pendiente de planificación futura.
**Confirmado por el autor.**

2. ⬜ **¿Cuál es el punto exacto en que el vínculo de mente colmena se vuelve bidireccional?**
El autor confirma que ocurre cuando los sentidos de Rodrigo comienzan a distorsionarse,
pero ese umbral no está definido con exactitud numérica en los scripts actuales.
Los susurros de Galaxia aparecen desde los Capítulos 6–7, antes de la distorsión visual.

---

## 8. Contradicciones encontradas

### C-01 — Azura y la fiesta: presencia física ambigua
**Fuentes:** `script_2.rpy` (Capítulo 9), `DOC-Cronologia.md` (sección CT-03).

El Capítulo 9 narra que Rodrigo "olvidó a Azura" mientras la fiesta lo arrastraba,
lo que implica que estaba presente en el lugar.
La documentación interna afirma que Azura "no estaba presente físicamente" cuando ocurrió el colapso
y que actuó como "la voz al teléfono."
Estas dos afirmaciones son inconsistentes pero no irreconciliables:
Azura pudo estar en el lugar de la fiesta pero no en la habitación específica del colapso.
Los archivos no lo resuelven con claridad.

### C-02 — Duplicación del flashback de la sobredosis
**Fuentes:** `script_2.rpy` (Capítulo 8 y Capítulo 9).

El mismo evento (la sobredosis de Rodrigo) aparece referenciado brevemente en el Capítulo 8
y como flashback jugable completo en el Capítulo 9.
No es una contradicción sobre los hechos, sino una redundancia narrativa
cuya intencionalidad no queda clara en el código.

### C-03 — "Dictadura" como contexto del orfanato: rumor vs. ausencia en fuentes primarias
**Fuentes:** `script.rpy` (Azura, apertura) vs. Bitácora del Dr. Montané.

Azura menciona el rumor de que el orfanato fue usado como centro de tortura durante una dictadura.
La bitácora confirma el experimento H-127 pero no menciona ninguna dictadura ni contexto político.
La conexión entre el proyecto y un régimen político específico no tiene respaldo documental
en ningún archivo del proyecto.

---

*Documento generado a partir de los archivos fuente del proyecto y las declaraciones directas del autor.*
*No se ha añadido información externa ni inferida sin indicación explícita.*
*Última actualización: sesión del autor — segunda ronda de respuestas incorporadas.*
