# Identidad — Nagi

## Información básica

**Nombre:** Nagi
**Apellido:** Katashi *(Fuente: script_3.rpy — epílogo de créditos, texto literal: "Nagi Katashi sobrevivió a la experiencia…")*
**Apodo:** Ninguno registrado en los scripts. El grupo lo llama "Nagi" sin variantes.
**Edad:** 22 años. *(Fuente: autor)*
**Variable de código:** `n` *(Fuente: definitions.rpy)*
**Color de texto en diálogos:** `#7b2cbf` (púrpura medio) *(Fuente: definitions.rpy)*
**Variable de afinidad:** `afinidad_nagi` (valor inicial: 0) *(Fuente: definitions.rpy)*
**Rol narrativo:** Personaje secundario principal. Figura de energía extrovertida y cohesión del grupo. Su lealtad o ruptura con Rodrigo tiene consecuencias narrativas directas, incluyendo su posible muerte.
**Creador del personaje:** HeartAttack51 *(Fuente: script_3.rpy — créditos)*

---

## Historia

### Adolescencia y formación del grupo

Nagi se incorporó al grupo a través de su relación con Cutipye. No hay un episodio de origen dramático como el de Rodrigo con Luz — simplemente era cercano a ella, y esa cercanía lo integró de forma orgánica al núcleo. *(Fuente: autor)*

Era parte del grupo cuando llegó el momento de la presentación pública de Luz. En la reunión en casa de Cutipye, Nagi fue uno de los impactados visiblemente al verla llegar:

> *"Nagi soltó su vaso. Azura se cubrió la boca."*

Su expresión fue de sorpresa genuina (`casual_young_shock`). *(Fuente: script_2.rpy, cap. 6 — narración literal)*

Cuando Rodrigo apareció en esa misma reunión como invitado desconocido de Lucien, Nagi fue el primero en reaccionar con sarcasmo:

> *"¿Eh? ¿Te equivocaste de biblioteca, amigo? El club de ajedrez es los martes."*

Cutipye lo frenó con un codazo. El grupo integró a Rodrigo de todas formas. Nagi no resistió más. *(Fuente: script_2.rpy, cap. 6 — diálogo literal)*

Su relación con Rodrigo desde secundaria está descrita de forma explícita en la narración del Cap 6:

> *"El chico ruidoso arrastrando al callado fuera de su caparazón. El equilibrio que habían tenido desde secundaria."*

La frase representativa que le dirigía:

> *"Vamos, ermitaño, muévete o te cargo."*

*(Fuente: script_2.rpy — narración y cita representativa)*

### La sobredosis de Rodrigo

En una fiesta organizada por Nagi, Rodrigo colapsó por mezcla de alcohol y sustancias. Nagi fue quien lo sostuvo físicamente para que no se ahogara. La escena aparece en los flashbacks del Cap 8 (rama normal) y del Cap 9 (rama `traicion_nagi`):

> *"Rodrigo inconsciente. Vomitando. Nagi sosteniéndolo para que no se ahogara."*

Esa misma noche, fue él quien le ofreció a Rodrigo el primer porro que fumó en su vida:

> *"¿Quieres probar algo más... elevado?"*

Le enseñó a fumar. La noche terminó con Rodrigo en colapso. *(Fuente: script_2.rpy, flashbacks caps. 8 y 9)*

Ese episodio carga dos realidades simultáneas: Nagi puso a Rodrigo en riesgo, y también fue quien lo mantuvo con vida. En la rama de traición del Cap 10, convierte ese recuerdo en arma:

> *"¡Debí dejar que te ahogaras en tu vómito esa noche, animal!"*

*(Fuente: script_2.rpy, label traicion_nagi — diálogo literal)*

### La noche en el orfanato

Nagi fue quien rompió el vidrio del orfanato para que el grupo pudiera entrar, con su bate metálico:

> *"Nagi alzó su bate y lo estrelló contra una ventanilla, destrozando el vidrio antes de bajar."*

Su primer diálogo en el presente narrativo marca su postura ante la duda de Rodrigo:

> *"¿Acaso vas a acobardarte ahora que todos estamos de acuerdo?"*

*(Fuente: script.rpy — narración y diálogo literal)*

A partir del reencuentro del grupo tras dispersarse, Nagi lidera la propuesta táctica de ir al ala administrativa en busca de planos:

> *"Hay una ala administrativa por aquí. Si hay planos o salidas, estarán ahí."*
> *"No podemos quedarnos dando vueltas. Información nos da ventaja."*

*(Fuente: script_2.rpy, cap. 6 — diálogo literal)*

En la oficina de administración, se queda al lado de Rodrigo, analiza su estado y le hace la pregunta que nadie más se atreve a hacer:

