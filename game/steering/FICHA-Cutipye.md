# Identidad — Cutipye

## Información básica

**Nombre:** Cutipye
**Apellido:** Hayashi *(Fuente: autor)*
**Apodo:** "Cuty" — usado por Rodrigo en el script. *(Fuente: script_2.rpy — `r "Tengo miedo, Cuty."` y otros contextos)*
**Edad:** 20 años (presente de la historia). *(Fuente: autor)*
**Variable de código:** `c` *(Fuente: definitions.rpy)*
**Color de texto en diálogos:** `#2dff5a` (verde brillante) *(Fuente: definitions.rpy)*
**Variable de afinidad:** `afinidad_cutipye` (valor inicial: 0) *(Fuente: definitions.rpy)*
**Rol narrativo:** Personaje secundario principal. Figura de humor defensivo y apoyo emocional directo. Su supervivencia o muerte depende de la afinidad acumulada con Rodrigo — el threshold `< 4` activa su traición verbal y eventual muerte a manos de Galaxia en Cap 11. *(Fuente: script_2.rpy — código condicional)*
**Diseñadora del personaje:** Uraku *(Fuente: script_3.rpy — créditos)*

---

## Historia

### Origen y entorno familiar

La casa de Cutipye es el escenario del flashback del Cap 6: "olía a perfume caro y aperitivos horneados. Era una reunión pequeña, pero el lujo se notaba en cada rincón." Su entorno familiar es económicamente acomodado, aunque no se detalla más en el script.

En el epílogo del ending donde muere (`cuty_dead == True`), el padre de Cutipye organiza un funeral privado al que solo asisten familiares y amigos cercanos. La familia se niega a hablar del tema con la prensa y no se inicia ninguna investigación formal. En el ending `bad1`, la desaparición es tratada "con absoluto hermetismo" y la familia se muda de la ciudad. Este patrón de silencio y hermetismo ante la tragedia es consistente con un entorno que prioriza la reputación por encima del duelo público.

*(Fuente: script_3.rpy — epílogos)*

### Fundadora del grupo

Junto con Azura, Cutipye forma el núcleo original del grupo de amigos. Son las amigas más antiguas entre sí y toda la dinámica del grupo creció a partir de esa relación.

En el flashback del Cap 6, es ella quien organiza la reunión en su propia casa para que Luz pueda presentarse con su identidad real. Cuando Rodrigo llega como desconocido, Cutipye abre la puerta y lo recibe con bienvenida cautelosa, frenando a Nagi cuando este hace un chiste incómodo:

> *"¡Nagi! Cierra la boca."*
> *"Ignóralo, Rodri. Bienvenido. Aunque... ¿Lucien te invitó?"*

El script la describe con "un toque de duda en sus ojos", pero esa duda no se traduce en rechazo. *(Fuente: script_2.rpy, cap. 6 — diálogos literales)*

### La noche de la sobredosis de Rodrigo (flashback)

En la fiesta organizada por Nagi, Cutipye fue quien le ofreció el vaso a Rodrigo:

> *"Sí, relájate un poco. Un par de tragos no matan a nadie. Ayúdanos a que el ambiente prenda."*

Cuando Rodrigo colapsó, Azura los guió desde el teléfono con instrucciones dirigidas a "Nagi. Cutipye." — confirmando que ella estaba presente y fue parte activa del rescate. *(Fuente: script_2.rpy, flashback cap. 9 — diálogos literales)*

### La noche en el orfanato

Cutipye entra al orfanato junto con el grupo a través de la ventana rota. En el primer pasillo se separa, sufre algún tipo de enfrentamiento con el Huésped-Rata (escena placeholder en el script actual), y su mochila es encontrada por Rodrigo y Luz en un pasillo:

> *"Es de Cutipye."*

La mochila contiene "el cuaderno de dibujos de su amiga" — detalle de caracterización que tiene importancia narrativa crítica más adelante: el cuaderno es una pieza clave en la planificación del incendio que termina por quemar el orfanato. *(Fuente: script.rpy, cap. 1 — narración literal; autor)*

**Cap. 3:** Cuando el suelo se derrumba bajo los pies de Rodrigo, Cutipye y Nagi lo presencian desde el piso superior. *(Fuente: script.rpy, cap. 3 — código)*

**Cap. 5:** Reacciona ante la peste de la zona de cocina:

> *"Ugh... ¿Qué es esa peste?"*

Durante el enfrentamiento con las avispas, Nagi y Cutipye se lanzan juntos contra la puerta bloqueada: *"¡Ayudenme! ¡Está atascada con esa cera!"*. Tras el combate, observa a Luz sostener la barra sin soltarla. No dice nada. Nadie dice nada. *(Fuente: script.rpy, cap. 5 — narración y diálogos literales)*

**Cap. 6 (debate nagi vs. cuty):** Cutipye se opone a adentrarse más en el orfanato mientras Nagi propone buscar información:

> *"¿Y si es una trampa? Ya vimos lo que hay cuando nos metemos más adentro."*
> *"O podemos irnos y vivir otro día. Yo prefiero no 'arriesgar ventaja'."*

Si el jugador le da la razón, ella toma el liderazgo del grupo para intentar retroceder. En esa rama, detecta el silencio inusual de Rodrigo y actúa directamente:

> *"¿Sabes cuál es la parte buena de que seas tan callado? Que cuando te quedas más callado de lo normal… es muy obvio."*

Si Rodrigo confiesa que tiene miedo, Cutipye baja la voz:

> *"Bien. Eso significa que todavía quieres salir de aquí. Yo también tengo miedo. Pero prefiero tener miedo contigo que hacerme la valiente sola."*

Cuando nota la marca oscura que Rodrigo deja en la pared, si él responde "No lo sé":

> *"Vale. Entonces lo vigilamos. No te voy a dejar convertirte en… Bueno. En algo raro sin avisarme."*

*(Fuente: script_2.rpy, cap. 6 — diálogos literales)*

**Cap. 7:** En la habitación abandonada con la Biblia, reacciona al nombre real de Galaxia con una sola frase:

> *"Entonces… ese no era su nombre real."*

Breve, directa, sin elaborar. *(Fuente: script_2.rpy, cap. 7)*

**Cap. 8 (Huésped-Rata):** Si `afinidad_cutipye` es la más baja del grupo, la criatura la ataca a ella. Su reacción: *"¡Atrás!"*. Tras el combate: *"Parecías... disfrutándolo. Tu cara..."* *(Fuente: script_2.rpy — código condicional y diálogo literal)*

**Cap. 9 (post-muerte de Luz):** En el vestíbulo, cuando el grupo forma el semicírculo de miedo ante Rodrigo:

> *"Miren, ya no tiene tanto caso el decir si Rodrigo tenía razón o no, venir a este orfanato fue una idea estúpida y debemos irnos cuanto antes."*

Cuando Galaxia ejerce influencia y Luz defiende a Rodrigo, Cutipye se opone: *"Luz, esto es peligroso. Debemos irnos antes de que... algo peor pase."* El narrador la describe en ese momento: "Cutipye calcula distancias." *(Fuente: script_2.rpy — diálogos literales y narración)*

**Cap. 10 (rama traición Nagi):** Cuando Nagi estalla contra Rodrigo, Cutipye dice lo que nadie había verbalizado:

> *"Tiene razón. Yo lo quiero… Pero también tengo miedo. No sé si podamos detenerlo si se transforma del todo."*

Es afecto y terror en la misma frase, sin elegir entre los dos. Cuando Galaxia captura a Nagi, Cutipye "apretó los puños hasta que sus nudillos blanquearon". Rodrigo la frena cuando intenta correr hacia el ruido. *(Fuente: script_2.rpy — narración y diálogos literales)*

**Cap. 10 (rama nagi no traiciona):** Cutipye alivia la tensión con humor nervioso:

> *"Sí, ¡vamos! Como en esas películas donde todos corren y nadie se queda atrás. Rodri, si te transformas, te doy un beso para que vuelvas... o un golpe, lo que funcione primero. ¡Je!"*

El narrador añade: "Pero su risa es nerviosa, y mira a Rodrigo con una mezcla de cariño y temor real." *(Fuente: script_2.rpy — diálogo literal y narración)*

**Cap. 11 (afinidad_cutipye < 4 — traición):** En la enfermería abandonada, Cutipye rompe. Le lanza a Rodrigo uno de los ataques verbales más duros del juego — una observación lúcida, expresada de forma hiriente a propósito:

> *"Es fascinante, ¿No? Como siempre logras que todo sea un caos absoluto."*
> *"Siempre tienes el consejo perfecto para los demás. 'Relájate', dices. 'Estás exagerando', dices."*
> *"Te da miedo convertirte en lo que siempre has sido en el fondo."*
> *"Eres un monstruo porque eliges comportarte como uno cuando tienes miedo."*

Rodrigo llora en silencio sin defenderse. Cutipye termina: *"No puedo más. Necesito aire antes de que yo también me vuelva loca."* — y sale de la sala. Azura intenta detenerla con un ruego que no es una orden.

En el pasillo, Galaxia la intercepta y le dice que lo que acaba de hacer fue "ser honesta". La empuja contra la pared. Cutipye llega a una habitación impecable donde Galaxia está sentada en una silla de mimbre. Saca la pistola de Rodrigo y dispara cuatro veces: pierna, hombro, torso, cuello. Las heridas se cierran. Con el cargador vacío:

> *"Eso no ha sido nada amable. Y yo que quería ser tu amiga."*

La escena termina con `$ cutipye_dead = True`. *(Fuente: script_2.rpy — diálogos literales, narración, código)*

**Cap. 11 (afinidad_cutipye ≥ 4 — mea culpa):** La escena de traición no se activa. En su lugar, Cutipye asume la responsabilidad de la situación: reconoce en voz alta que fue ella quien tuvo la idea de explorar el orfanato, y que la tragedia — todo lo que el grupo ha perdido — arranca de esa decisión. Es el contraste directo con la escena de baja afinidad: en vez de "cantarle sus verdades" a Rodrigo, se las canta a sí misma. El mea culpa reemplaza el ataque externo por una carga interna asumida, y el efecto dramático es opuesto — en lugar de romper la relación con Rodrigo, la escena la refuerza. El peso emocional de Cutipye es igual de pesado en ambas ramas. La escena está planificada pero pendiente de implementación en el script. *(Fuente: autor; script_2.rpy — código, comentario `# Placeholder para afinidad alta`)*

---

## Personalidad

**Humor como mecanismo de aguante.** Su recurso más inmediato ante el peligro o la tensión es el chiste. En Cap 6, el narrador lo lee con claridad: *"No estaba tratando de ser graciosa. Estaba tratando de que nadie se rompiera."* Cuando deja de hacer chistes, algo está muy mal. *(Fuente: script_2.rpy, cap. 6 — narración literal)*

**Directa y sin rodeos.** No disimula lo que ve. Cuando Rodrigo se calla de más, lo nombra. Cuando algo es peligroso, lo dice. Sus intervenciones más duras son también sus más honestas. La frase del Cap 11 no es un insulto instintivo: es una observación lúcida dicha con intención de herir. *(Fuente: autor; script_2.rpy, cap. 11)*

**Pragmatismo en crisis.** Es la voz del "vamos a sobrevivir" por encima de todo. Prefiere retroceder, prefiere salir. Su lógica es funcional pero no fría: convive con el afecto sin contradicción.

**Afecto real con miedo real, en la misma frase.** Su línea más reveladora del juego: *"Yo lo quiero… Pero también tengo miedo."* No elige entre los dos. Esa incapacidad de separar el cariño del terror es la raíz de lo que ocurre en Cap 11. *(Fuente: script_2.rpy, cap. 10 — diálogo literal)*

**Se rompe cuando ya no puede sostener más.** El ataque verbal en Cap 11 no es crueldad por vocación. Es el desborde de alguien que ha estado aguantando demasiado tiempo. El hecho de que Galaxia la intercepte justo en ese momento sugiere que la criatura esperaba activamente esa fractura. *(Fuente: script_2.rpy, cap. 11)*

**Observadora.** Nota cuando Rodrigo deja de hacer chistes. Nota la marca oscura en la pared. Nota el gesto de limpiarse la manga. No siempre actúa sobre lo que observa, pero registra. *(Fuente: script_2.rpy, cap. 6)*

**No se rinde.** Cuando Galaxia la arrincona con el cargador vacío, ya ha disparado cuatro veces. No funcionó. Pero lo intentó. *(Fuente: script_2.rpy, `escena_traicion_cutipye`)*

---

## Motivaciones

**Motivación principal:** Sacar al grupo del orfanato con vida. Su postura consistente es la retirada estratégica: *"O podemos irnos y vivir otro día."*