> *"Ella te tocó, ¿no?"*

Y más tarde nombra lo que todos evitan nombrar:

> *"No. Suena a que estás infectado."*

*(Fuente: script_2.rpy — diálogos literales)*

En el Cap 7, levanta una vieja Biblia del suelo en la habitación abandonada y descubre el nombre real de Galaxia: *"Shio Katashi"*. Lee el versículo subrayado en voz alta ante el grupo. *(Fuente: script_2.rpy — narración y diálogo literal)*

### La confrontación del Cap 10

Según la variable `afinidad_nagi`, su comportamiento se bifurca radicalmente:

**Si `afinidad_nagi < 3` → `label traicion_nagi`:**

Nagi estalla contra Rodrigo, lo acusa frente al grupo de haber centrado todo el peso de la noche en él, y decide abandonar al grupo:

> *"Desde que entramos en este jodido lugar, todo gira en torno a él. Sus ataques. Sus cambios de humor. Sus… Malditas cosas raras."*
> *"¿Y quién nos salva a nosotros?"*
> *"No voy a morir aquí porque él no puede 'contener a su demonio interno'."*

Azura corre tras él y lo sujeta del brazo. Nagi la aparta con brusquedad que "ocultaba su propio miedo" — la narración lo señala explícitamente. Antes de alejarse definitivamente, usa el apodo de Azura:

> *"Zu-chan… míralo. Ya no es el chico con el que crecimos."*

Sus pasos se pierden en el pasillo oscuro. Segundos después, un grito desgarrador. Galaxia lo sostenía del cuello. Su último acto antes de ser arrastrado es escupirle en la cara:

> *"...Púdrete."*

La puerta metálica se cierra. El grupo no llega a tiempo. `$ nagi_dead = True` *(Fuente: script_2.rpy, label traicion_nagi — diálogos literales y código)*

**Si `afinidad_nagi ≥ 3` → `label nagi_no_traiciona`:**

También explota, también usa el recuerdo de la sobredosis, también acusa. Pero no cruza la puerta. Acepta la mediación de Azura. Termina dando una palmada en la espalda de Rodrigo con tono que mezcla frustración y lealtad:

> *"¡Eso es! No te voy a dejar solo, idiota. Pero apúrate, o te cargo yo mismo."*

El grupo avanza unido. *(Fuente: script_2.rpy, label nagi_no_traiciona — diálogo literal)*

---

## Personalidad

**Extrovertido y ruidoso por diseño.** El script lo describe repetidamente como quien hace chistes, arrastra al grupo hacia adelante y rompe el silencio. Su ausencia de ruido funciona como indicador narrativo de alarma. El narrador lo señala de forma explícita:

> *"No hubo sonrisa. No hubo exageración teatral. Solo una frase corta. Directa. Rodrigo sintió esa ausencia más que cualquier grito."*

*(Fuente: script_2.rpy — narración literal)*

**Lee a Rodrigo con precisión.** Es el personaje que mejor interpreta la comunicación no verbal del protagonista. Lo nombra directamente:

> *"Te conozco. Cuando te quedas así de callado no es porque estés pensando. Es porque algo te aplasta por dentro."*

*(Fuente: script_2.rpy — diálogo literal)*

**Impulsivo y directo.** Sus primeras respuestas son verbales y físicas. Sarcasmo, señalar, empujar. Cuando la situación exige moderación, puede reencauzarse — pero le cuesta visible esfuerzo.

**Valentía sin glamour.** Ante Galaxia, siendo sostenido del cuello, le escupe en la cara. No hay heroísmo calculado en ese gesto — es solo Nagi siendo Nagi:

> *"...Púdrete."*

*(Fuente: script_2.rpy — diálogo literal)*

**Protector ambiguo.** Sostuvo a Rodrigo para que no muriera en la fiesta que él mismo organizó. También fue quien le ofreció las sustancias esa noche. Esa tensión entre haber salvado y haber puesto en riesgo es parte irresuelta de su relación con Rodrigo, y es el material de la acusación más brutal del Cap 10.

**Humor como herramienta social.** Sus chistes tienen función práctica: romper tensión, integrar, empujar al grupo. Cuando deja de usarlos es porque algo lo está aplastando. Cutipye lo reconoce como "territorio de Nagi":

> *"No estoy haciendo un discurso motivacional. Eso es territorio de Nagi."*

*(Fuente: script_2.rpy — diálogo literal)*

**Cobardía disfrazada de rabia.** Su explosión del Cap 10 no es solo furia. La narración lo deja explícito: *"Nagi la apartó con una brusquedad que ocultaba su propio miedo."* *(Fuente: script_2.rpy — narración literal)*