**Motivación secundaria:** Proteger a Rodrigo de sí mismo, mientras sea posible. Le dice la verdad sin suavizarla y le recuerda quién es:

> *"No eres el guardaespaldas oficial del grupo. Eres Rodrigo. Y eso ya es suficiente."*

*(Fuente: script_2.rpy, cap. 6 — diálogo literal)*

**Miedo central (implícito):** Quedarse sin nada a qué aferrarse. Cuando Rodrigo se transforma más allá de lo reconocible, Cutipye pierde el único ancla que le permitía sostener el miedo: la certeza de que él sigue siendo él.

---

## Relaciones

### Azura — amiga fundadora
La relación más antigua del grupo. Juntas forman el núcleo a partir del cual creció todo lo demás. Comparten todas las escenas de acción disponibles en el script: empujan puertas juntas, se aferran al suelo juntas. En Cap 11, Azura intenta detenerla con un ruego cuando Cutipye ataca verbalmente a Rodrigo. En la rama de alta afinidad (pendiente de desarrollo), se planea una conversación donde juntas lamentan haber traído al grupo al orfanato y buscan un escape. *(Fuente: script.rpy, script_2.rpy, FICHA-Azura.txt)*

### Rodrigo — amigo cercano, relación con tensión latente
Cutipye conoce a Rodrigo mejor de lo que él reconoce. Lo lee con precisión, lo confronta sin insultar (en los capítulos intermedios), y lo ancora cuando se desorienta. Cuando la afinidad cae, esa misma capacidad de leerlo se convierte en el filo del ataque más duro que él recibe en todo el juego. El núcleo de su relación es la ambivalencia: afecto genuino que no puede sostenerse cuando el miedo supera un umbral.

**Variable:** `afinidad_cutipye` — threshold `< 4` activa su traición y muerte en Cap 11. *(Fuente: script_2.rpy — código condicional)*

### Nagi — amigo cercano
Comparten la misma tolerancia baja ante la transformación de Rodrigo. Cuando Nagi estalla en Cap 10, Cutipye no lo frena — confirma su miedo. Son los dos personajes con el umbral de ruptura más bajo. *(Fuente: script_2.rpy, cap. 10)*

### Luz — amiga del grupo
Sin conflicto personal visible en el script. Cuando Luz defiende a Rodrigo en Cap 9, Cutipye se opone desde el pragmatismo, no desde la animosidad. *(Fuente: script_2.rpy, cap. 9)*

### Galaxia — relación depredador-presa con componente psicológico
Galaxia elige el momento exacto de fractura de Cutipye para interceptarla. Le dice que lo que hizo fue "ser honesta". No la ataca en la oscuridad: la sienta frente a ella en una habitación impecable y tiene una conversación antes de matarla. El ataque es tan calculado como el que ejecutó contra Rodrigo: espera a que la presa esté sola, exhausta, y sin el escudo del grupo. *(Fuente: script_2.rpy, `escena_traicion_cutipye`)*

---

## Habilidades

**Gestión del ambiente del grupo.** Su principal recurso: detectar cuándo el grupo está a punto de romperse y actuar para evitarlo. Lo hace con humor, con preguntas directas, con chistes nerviosos. *(Fuente: script_2.rpy, múltiples escenas)*

**Combate improvisado.** Participó en el combate del Zángano (Cap 5), lanzando el extintor en la Fase 1 del QTE junto al grupo. *(Fuente: script.rpy, cap. 5 — código QTE)*

**Manejo de arma de fuego (básico).** En `escena_traicion_cutipye` usa la pistola de Rodrigo y dispara cuatro veces, impactando en pierna, hombro, torso y cuello. Tiene sangre fría para disparar. *(Fuente: script_2.rpy)*

**Dibujo.** Lleva un cuaderno de dibujos en su mochila. Es el único dato sobre este hábito en el script. El cuaderno funciona inicialmente como detalle de caracterización, pero es una pieza clave en la planificación del incendio que destruye el orfanato. *(Fuente: script.rpy, cap. 1 — narración literal; autor)*

**Observación emocional.** Detecta cambios en Rodrigo antes de que él los verbalice. Nota la marca en la pared, el gesto de limpiarse la manga, la calidad del silencio. *(Fuente: script_2.rpy, cap. 6)*

---

## Diseño