**Post-supervivencia (ending good):** Quien sobrevive no es el mismo Nagi. El cambio es brusco: de alguien impulsivo y ruidoso, pasa a ser alguien temeroso y precavido. La experiencia del orfanato lo reescribió. *(Fuente: autor; script_3.rpy — epílogo literal: "nunca volvió a ser el mismo")*

---

## Motivaciones

**Motivación principal (implícita):** Sobrevivir y sacar al grupo del orfanato. No la verbaliza de forma heroica — la expresa a través de acción y decisiones prácticas.

**Conflicto central:** La tensión entre su lealtad a Rodrigo y su miedo a lo que Rodrigo se está convirtiendo. Es el personaje que pronuncia en voz alta lo que nadie quiere decir:

> *"No. Suena a que estás infectado."*

*(Fuente: script_2.rpy — diálogo literal)*

**Lo que lo ancla:** Su pertenencia al grupo. Su identidad no existe fuera de ese núcleo. Abandonarlos — aunque lo intente — no le sale de forma limpia:

> *"Nagi duda. Por un segundo, realmente duda."*

*(Fuente: script_2.rpy — narración literal)*

**Lo que lo rompe:** Sentir que la carga de cuidar a Rodrigo es unilateral y que nadie los cuida a ellos:

> *"¿Y quién nos salva a nosotros?"*

*(Fuente: script_2.rpy, label traicion_nagi — diálogo literal)*

---

## Relaciones

### Cutipye — pareja romántica
La relación más larga y fundacional de Nagi en la historia. Su incorporación al grupo de amigos ocurrió a través de ella — no hubo un evento dramático de origen, sino la proximidad natural de estar con alguien que importa. La narración del Cap 6 lo describe "apoyándose muy cerca de Cutipye" en la fiesta de su casa. *(Fuente: script_2.rpy — narración literal; autor — confirmación de relación romántica)*

La dinámica entre ambos es de pique amistoso constante: ella lo frena con codazos cuando se pasa, él la provoca con humor. El narrador asigna el "territorio" de los discursos motivadores exclusivamente a Nagi, que Cutipye reconoce como suyo.

La relación no tiene peso narrativo explícito en los arcos de decisión del juego, pero constituye la base de la presencia de Nagi en el grupo. *(Fuente: autor)*

### Rodrigo — amigo desde secundaria con dinámica de empuje-resistencia
La relación más documentada de Nagi en los scripts. Definida como "el chico ruidoso arrastrando al callado fuera de su caparazón." Nagi lo llama "ermitaño", "fantasma", "poeta deprimido", "ratón de biblioteca". Lo empuja. Lo sostiene. Lo conoce con suficiente profundidad para leerle el estado sin palabras — y para usar esa misma profundidad como arma en el peor momento.

**Variable:** `afinidad_nagi` — Threshold < 3 activa traición y muerte. Threshold ≥ 3 mantiene la unidad del grupo y activa el rol de Nagi como soporte físico en el escape final.

### Azura — amiga cercana
Nagi la llama "Zu-chan". El uso del apodo tiene su momento de mayor peso en el Cap 10, cuando lo pronuncia justo antes de intentar separarse del grupo — un gesto de cercanía en el peor contexto:

> *"Zu-chan… míralo. Ya no es el chico con el que crecimos."*

*(Fuente: script_2.rpy — diálogo literal)*

### Luz — amistad funcional dentro del grupo
Estuvo presente en la presentación pública de Luz y fue uno de los impactados visiblemente. No tiene diálogos directos significativos con ella más allá del contexto grupal. *(Fuente: script_2.rpy)*

### Galaxia — captor y posible verdugo
El único personaje con contacto físico directo con Nagi en los scripts. Lo sostiene del cuello. Nagi le escupe. Galaxia lo califica con tono burlón:

> *"Y tú te ofreciste solito."*
> *"Empezaba a tener hambre~"*

*(Fuente: script_2.rpy — diálogos literales)*

---

## Habilidades

- **Bate metálico deportivo** — su arma personal, con evidentes signos de desgaste. Lo lleva a propósito, oculto en la mochila. Lo usa para romper el vidrio del orfanato en la entrada. *(Fuente: script.rpy — narración; autor — descripción física del arma)*
- **Fuerza física y combate directo** — en la rama donde sobrevive al Cap 10, asume el rol de soporte físico y defensa del grupo durante el escape final. *(Fuente: autor)*
- **Liderazgo situacional** — propone el siguiente movimiento cuando el grupo se paraliza (ir a administración, buscar planos, mantener la ruta).
- **Lectura interpersonal** — identifica el estado emocional de Rodrigo antes de que él mismo lo verbalice.
- **Tolerancia física** — aguanta ser sostenido del cuello por Galaxia con suficiente control para articular una respuesta verbal.
- **Conocimiento de sustancias** — familiaridad con alcohol y cannabis confirmada en el flashback del Cap 9. Fue quien introdujo a Rodrigo a fumar.