### Apariencia física *(Fuente: autor)*
- **Cabello:** Castaño claro
- **Ojos:** Verde menta
- **Altura:** 1.60 m
- **Ropa habitual:** Polerón negro / camisa blanca por debajo / falda azul de mezclilla / calcetas blancas / zapatillas negras

### Sprites implementados
Todos los sprites usan actualmente el mismo archivo placeholder `images/sprites/Cutipye.png`. *(Fuente: definitions.rpy)*

Expresiones definidas en `definitions.rpy`:
`neutral`, `smile`, `smile_nervous`, `determined`, `serious`, `soft`, `scared`, `shocked`, `tired`, `disgust`, `casual_young`, `throw`, `worried`

**Estado muerto:** `dead` — efecto `TintMatrix("#000000")`, sprite teñido completamente negro. *(Fuente: definitions.rpy)*
**Versión joven (flashback):** `casual_young` — usada en el flashback del cap. 6. *(Fuente: script_2.rpy y definitions.rpy)*

**Discrepancia técnica — sprites del Cap 11:** El script de la escena de traición referencia las siguientes expresiones: `media_sonrisa`, `mirada_reojo`, `sorpresa_fingida`, `seria`, `fria`, `cansada`. Ninguna de estas está definida en `definitions.rpy`. Requieren ser añadidas antes de implementar esa escena. *(Fuente: script_2.rpy, cap. 11; definitions.rpy — discrepancia confirmada)*

### Color de diálogo
`#2dff5a` — verde brillante. *(Fuente: definitions.rpy)*

---

## Curiosidades

- La reunión en la que Luz se presentó con su identidad real fue organizada y alojada en casa de Cutipye. Es su acto de lealtad más antiguo registrado en el script. *(Fuente: script_2.rpy, cap. 6)*
- Tiene un cuaderno de dibujos que parece ser solo un detalle de caracterización, pero es una pieza clave en la planificación del incendio que destruye el orfanato. *(Fuente: script.rpy, cap. 1; autor)*
- La frase del Cap 11 — *"Te da miedo convertirte en lo que siempre has sido en el fondo"* — es una observación lúcida de Cutipye, dicha con intención de herir. No es un insulto instintivo ni la voz de Galaxia: es lo que Cutipye genuinamente cree, expresado en el peor momento posible. *(Fuente: autor)*
- Es la única del grupo que ataca verbalmente a Rodrigo sin haber recibido daño directo de él. Su desborde nace del miedo acumulado, no de una herida personal. *(Fuente: script_2.rpy, cap. 11)*
- El algoritmo del Cap 8 la ubica en segundo lugar de prioridad para el Huésped-Rata, después de Nagi: `prioridad = {"nagi": 0, "cutipye": 1, "azura": 2, "luz": 3}`. Esto implica que el jugador tiende a tener más roces con ella que con Azura o Luz. *(Fuente: script_2.rpy — código Python literal)*
- En el ending de supervivencia, no puede superar el trauma, se vuelve retraída y distante, y se muda a otra ciudad. Es el ending de supervivencia más sombrío entre los personajes que sobreviven. Esta mudanza puede dar pie a un arco personal en una hipotética secuela. *(Fuente: script_3.rpy — texto literal; autor)*
- Galaxia la intercepta inmediatamente después de que sale sola del grupo, lo que sugiere que la criatura monitoreaba activamente el momento de fractura. *(Fuente: script_2.rpy, cap. 11)*

---

## Información pendiente

- Diseño visual final de sprites (actualmente todos son placeholder con el mismo PNG).
- Los sprites del Cap 11 (`media_sonrisa`, `mirada_reojo`, `sorpresa_fingida`, `seria`, `fria`, `cansada`) no están definidos en `definitions.rpy` y necesitan ser añadidos antes de implementar esa escena.
- Contenido detallado de la escena de mea culpa en la rama `afinidad_cutipye ≥ 4` del Cap 11 (planificada por el autor, sin implementar en el script).
- Contenido exacto del enfrentamiento con el Huésped-Rata que la separó del grupo en Cap 1/2 (mencionado en el script pero no implementado).
- Mecánica exacta por la que el cuaderno actúa como pieza clave en la planificación del incendio (no implementada en los scripts actuales).

---

## Preguntas para el autor

*Todas las preguntas anteriores han sido respondidas. No hay preguntas abiertas en este momento.*