---

## Diseño

### Apariencia física *(Fuente: autor)*
- **Altura:** 1.75 m
- **Cabello:** Negro opaco
- **Ojos:** Púrpura
- **Ropa habitual:** Polerón púrpura con cierre (siempre abierto) / polera negra deportiva por debajo / pantalón baggy morado oscuro / zapatillas deportivas púrpura
- **Accesorio:** Collar de una cruz

### Sprites implementados
Todos los sprites usan actualmente el mismo archivo placeholder `images/sprites/Nagi.png`. *(Fuente: definitions.rpy)*

Expresiones definidas en código:
`neutral`, `smug`, `smile`, `serio`, `soft`, `tired`, `angry`, `annoyed`, `worried`, `shocked`, `surprised`, `scared`

**Versión joven (flashbacks):** `casual_young`, `casual_young_molesto`, `casual_young_shock` — usadas en el flashback del cap. 6. *(Fuente: script_2.rpy y definitions.rpy)*

**Estado muerto:** `dead` — efecto `TintMatrix("#000000")`, sprite teñido completamente negro. *(Fuente: definitions.rpy)*

**Detalle técnico:** El sprite `sujeto_herido` (el hombre moribundo de la habitación H-127) reutiliza `images/sprites/Nagi.png` con `TintMatrix("#000000")`. Es un sprite compartido por limitación técnica, sin relación narrativa entre ambos personajes. *(Fuente: definitions.rpy — comentario en código)*

### Color de diálogo
`#7b2cbf` — púrpura medio. *(Fuente: definitions.rpy)*

### Tema musical
Sin tema propio asignado. *(Fuente: definitions.rpy)*

---

## Curiosidades

- Nagi organizó la fiesta donde Rodrigo consumió sustancias y casi murió. También fue quien lo sostuvo para que no se ahogara. Ambas cosas son ciertas al mismo tiempo, y esa dualidad es el núcleo de la acusación más devastadora del Cap 10.
- Es el único personaje que pronuncia en voz alta la palabra "infectado" ante Rodrigo cuando nadie más se atreve: *"No. Suena a que estás infectado."* La narración anota: *"La palabra cayó como plomo."*
- El narrador describe el equilibrio entre Nagi y Rodrigo desde la secundaria como "el chico ruidoso arrastrando al callado fuera de su caparazón". En el orfanato ese equilibrio se invierte: Nagi deja de empujarlo hacia afuera y empieza a intentar impedir que algo se lo lleve por dentro.
- Ante Galaxia, sostenido del cuello, le escupe en la cara. Es el único personaje del script con ese tipo de respuesta ante ella.
- Su apellido, Katashi (堅), significa en japonés "firme", "sólido", "duro" — coherente con su función narrativa hasta el momento en que se rompe.
- El catálogo de expresiones negativas en su sprite supera al de expresiones positivas: `angry`, `annoyed`, `worried`, `shocked`, `scared`, `tired`, `serio` frente a `smug` y `smile`. La variedad de tensión contrasta con sus dos estados "normales".
- Si sobrevive, el epílogo del ending good dice que "nunca volvió a ser el mismo": deja de ser impulsivo y ruidoso para convertirse en alguien temeroso y precavido. El orfanato lo reescribió. *(Fuente: script_3.rpy — texto literal; autor — descripción del cambio)*
- Si muere en la rama `traicion_nagi`, su familia gastó todos sus recursos en una búsqueda sin resultado. Su habitación permanece intacta. Si muere en `ending_type == "bad1"`, no hay cuerpo ni pistas. *(Fuente: script_3.rpy — textos literales de ambas variantes)*

---

## Información pendiente

- Descripción de la ropa de Nagi en los flashbacks de adolescencia (¿usa `casual_young` con alguna variante de diseño específica o es la misma paleta de colores que en el presente?).
- Diseño visual final de sprites (actualmente todos son placeholder con el mismo PNG).
- Desarrollo de capítulos posteriores al Cap 10 en la rama donde sobrevive — solo está esbozado como "soporte físico en el escape".
- Tema musical propio — no existe asignado en `definitions.rpy`.
- Historial anterior con Cutipye — la relación romántica está confirmada, pero no hay flashback propio ni escena de origen dentro del script.

---

## Preguntas para el autor

*Todas las preguntas anteriores han sido respondidas. No hay preguntas abiertas en este momento.*
