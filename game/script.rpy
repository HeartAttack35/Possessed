################
#   ACTO 0
################

label start:
    # Configuración inicial: Transición a negro para preparar la inmersión
    show screen hud_stats
    stop music fadeout 1.0
    scene black with fade
    pause 1.0

    # Texto en pantalla para ubicar al jugador temporalmente
    centered "{i}Hace 15 años...\nCentro de Investigación Subterráneo H-127{/i}" with fade
    pause 1.5
    scene black with fade
    pause 0.4

    scene pasillo_abandonado at oscuro, distortion_heavy with hpunch
    play ambient "sfx/alarm.mp3" loop volume 0.7
    play music chase fadein 1.0

    "Luz roja. Intermitente."
    "Un pitido metálico, el mismo, una y otra vez."

    play sound "sfx/heavy_breathing.mp3" loop volume 0.9
    "Un hombre corría. No hacia ningún lugar en particular."
    "Solo lejos."

    play sound objfall
    "Algo metálico cayó de sus manos. No se detuvo a recogerlo."

    play sound "sfx/keycard_fail.mp3" volume 0.5
    "{color=#999999}{i}[[ALTAVOZ] Protocolo Hades activado. Personal no autorizado, evacúe el nivel de inmediato.{/i}{/color}"

    investigador "{cps=25}No, no, no—{/cps}"

    pause 0.3
    "{color=#999999}{i}[[ALTAVOZ] Esto no es un simulacro.{/i}{/color}"

    "Una carpeta abierta en el suelo. Un sello a medio borrar."
    "{cps=15}{b}CONFIDENCIAL{/b}{/cps}"
    "Una palabra tachada a mitad, ilegible salvo por una esquina: {i}...cindibles.{/i}"
    "No se detuvo a leerla completa."

    play sound "sfx/radio_static.mp3" volume 0.6
    "Estática. Una voz partida, casi irreconocible, en su radio."
    "{cps=25}—perdimos el nivel tres, repito, perdimos el—{/cps}"

    play sound scream2 volume 0.5
    "Un grito. Después, nada."
    "No era la primera vez que un canal se apagaba así esa noche."

    stop sound
    play sound run loop

    scene pasillo_abandonado at oscuro with dissolve
    "Dobló una esquina. Una mancha oscura en la pared, todavía brillante."
    "No se detuvo a preguntarse de quién era."

    scene pasillo_abandonado at oscuro
    "Las luces rojas parpadearon... y por un segundo, se quedaron fijas."
    "Silencio."

    stop sound fadeout 0.4
    play sound "sfx/heavy_breathing.mp3" loop volume 0.5

    investigador "{cps=20}...¿Ya está? ¿Ya pasó?{/cps}"

    pause 1.2

    # La falsa calma se rompe
    play sound crack
    with vpunch
    "Un crujido lejano. Algo, en algún nivel inferior, terminó de ceder."

    "Las luces volvieron a fallar. Rojo. Negro. Rojo."

    stop sound
    play sound run loop

    # --- ACERCAMIENTO: solo sonido, nunca confirmación visual ---
    play sound "sfx/claw_drag_concrete.mp3" volume 0.4
    "Algo, detrás de él, arrastraba algo metálico contra el hormigón."
    "No se giró a comprobarlo."

    "Los gritos de los niveles inferiores se habían apagado uno por uno."
    "Ese silencio pesaba más que cualquier alarma."

    # --- ÚLTIMA CORRIDA ---
    scene escape_1 at oscuro with vpunch
    play sound land

    "La puerta de emergencia. Al final del pasillo."
    "El aire frío se filtraba por los bordes oxidados del marco."

    investigador "{cps=20}Casi... ya casi...{/cps}"

    "Sus dedos rozaron la manija."
    "Fría. Real."

    play sound door_open
    "Empujó una puerta metálica. No cedió."
    
    stop music
    stop sound
    play sound door_slam
    with vpunch

    "La puerta se cerró de golpe."
    "Nadie la tocó."

    "El hombre retrocedió un paso, tropezando con sus propios pies."

    scene pasillo_abandonado at oscuro with fade
    pause 0.7

    play sound "sfx/claw_drag_concrete.mp3"
    "Un chirrido lento. Deliberado."
    "Cada vez más cerca."

    investigador "{cps=15}¿Q-quién anda ahí?{/cps}"

    show galaxia shadow_eyes at center with dissolve

    "Dos puntos de luz en la oscuridad."
    "Y, debajo de ellos, algo que podría haber sido una sonrisa."

    play sound glx_laugh
    "Una risa. Aguda. Casi infantil."

    "{color=#390169}{font=fonts/HelpMe.ttf}{cps=20}Shhh... No hace falta gritar todavía~{/cps}{/font}{/color}"

    investigador "P-por favor... yo solo... yo solo hacía mi trabajo—"

    "{color=#390169}{font=fonts/HelpMe.ttf}{cps=20}Todos dicen eso.{/cps}{/font}{/color}"

    play music curse fadein 0.5
    pause 0.4

    "{color=#390169}{font=fonts/HelpMe.ttf}{cps=15}Pero no te preocupes... Yo también estoy haciendo el mío~{/cps}{/font}{/color}"

    stop ambient
    play sound thud
    with hpunch
    "Algo lo levantó del suelo con una facilidad que no debería ser posible."

    play sound slash
    scene black with flashred

    play sound "sfx/flesh_bubble.mp3"
    play sound "sfx/bone_crack.mp3"
    investigador "¡AAAAAHHH!"

    "El sonido se cortó de golpe."
    "Después, solo el eco de algo siendo arrastrado hacia la oscuridad."

    scene black with flash
    pause 1.0

    # Pantalla de título — no interactiva, avanza sola tras 3 segundos
    show screen title_card with fade
    pause 3.0
    hide screen title_card with fade
    scene black with fade
    stop music fadeout 2.0
    pause 1.0

    jump cap_1

################
#    ACTO 1
################
label cap_1:

    scene bosque_tarde with fade
    play music forest fadein 2

    "Una fría tarde de otoño, el grupo de amigos se encontraba caminando en medio del bosque, kilómetros más allá de la autopista."
    "Los árboles a su alrededor danzaban al suave ritmo del viento. A medida que se abrían paso a través del sendero, la conversación inevitablemente retornó al motivo de aquella junta."

    # Nagi lideraba la marcha, golpeando los troncos con su bate de béisbol
    show nagi neutral at center with dissolve
    "El viento otoñal cortaba como navaja, pero a Nagi no parecía importarle."
    "Caminaba marcando el paso, golpeando los troncos con su bate de béisbol."

    show azura smile at right with dissolve
    "Azura aceleró para alcanzarlo. Sonreía, pero la sonrisa no le llegaba a los ojos."
    a "Oigan... ¿y si mejor lo dejamos para otro día?"
    a "Es que dicen que este lugar no era solo un orfanato. Y no sé, me da mala espina."

    show cutipye neutral at left with dissolve
    "Desde atrás, Cutipye soltó una risa corta."
    c "Oh, genial. ¿Fantasmas huérfanos? ¿Un sótano con experimentos y todo?"
    c "Nagi, elegiste el mejor plan para un viernes. Yo pedí algo emocionante, no un documental de crímenes."

    show nagi smile at center
    n "Tonterías, Zu-chan. Son puros cuentos para asustar a los niños de secundaria."
    n "Es solo un edificio abandonado. Lo peor que vamos a encontrar son goteras y ratas."
    n "Y tú, Cuty, pediste emoción. Yo solo la conseguí."

    "Sin esperar respuesta, Nagi retomó la marcha a grandes zancadas. Azura lo siguió unos pasos atrás, mirando por encima del hombro cada tanto, como si el bosque pudiera contestarle."

    hide nagi
    hide azura
    show cutipye at right
    with moveoutright
    show rodrigo neutral at centro_izquierda with moveinleft

    "[nombre_jugador!c] había caminado hasta entonces al final del grupo, sin abrir la boca, con la mano rozando instintivamente la daga oculta en su cinturón."
    r "¿Están seguros de que quieren hacer esto?"
    r "Y no lo digo por los fantasmas. Hay formas menos estúpidas de ser buscados por la policía..."

    show cutipye smile with dissolve
    c "Vamos, [apodo_jugador], no seas tan agüafiestas. Nadie vigila un edificio que lleva años abandonado."
    c "Además, solo está a unos diez minutos de aquí."

    menu:
        "Respondes con sarcasmo":
            $ afinidad_cutipye += 1
            show rodrigo molesto with dissolve
            r "Tch, estoy seguro de que solo encontraremos insectos y poco más..."
            r "Solo es un orfanato abandonado. ¿Qué es tan especial sobre este lugar?"
            
            show azura smile at centro_derecha with dissolve
            a "No es solamente un orfanato abandonado, [apodo_jugador]."

        "Aceptas de mala gana":
            $ afinidad_cutipye += 2
            show rodrigo molesto with dissolve
            r "Está bien... Pero si nos arrestan, no pienso correr."
            
            show azura smile at centro_derecha with dissolve
            a "No creo que debas preocuparte por eso, el lugar fue desalojado hace mucho tiempo."
            a "Es más."

        "No dices nada":
            show rodrigo molesto with dissolve
            "[nombre_jugador!c] simplemente suspira, resignado."
            pause 1
            show azura smile at centro_derecha with dissolve
            a "Si sirve de algo..."
    
    a "Hay rumores de que en la época de la dictadura fue usado como centro de tortura."

    menu:
        "Te burlas del rumor":
            $ afinidad_azura -= 1
            show rodrigo neutral with dissolve
            r "Vaya giro de guión. Qué conveniente."
            r "¿También hay una niña de pelo largo que aparece en los espejos o eso viene en el DLC de pago?"

        "Te muestras incómodo":
            $ afinidad_azura += 1
            $ estado_mental += 1
            show rodrigo incomodo with dissolve
            r "...Ok, eso sí fue un poco más turbio de lo que esperaba."

        "Guardas silencio":
            show rodrigo neutral with dissolve
            "[nombre_jugador!c] se limitó a fruncir el ceño sin responder, su mueca una clara muestra de desapruebo."

    show azura at centro_derecha with moveinright
    show nagi smug with dissolve
    
    n "¿Acaso vas a acobardarte ahora que todos estamos de acuerdo?"

    show luz smile at left
    show rodrigo at centro_izquierda
    with moveinleft
    "Antes de que [nombre_jugador!c] pudiera responder, la suave y cálida mano de la pelirroja rodeó la suya con gentileza..."
    "Su celeste mirada acompañada por una leve sonrisa, aquella mueca siendo suficiente para calmar el impulso del castaño."

    show rodrigo neutral with dissolve
    r "Y, en todo caso, ¿cómo tienen pensado entrar?"

    hide rodrigo
    hide luz
    hide nagi
    hide azura
    hide cutipye
    with dissolve
    "Como respuesta, Nagi simplemente extendió su sonrisa y se adelantó unos cuantos pasos..."

    scene orfanato_exterior at center with fade
    play sound walk
    "Al cabo de unos diez minutos, el grupo fue capaz de entrar al orfanato a través de una brecha en la enorme cerca de acero."
    
    scene orfanato_exterior2 with fade
    show rodrigo neutral with moveinleft
    stop sound
    r "Bien, llegamos... Entonces tomamos unas cuantas fotos y nos vamos."

    show nagi smile at right with moveinleft
    n "No creas que te escaparás tan fácil, cobarde."
    "Acto seguido, Nagi se quitó la mochila para sujetar su apenas escondido bate de béisbol."
    
    show nagi smug with dissolve
    n  "De aquí no te irás sin acompañarnos."
    n "Y nos quedaremos un buen rato."
    
    hide rodrigo
    hide nagi
    pause 1

    play sound break_glass
    scene orfanato_exterior2 at shake
    "Nagi alzó su bate y lo estrelló contra una ventanilla, destrozando el vidrio antes de bajar."

    stop music fadeout 1.0
    play sound "sfx/land.mp3"
    queue sound "sfx/land.mp3"
    queue sound "sfx/land.mp3"
    queue sound "sfx/land.mp3"
    
    scene lavanderia_abandonada with fade
    "Uno a uno, saltaron al interior. El sonido de sus botas contra las baldosas resquebrajadas resonó con un eco seco y hueco."
    
    "Una vez bajaron todos, [nombre_jugador!c] se mantuvo de pie cerca de la ventana rota, observando cómo sus amigos encendían sus linternas e iluminaban lo que parecía ser una vieja lavandería industrial."

    pause 0.8
    show rodrigo molesto at left with dissolve
    r "Tch, hasta acá llega el olor a muerto... Qué lugar tan encantador."

    show cutipye annoyed at right with dissolve
    c "Ugh, dímelo a mí. Mis botas nuevas acaban de pisar algo viscoso y prefiero no saber qué es."
    "Cutipye alzó su teléfono, moviéndolo en el aire con frustración mientras la pantalla le iluminaba el rostro con un brillo pálido."
    c "Y para colmo, apenas tengo una raya de señal. Así no puedo subir historias."

    show nagi smug at center with moveinbottom
    n "Relájate, princesa. No vinimos a actualizar tu perfil, vinimos a ver si los rumores son ciertos."
    "Nagi dio un par de golpecitos con el bate sobre su propio hombro, mirando las dos salidas que daban hacia el interior del edificio."
    n "Este lugar es enorme. Si caminamos los cinco pegados como patitos, solo vamos a ver un par de pasillos vacíos antes de que anochezca."

    show rodrigo serio at left
    r "¿Estás sugiriendo que nos separemos? ¿En serio, Nagi? ¿No has visto ni una sola película de terror en tu vida?"

    show nagi annoyed at center
    n "Ay, por favor, ermitaño. Lo único que nos va a atacar aquí es el moho o un mapache con rabia."
    show nagi smile at center
    n "Si nos dividimos por zonas, cubrimos la planta baja en quince minutos, tomamos las fotos que tanto quieres para largarte rápido y nos vamos."

    hide cutipye with dissolve
    show azura worried at right with dissolve
    a "No me hace mucha gracia la idea de separarnos... El edificio se ve muy deteriorado, alguien podría pisar mal y lastimarse."

    show luz neutral at centro_derecha with dissolve
    l "Azura tiene razón, pero Nagi también tiene un punto. Si lo hacemos rápido, no tenemos por qué alejarnos demasiado."
    show luz smile at centro_derecha
    l "Podemos revisar las salas contiguas y volver a esta lavandería en diez minutos exactos. Si alguien no regresa o escucha algo raro, nos llamamos a gritos."

    show nagi smug at center
    n "Exacto. Yo iré a buscar las escaleras al segundo piso o la oficina del director, ahí siempre dejan las cosas interesantes."

    hide azura with dissolve
    show cutipye neutral at right with dissolve
    c "Yo iré por el pasillo del fondo a ver si cerca del patio interior agarro algo de señal... Y de paso busco algún rincón con buena estética para un par de fotos."

    show rodrigo neutral at left
    r "Haz lo que quieras, pero no te quedes pegada a la pantalla. Mira por dónde pisas."

    show cutipye smile at right
    c "Sí, sí, gracias por el consejo, papá."
    hide cutipye with moveoutright

    show nagi smile at center
    n "No te mueras de miedo, [nombre_jugador!c]. Nos vemos en diez."
    hide nagi with moveoutleft

    hide luz with dissolve
    show azura neutral at right with dissolve
    a "Yo me quedaré cerca del vestíbulo principal para asegurarme de que tengamos otra salida despejada además de esa ventana alta."
    hide azura with moveoutleft

    show luz smile at center with moveinright
    l "Bueno, parece que quedamos tú y yo para revisar esta ala."

    show rodrigo soft at left
    r "Mejor así. Al menos sé que tú no vas a romper otra ventana con un bate."

    "Ambos intercambiaron una breve mirada cómplice antes de encender sus linternas y adentrarse en el corredor más cercano, aunque a los pocos metros decidieron revisar puertas en lados opuestos del mismo pasillo para terminar antes."

    hide rodrigo with dissolve
    hide luz with dissolve
    
    scene pasillo_abandonado with wipeleft
    "Mientras tanto, a unos pasillos de distancia..."

    show cutipye neutral at centro_derecha with dissolve
    c "Nagi es un idiota... Ni siquiera hay buena señal aquí para subir nada."
    "Cutipye ajustó las correas de su mochila, iluminando un suelo atestado de escombros, cristales rotos, y un polvo denso que bailaba en la luz."
    "De pronto, un sonido la hizo detenerse en seco."

    play sound nailtap
    "No eran los pasos de Nagi. Era un repiqueteo seco."
    "Garras. Arañando el linóleo."
    show cutipye worried
    c "¿Azura? ¿Eres tú intentando asustarme?"

    play sound "sfx/claw_drag_concrete.mp3"
    "El sonido no venía de atrás. El eco rebotaba de una forma extraña... {cps=20}Venía desde arriba.{/cps}"

    show cutipye scared at centro_derecha, vjump
    "Cutipye alzó la linterna con pulso tembloroso hacia el techo."

    #play sound larvcry volume 0.7
    "Un enorme bulto desgarbado se desprendió de las sombras y se alzó frente a ella de forma lenta."

    #agregar scene de Cutipye iluminando asustada.
    #AÑADIR IMÁGEN DE CUTIPYE ILUMINANDO HACIA LA PANTALLA
    scene rat_shadow with dissolve
    pause 0.7
    play music shock noloop
    "La luz temblorosa iluminó una aberración: Un torso de piel estirada al límite, espinazos expuestos rompiendo la carne y extremidades demasiados largas para su cuerpo."
    "Pero lo peor eran sus ojos. Dos orbes que la miraban fijamente, brillando en la oscuridad como rubíes podridos."
    c "¡D-Dios mío!"
    "La criatura se abalanzó con un chillido ensordecedor."

    scene rat_slash
    play sound slash
    with shake
    "Cutipye giró bruscamente por puro instinto, pero una garra rasgó el costado de su brazo y se enganchó profundamente en las correas de su mochila."
    "El dolor fue agudo. Ardiente."

    play sound objfall
    "Con un tirón desesperado impulsado por la adrenalina, Cutipye consiguió zafarse."
    "La mochila cayó pesadamente al suelo, salpicada con las primeras gotas de su propia sangre."

    play sound run
    c "¡NAGI! ¡AYUDA!"

    hide cutipye with moveoutleft
    "Corrió ciegamente, perdiéndose en la negrura del pasillo mientras la criatura se distraía un segundo vital desgarrando la tela ensangrentada de la mochila."

    stop sound fadeout 1.5
    scene pasillo_oscuro with dissolve
    "[nombre_jugador!c], ajeno al grito que se había ahogado al otro lado del edificio, se adentró en una de las habitaciones en el pasillo..."

    scene bg_dolls with dissolve
    play sound walk
    "El suelo crujía bajo sus zapatillas con cada paso cauteloso."
    "Al enfocar su linterna en una esquina cubierta de moho, encontró un montón de muñecas antiguas y deshechas."
    "A pesar de parecer un simple montón de basura olvidada, algo no cuadraba. Faltaban piezas. Estaban... desmembradas metódicamente."
    r "¿...?"

    scene pasillo_exploration1 with dissolve
    play music melody
    play sound "pasos_susurro.ogg"
    "[nombre_jugador!c] comenzó a notar un sonido leve y sutil, como pasos pequeños..."
    r "Chicas, esto no es gracioso..."

    pause(1.5)
    scene pasillo_exploration2 with dissolve
    r "¿Chicas?"
    pause(1.5)
    
    "Al no recibir respuesta, [nombre_jugador!c] decidió dar marcha atrás, esta vez enfocado en encontrar a alguna de sus amigas, quien sea."
    
    scene pasillo_exploration3 with dissolve
    play sound run
    "Puerta tras puerta, [nombre_jugador!c] buscó a sus amigas. Mientras más merodeaba, menos opciones tenía."
    
    "Su una vez lento y cuidadoso caminar se volvió un ligero trote."
    
    scene pasillo_exploration4 with dissolve
    stop sound fadeout 1.5
    "Las opciones se acababan en aquel primer pasillo, hasta que el castaño trató de abrir un de las puertas."
    "Pero antes de poder intentarlo nuevamente..."

    stop music
    play sound scream1
    scene pasillo_exploration4 with vpunch
    pause 1
    r "¿¡Luz!?"

    "Acto seguido, [nombre_jugador!c] esprintó hacia la puerta, la cual debido a lo oxidada que estaba, no cooperaba con su frágil corazón."
    play sound door_slam
    with vpunch
    "Golpeó una vez."
    play sound door_slam
    with vpunch
    "Dos veces."
    play sound door_break volume 0.8
    with hpunch
    scene black
    "Al tercer embate, la cerradura cedió con un chasquido metálico."
    
    scene foreboding_1 with fade
    show luz scared at left
    show rodrigo alert at right with moveinright
    pause 1.3
    
    "Luz estaba pálida, sus pupilas contraídas en dos puntos negros que temblaban al compás de su respiración entrecortada."

    "El castaño, pese al miedo, estaba decidido a ver lo que Luz había encontrado."
    "Se giró hacia la puerta frente a ella, abriéndola lentamente."
    
    play sound door_open
    scene black
    pause(0.5)

    "[nombre_jugador!c] cruzó el umbral y la oscuridad lo recibió como una mano sobre la cara."
    "El aire era espeso. Dulce y podrido a la vez, con una humedad que se le pegaba a la garganta."
    "Y bajo eso, un zumbido constante, en algún punto frente a él."

    l "[apodo_jugador]... espera."
    "Luz habló pegada a su espalda, en un susurro que apenas se sostenía."
    l "Algo se movió ahí dentro. Solo un segundo, pero... se movió."
    r "Por eso entro yo primero."
    l "...No me voy a quedar sola en el pasillo."
    r "Lo sé. Entonces no te sueltes."

    "Los dedos de Luz se cerraron sobre la tela de su polo."
    "Con la mano libre, [nombre_jugador!c] recorrió la pared a ciegas, lento y torpe, buscando el interruptor. Yeso frío. Un clavo oxidado. Algo pegajoso que decidió no identificar."
    "Por fin, sus dedos dieron con un botón de plástico. Lo presionó."
    "Una bombilla amarillenta parpadeó, dudó... y se encendió."
    "Y lo que vio lo dejó paralizado."

    window hide
    play music shock noloop
    scene habitacion_cadaver with flash
    play sound flies
    pause 0.5
    window show
    $ renpy.save("1-1", "Encuentro 1")
    pause 1.5

    r "Qué ca..."

    play audio "goteo_lento.ogg"
    pause 0.1
    "Antes de poder terminar la frase, una gota espesa y tibia cayó sobre su mejilla. No era agua."
    "La mano de Luz se cerró sobre su brazo con una fuerza que dolió."
    "Acto seguido, subieron la vista."

    scene scene_spdr with dissolve
    pause 0.7
    play music chase fadein 0.5

    "En el techo, desafiando la gravedad, algo que alguna vez fue humano los observaba."
    "No se movía. Ni siquiera parecía respirar. Solo una cabeza ladeada de más y unos dedos largos clavados en el yeso, como si el techo fuera el suelo y ellos los que estaban cabeza abajo."

    l "[apodo_jugador]..."
    "Su voz era apenas un hilo."
    r "No te muevas."

    "[nombre_jugador!c] dio un paso atrás, manteniendo su daga en alto."
    "Pero la criatura ya no los miraba a los dos. Giró la cabeza, despacio, con un chasquido seco, como el de una rama al romperse."
    "Y se detuvo en Luz."

    play sound nailtap
    "Las uñas rasparon el yeso. Una mano. Luego la otra."
    "Descendía por la pared, centímetro a centímetro, hacia la puerta. Hacia ella."

    r "(No. A ella no.)"

    "No había tiempo para pensar. Tenía, con suerte, un segundo para decidir."

    menu:
        "Te interpones entre Luz y la criatura":
            $ estado_mental += 2
            "El miedo no desapareció. Solo se volvió estrecho, como si el mundo se redujera a un túnel con dos puntos al fondo: la criatura y Luz."
            "[nombre_jugador!c] se movió antes de decidirlo. Un paso al frente, luego otro, hasta quedar entre la pared y ella, con la daga en alto y el cuerpo tapándola."

            r "Ni se te ocurra."
            "Salió más firme de lo que esperaba. La daga, en cambio, temblaba."
            r "¡Atrás!"

            l "¡[apodo_jugador], no! ¡No sabemos qué es!"

            "La criatura se detuvo, con la cabeza ladeada, como si lo estudiara."
            "Luego sus dedos se soltaron del yeso, uno por uno, y una lluvia fina de polvo cayó sobre los hombros de [nombre_jugador!c]."
            "Luz le agarró el brazo con las dos manos, tirando de él hacia la puerta."

            l "Esto no es una pelea... ¡Por favor, vámonos!"

            "Pero la puerta estaba a cinco pasos, y las rodillas de Luz apenas la sostenían."
            "Cinco pasos que ella no podría dar a esa velocidad. Cinco pasos que la criatura cruzaría en un parpadeo."

            menu:
                "Sacas a Luz de ahí":
                    "El tirón de Luz lo sacó del túnel. No podía ganar esto. Y si caía, ella se quedaba sola con esa cosa."
                    r "Está bien... Está bien. ¡Vámonos!"
                    "Retrocedió empujándola delante de sí, sin bajar la daga, hasta que el umbral quedó a su espalda."
                    jump escapar_araña

                "Te quedas para darle tiempo":
                    "Lo vio con una claridad tan nítida que casi fue calma: si corrían juntos, la criatura los alcanzaría en el pasillo. Si él la retenía, aunque fuera un segundo, Luz tendría una oportunidad."
                    r "Luz. Tienes que soltarme."
                    l "No. No, no, no..."
                    r "Cuando te diga, corres. No mires atrás."
                    l "¡No voy a dejarte!"
                    r "No me dejas. Yo te alcanzo."
                    "Mintió. Y ella lo supo."
                    r "¡Vete! ¡Yo te doy tiempo!"
                    "[nombre_jugador!c] arremetió contra la criatura con todas sus fuerzas."
                    jump game_over_spdr

        "Retrocedes con Luz, sin darle la espalda":
            $ estado_mental += 1
            r "Despacio... Esto no vale la pena. Ven."
            "[nombre_jugador!c] mantuvo la daga en alto, pero no atacó. Tomó a Luz del brazo y dio un paso atrás. Luego otro."
            "Sin movimientos bruscos. Sin dar la espalda. Como se hace con un perro desconocido."
            "Solo que los perros no cuelgan del techo."
            "Cruzaron el umbral de espaldas. Tres pasos. Cuatro."
            play sound crack
            "Y entonces, sobre sus cabezas, el yeso crujió. La criatura se había soltado."
            jump escapar_araña

        "El pánico te gana: echas a correr":
            $ estado_mental += 3
            "El miedo pudo más. [nombre_jugador!c] giró y corrió sin pensarlo."
            "Su mano encontró la muñeca de Luz a medio giro. No recordaría haberla agarrado."
            "Detrás, algo arañó el yeso. Rápido. Muy rápido."
            jump escapar_araña

label game_over_spdr:
    stop sound
    scene black with fade

    "Pero..."

    play music curse
    scene spdr1 with fade
    play sound slash
    pause(1)
    "La criatura fue más rápida, más fuerte, más letal de lo que [nombre_jugador!c] jamás pudo anticipar."
    "Ganó un segundo. Quizá dos. Para él no fueron suficientes."
    "Su acto de valentía solo resultó en una muerte sin gloria."
    pause(1)
    "{cps=15}[nombre_jugador!c] murió como un idiota...{/cps}"
    pause(1.5)
    "{cps=15}...pero se puso delante.{/cps}"

    pause(2)

    scene gameover_screen with dissolve
    pause(2)
    menu:
        "Cargar partida":
            jump load_screen
        "Volver al menú principal":
            return

label escapar_araña:
    r "¡Corre!"
    stop sound
    play sound run loop

    scene pasillo_corriendo
    scene pasillo_corriendo at truecenter with None
    scene pasillo_corriendo at truecenter:
        linear 0.1 xalign 0.02
        linear 0.1 xalign -0.02
        repeat
    "[nombre_jugador!c] y Luz corrieron por los pasillos sin mirar atrás."
    "El pasillo se convertía en un túnel borroso mientras sus pulmones ardían."
    "Detrás, ningún paso los seguía. Y por alguna razón, eso era peor."

    scene escape_1
    show rodrigo scared at right:
        linear 0.5 xalign 0.4
        linear 0.5 xalign 0.3
        repeat

    show luz scared at left:
        linear 0.5 xalign 0.6
        linear 0.5 xalign 0.7
        repeat

    l "¿¡Qué era eso!? ¡[apodo_jugador], qué era eso!"
    r "¡No lo sé, y no pienso preguntárselo!"
    r "¿¡Dónde están los demás!?"

    l "¡No lo sé! ¡Nos separamos y los perdí de vista!"

    pause 1.0
    stop music fadeout 2.0

    "[nombre_jugador!c] y Luz siguieron corriendo durante un rato, hasta que finalmente encontraron un lugar que parecía ser seguro."

    scene sala_espera_abandonada with dissolve
    show luz scared at left
    show rodrigo nervioso at centro_derecha
    with moveinright
    play music "ambiente_tenso.ogg" fadein 2.0
    stop sound fadeout 1.5

    "Una sala de espera. Sillas de madera alineadas contra una pared, una mesa baja con revistas hinchadas por la humedad y un reloj detenido en una hora que nadie recordaba."
    "[nombre_jugador!c] cerró la puerta tras ellos y se quedó apoyado contra ella, escuchando."
    "Nada. Solo su pulso en los oídos, y la daga, que seguía en su mano sin que él hubiera decidido sostenerla."

    "Luz resbaló por la pared hasta quedar sentada en el suelo, con las rodillas contra el pecho. Las manos no dejaban de temblarle."

    r "Oh mierda, oh mierda, oh mierda..."
    r "Sabía que era una pésima idea..."

    l "Me miró a mí. ¿Lo viste? Me miró a mí."
    r "Lo vi."
    l "Y si hay más... Azura, Nagi, Cuty... Si esa cosa los encontró a ellos..."
    "No terminó la frase. No hacía falta."

    show rodrigo serio
    "[nombre_jugador!c] sentía dos tirones a la vez, y ninguno era un capricho."
    "Uno lo empujaba hacia ella. Luz se estaba deshaciendo a un metro de él, y él sabía bien lo que era hundirse, y lo que cambiaba que alguien se quedara al lado."
    "El otro lo empujaba hacia la puerta. Cada minuto en esa sala era un minuto que los demás pasaban solos con lo que fuera que habitara ese lugar. Y las manos le temblaban a él también: mientras no se detuviera, no tendría que notarlo."

    menu:
        "Sentarte con ella un momento":
            $ afinidad_luz += 2
            show rodrigo soft
            "Se despegó de la puerta. Si no recuperaban el aliento, no llegarían lejos, y los dos lo sabían."
            show rodrigo at center with move
            "[nombre_jugador!c] se sentó junto a ella en el suelo, hombro con hombro, con el filo de la daga lejos de ambos."

            r "Hey... vamos a salir de esta, cariño."
            pause 1
            l "¿Me lo prometes...?"
            r "Con mi vida..."

            "Luz no respondió al principio. Pero su respiración se fue volviendo más lenta, y sus dedos terminaron enredados en la manga de él."

            r "Un minuto. Respiramos un minuto y salimos a buscarlos."
            l "Un minuto."

            "Por un momento, el silencio dejó de ser tan pesado."
            "Pero [nombre_jugador!c] no dejó de pensar en los demás ni un segundo. Ese minuto era un préstamo, y alguien más lo estaba pagando."

        "Revisar la sala y buscar por dónde seguir":
            $ estado_mental -= 1
            r "Tenemos que movernos... Debe haber una salida."
            "No lo dijo como una orden. Lo dijo bajo, casi para sí mismo."
            l "...¿Ahora?"
            r "Si me quedo quieto, no sé si voy a poder volver a moverme."
            "Era la frase más honesta que había dicho en toda la tarde. Luz lo miró un largo segundo."
            l "Eso último no era solo para mí, ¿verdad?"
            r "Un poco para los dos."

            "Se agachó frente a ella lo justo para quedar a su altura."
            r "Ayúdame. Tú mira esa pared, yo reviso el fondo. Cinco minutos, y dejamos de ser dos que se esconden para ser dos que buscan."

            "Luz tardó un segundo. Luego se aferró a su mano y se incorporó, despacio, apoyándose en la pared."
            "Seguía temblando, pero ahora sus manos tenían algo que hacer. A veces era lo único que hacía falta."

            "Revisaron la sala en silencio. Una segunda puerta, condenada con tablones. Una ventana tapiada con chapa. Tras el mostrador, papeles amarillos y un cajón vacío."
            "Nada que sirviera. Pero al menos sabían que no había nada más allí con ellos."

    "El silencio volvió a asentarse en la sala, interrumpido únicamente por la respiración de ambos."
    pause(1.0)
    "El tiempo parecía haberse detenido..."

    pause(0.5)
    play sound wood_creak volume 0.7
    show rodrigo serio at vjump
    show luz worry at vjump
    pause(0.5)
    "Hasta que un leve crujido de madera, proveniente del techo, los obligó a intercambiar miradas."

    r "No puede ser... ¿Otra vez?"
    l "[apodo_jugador]... Tenemos que buscar a los demás."

    "[nombre_jugador!c] asintió. Luz le buscó la mano sin mirarla y él se la dejó tomar; ninguno de los dos habría sabido decir quién la buscó primero."
    "Y aunque aún no sabían cómo salir, sabían que no podían quedarse quietos."

    scene pasillo_abandonado with dissolve
    play sound walk
    "Comenzaron a explorar nuevamente los pasillos, esta vez avanzando más despacio."
    "En su camino, encontraron algunas puertas cerradas y otras que solo daban a oficinas vacías o salas comunes en ruinas."

    stop sound fadeout 0.7
    show obj-bag at truecenter
    with dissolve

    "Pero entonces, una linterna tirada en el suelo, junto con una mochila abierta, captó su atención."

    pause 0.7

    hide obj-bag
    show rodrigo sorprendido
    with dissolve

    "[nombre_jugador!c] se acercó con rapidez, reconociendo los pines personalizados en la tela negra."

    r "...Es de Cutipye."

    "Al revisar el contenido, encontró una botella de agua rota, el cuaderno de dibujos de su amiga... y algunas manchas oscuras en el suelo, que se extendían hacia el interior de una puerta semiabierta."

    l "¿Sangre?"

    "Ambos tragaron saliva."

    show rodrigo alert
    play sound "daga_desenvainada.ogg"

    "El castaño alzó su daga, empujando lentamente la puerta..."

    play sound door_open
    pause 0.8
    scene puerta_abierta_sotano with dissolve

    "Pero no había cuerpo. Solo huellas de pisadas, algunas arrastradas, otras firmes..."

    "Todas llevaban escaleras abajo, a lo que parecía ser el sótano del orfanato."

    call chapter_complete("Capítulo 1")
    jump cap_2

label cap_2:

    # ============================================================
    # CAPÍTULO 2: EL SACRIFICIO Y EL MONSTRUO ENTRE LAS SOMBRAS
    # ============================================================

    scene puerta_abierta_sotano with fade
    play music ambiental fadein 1.0

    "[nombre_jugador!c] y Luz bajaron por unos escalones de concreto que crujían bajo su peso."
    "El frío del sótano no era solo temperatura... era abandono."

    scene pasillo_lab with wipeleft

    "Llegaron a un pasillo revestido de azulejos blancos manchados. Había puertas metálicas pesadas con números borrosos."

    show rodrigo alert at left
    show luz worry at right
    with dissolve

    l "[nombre_jugador!c]... esto no es un sótano normal. Parece un laboratorio."
    "Mientras se abrían paso, las miradas de ambos recorrían las paredes, los cables colgantes, las manchas oscuras sobre el azulejo."

    show rodrigo at centro_izquierda
    show luz worry at centro_derecha
    with moveinleft

    "A medida que avanzaban, lentamente se apegaban el uno al otro sin decir una sola palabra."

    show rodrigo incomodo with dissolve
    r "Jamás pensé que terminaríamos perdidos en un lugar así..."
    show luz smile with dissolve
    l "Siendo honesta... Si me hubieran dicho que terminaría en una casita de terror con el callado del salón... Tampoco me lo hubiera creído."
    $ afinidad_luz += 1

    # -- Descubrimiento de la bitácora --
    "Entraron a la sala contigua."

    scene lab1 with dissolve
    "Sobre un escritorio metálico, una caja fuerte abierta revelaba un cuaderno polvoriento."

    scene lab2 with dissolve
    play sound paper_flip
    play music story
    "[nombre_jugador!c] lo abrió. El encabezado era claro:"

    """
    {cps=20}{b}Bitácora del proyecto H-127: SUJETOS HUÉSPEDES{/b}{/cps}\n

    {cps=20}Director: Dr. Édgar L. Montané{/cps}\n

    {cps=20}Ubicación: Centro de Investigación Subterráneo del Orfanato "Luz y Esperanza"{/cps}\n
    """

    play sound paper_flip

    """
    {cps=20}{b}Entrada 01 – Día 0{/b}{/cps}
    \n
    {cps=20}Los niños refugiados, sin lazos familiares, han sido seleccionados para la integración del Patógeno H-127.
    Sus historiales clínicos los hacen... prescindibles{/cps}.
    """

    play sound paper_flip

    """
    {cps=20}{b}Objetivo:{/b} Inducir una simbiosis controlada.
    Los resultados preliminares son...{/cps}
    \n\n
    {cps=10}{color=#f00}...{b}esperanzadores.{/b}{/color}{/cps}
    """

    hide text
    scene lab3 with dissolve
    pause (2)

    r "Estaban usando a los huérfanos... los llamaban 'sujetos prescindibles'."

    pause (1)

    l "Entonces..."
    l "Esa cosa que vimos... ¿Era uno de ellos?"
    scene lab4
    play sound door_slam
    with hpunch
    "[nombre_jugador!c] cerró el cuaderno de golpe, con los nudillos blancos por la ira."

    stop music fadeout 3
    "Antes de que pudieran procesar el horror del descubrimiento, un quejido ahogado provino del fondo de la sala."

    scene sala_h127_1
    play ambient flies volume 0.3 loop
    show rodrigo linterna at centro_izquierda
    show luz neutral at centro_derecha
    with dissolve

    "Nadie habló durante un largo rato."
    "Lo que acaban de ver no se dejaba procesar. Era demasiado ordenado para ser un accidente. Demasiado deliberado."

    "[nombre_jugador!c] movió la linterna despacio, casi sin querer, y la sala fue apareciendo por pedazos."
    "Azulejos blancos vueltos amarillos, con grietas que subían como venas. Camillas metálicas con correas de cuero resecas, abiertas, esperando. Un desagüe en el centro del suelo y, alrededor, un círculo oscuro que ninguna fregona había logrado borrar."
    "Arriba, un tubo fluorescente colgaba de una cadena, zumbando con un hilo de luz enferma que se encendía y se apagaba sin ritmo."

    "El olor ya lo habían notado desde la puerta. Agrio. Metálico. Animal."
    "Dentro era peor: tenía un fondo dulzón de formol y de algo más viejo que el formol."
    "Y bajo todo eso, un goteo. Una gota. Un silencio largo. Otra gota. Como alguien contando."

    show luz worry with dissolve
    l "No quiero saber para qué eran las correas."
    r "Entonces no las mires."

    "Lo dijo seco, sin darle peso. Era lo único que le quedaba para sostener el momento."

    "El haz de la linterna bajó al suelo y se detuvo."
    "Un rastro. Ancho, arrastrado, como una mano enorme pasada de lado a lado sobre el linóleo. Partía de las sombras del fondo y terminaba tras unos archivadores volcados."
    "Aún brillaba."

    r "Esto es reciente."

    "Siguiendo el rastro, la luz rozó la pared del fondo."
    "A dos metros del suelo había una rejilla de ventilación. Le faltaba un tornillo. Del hueco caía polvo en hilos finos, muy despacio, como si algo, allá arriba, acabara de cambiar de postura."

    "[nombre_jugador!c] la miró un segundo. Lo registró sin entenderlo."
    "Y el haz siguió su camino."

    # -- El hombre herido --
    pause 1
    "Entonces lo oyeron."
    "Un quejido húmedo, ahogado, desde detrás de los archivadores."
    "Humano. Demasiado humano."

    show rodrigo alert at vjump
    "La mano de Luz buscó su manga y se aferró a ella. [nombre_jugador!c] apretó la daga."
    r "Quedate detrás de mí."

    "Rodeó los archivadores con el arma por delante y la luz por detrás, paso a paso, escuchando como sus propias suelas pegaban en el suelo."

    show sujeto_herido at right with dissolve

    "Un hombre estaba sentado contra el metal, con las piernas estiradas, como un muñeco al que le hubieran cortado los hilos."
    "Chaqueta de montaña rasgada de hombro a costilla. Botas con barro seco que no era de ahí. En la mano derecha, una linterna apagada, aferrada con tanta fuerza que los nudillos parecían de cera."
    "No era de los de la bata. No era uno de los niños. Era alguien que había entrado por su propio pie."
    "Igual que ellos."
    "Y respiraba."
    l "¡Dios mío! ¡Señor, aguante!"

    show luz surprised at centro_derecha with moveinleft
    show rodrigo at vjump
    r "Luz, espera... ¡Luz!"
    r "Mira el rastro. Algo lo arrastró hasta aquí y lo dejó vivo. Eso no es normal."
    l "Entonces me lo explicas después."

    "Luz se arrodilló junto al hombre y le pasó el brazo sobre sus hombros, sin importarle la sangre."
    "Olía a hierro, a sudor frío y a algo dulce debajo. Algo de enfermo."

    sujeto "No... no hagan ruido... ella los escuchará..."
    "Hablaba en un hilo, casi sin mover los labios."
    "Y mientras hablaba, sus ojos, muy abiertos, muy secos, se iban una y otra vez hacia el techo."

    l "Tranquilo. Lo sacaremos de aquí. ¿Quién le hizo esto?"
    sujeto "Ella... Ella no es como los otros... Ella lo disfruta..."

    pause 1
    "La pareja intercambió una mirada, sus corazones acelerándose."

    show luz worry with dissolve
    l "¿Ella...? ¿Te refieres a una de las criaturas?"
    sujeto "Éramos... más. Cuando entramos. Los otros... Ya no..."

    pause (1)
    sujeto "Galaxia... su nombre... es Galaxia..."
    sujeto "No quiere que se vayan... No deja que nadie..."
    pause (1)

    "El hombre tosió sangre. Con la ayuda de Luz logró incorporarse, y pesaba menos de lo que debería, o ellos estaban demasiado asustados para sentir el peso."

    l "[nombre_jugador!c], ayúdame. Aún podemos salvarlo."

    "[nombre_jugador!c] asintió, tomando el otro brazo del hombre. Por un segundo, hubo una falsa sensación de esperanza."
    "Quizás no todo estaba perdido."
    "Quizás podían salir de allí."

    "Caminaron hacia la puerta. Tres pasos. Cuatro. Las suelas arrastrándose, la respiración del hombre sibilante entre ambos."
    "Y entonces la gota dejó de caer."
    
    pause 1.2

    "[nombre_jugador!c] esperó la siguiente. No llegó."
    "Un segundo después el zumbido del tubo fluorescente se apagó, como si alguien le hubiera puesto un dedo encima. La luz siguió, pero ya sin voz."
    "Uno por uno, los ruidos de la sala se fueron retirando."

    pause 1.0
    play sound objfall volume 0.4
    "Algo diminuto y metálico cayó desde lo alto y rodó por el linóleo, tintineando hasta chocar con el desagüe."
    "Un tornillo."

    stop music
    play sound wood_creak
    "Un crujido sobre sus cabezas los congeló."

    sujeto "No... no..."

    "El hombre miró hacia el techo, sus ojos inyectados en terror absoluto. Sus últimas palabras salieron como un rezo ahogado:"
    sujeto "No se puede huir de ella."

    # -- El ataque --
    play sound objfall volume 0.8
    "La rejilla salió despedida del muro y golpeó el suelo con un estruendo de lata."

    play sound "sfx/flesh_bubble.mp3"
    play music chase fadein 0.5
    show luz scared at vjump
    show rodrigo sorprendido at vjump

    "Del hueco cayó una forma encorvada, un contorno más oscuro que el propio ducto, demasiado largo para haber cabido allí dentro, desenrollándose en el aire."
    "No hubo tiempo de reaccionar. Las garras se hundieron en su clavícula, arrancándolo de los brazos de Luz con una fuerza sobrehumana."

    play sound "sfx/bone_crack.mp3"
    play sound slash
    with hpunch
    scene black with flashred

    sujeto "¡AAAAAAAH!"

    $ estado_mental += 2

    "El grito fue silenciado de golpe por un crujido húmedo y el sonido de carne desgarrándose."
    "La sangre salpicó el rostro de [nombre_jugador!c]. Tibia. Espesa. Casi agradable después del frío sepulcral de la sala. Y darse cuenta de eso fue lo peor."

    play sound objfall
    "La linterna de Luz cayó al suelo y rodó sin control. Su haz de luz giró una vuelta completa sobre las paredes manchadas, la rejilla vacía y las correas rotas, hasta detenerse contra un rincón, iluminando la nada."

    "{color=#390169}{font=fonts/HelpMe.ttf}{cps=20}Jueguen mientras puedan...{/cps}{/font}{/color}"

    play sound "sfx/claw_drag_concrete.mp3"
    "Algo pesado se arrastró sobre el linóleo, alejándose hacia la penumbra. Lento. Sin la menor urgencia."
    "La figura se llevó el cuerpo inerte hacia la oscuridad del corredor, perdiéndose entre las sombras con una risa gutural que rebotó en las paredes de concreto."
    play sound glx_laugh

    "Durante un par de segundos, nadie respiró."
    "Luz seguía de rodillas en el suelo, con los brazos todavía a medio alzar, aferrándose al vacío donde hacía un instante estaba aquel hombre."
    "Tenía las manos bañadas en rojo. Las miraba fijamente, temblando, como si pertenecieran a otra persona."

    l "Lo... lo tenía... Yo lo estaba sujetando..."
    l "Prometí que lo sacaríamos..."

    play sound "sfx/distant_scratch.mp3"
    "Un chillido metálico resonó desde el fondo del laboratorio, seguido por el eco de múltiples patas moviéndose entre las tuberías. El olor de la sangre fresca estaba atrayendo a los demás."

    r "¡Luz, mírame! ¡Tenemos que irnos ya!"

    "Ella no reaccionó. Sus pupilas estaban fijas en el charco oscuro que se extendía hasta sus rodillas."

    r "¡¡LUZ, CORRE!!"

    "[nombre_jugador!c] la sujetó con fuerza de las muñecas, obligándola a levantarse de un tirón. El contacto pareció romper el trance; ella inhaló una bocanada de aire ahogada y apretó su mano con desesperación."

    # -- Huida --
    scene pasillo_huida with fade
    play sound run loop

    "Corrieron sin mirar atrás. El pasillo subterráneo parecía estirarse ante ellos como una garganta interminable mientras las luces del techo parpadeaban con violencia."
    "Sus respiraciones entrecortadas se mezclaban con el golpeteo frenético de sus zapatillas contra el suelo húmedo."

    l "¡Por aquí! ¡Las escaleras hacia el ala sur deberían estar cruzando esta puerta!"

    "Doblaron la esquina derrapando contra el muro, buscando la salida, pero el alivio se les congeló en el pecho."

    scene escombros_bloqueo with dissolve
    stop sound
    "¡Bloqueado! Una montaña de vigas colapsadas, camillas oxidadas y bloques de concreto sellaba el paso por completo."

    play sound door_slam
    with shake
    r "¡Mierda! ¡No, no, no!"
    
    "[nombre_jugador!c] empujó una de las placas metálicas con el hombro, pero apenas logró arrancarle un quejido al óxido. Era imposible mover eso a tiempo."
    
    r "¡Está cerrado! ¡Debimos tomar la bifurcación de atrás!"

    play sound nailtap
    "Clic. Clic. Clic."
    "El sonido detuvo sus corazones. No venía de arriba; venía del mismo pasillo por el que acababan de correr. Pesado, rítmico, como cuchillas golpeando el linóleo a toda velocidad."
    "Algo se acercaba hacia ellos. Y ya estaba a la vuelta de la esquina."

    show luz scared at right with dissolve
    l "¡No nos va a dar tiempo a volver juntos, [apodo_jugador]! ¡Nos va a acorralar contra los escombros!"

    show rodrigo alert at left with dissolve
    r "¿¡Qué quieres hacer!? ¡No pienso dejarte sola con esa cosa!"

    l "¡Mira! ¡Hay puertas a ambos lados del corredor!"
    "Luz señaló con urgencia las habitaciones laterales antes de empujarlo del pecho hacia los dormitorios de la izquierda."
    l "¡Si corremos juntos, nos atrapará a los dos! ¡Entra ahí y escóndete, yo buscaré por el ala este para dividir el rastro!"

    r "¡Luz, espera—!"

    l "¡Grita si ves una salida! ¡Te prometo que no me dejaré atrapar!"

    hide luz with moveoutright
    "Antes de que [nombre_jugador!c] pudiera sujetarla de nuevo, ella ya había cruzado hacia el corredor opuesto. El sonido de las garras doblando la esquina le heló la sangre."
    "Separarse era una pésima idea. [nombre_jugador!c] lo sabía con cada fibra de su cuerpo. Pero con la muerte a diez metros de distancia, el pánico decidía por ellos."

    stop music fadeout 2.0
    scene foreboding_2 with fade
    stop sound
    $ renpy.save("1-1", "Encuentro 2")
    show rodrigo nervioso at center with moveinright
    play sound door_close
    play ambient audio.heartbeat fadein 0.8
    "[nombre_jugador!c] entró tropezando en una antigua habitación de literas y cerró la puerta a sus espaldas en el último segundo, conteniendo el aliento para no hacer ruido."
    "Se apoyó de espaldas contra la madera fría. Su pecho subía y bajaba con violencia; el latido en sus oídos y el eco de su propia respiración le parecían demasiado fuertes para un cuarto tan quieto."
    "Estaba solo. O al menos, eso quería creer."

    "Encendió la linterna con manos temblorosas."
    "El haz recorrió filas de literas oxidadas, colchones hundidos y un armario alto con la puerta entornada."
    "No había ventanas. El aire era viejo y seco, con un fondo de metal frío y hierba muerta que no supo ubicar."

    "Sobre una de las camas bajas, la luz encontró un pequeño zapato escolar, gastado en la punta."
    "Solo uno."

    r "Cálmate... Respira... Busca una salida. Avisa a Luz."

    "Dio un paso hacia el armario..."
    "...y la linterna parpadeó."
    "Una vez."
    "Dos."
    "Luego se apagó, y la oscuridad cayó sobre la habitación como una tela gruesa."

    pause 1.5
    "Silencio."
    "No la ausencia de ruido, sino un silencio con forma. El de algo que también contiene el aliento."
    "Su propio pulso le martillaba los oídos."

    play sound wood_creak volume 0.6
    "Afuera, en el pasillo, una tabla cedió bajo un peso."
    pause 1.2
    play sound wood_creak volume 0.6
    "Otra."
    "Lentas. Medidas. No tenían prisa."
    "Pero había algo mal en el ritmo. Demasiados apoyos. Ninguno donde debía estar."

    pause 1.0
    "Los pasos se detuvieron frente a la puerta."
    pause 1.5
    "Del otro lado, algo respiraba."
    "No con pulmones. Era un aliento seco y entrecortado, como el roce de páginas muy viejas pasando una tras otra."
    "El olor a hierba muerta se coló bajo la puerta."

    show rodrigo alert at vjump
    "La manija giró."
    "Despacio. Con una paciencia que no encajaba con nada de lo demás."

    play sound door_open
    "La puerta se abrió sin prisa, arrastrando un quejido largo contra el marco."
    "Nadie entró."
    pause 1.5
    "[nombre_jugador!c] no veía nada. Solo un rectángulo de negro apenas más denso que el negro de la habitación."

    play sound nailtap
    "Clic."
    pause 0.8
    "Clic."
    pause 0.8
    "Clic."
    "Algo duro golpeaba el linóleo. Con ritmo. Como un metrónomo sin música."

    play music chase fadein 1.0
    show rodrigo scared
    "Nunca lo oyó cruzar el umbral."
    "Pero el sonido ya no venía de la puerta."

    play sound "sfx/claw_drag_concrete.mp3" volume 0.5
    "Un chasquido metálico, suave y seco. Después otro. Metal contra metal, como quien afila algo sin prisa."

    "Y bajo eso, un olfateo húmedo y largo. Muy cerca del suelo."
    "Se detuvo junto a las literas del fondo. Junto a la cama del zapato."
    "Un segundo. Dos."
    "Como si algo allí le resultara... familiar."

    "Luego siguió. El roce de algo duro arrastrándose bajo los somieres, centímetro a centímetro."
    "No buscaba a ciegas. Lo estaba rastreando."
    "Y [nombre_jugador!c] no lograba dejar de temblar."
    menu:
        "Te acercas a comprobar":
            jump game_over_mnts_1
        "Te escondes bajo una de las camas":
            jump game_over_mnts_2
        "Te escondes tras el armario":
            jump escape_mnts
    
label escape_mnts:
    "[nombre_jugador!c] apagó la linterna y se pegó a la pared, tras el viejo armario metálico, conteniendo el aliento hasta que le dolieron los pulmones."

    scene foreboding_2 with dissolve
    play sound "sfx/claw_drag_concrete.mp3"
    "Entonces, un chasquido metálico, seguido del raspado de una garra recorriendo la pared..."
    
    play sound door_open fadein 0.3
    "...y el crujido de la puerta abriéndose."
    scene habitacion_mantis with dissolve
    
    centered "{cps=10}La criatura te está buscando.{/cps}"
    
    "La Mantis entró. Sus antenas vibraban, captando el miedo en el aire."
    "Se acercó muy lentamente."
    "Un brazo se alza, una hoja afilada..."
    
    "Una."
    "Dos veces."
    
    "[nombre_jugador!c] sostuvo el aire, cerrando sus ojos y preparándose para lo peor. Un solo movimiento en falso y era hombre muerto."
    
    "La Mantis pasó de largo frente a las camas, ignorando el armario alto."
    pause (2.5)
    stop music fadeout 1.5
    play sound alarm volume 0.2 loop
    stop ambient
    "¡BEEEEEP! ¡BEEEEEP!"
    
    "La criatura giró bruscamente y salió de la habitación, atraída por el nuevo ruido."
    stop sound fadeout 2.0
    play ambient heartbeat fadein 0.8 volume 0.6
    scene foreboding_2
    show rodrigo scared at center
    with dissolve
    
    $ estado_mental += 1
    play sound thud
    "[nombre_jugador!c] cayó al suelo, temblando. Había estado a centímetros."
    show rodrigo nervioso with dissolve
    pause (1)
    "Finalmente respira."
    
    "Sus manos tiritaban."
    
    r "Esa cosa... Me buscaba..."
    r "Sabía lo que hacía..."
    
    "Cuando por fin se incorporó, su espalda crujió y soltó un suspiro contenido."
    "Abrió la puerta de la habitación lentamente, asomandose al pasillo."
    
    stop ambient fadeout 1.5
    scene pasillo_abandonado with fade
    "Vacío."

    show rodrigo neutral at center with dissolve
    
    stop music fadeout 1.5
    "El aire seguía denso, cargado de polvo viejo y una humedad que parecía aferrarse a su ropa como telarañas invisible."
    "A cada paso, sus zapatillas crujían apenas, y su vista barría todo en busca de movimiento."
    pause(1.6)
    "Pero nada..."
    pause (1.3)
    "Solo silencio y la suave vibración de la tensión que aún se negaba a soltar su pecho."
    
    "Dobló por un pasillo corto, pasando junto a un antiguo retrato infantil que colgaba torcido."
    "Avanzó sin rumbo claro, deseando encontrar a Luz, escuchar su voz."
    "Y entonces, como si el orfanato se burlara de sus pensamientos..."

    show luz smile at centro_derecha
    show rodrigo sorprendido at centro_izquierda
    with moveinright
    play music menu
    l "¡[apodo_jugador]!"
    "Él se giró en seco, instintivamente alzando el brazo con el que sostenía su daga, aunque sin intención real de atacar."
    
    l "¡Te estaba buscando! ¡Encontré algo genial!"
    
    "[nombre_jugador!c] apenas pudo contestar, atónito por el contraste."
    
    "Luz estaba limpia. Demasiado limpia. Y esa sonrisa..."
        
    menu:
        "Abrazarla sin pensar":
            $ afinidad_luz += 2
            $ estado_mental -= 1
            "El alivio le ganó al orgullo."
            
            show rodrigo soft at center
            show luz surprised
            with moveinleft
            pause 0.85
            l "¿[apodo_jugador[0]]-[apodo_jugador]?"
            "Antes de poder analizarlo, [nombre_jugador!c] avanzó y la rodeó con los brazos con más fuerza de la que pretendía."
            
            "Su cuerpo estaba tibio. Real. No había rigidez antinatural. No había trampa."
            
            r "Esa cosa estaba cerca..."
            r "Pensé que..."
            
            "No terminó la frase."
            
            "Luz, todavía sorprendida por lo inusualmente físico del gesto —porque [nombre_jugador!c] rara vez iniciaba contacto así—, dudó apenas un segundo antes de corresponder."
            
            show luz smile with dissolve
            l "...Estoy aquí."
            "Sus manos se apoyaron en su espalda, suaves. Firmes."

            pause 0.75
            show luz neutral at right with moveinleft
            
            "Después de unos segundos, fue ella quien se separó primero, mirándolo con una mezcla de ternura y preocupación."
            l "Debió ser horrible."


        "Comprobar si está bien":
            $ afinidad_luz += 1
            $ estado_mental += 1
            show rodrigo neutral at center
            show luz surprised
            with moveinleft

            "[nombre_jugador!c] se acercó sin decir nada."
            "Sus manos se alzaron y sostuvieron el rostro de Luz entre sus dedos, examinando cada rasgo con intensidad."
            
            l "¿Qué haces?"
            
            "Bajó las manos por su cuello, palpando con cuidado, como buscando marcas invisibles."
            
            r "Quédate quieta."
            
            "No había suavidad en su voz. Solo tensión."
            "Sus ojos recorrían su piel en busca de heridas… o algo peor."
            pause 0.5
            "Nada."
            "La piel estaba limpia. Demasiado limpia."
            "Entonces, como si recién recordara lo extraño de su actitud, [nombre_jugador!c] inclinó el rostro y dejó un beso breve en sus labios."
            
            show rodrigo incomodo at centro_izquierda with moveinright

            r "...Solo quería asegurarme."
            
            show luz smile with dissolve
            "Luz parpadeó, confundida, pero sonrió."
            
            l "Podías haber empezado por ahí, paranoico."


        "Cuestionar a Luz":
            $ estado_mental += 2
            $ afinidad_luz += 1
            show rodrigo alert with dissolve
            "[nombre_jugador!c] no se movió."
            
            r "¿Por qué estás tan tranquila?"
            r "Y limpia."
            
            show luz neutral with dissolve
            "La sonrisa de Luz vaciló apenas."
            
            l "¿Eh?"
            r "Hemos visto un fenómeno araña colgar del techo."
            r "No pareces... afectada."
            "Por un momento, el silencio pesó entre ambos."

            show luz smile with dissolve
            "Luego, la expresión de Luz se suavizó."
            
            l "[apodo_jugador]..."
            l "Tuvimos suerte. No nos encontró."
            l "Y si no sonrío, me pongo a temblar."
            
            show luz at center
            show rodrigo sorprendido at vjump
            with moveinright
            "Antes de que él pudiera responder, ella dio un paso al frente y lo abrazó."
            "Esta vez fue ella quien lo sostuvo con fuerza."
            
            l "Estás tenso."
            show rodrigo incomodo with dissolve
            "[nombre_jugador!c] tardó un segundo en corresponder."
            
            r "...Estoy bien."
            
            "Mentía."

            show luz at centro_derecha
            with moveinleft
            "Luz se separó con suavidad, pero su mirada permaneció atenta."
    
    l "Ven, quiero mostrarte esto."
    "Sin esperar respuesta, lo tomó de la mano, apretándola fuerte, arrastrándolo con ella."

    scene pasaje_secreto with dissolve
    pause (0.7)
    
    r "No había visto ese rincón antes..."
    pause(0.4)
    r "¿Estaba oculto?"
    l "Si... Hasta que cayó una tabla y escuché una corriente de aire."
    l "Da al otro lado del ala sur. Puede que haya una salida... O al menos, más espacio."
    "[nombre_jugador!c] asintió, por primera vez en mucho tiempo..."
    "...sintiendo que las cosas van a mejorar."
    r "Vamos."

    call chapter_complete("Capítulo 2")
    jump cap_3

label game_over_mnts_1:
    "[nombre_jugador!c] avanzó con cautela, su linterna apagada, guiado solamente por instinto."
    scene black with fade
    "Pero no había tiempo para dudar. La criatura detectó su pulso acelerado."
    
    play sound "sfx/claw_drag_concrete.mp3"
    "Una figura se abalanzó desde las sombras, dos hojas brillantes descendieron."
    play music curse
    scene death_mnts_1 with fade
    
    "Por un momento, la aterrada mirada de [nombre_jugador!c] se encontró con los seis ojos de aquella criatura, pero antes de poder siquiera gritar por ayuda..."
    scene death_mnts_2 with shake
    play sound slash
    pause 3
    "{cps=20}Un corte limpio y rápido le atravesó el pecho. Ni siquiera sintió dolor antes de caer.{/cps}"
    pause 2
    scene gameover_screen with dissolve
    pause(2)
    menu:
        "Cargar partida":
            jump load_screen
        "Volver al menú principal":
            return    

label game_over_mnts_2:
    "Rápidamente, [nombre_jugador!c] se deslizó bajo una de las camas, conteniendo la respiración."
    
    scene habitacion_mantis with fade
    play sound nailtap volume 1.3
    "El sonido de los pasos se intensificaba... Cada vez más cerca..."
    stop sound fadeout 0.3
    "Una sombra se detuvo justo frente a la cama..."
    pause (2)
    
    play sound "sfx/claw_drag_concrete.mp3"
    "Una garra raspa el suelo... Luego la cama."
    
    
    pause (1.5)
    scene death_mnts_3 with shake
    play music curse
    play sound slash
    "Sin aviso, la hoja atraviesa el colchón y su torso."
    
    play sound "sfx/ultimo_aliento.wav"
    pause(2)
    scene gameover_screen with dissolve
    pause(2)
    menu:
        "Cargar partida":
            jump load_screen
        "Volver al menú principal":
            return


label cap_3:
    scene black
    "El eco de sus propios pasos en el pasadizo lo transportó a otro tiempo. A un lugar donde el único monstruo era la soledad."

    scene expression Solid((255,255,255)) with fade
    centered "{i}{color=#000000}...Estático. Luz cálida. Voces infantiles a lo lejos...{/color}{/i}"

    play music flashback fadein 2
    scene luzdrigo_fb_1 at sepia_filter with dissolve
    "El sol de primavera caía oblicuo sobre el patio de la escuela, manchado con sombras largas el concreto rajado."
    
    scene luzdrigo_fb_2 at sepia_filter with fade
    "En una esquina, lejos de los juegos, los gritos, y las risas, un niño de cabello desordenado se acurrucaba contra una pared, con la mirada baja y con los brazos cruzados sobre las rodillas."
    
    "[nombre_jugador!c]."
    
    "Su uniforme estaba limpio, pero arrugado. En el suelo junto a él había un cuaderno con garabatos oscuros, de formas extrañas y sin nombre. Dibujos de criaturas, de ojos tristes, de árboles secos."
    "No hablaba. No miraba. Solo esperaba que el recreo acabara."
    "Hasta que oyó pasos. Lentos, ligeros. Y una sombra diferente a las demás cubrió parte de su cuaderno."
    
    scene luzdrigo_fb_3 at sepia_filter with dissolve
    '?' "{i}¿Tú lo dibujaste?{/i}"

    "[nombre_jugador!c] levantó apenas la vista. Frente a él había un niño de cabello castaño claro, suelto y algo desordenado. Sostenía una manzana a medio comer, y lo miraba sin miedo, sin burla. Solo… con interés genuino."

    '?' "{i}No está feo. Da miedo, pero es bonito.{/i}"

    "[nombre_jugador!c] no respondió. Volvió a mirar el cuaderno, esperando que el niño se aburriera y se marchara."
    "Eso es lo que todos hacían."

    scene luzdrigo_fb_4 at sepia_filter with dissolve
    "Pero no se fue."
    "El niño se sentó a su lado sin invitación, cruzando las piernas sobre el suelo sucio."

    ln "{i}Yo soy Lucien. Tú eres el que no habla, ¿cierto?{/i}"

    "Silencio."
    "El se encogió de hombros."

    ln "{i}Está bien. No tienes que hablar. Puedo hablar yo.{/i}"

    "Y así lo hizo."
    "Sin pedir permiso, comenzó a llenar el vacío."

    ln "{i}Ayer mi perro se comió uno de mis calcetines. Es muy tonto, pero lo quiero mucho. Mi mamá casi lo regaña, pero yo lo escondí debajo de mi cama.{/i}"
    r "..."

    ln "{i}Oh, y mi abuela hizo sopa ayer. Sopa verde. Dice que te hace fuerte, pero...{/i} "
    "Lucien arrugó la nariz con disgusto."
    ln "{i}Sabe a pasto hervido.{/i}"

    "[nombre_jugador!c] parpadeó, mirándolo de reojo. Era la primera vez que alguien le hablaba de cosas tan normales. Tan aburridas. Tan... cálidas."

    ln "{i}Me gusta más estar aquí.{/i} "
    "Lucien señaló hacia el centro del patio con su manzana."
    ln "{i}Los niños grandes gritan mucho allá. Juegan a la pelota y siempre te empujan si no te quitas. Aquí es más tranquilo. Además, tú dibujas cosas geniales.{/i}"
    
    scene luzdrigo_fb_5 at sepia_filter with dissolve
    "Lucien partió un trozo de su manzana con las manos. Se lo tendió."
    ln "{i}¿Quieres? Mi mamá siempre me manda mucha comida. Y la manzana sabe mejor que la sopa verde.{/i}"
    "[nombre_jugador!c] dudó. Sus ojos fueron de la manzana a la sonrisa de Lucien. Finalmente, la tomó con torpeza, sorprendido de que alguien se quedara tanto rato con él."

    scene luzdrigo_fb_6 at sepia_filter with fade
    pause 1
    "Pasaron semanas."

    "Y cada día, Lucien encontraba una excusa para buscarlo. A veces dibujaban juntos; Lucien le prestaba sus lápices de colores para que las criaturas no fueran solo oscuras. A veces solo se sentaban a comer en silencio."
    "Y un día, cuando la campana sonó anunciando el fin del recreo, [nombre_jugador!c] guardó su cuaderno, miró a su acompañante, y habló por primera vez:"

    scene luzdrigo_fb_7 at sepia_filter with dissolve
    pause 1
    r "{i}Me llamo [nombre_jugador!c].{/i}"
    "Lucien no pareció sorprendido. Lo miró con una sonrisa que iluminó más que el sol."

    ln "{i}Ya lo sabía. Pero me alegra oírlo de ti.{/i}"

    scene black with fade
    stop music fadeout 2
    pause 3
    play music "sfx/goteo_lento.wav" volume 0.5 loop
    scene pasillo_oscuro with dissolve

    "La luz del recuerdo se desvanece."
    "El aire vuelve a ser espeso. Húmedo. Muerto."

    scene corredor_amplio with dissolve
    "El pasadizo por el que [nombre_jugador!c] y Luz avanzaban se abre finalmente hacia un corredor más amplio."
    "Los escombros se acumulan en las esquinas y algunas lámparas cuelgan inertes del techo."
    "A lo lejos, las puertas del vestíbulo se vislumbran a través de las sombras."

    scene vestibulo
    show azura temblor at left, shaking
    with dissolve
    play music menu fadein 1.5
    "Una figura se apoya contra la pared. Tiembla."

    show luz surprised at center with moveinright
    l "¡Azura!"
    "Azura levanta la vista de golpe, conteniendo el aliento. Al reconocerla, sus ojos se llenan de lágrimas contenidas."
    a "Luz… [nombre_jugador!c]… Pensé que…"

    show rodrigo serio at right with moveinright
    menu:
        "Preguntas si está bien":
            $ afinidad_azura += 2

            show rodrigo serio at centro_izquierda
            show luz surprised at centro_derecha
            with move
            "[nombre_jugador!c] acorta la distancia en dos pasos firmes."

            "No mira el vestíbulo. No mira las sombras."
            "Mira a Azura."

            r "¿Estás herida?"

            "Sus ojos recorren sus brazos, su cuello, las mangas rasgadas."
            "Azura tarda un segundo en responder, como si la pregunta tuviera que atravesar una niebla espesa."
            
            a "No... solo asustada."
            a "No quise separarme, pero… algo nos forzó a dispersarnos."
            a "Fue... el ruido."

            "Se seca una lágrima rápidamente y se endereza."
            "Está intentando mantenerse compuesta, fallando apenas."
            "[nombre_jugador!c] asiente, pero su mandíbula permanece tensa."

            r "Nagi y Cuty."
            r "¿Los viste lastimados?"

            a "No."
            a "Corrían."

            "No dice 'están bien'. No dice 'están vivos'"
            "Solo 'corrían'."
            "Eso basta para que el silencio vuelva a pesar"
        
        "Preguntas por lo que ocurrió":
            $ afinidad_azura += 1
            "[nombre_jugador!c] no se acerca."
            "Su postura se mantiene rígida, como si cualquier paso en falso pudiera activar algo."

            r "¿Qué ocurrió?"
            r "¿Donde están los otros?"

            "La pregunta sale rápida. Precisa."
            "Casi militar."
            "Azura parpadea, desorientada por el tono."
            
            a "Yo..."

            "Miró el suelo, tratando de ordenar el recuerdo."

            a "No lo sé. Corrimos en direcciones opuestas."
            a "Nagi y Cuty subieron al segundo piso."

            "Se lleva una mano a la sien."
            
            a "Escuché algo detrás de nosotros."
            a "No eran pasos."
            a "Era... más pesado."
            
            "Su respiración se acelera apenas al recordarlo."
            
            "[nombre_jugador!c] aprieta la empuñadura de su daga."
            
            r "¿Los viste caer?"
            
            a "¡No!"
            
            "La respuesta es demasiado rápida."
            "Demasiado frágil."
            
            a "Solo... corrimos."
            
            "El vestíbulo vuelve a sentirse inmenso."
            "Y el segundo piso, peligrosamente lejano."
        
        "Te quedas callado":
            $ estado_mental += 2
            "[nombre_jugador!c] no respondió."
            
            "Su mirada no estaba en Azura… sino en el espacio detrás de ella."
            
            "El vestíbulo era demasiado grande. Demasiado abierto. Demasiados lugares donde algo podía estar observándolos."
            
            a "[nombre_jugador!c]…"
            show azura emocion at centro_izquierda, shaking
            with move
            
            "Azura da un paso hacia él, pero vacila a mitad de camino."
            
            a "Oye… di algo."
            
            "Sus manos tiemblan. No de miedo inmediato… sino de agotamiento. De sobrecarga."
            
            a "No sé dónde están Nagi y Cuty."
            a "Y si tú te quedas así…"
            
            "Traga saliva. Sus palabras se fragmentan."
            
            a "No puedo ser la única que piense."
            
            "Eso lo golpea más que cualquier grito."
            "[nombre_jugador!c] parpadea. La imagen de cuerpos mutilados desaparece lentamente."
            
            r "...Siguen vivos."
            r "Tienen que estarlo."
            
            "No suena convencido."
            
            a "Entonces vamos a encontrarlos."
            
            "Azura no sonríe. No se recompone."
            "Solo se obliga a mantenerse en pie."

    show luz worry
    "Luz mira hacia [nombre_jugador!c]. Él evita la mirada por un segundo, pero luego asiente."

    l "Entonces los buscaremos. No vamos a dejarlos atrás."

    a "Gracias… De verdad."

    "[nombre_jugador!c] lanza una última mirada hacia el vestíbulo. Aún bloqueado. La salida parece más lejana que nunca."

    "Sin decir nada, se gira, comenzando a avanzar hacia las escaleras con pasos firmes."

    "Azura y Luz lo siguen."

    # -- La escalera --
    stop music fadeout 1.5
    scene escaleras_con_sombra with fade
    play sound wood_creak volume 0.4

    "La escalera era ancha y vieja, con una barandilla que se descascaraba bajo los dedos. Cada peldaño devolvía un quejido distinto."
    "[nombre_jugador!c] subió pegado a la pared, probando el peso de cada escalón antes de confiarle el siguiente paso. Detrás, la respiración de Azura. Más atrás, la de Luz. Tres ritmos distintos intentando no hacer ruido."
    "Subieron al segundo piso. El silencio era peor que los gritos."

    show rodrigo serio at center
    show luz worry at left
    show azura worried at right
    with dissolve

    "En el rellano, la linterna cortó un pasillo largo con puertas a ambos lados. Todas cerradas. Todas iguales."
    "Al fondo, algo goteaba. Y bajo el goteo, un golpeteo leve y regular que podía ser una tubería, una ventana suelta, o cualquier otra cosa."

    a "Si corrían, tuvieron que subir por aquí. Es la única escalera que quedó libre."
    a "Pero mira cuántas puertas. Podrían estar detrás de cualquiera."

    l "Entonces los llamamos. Si están cerca, nos oirán."

    "Azura se giró hacia ella tan rápido que la linterna le bailó en la mano."

    a "No. Luz, no. Lo que nos separó también oye."
    l "¿Y si están heridos? ¿Y si están a diez metros y no se atreven a contestar?"

    "La pregunta quedó colgando en el pasillo. Las dos miraron a [nombre_jugador!c]."

    menu:
        "Llamarlos en voz alta, una sola vez":
            $ afinidad_luz += 1
            r "Una vez. Bajito, pero que se oiga."
            "Azura apretó los labios, pero no discutió."
            "Luz acercó las manos a la boca, cuidando el volumen."
            l "¡Nagi! ¡Cuty!"
            "Su voz recorrió el pasillo y se fue apagando contra el fondo, puerta tras puerta."
            pause 1.5
            "Nada."
            "Ni pasos. Ni una voz. Solo el goteo, y un eco que tardó demasiado en volver."
            l "...Quizá no nos oyen."
            a "O no pueden contestar."
            "Nadie corrigió a Azura."

        "Pedir silencio y revisar las puertas una a una":
            $ afinidad_azura += 1
            $ estado_mental -= 1
            r "Nada de gritos. Primero escuchamos."
            "Azura soltó el aire que tenía retenido. Luz dudó. Luego asintió, despacio."
            l "Está bien. Pero si en algún momento..."
            r "Lo sé. Si pasa, gritamos todos."
            "Se quedaron quietos, con las linternas apuntando al suelo. El pasillo se fue llenando de sonidos pequeños: el goteo, el golpeteo regular, la madera asentándose, sus propios pulsos."
            "Ni una voz. Pero tampoco ninguna señal de que alguien los hubiera oído llegar."

    "Fueron probando puertas. La primera estaba atrancada. La segunda daba a un cuarto con el techo hundido y las paredes negras de humedad, y nadie quiso entrar."
    "La tercera cedió sin un solo chirrido."
    "Demasiado bien aceitada."

    # -- La habitación --
    scene habitacion_intacta with dissolve
    pause 0.5

    "Una habitación... Limpia. Sin sangre. Sin roturas."
    "[nombre_jugador!c] entró primero. Revisó detrás de la puerta. Bajo la cama. Tras la cortina de la ventana. Un procedimiento aprendido de memoria; la paranoia, otra vez, ejerciendo de oficio."
    "Nada. Solo una cama con las sábanas tensas, un escritorio de madera clara, una mesa en el centro y tres acuarelas de paisajes pálidos colgadas de la pared."

    show rodrigo neutral
    show luz neutral at left
    show azura neutral at right
    with dissolve

    "Por primera vez desde que entraron al orfanato, el aire no olía a podredumbre."
    "En el fondo, en un perchero, colgaba un abrigo viejo. Un olor a humedad y tinta seca impregnaba el ambiente, pero era un espacio extrañamente pacífico."
    "Sobre la mesa central, una baldosa del falso techo estaba combada, con una mancha oscura en el medio, del tamaño de una mano. [nombre_jugador!c] la registró y la descartó: humedad, probablemente."

    a "Es raro... Alguien cuidaba este lugar..."

    "Sus ojos esmeralda se dirigen a los cuadros mientras da un par de pasos hacia ellos, bajando los hombros visiblemente."
    "Era el espejismo de un refugio. Una falsa sensación de seguridad que todos necesitaban desesperadamente."

    show luz smile with dissolve
    "Luz, aprovechando la pausa, revisaba los cajones del escritorio en busca de información útil. Los abría apenas lo necesario para que no rechinaran."

    l "[apodo_jugador]... ven. Mira esto."

    "Luz sacó un bulto envuelto en un pañuelo de un cajón. Dentro, el metal frío brilló bajo la linterna."

    hide rodrigo
    hide azura
    hide luz
    show pistola_primer_plano at truecenter
    with dissolve
    "Una pistola. Vieja, pero aceitada. Y una caja de balas."

    show rodrigo neutral
    show luz smile at left
    show azura neutral at right
    hide pistola_primer_plano
    with dissolve

    l "¿Crees que funcione?"
    r "Esperemos no tener que averiguarlo."

    "Luz giró el arma entre las manos con el dedo lejos del gatillo, como quien sostiene un animal dormido."

    show luz worry
    l "No sé si podría usarla, [apodo_jugador]. De verdad. Si llegara el momento..."

    "No terminó la frase. Azura bajó la mirada al suelo."

    menu:
        "Dejar que Luz se la quede: \"Tú tienes mejor pulso\"":
            $ afinidad_luz += 1
            r "Quédatela. Tú tienes mejor pulso que yo."
            l "Mentiroso. Pero gracias por fingir."
            r "No estoy fingiendo."
            "Luz sostuvo su mirada un segundo. Después volvió a envolver el arma en el pañuelo y se la acomodó en la cintura, con cuidado."

        "Intentar quedártela: \"Dámela, yo me encargo\"":
            $ estado_mental += 1
            r "Dámela. Yo me encargo."
            l "No."
            r "Luz..."
            l "No, [apodo_jugador]. Tú siempre quieres llevarlo todo tú."
            l "Si hay que apretar el gatillo, prefiero que sea decisión mía. No algo que me quitaron de las manos."
            "[nombre_jugador!c] conocía esa mirada. Nunca había ganado contra ella."
            r "...Está bien."
            "Luz guardó el arma en su cintura. Él se quedó con las manos vacías y con la sensación de que acababa de perder algo más que una discusión."

    "La caja de balas desapareció en el bolsillo de Luz."

    # -- La nota --
    "Luego, [nombre_jugador!c] se dirigió al pequeño librero."
    "Un manual de puericultura. Una libreta de asistencia con las páginas pegadas por la humedad. Libros de cuentos con los lomos vencidos de tanto uso."
    "Y entre dos tomos, una nota amarillenta doblada con una prolijidad que desentonaba con todo lo demás."

    play sound paper_flip
    play music story
    show rodrigo serio with dissolve
    pause 0.5

    "Al abrirla, su expresión se endurece."

    "{cps=20}{b}Entrada 04 – Día 11{/b}{/cps}"

    "{cps=20}El {b}60%%{/b} de los primeros sujetos han fallecido. El proceso de mutación resultó inestable; los tejidos colapsan, los huesos se expanden sin orden y los sistemas vitales no resisten.{/cps}"
    "{cps=20}Los cuerpos se deforman en masas amorfas, aún respirando en algunos casos por horas. Las cámaras frías están saturadas. Se incrementó la dosis de estabilizadores para los próximos voluntarios.{/cps}"

    "La leyó dos veces. La segunda, más despacio, como si el número pudiera cambiar."
    "Detrás de él, los pasos de Luz se acercaron sobre las tablas."

    l "¿Y? ¿Qué encontraste?"

    "[nombre_jugador!c] arrugó la nota antes de guardarla en su bolsillo, tragándose el nudo de horror moral que se le formó en la garganta."

    menu:
        "Decir que no es nada":
            $ estado_mental += 1
            r "Nada útil... Solo... Basura vieja..."
            show luz neutral
            l "¿Seguro? Te vi la cara."
            l "¿No será algo importante?"
            r "No nos sirve. Vamos."
            "Luz abrió la boca. La cerró."
            "Conocía a [nombre_jugador!c] lo suficiente para saber cuándo empujar y cuándo no. Esta vez no empujó. Eso no significaba que se lo hubiera creído."

        "Decir que es más de lo mismo, pero que no quieres leerlo en voz alta":
            $ afinidad_luz += 1
            r "Más de lo mismo. Lo que ya sabemos, pero peor."
            r "No quiero leerlo en voz alta. Todavía no."
            "No era mentira. Solo era la parte más pequeña de la verdad."
            show luz worry
            l "...Está bien."
            l "Pero cuando puedas, me lo cuentas. Aunque sea feo."
            r "Cuando pueda."
            "Le salió más fácil de lo que esperaba. Eso fue lo que lo asustó."

    "Incluso si no quería admitirlo, [nombre_jugador!c] se estremeció por lo que leyó."
    "La sola idea le revolvía el estómago."

    # -- La pregunta de Azura --
    pause 0.5
    "Azura se había quedado de pie frente a las acuarelas. Pasó un dedo por el borde de un marco. Ni una mota de polvo."

    show azura worried with dissolve
    a "Chicos... ¿Creen que alguien dormía aquí... sabiendo todo lo que pasaba?"

    "La pregunta no iba dirigida a nadie en concreto. Pero [nombre_jugador!c] sintió el papel en su bolsillo como si ardiera."

    menu:
        "Querer creer que no sabía":
            $ afinidad_azura += 2
            r "Quiero creer que no sabía."
            "Salió suave. Casi convincente."
            "Tenía en el bolsillo una hoja arrugada que decía exactamente lo contrario."
            a "Yo también."
            "Azura sonrió apenas. Una sonrisa pequeña, agradecida, que a [nombre_jugador!c] le quemó más que cualquier grito."
            a "Es una tontería, pero necesito creerlo. Si no, esta habitación..."
            "No terminó la frase. No hacía falta."

        "Decir que sí sabía, y que se quedó callado":
            $ estado_mental += 1
            r "Alguien que lo sabía... y se quedó callado."
            "No lo pensó. La frase salió sola, con un filo que no esperaba."
            "Solo después, tarde, notó el peso exacto de la hoja en su bolsillo."
            "Azura parpadeó. La poca sonrisa que le quedaba se apagó."
            a "...Eso es peor, ¿sabes?"
            r "Lo sé."
            "Luz se acercó un paso y le rozó la manga. No dijo nada."

        "Cambiar el foco: Nagi y Cuty":
            $ estado_mental -= 1
            $ afinidad_azura += 1
            r "Ahora mismo, lo único que me importa es dónde están Nagi y Cuty."
            "Lo dijo sin dureza. Era verdad."
            a "Tienes razón. Perdón. Es que... los pensamientos se me van a lugares feos."
            r "A mí también. Por eso mejor miramos al frente."
            "Azura asintió, aferrándose a la frase como a una barandilla."

    "Luz lo miró un segundo más de lo necesario. Era la mirada de quien guarda una pregunta para después."

    # -- El derrumbe --
    pause 1.0
    stop music fadeout 1.5
    stop ambient fadeout 1.0
    "El silencio reinó unos segundos."
    "Demasiados."
    "Y en algún momento, sin que nadie lo notara, el golpeteo del pasillo dejó de sonar."
    "Sobre la mesa central, un hilo fino de polvo gris se desprendió de la baldosa combada."

    play sound wood_creak
    "Un crujido seco sobre sus cabezas los hizo congelarse."

    play sound thud
    play sound objfall
    with vpunch
    show azura scared at right, vjump
    show luz scared at left, vjump
    show rodrigo alert at center, vjump

    "¡CRASH!"
    "Las baldosas del falso techo cedieron de golpe. Un bulto pesado cayó en picada y se estrelló violentamente contra la mesa central, levantando una nube de polvo gris."
    "No era un monstruo."
    "Era un cadáver momificado. Vestía una bata de laboratorio podrida, probablemente un investigador atrapado desde la caída del Proyecto H-127."
    "Su rostro estaba congelado en una mueca de terror absoluto, con la mandíbula desencajada."

    a "¡Dios mío!"

    "Luz alzó la pistola con las manos temblorosas, apuntando instintivamente hacia el hueco oscuro en el techo."
    "Pero no había nada allí. Solo el eco del impacto desvaneciéndose."

    "Por un instante, nadie se atrevió a mirar el rostro del cadáver. Los tres pensaron lo mismo y ninguno lo dijo: ¿y si no era un desconocido?"
    a "No es... no es ninguno de ellos."
    "Lo dijo como se dice una oración. Luz soltó el aire que no sabía que contenía."
    "El alivio duró un segundo. Después llegó la culpa de haberse alegrado frente a un muerto."

    "[nombre_jugador!c] da unos pasos hacia la puerta, cada músculo tenso. El espejismo de refugio se había hecho pedazos."

    $ renpy.save("1-1", "Encuentro 3")
    "[nombre_jugador!c] se detiene. Su mirada se dirige hacia la ventana."

    r "(Algo está mal... Todo se quedó en silencio de nuevo...)"
    l "¿[apodo_jugador]...?"
    r "No se muevan."

    "Extiende su mano hacia Luz sin apartar la vista del cristal sucio."
    
    play music melody

    "Una voz femenina se desliza entre las paredes, suave, casi cantarina, con un tono juguetón que hiela la sangre."

    play ambient "sfx/susurro_cercano.wav"
    g "Sé que están ahí~"

    "Azura se cubre la boca con ambas manos, retrocediendo."
    "Luz gira lentamente hacia la ventana, donde una silueta se asoma."

    scene galaxia_ventana with dissolve
    
    "Allí estaba. Una silueta oscura recortada contra la noche, con orejas de gato y una sonrisa demasiado ancha."
    
    g "¿Ya juegan al escondite? Me encanta ese juego..."

    "[nombre_jugador!c] baja el rostro, dientes apretados."

    play sound "sfx/bang_window.mp3" volume 2.0
    with vpunch 
    
    g "Pero yo siempre gano."
    
    r "Vámonos. ¡YA!"
    
    play sound "sfx/rasguño_vidrio.wav"
    "Un chirrido agudo de garras contra el cristal los persiguió mientras huían."
    
    scene pasillo_corriendo with dissolve
    play sound run
    "Cuando finalmente abandonan la habitación y cierran la puerta con suavidad, el grupo suelta el aire contenido."

    show rodrigo alert
    "[nombre_jugador!c], aún en tensión, no mira atrás. Solo camina al frente, guiándolas."
    "Pero por un momento... su sombra proyectada en la pared parece temblar."
    "Como si algo dentro de él empezara a agitar"
    
    scene pasillo_abandonado
    show rodrigo serio at centro_izquierda
    show luz worry at left
    show azura worried at centro_derecha
    with fade
    play sound walk loop
    stop music fadeout 1.5

    "Los tres avanzaban con pasos medidos. La linterna de [nombre_jugador!c] barre el pasillo, revelando capas de polvo, trozos de pintura descascarada, y puertas cerradas con placas oxidadas."
    "A cada paso, el crujido del suelo de madera hace eco, forzándolos a contener la respiración."

    l "¿Siempre fue así de frágil...?"
    a "No es solo viejo... Está a punto de ceder..."
    r "Entonces vayamos más lento... Por las orillas si es posible."

    show luz worry at centro_derecha
    show azura worried at right
    show rodrigo serio at center
    with moveinleft
    "Se acomodan, caminando en fila, pegados a la pared. Sus sombras oscilan con la luz, proyectándose deformadas."
    "La tensión se siente con cada movimiento."

    stop sound fadeout 1.5
    "De pronto, al fondo del pasillo, dos siluetas cruzan brevemente el marco de una puerta abierta."
    "Una de ellas voltea, mostrando el rostro de Cutipye, quien parece decir algo antes de entrar. Nagi le sigue, como si lo que encontraron fuera importante."

    show luz surprised at vjump
    l "¡Hey! ¡Cuty! ¡Nagi!"

    "Ellos voltearon. Nagi abrió la boca para gritar algo, pero el sonido fue otro."

    stop sound
    play sound crack
    show rodrigo sorprendido at vjump
    "CRRRK…"
    "El piso bajo los pies del trío se agrieta. Se oye un crujido largo, siniestro."

    r "¡No se muevan!"

    play sound crack
    pause 0.5
    show rodrigo scared at vfall
    show azura scared at vjump
    show luz scared at vjump
    play music shock noloop
    pause 0.2
    scene derrumbe with shake
    play sound break_wood
    pause 0.5
    
    "Demasiado tarde."
    "El suelo desapareció."
    "Azura y Luz logran aferrarse a los bordes, gritando al hacerlo, pero [nombre_jugador!c] —el más cercano al centro— desaparece en la penumbra, tragado por el derrumbe."

    $ _nombre_upper = nombre_jugador.upper()
    $ _ultima_vocal = next((c for c in reversed(_nombre_upper) if c in "AEIOUÁÉÍÓÚÜ"), _nombre_upper[-1])
    $ _idx_vocal = len(_nombre_upper) - 1 - next(i for i, c in enumerate(reversed(_nombre_upper)) if c in "AEIOUÁÉÍÓÚÜ")
    $ grito_nombre = _nombre_upper[:_idx_vocal] + _ultima_vocal * 5 + _nombre_upper[_idx_vocal + 1:]
    l "¡[grito_nombre]!"

    a "¡No... no, no, no!"

    scene pasillo_abandonado
    show luz scared at centro_derecha
    show azura scared at right
    show nagi surprised at centro_izquierda
    show cutipye scared at left
    with dissolve
    "El polvo cubre todo. Desde el piso superior sólo se ve el vacío, y el eco lejano del cuerpo de [nombre_jugador!c] golpeando estructuras al caer."

    play ambient "dust_and_echo.ogg"
    pause 2

    call chapter_complete("Capítulo 3")
    jump cap_4



label cap_4:
    scene black with fade
    play music melody fadein 2
    play ambient "sfx/drop_distant.mp3" loop
    play sound "sfx/heavy_breathing.ogg" loop volume 0.8
    pause 1

    "Oscuridad."
    "El polvo desciende como ceniza."
    "La boca de [nombre_jugador!c] se llenó de un sabor a sangre y tierra."
    "El aire es espeso, y el único sonido es el lento jadeo del castaño."
    r "Estoy vivo... Creo que eso cuenta para algo..."

    scene bodega_dark with fade
    show rodrigo injured at center
    with dissolve

    "Se sentó con dificultad, tosiendo. Su linterna parpadeó, iluminando escombros y vigas rotas."
    "El aire en el subsuelo era denso, una mezcla rancia de humedad, moho y sangre seca."

    show item_gun at left with dissolve
    "A unos metros, reflejando la escasa luz, algo metálico relucía entre el polvo."
    "La pistola."
    hide item_gun

    scene rodrigo_grab_pistol with dissolve
    "[nombre_jugador!c] se arrastró hasta ella y la tomó con la mano temblorosa, recordando brevemente el rostro de Luz al encontrarla."
    "Apretando los dientes, la aseguró en su cinturón improvisado."

    scene bodega_dark
    show rodrigo neutral at center
    with dissolve

    r "Perfecto... Un sótano oscuro en un orfanato abandonado."
    show rodrigo molesto with dissolve
    r "Solo falta una niña en triciclo y tengo el bingo del terror completo."

    scene bg_bodega_pan with dissolve
    stop sound fadeout 1.5
    "Silencio. Solo el lejano goteo de agua."
    "Observa a su alrededor."
    "Estanterías corroídas, cajas desechas, frascos vacíos y algunos envases sellados con etiquetas ilegibles."
    "El lugar parece una bodega metálica olvidada, húmeda y colapsada en varias secciones."

    show rodrigo move_slow with dissolve
    play sound walk loop
    "[nombre_jugador!c] da unos pasos con lentitud, examinando la habitación. Se apoya contra una pared para mantener el equilibrio."
    "Por unos instantes, se permite respirar."

    r "Podría ser peor... Podría estar atrapado con uno de esos monstruos..."

    pause 1.5

    stop sound
    stop music
    play sound "sfx/claw_drag_concrete.mp3"
    show rodrigo alert at vjump
    "CRRRK..."
    "Un sonido rasposo. Uñas largas contra el hormigón."
    
    play sound glx_laugh
    "Y una risita baja, gutural."

    stop sound fadeout 3
    "[nombre_jugador!c] se detiene en seco."
    "Nada visible, pero algo se movió en la penumbra."
    "Aprieta el arma."

    play music chase fadein 1
    $ renpy.save("1-1", "Encuentro 4")
    centered "{cps=20}No estás solo...{/cps}"

    "La oscuridad parece expandirse, como si algo lo observara desde más allá del ojo humano."

    scene bodega_gal_shadow with dissolve
    pause 0.7
    show galaxia shadow_eyes at center with dissolve

    "{color=#390169}{font=fonts/HelpMe.ttf}{cps=20}Tan frágil... Hueles a miedo... y a sudor frío. Me encanta.{/cps}{/font}{/color}"

    r "¡Déjame en paz, maldita sea!"
    
    play sound "sfx/monster_parkour.ogg"
    "La criatura se abalanzó, rebotando desde la pared hacia él con una agilidad inhumana."

    # --- DECISIÓN 1: LA RUTA DE HUIDA ---
    menu:
        "Correr por el pasillo de la izquierda":
            jump persecucion_cap4_pasillo
            
        "Correr por el pasillo de la derecha":
            "[nombre_jugador!c] se lanzó hacia el corredor derecho, buscando una salida rápida."
            scene escombros_bloqueo with vpunch
            "Pero a los pocos metros, un derrumbe de vigas oxidadas y hormigón bloqueaba el paso por completo."
            r "¡No, no, no! ¡Está cerrado!"
            jump game_over_persecucion_bodega

        "Esconderse tras las estanterías":
            "[nombre_jugador!c] se arrojó detrás de una hilera de estanterías corroídas, conteniendo el aliento en la penumbra."
            play sound "sfx/shelf_rip.ogg"
            with vpunch
            "Fue inútil. Ella no buscaba con los ojos; su olfato la guio directo hacia él, arrancando el metal de cuajo como si fuera cartón."
            jump game_over_persecucion_bodega

label persecucion_cap4_pasillo:
    scene pasillo_corriendo with vpunch
    play sound run loop
    #show rodrigo run_panic at center
    show rodrigo alert at center
    
    "[nombre_jugador!c] giró sobre sus talones y corrió por el pasillo de la izquierda, más rápido de lo que jamás había corrido en su vida."
    "Se lanzó a través de una serie de habitaciones conectadas: antiguas lavanderías con máquinas oxidadas que parecían fauces abiertas y cuartos de calderas donde las tuberías silbaban como serpientes."
    "Detrás de él, no había pasos humanos. Había una bestia cazando."
    
    play sound "sfx/claw_drag_concrete.mp3"
    "Clic-clic-clic."
    "Impactos pesados contra las paredes y el techo. Galaxia no solo lo perseguía; jugaba con el terreno, cerrando la distancia a cada segundo."

    # --- DECISIÓN 2: OBSTÁCULO EN EL CORREDOR ---
    menu:
        "Derribar una estantería pesada a su paso":
            play sound "sfx/heavy_bang.mp3"
            with hpunch
            "Sin dejar de correr, [nombre_jugador!c] aferró el borde de un armario de suministros oxidado y lo volcó tras de sí con un estruendo metálico."
            "Las garras de Galaxia rasparon el metal al saltar por encima del obstáculo, dándole apenas un par de segundos vitales de ventaja."
            jump persecucion_cap4_almacen

        "Disparar hacia atrás sin detenerse":
            $ estado_mental += 1
            play sound gunshot
            with flash
            "Dominado por el pánico, [nombre_jugador!c] giró el torso y disparó a ciegas hacia la penumbra del corredor."
            "El fogonazo iluminó por una fracción de segundo una silueta que se desplazaba por el techo, esquivando el tiro sin esfuerzo."
            play sound glx_laugh
            g "{cps=20}¡Uy, casi! ¡No desperdicies tus juguetes tan pronto, [apodo_jugador]!~{/cps}"
            "El retroceso lo hizo trastabillar, pero el terror puro mantuvo sus piernas en movimiento."
            jump persecucion_cap4_almacen

        "Ocultarse entre las calderas de vapor":
            stop sound
            "[nombre_jugador!c] frenó de golpe y se deslizó en el hueco estrecho entre dos enormes calderas inactivas, rezando para que las sombras lo cubrieran."
            "Pero en el silencio húmedo, el latido desbocado de su corazón y el olor de su propio sudor eran como un faro en la oscuridad."
            jump game_over_persecucion_bodega

label persecucion_cap4_almacen:
    stop sound
    scene bg_almacen_medico with fade
    show rodrigo alert at left with moveinright
    play sound "sfx/glass_break_footsteps.mp3"
    
    "Derrapó al entrar en un antiguo almacén médico. Estanterías volcadas y frascos rotos cubrían el suelo."
    "Cayó de rodillas sobre los cristales rotos, sintiendo el corte frío en la piel, pero se levantó al instante."

    g "¡Vamos, [apodo_jugador]! ¡Corre más rápido!"
    g "Si te alcanzo, te doy un besito. O un mordisco~"

    # --- DECISIÓN 3: DENTRO DEL ALMACÉN MÉDICO ---
    menu:
        "Correr hacia la puerta metálica del fondo":
            "[nombre_jugador!c] divisó una puerta de acero al otro extremo del almacén y se lanzó hacia ella como su última esperanza."
            jump persecucion_acorralado

        "Empujar una camilla para bloquear la entrada":
            play sound "sfx/metal_crunch.mp3"
            "[nombre_jugador!c] aferró una camilla oxidada y la arrojó contra el umbral por el que acababa de entrar."
            play sound "sfx/monster_parkour.ogg"
            with vpunch
            "La sombra ni siquiera tocó el suelo: pasó por encima del marco de la puerta, obligándolo a retroceder desesperado hasta el fondo del salón."
            jump persecucion_acorralado

        "Plantarse en medio de la sala y apuntar a la entrada":
            "[nombre_jugador!c] alzó la pistola en el centro del almacén, apuntando fijo hacia el umbral oscuro con las manos temblorosas."
            "Pero no hubo ruidos frente a él. Un crujido metálico resonó directamente sobre su cabeza, entre las vigas del techo."
            jump game_over_persecucion_bodega

label game_over_persecucion_bodega:
    stop sound
    play sound slash
    play music curse
    scene black with flash

    "{cps=15}Error fatal.{/cps}"

    play sound "sfx/heavy_bang.mp3"
    with vpunch
    "Un peso brutal cayó desde arriba, derribando a [nombre_jugador!c] contra el concreto húmedo antes de que pudiera levantar el arma."
    
    play sound "sfx/bone_crack.mp3"
    "La pistola salió volando de sus manos, perdiéndose en la oscuridad con un eco metálico."

    scene bodega_gal_shadow with dissolve
    show galaxia shadow_eyes at center with dissolve
    
    g "{color=#390169}{font=fonts/HelpMe.ttf}{cps=20}¿Eso fue todo? Qué decepción, [apodo_jugador]~{/cps}{/font}{/color}"
    g "{color=#390169}{font=fonts/HelpMe.ttf}{cps=20}Pensé que jugaríamos un ratito más.{/cps}{/font}{/color}"

    play sound "sfx/bite_crunch.mp3"
    scene black with vpunch
    pause 1.0

    "{cps=15}[nombre_jugador!c] fue devorado en la oscuridad del subsuelo.{/cps}"

    scene gameover_screen with dissolve
    pause(2)
    menu:
        "Cargar partida":
            jump load_screen
        "Volver al menú principal":
            return

label persecucion_acorralado:
    play sound door_slam
    "Llegó al final. Puerta metálica. Cerrada."
    r "¡Mierda!"
    
    "El sonido de las garras se detuvo."
    "El silencio fue peor."

    show rodrigo aim_gun at left with dissolve
    "[nombre_jugador!c] se giró lentamente, espalda contra la puerta fría."

    show galaxia walk_creepy at right with moveinright
    "De las sombras surgió ella."
    "Caminaba erguida, pero con la postura encorvada de una hiena. Ojos luminiscentes. Dientes afilados."

    g "Te acorralaste solito. Qué torpe eres."
    
    r "Aléjate. Soy alérgico al pelo de perro."

    show galaxia smile
    "Galaxia soltó una carcajada y se lanzó."
    
    # --- INICIO DE LA SECUENCIA DE IMPACT FRAMES ---
    show galaxia at centro_izquierda with moveinright
    window hide None

    # --- F0 (~2 frames): lanzamiento + arranca el disparo ---
    play sound gunshot
    stop music

    # --- F1 (~3 frames): negativo + sacudida vertical ---
    scene black
    show rodrigo aim_gun at left, impact_white_silhouette, impact_jolt(0, 10)
    show galaxia headshot at centro_izquierda, impact_white_silhouette, impact_jolt(0, 10)
    $ renpy.pause(0.05, hard=True)

    # --- F2 (~4 frames): IMPACT FRAME principal + sacudida horizontal ---
    scene white
    show rodrigo aim_gun at left, impact_silhouette_left, impact_jolt(15, 0)
    show galaxia headshot at centro_izquierda, impact_silhouette_hit, impact_jolt(15, 0)
    $ renpy.pause(0.066, hard=True)

    # --- Cierre: flash blanco corto que se apaga a negro ---
    scene black with impact_flash
    window show None
    #return

    
    "¡BANG!"
    
    play sound "sfx/thud.mp3"
    scene gal_dead_floor with vpunch
    "El disparo fue ensordecedor en el espacio cerrado. El retroceso casi le disloca la muñeca."
    "El impacto fue brutal. Un agujero perfecto perforaba el centro de su frente."
    
    play sound "sfx/body_fall_glass.mp3"
    "El cuerpo cayó pesadamente entre los cristales."
    
    scene bg_almacen_medico
    show rodrigo shocked at center
    with dissolve
    
    r "Dios... Se acabó."
    
    "[nombre_jugador!c] bajó el arma, temblando. Exhaló. Necesitaba salir."
    scene pasillo_corriendo
    show rodrigo neutral at center
    with fade
    "Se giró para buscar otra salida, dándole la espalda al cuerpo."
    
    play sound "sfx/wet_whisper.mp3" volume 2.0
    show rodrigo sorprendido at vjump
    g "{size=+10}{cps=5}Oye...{/cps}{/size}"
    "[nombre_jugador!c] tropezó hacia atrás."

    play music chase1
    scene chase1_reprise with fade
    "Estaba de pie."
    "El lado izquierdo de su rostro era una ruina sanguinolenta y humeante."
    "Pero el lado derecho... sonreía. Coqueta. Viva."

    g "{b}{cps=15}Las balas no funcionan, [apodo_jugador]~{/cps}{/b}"
    
    # Efecto visual de regeneración
    scene chase1_1
    show galaxia half_smile at truecenter:
        zoom 1.5
        linear 0.5 zoom 1.8
    with dissolve

    play sound "sfx/glx_regen.wav" # Sonido asqueroso de regeneración
    "Se acercó. Le dio un toquecito en la nariz con una garra, manchándolo de sangre."
    
    show galaxia regen with dissolve 
    pause 0.5
    show galaxia healed with dissolve

    "Frente a sus ojos, el cráneo destrozado se reacomodó. La piel se tejió sobre le agujero de bala."
    g "Vas a tener que esforzarte más si quieres romperme el corazón."
    r "¡NO!"
    
    scene bg_pasillo_escombros
    show rodrigo run_panic
    with vpunch
    
    g "¡CORRE, CORRE, CORRE!"
    "Ya no había coquetería. Solo hambre."

    # --- INICIO DE LA CUENTA REGRESIVA EN TIEMPO REAL ---
    $ _skipping = False
    $ opciones_agotadas = set()
    $ timer_persecucion = 40

    # Deshabilitar rollback durante toda la persecución
    $ config.rollback_enabled = False

    show screen hud_reloj_persecucion("game_over_ladder")

    "Las cuatro extremidades de Galaxia golpearon el suelo al unísono, recortando la distancia."

# ==========================================================
# MENÚ 1: OBSTÁCULO EN EL PASILLO
# ==========================================================
label cap4_menu_persecucion_1:

    $ renpy.block_rollback()

    menu:
        set opciones_agotadas

        "Volcar el archivador metálico":
            play sound "sfx/heavy_bang.mp3"
            with hpunch

            "[nombre_jugador!c] volcó un viejo archivador metálico para ganar tiempo."
            "No sirvió para detenerla —ella saltó sobre él rebotando en las paredes—, pero evitó el impacto directo."

            jump cap4_menu_persecucion_2

        "Forcejear con la puerta lateral":
            play sound door_slam
            with vpunch

            $ renpy.pause(1.0, hard=True)
            "Se lanzó contra la manija de una puerta oxidada. ¡Soldada por dentro! Tiene que seguir por el pasillo."

            jump cap4_menu_persecucion_1

        "Empujar unos tambores vacíos":
            play sound objfall
            $ renpy.pause(1.0, hard=True)

            "Arrojó unos barriles plásticos a su paso, pero eran demasiado ligeros; Galaxia ni siquiera redujo el paso."

            jump cap4_menu_persecucion_1

# ==========================================================
# MENÚ 2: DISTANCIA CRÍTICA ANTES DE LA ESCALERA
# ==========================================================
label cap4_menu_persecucion_2:

    $ renpy.block_rollback()

    menu:
        set opciones_agotadas

        "Lanzarle un ladrillo a la cara":
            r "¡Aléjate, monstruo!"
            play sound "sfx/brick_throw.mp3"

            "Lanzó un ladrillo sin dejar de correr. Ella ni se inmutó, pero el gesto le permitió alcanzar el fondo del corredor."

            jump cap4_llegada_escalera

        "Disparar a ciegas hacia atrás":
            $ estado_mental += 1
            play sound gunshot
            with flash

            $ renpy.pause(1.0, hard=True)
            "Disparó por encima del hombro presa del pánico. El tiro se perdió en el techo y el retroceso lo hizo trastabillar."

            jump cap4_menu_persecucion_2

        "Esconderse tras una columna agrietada":
            play sound "sfx/claw_drag_concrete.mp3"
            with vpunch

            $ renpy.pause(1.0, hard=True)
            "Intentó pegarse tras un pilar, pero las garras de Galaxia destrozaron el borde de concreto a centímetros de su cabeza. ¡Imposible esconderse!"

            jump cap4_menu_persecucion_2

# ==========================================================
# LLEGADA A LA ESCALERA — CONEXIÓN CON LOS 3 QTEs FINALES
# ==========================================================
label cap4_llegada_escalera:

    "Al final del pasillo, un resquicio de luz iluminaba su única salvación: una vieja escalera de mano oxidada que subía hacia una escotilla."
    "Estaba a cinco pasos. Pero el sonido de las garras estaba, literalmente, sobre su cuello."

    # El reloj global sigue corriendo durante los QTEs hasta que cierre la escotilla

# --- FASE 1: ALCANZAR LA ESCALERA (3.0s) ---
    call screen qte_escalera

label continue_escape_ladder:
    scene escalera_mano_1 with shake
    
    "[nombre_jugador!c] saltó y se aferró al primer peldaño de metal, impulsándose hacia arriba con desesperación."
    
    scene escalera_mano_2 with shake
    play sound slash
    r "¡¡AAAGH!!"
    
    "Antes de que sus pies despegaran del todo, unas garras como cuchillas le atravesaron el costado. Ardor lacerante."
    "El dolor fue cegador. La criatura lo estampó contra la pared de concreto mientras él seguía colgado de la escalera, intentando arrastrarlo hacia abajo."
    "En ese instante, a través de las garras hundidas en su carne, [nombre_jugador!c] sintió algo antinatural. Un latido ajeno filtrándose en sus venas."
    
    g "Te tengo."
    r "¡Suéltame!"
    
    # --- FASE 2: EL DISPARO A QUEMARROPA (2.5s) ---
    call screen qte_disparo_escalera

label exito_disparo_escalera:
    play sound gunshot
    with flash
    
    "Disparo a quemarropa en el abdomen."
    play sound "sfx/gal_pain_scream.mp3"
    
    "El impacto la dobló. [nombre_jugador!c] trepó como una exhalación y se arrojó hacia el interior del cuarto superior."

    scene bg_cuarto_maquinas with vpunch
    "Abajo, el eco de las garras rasgando el metal anunciaba que Galaxia ya estaba subiendo a toda velocidad."

    # --- FASE 3: CERRAR LA ESCOTILLA (2.0s) ---
    call screen qte_cerrar_escotilla

label exito_cerrar_escotilla:
    hide screen hud_reloj_persecucion
    $ _skipping = True # Restauramos el salto de texto normal
    play sound "sfx/hatch_slam_lock.mp3"
    with vpunch
    
    "Cerró la escotilla de golpe y giró la válvula con todas sus fuerzas, justo un instante antes de que ella lo alcanzara."
    
    play sound "sfx/heavy_bang.mp3"
    with vpunch
    "BAM."
    
    play sound "sfx/heavy_bang.mp3"
    with vpunch
    "BAM."
    
    "Arañazos frenéticos... y luego, silencio."

    show rodrigo bleeding_wall at center with dissolve
    stop music fadeout 3.0

    # Persecución superada — reactivar rollback
    $ config.rollback_enabled = True
    $ renpy.block_rollback()

    "[nombre_jugador!c] se dejó caer. Sangre caliente en sus dedos."
    "Miró su arma. Pocas balas."
    
    play music "music/sad_piano.mp3" fadein 2.0
    
    r "No tienen oportunidad..."
    
    "Una lágrima de impotencia se mezcló con el sudor."
    
    r "Si esa cosa los encuentra... si encuentra a Luz..."
    
    "La verdadera pesadilla no era morir."
    "Era sobrevivir para ver lo que ella les haría."

    call chapter_complete("Capítulo 4")
    jump cap_5

# --- PANTALLAS (QTE) ---

# QTE 1: Abajo al centro (3.0 segundos)
screen qte_escalera():
    modal True
    timer 3.0 action Jump("game_over_ladder")
    
    vbox:
        xalign 0.5
        yalign 0.8
        spacing 15
        text "{font=fonts/HelpMe.ttf}{size=50}¡LA ESCALERA! ¡AHORA!{/font}{/size}" color "#f00" at transform_blink
        textbutton "TREPAR" action Return() style "button_panic"

# QTE 2: Derecha al centro (2.5 segundos)
screen qte_disparo_escalera():
    modal True
    timer 2.5 action Jump("game_over_ladder")
    
    vbox:
        xalign 0.8
        yalign 0.5
        spacing 15
        text "{font=fonts/HelpMe.ttf}{size=50}¡APUNTA AL ABDOMEN!{/font}{/size}" color "#f00" at transform_blink
        textbutton "¡DISPARAR!" action Jump("exito_disparo_escalera") style "button_panic"

# QTE 3: Izquierda arriba (2.0 segundos - Clímax de tensión)
screen qte_cerrar_escotilla():
    modal True
    timer 2.0 action Jump("game_over_ladder")
    
    vbox:
        xalign 0.2
        yalign 0.3
        spacing 15
        text "{font=fonts/HelpMe.ttf}{size=55}¡VIENE SUBIENDO!{/font}{/size}" color "#f00" at transform_blink
        textbutton "¡SELLAR ESCOTILLA!" action Jump("exito_cerrar_escotilla") style "button_panic"

label game_over_ladder:
    # Persecución terminada (muerte) — reactivar rollback
    $ config.rollback_enabled = True
    $ renpy.block_rollback()

    play sound slash
    play music curse
    scene black with flash
    
    "{cps=15}Demasiado lento.{/cps}"
    
    scene death_glx_1 with fade
    g "Te dije que eras torpe~"
    
    pause(1)
    "[nombre_jugador!c] sintió cómo unos dedos fríos y duros como el acero se cerraban alrededor de su tobillo."
    
    "Un tirón brutal lo arrancó de la escalera, lanzándolo contra el suelo con la fuerza de un animal salvaje jugando con su comida."
    
    "El aire escapó de sus pulmones con un gemido ahogado."
    
    play sound "sfx/bone_crack.mp3"
    
    "Antes de poder siquiera intentar levantarse, un peso inmenso le aplastó el pecho. Galaxia estaba sobre él, sus rodillas clavadas en sus brazos, inmovilizándolo con una facilidad humillante."
    
    "Ella acercó su rostro al de él, saboreando el terror en sus ojos, sus fauces abiertas goteando saliva sobre la mejilla de [nombre_jugador!c]."
    
    "No hubo lucha. Solo la aceptación paralizante de una presa que sabe que el depredador ya ha ganado."
    
    play sound "sfx/bite_crunch.mp3"
    scene black with fade
    pause(1)
    
    "{cps=15}[nombre_jugador!c] murió con la garganta destrozada, a centímetros de la salvación.{/cps}"
    
    scene gameover_screen with dissolve
    pause(2)
    menu:
        "Cargar partida":
            jump load_screen
        "Volver al menú principal":
            return
            


label cap_5:
    scene pasillo_abandonado
    show luz scared at centro_derecha
    show azura scared at right
    show nagi surprised at centro_izquierda
    show cutipye scared at left
    with fade
    stop music fadeout 2
    play music ambiental fadein 1.5

    l "¡RODRIGO! ¡RESPONDE!"

    "El grito de Luz se pierde en la oscuridad del agujero. El polvo tarda en asentarse."
    "Nagi y Cutipye acaban de arrastrarlas lejos del borde, a tirones, sin soltarles las muñecas. Luz y Azura todavía no recuperan el aliento. Ninguna piensa hacerlo."

    play sound "sfx/rocks_falling_echo.mp3"
    "Solo se escucha el eco lejano de piedras cayendo. Y luego... nada."
    "El último trozo tarda demasiado en llegar al fondo. Nadie quiere decirlo en voz alta."

    show nagi serio
    n "Mierda... El suelo estaba podrido."
    "Nagi mira el hueco con la mandíbula tensa, como quien mira un error propio."
    n "Y nosotros caminando encima como idiotas."

    show cutipye worried
    c "¿Se... se mató? ¿Cayó hasta el fondo?"
    "La voz de Cutipye sale pequeña. Demasiado pequeña para ella."

    l "¡No! ¡Él está bien! ¡Tiene que estar bien!"

    # -- El borde --
    show nagi angry
    "Luz se lanza hacia el borde. Las rodillas casi no la sostienen, pero avanza a rastras sobre las tablas rotas, buscando la orilla con los dedos. Nagi la sujeta del brazo."

    n "¡Atrás! Si te acercas, te vas con él. Toda esta estructura es inestable."
    l "¡Suéltame! ¡Está ahí abajo, Nagi! ¡Está solo!"
    n "¿¡Y de qué le sirves tú ahí abajo, con la espalda rota!?"

    "Nagi no la suelta. Con la mano libre ahueca la boca y se asoma lo mínimo, con el cuerpo echado hacia atrás."
    n "¡[apodo_jugador]! ¡Si me oyes, haz ruido! ¡Lo que sea, idiota!"

    pause 1.5
    "El agujero le devuelve su propia voz, más lenta y más grave. Nada más."

    show nagi worried
    n "...Vamos, ermitaño. Responde."
    "Nagi, que nunca habla bajo, lo dice casi sin voz."

    # -- La cuenta --
    show azura worried
    "Azura no discute. Se arrodilla junto a la orilla y recoge un trozo de yeso del tamaño de un puño."
    a "Voy a soltarlo. Cuenten conmigo."
    "Nadie pregunta para qué."
    "Lo deja caer. Cuentan."
    "Un segundo. Un segundo largo. Casi dos."
    play sound objfall volume 0.3
    "Y entonces, abajo, un golpe seco."

    a "Diez metros. Doce, como mucho."
    c "¿Eso es... bueno?"
    a "Es posible. Si cayó sobre escombros y no sobre concreto. Si se cubrió la cabeza. Si..."
    "No termina la lista. Su voz es firme. Sus manos, no."
    a "Es posible. Eso es todo lo que sé."

    l "Entonces está vivo."
    a "Luz..."
    l "Está vivo."

    "Cutipye abre la boca. Busca el chiste de siempre, el que tiene a mano para estos momentos. No aparece."
    c "Azura... dime que es de los que caen de pie."
    a "Es de los que se levantan."
    "Lo dice rápido, sin pensarlo. Quizá por eso suena a verdad."

    # -- Lo que hay abajo --
    show cutipye serious
    c "Luz, yo quiero bajar tanto como tú. Pero no sabemos qué hay ahí abajo."
    c "Lo que nos persiguió arriba... si hay más de eso, o algo peor..."

    show luz serious
    l "Hay más."
    l "Rodrigo y yo bajamos antes. Hay un laboratorio, Cuty. Y hay cosas dentro."
    n "¿Cosas?"
    l "Vi cómo se llevaban a un hombre. Lo tenía agarrado yo. Estaba vivo, Nagi, y en un segundo ya no."
    "Luz se mira las manos. Todavía no ha podido limpiárselas del todo."
    l "Y la de la ventana, la de antes... Se llama Galaxia."
    n "¿Qué ventana? ¿Quién es Galaxia?"
    l "No hay tiempo para explicarlo, Nagi. Después. Te lo cuento todo después."

    "Luz se lleva la mano a la cintura. Vacía."
    show luz scared
    l "La pistola."
    n "¿Qué pistola?"
    l "Encontramos una arriba. La tenía yo, y cuando me aferré al borde..."
    "No termina. Mira el agujero."
    l "Está ahí abajo. Con él."
    a "Entonces tiene con qué defenderse."
    "Luz saca del bolsillo la caja de balas. La sostiene un segundo, inútil, y la aprieta contra el pecho."
    l "Con lo que le quede en el cargador. Las balas las tengo yo."

    # -- El suelo cede --
    stop ambient
    play sound crack
    "Un crujido largo, más cerca que los anteriores. Un tramo de tablas junto al agujero se hunde un palmo."

    show nagi shocked
    n "¡Atrás! ¡Todos atrás, ahora!"

    play sound objfall volume 0.6
    "Retroceden de espaldas, tropezando entre sí. El borde del agujero avanza medio metro hacia ellos... y se detiene."
    "Nadie respira."

    # -- Algo abajo --
    pause 1.0
    play sound "sfx/claw_drag_concrete.mp3" volume 0.3
    "Y entonces, desde el fondo, llega algo."
    "Un rasguño largo. Uñas contra hormigón, tan lejos que podría ser una tubería."

    pause 1.0
    play sound glx_laugh volume 0.25
    "Y después, apenas un hilo que sube por el hueco como humo: una risita baja, gutural."

    show azura shocked
    show luz scared
    show cutipye scared
    "Azura se cubre la boca con ambas manos. Luz se queda sin color."

    n "¿Eso fue... una risa?"
    c "Dime que fue el eco. Por favor, dime que fue el eco."
    a "No fue el eco."
    l "Es ella."
    "No lo dice como pregunta. Lo dice como quien ve cerrarse una puerta."

    "Nadie vuelve a gritar su nombre. Todos entienden, sin decirlo, que ahora cada grito es una dirección."
    "Y esa impotencia duele más que el silencio de abajo."

    # -- Moverse --
    show luz determined
    l "Buscamos las escaleras. El sótano. Tiene que haber un acceso de servicio."
    l "No me voy de aquí sin él."

    show azura worried
    a "La cocina. Un lugar así no subía la comida ni el carbón por la escalera principal. Tiene que haber un montacargas o una escalera de servicio, y casi siempre quedan juntos."
    a "Hacia el fondo del ala, creo. Si nos damos prisa..."

    show cutipye determined
    c "Entonces nos damos prisa. Pero juntos. Esta vez, nadie se separa."
    "Nadie la contradice."

    show nagi serio
    n "Bien. Muévanse. Quedarnos aquí llorando no lo va a sacar."

    "Nagi toma la delantera con el bate en alto. Luz es la última en apartarse. Desde el borde, el agujero sigue mirándola."

    # -- Dejando el agujero --
    scene pasillo_servicio with fade
    play music melody fadein 2.0
    play ambient flies loop volume 0.15 fadein 3.0
    play sound walk loop volume 0.4

    show nagi serio at centro_izquierda
    show cutipye worried at left
    show luz worry at centro_derecha
    show azura worried at right
    with dissolve

    "El grupo avanza hacia el área de servicio. Dejan atrás el agujero, pero no lo que salió de él: la risita sigue colgada en el aire, aunque ya nadie la oiga."
    "Avanzan en fila, pegados a la pared. Nagi al frente, con el bate en alto. Cutipye, con dos dedos enganchados en la correa de la mochila de Azura, como quien se agarra a una barandilla. Y al final Luz, que cada tres pasos gira la cabeza hacia atrás, hacia un hueco que ya ni siquiera se ve."
    "«Nadie se separa». Cutipye lo dijo como una regla. Ahora la cumplen con el cuerpo."

    # -- El pasillo --
    "El ala de servicio no se parece al resto del edificio."
    "Arriba, el abandono era seco: polvo, pintura descascarada, madera que se quebraba como galleta. Aquí es húmedo, y la humedad lo ha ido desmontando todo desde dentro."
    "El papel tapiz cuelga en tiras largas e hinchadas, como piel que se despega después de una quemadura. Debajo, el yeso está negro de moho: manchas que trepan desde el zócalo en abanico, con un borde verde y aterciopelado donde roza la luz."
    "Las baldosas están levantadas, y en las hendiduras duerme agua quieta, color té, que devuelve el haz de las linternas con un brillo aceitoso. Cada paso la rompe. Cada paso suena a chapoteo."
    "Gotea. En todas partes gotea, y ningún goteo coincide con otro: un reloj de mil manecillas que no se ponen de acuerdo sobre la hora."

    "En el bolsillo de Luz, la caja de balas traquetea a cada paso. Un tableteo diminuto y seco que, en ese silencio, suena a campana."
    "Nagi se vuelve sin detenerse y le clava la mirada. Luz cierra el puño sobre el bolsillo y aprieta la caja contra el muslo hasta que calla."
    "Sus manos todavía huelen a hierro. Se las frota contra el pantalón, una y otra vez. Ya no queda nada que limpiar. El olor sí."

    # -- El olor --
    "Primero, solo humedad: moho, cañería vieja, tierra mojada."
    "Después, algo más. Tan leve que al principio nadie lo nombra. Como una fruta olvidada en el fondo de una bolsa."
    "Dulce."

    "Mientras más avanzan, más se espesa. Ya no es fruta. Es caramelo quemado, azúcar fermentada, miel dejada al sol demasiados días."
    "Y debajo, sosteniéndola, como el hueso bajo la carne, algo que no es dulce en absoluto: carne que lleva mucho tiempo dejando de ser carne."
    "El aire se vuelve tibio. Tibio de verdad, como el aliento de alguien dormido. Se pega a la garganta."
    "Luz traga saliva y lo nota en la lengua: azúcar y cobre."

    show cutipye disgust with dissolve
    c "Ugh... ¿Qué es esa peste?"
    "Cutipye se tapa la nariz con la manga. Le sale una voz nasal, de resfriado."

    n "(sin volverse) Respira por la boca."
    c "Peor. Así la estoy comiendo."
    "Lo dice plano, sin el filo de siempre. El chiste sale, pero no suena a chiste: suena a alguien comprobando que todavía puede hacer uno."
    "Nadie ríe. Cutipye tampoco lo esperaba."

    "La primera mosca se posa en el hombro de Azura, perezosa, y ella la sacude con un respingo."
    "La segunda ya está en la pared. Después, decenas: negras, gordas, quietas sobre el moho, como si el moho hubiera echado ojos."
    "Cuando el haz de una linterna las roza, se levantan todas a la vez, y por un segundo el pasillo entero parece respirar."

    "En la juntura entre el techo y la pared aparece un hilo ámbar, translúcido. Cera: cera de vela derramada que se endureció a mitad de goteo."
    "Al principio es un solo hilo. Luego una vena que baja por el marco de una puerta. Luego láminas gruesas que cubren el zócalo y se arrastran hacia el suelo."
    "Las suelas dejan de chapotear. Se pegan. Cada paso se despega con un chasquido húmedo, como cinta arrancada de la piel."

    # -- El zumbido --
    "Bajo el chapoteo y los goteos, empieza a oírse algo más."
    "Primero ni siquiera se oye: se siente. Una vibración baja en las costillas, en los dientes, en la linterna que Azura aprieta con las dos manos."
    "En los charcos, el agua tiembla sin que nadie la toque, dibujando anillos que nacen en el centro y se pierden en los bordes."

    a "Suena como... ¿electricidad?"
    "Lo dice con algo parecido a la esperanza. Un ala con corriente es un ala con luces, y las luces son salidas."

    "No es electricidad. Es un zumbido orgánico."
    "Grave, húmedo, hecho de miles de pequeños latidos superpuestos. Cuando la luz roza la cera de las paredes, la cera tiembla."
    $ renpy.save("1-1", "Encuentro 5")

    show luz determined
    "Luz acelera sin darse cuenta. Se abre paso entre Azura y la pared, luego entre Cutipye y la pared. Nagi la sujeta del hombro sin mirarla."
    n "Detrás de mí. Aunque tengas prisa. Sobre todo si tienes prisa."
    l "Cada minuto que estamos aquí..."
    n "Lo sé."
    "Y sin decir nada más, Nagi acelera él también."

    # -- La cocina --
    "Al final del pasillo, dos puertas vaivén con ojos de buey tan sucios que solo dejan pasar un resplandor ámbar."
    "Nagi apoya la palma en una. Está tibia. Tibia como una frente con fiebre."

    stop sound fadeout 1.0
    play sound door_open volume 0.6
    "Empuja. La hoja cede con un tirón húmedo: hilos de cera se estiran entre la puerta y el marco, como saliva, y se rompen uno a uno."

    scene cocina_infestada with dissolve
    play ambient flies loop volume 0.7 fadein 1.0

    "El calor los golpea primero. Una bocanada espesa, cargada de azúcar, que se pega a la cara como una mano abierta."
    "Aquí el olor ya no se huele: se bebe. Es un caramelo que lleva meses pudriéndose por dentro."
    "Cutipye se dobla, con la manga contra la boca, conteniendo una arcada."
    "Dan dos pasos hacia el interior. Y se detienen en seco."

    "Lo que alguna vez fue una cocina industrial ahora es un nido."

    "Las linternas lo recorren a trozos, y cada trozo es peor que el anterior."
    "Hornillas del largo de un autobús. Campanas extractoras. Ollas del tamaño de barriles, colgadas de sus ganchos y selladas por una costra amarilla."
    "En el techo, la cera no gotea: construye. Capas, celdas, un patrón de hexágonos torcidos que se repite hasta perderse en la oscuridad."
    play sound thud volume 0.2
    "De las campanas cuelgan estalactitas ámbar con una gota gorda temblando en cada punta. Cuando una cae, golpea la mesa de abajo con un plop mucho más pesado de lo que debería."
    "El suelo es una piel brillante y tibia que se pega a las botas. En las esquinas, moscas muertas amontonadas como arena. Cuando Nagi da un paso, crujen bajo su suela como cereal."

    "Las mesas de metal, alineadas en filas como en una morgue, están cubiertas de una sustancia cerosa y amarillenta."
    "Y sobre ella... cosas."

    c "Dios... son..."

    "Larvas. Del tamaño de perros grandes. Pálidas, húmedas, retorciéndose lentamente."
    "Se mueven todas al mismo ritmo, como una sola ola que respira. Su piel es tan fina que la luz de las linternas la atraviesa, y debajo se ve algo oscuro y latiendo."
    "Un chasquido pegajoso cada vez que una se despega de la cera para volver a pegarse."
    "Pero tienen rasgos. Pequeñas manos atrofiadas. Rostros humanos a medio formar que boquean en silencio."
    "Una abre la boca hacia la linterna de Azura, como una cría hacia la luz. No emite ningún sonido."

    "Luz sabe de dónde vienen estas cosas. Lo leyó en la bitácora. Saberlo no ayuda."
    l "No miren. Solo... busquemos la salida al fondo."

    "Al otro lado de la sala, entre las hornillas y una hilera de cámaras frías con las puertas entreabiertas, hay una puerta de metal pesada. La cera se acumula en su marco como una cicatriz."
    "Azura la ilumina un segundo. Un letrero de esmalte descascarado: «Servicio». Tenía razón, y no sirve de nada tenerla: entre ellos y la puerta hay doce mesas."

    # -- La nodriza --
    play sound "sfx/wasp_wings.mp3" fadein 1.0

    "Avanzan. Y entonces el zumbido, que llevaba rato siendo parte del aire, cambia de tono."
    "Se separa. Se concentra. Se vuelve uno solo."
    "Un aleteo pesado desciende del techo."

    scene avispa_guardia with dissolve
    "Una criatura desciende. Mitad hombre, mitad insecto. Sus piernas son largas y quitinosas, su abdomen palpita con un aguijón rezumante."
    "El aire se desplaza antes que ella: una corriente tibia, todavía más dulce. Cuatro alas vidriosas siguen vibrando incluso después de plegarse, y esa vibración se siente en los dientes."

    "El grupo retrocede, preparando sus armas."

    "Pero la criatura no ataca."

    "Se posa sobre una de las larvas humanoides. Acaricia su cabeza deforme con sus antenas. La limpia, con una delicadeza que eriza la piel."
    "Una gota de cera tibia resbala por la frente de la larva, y la nodriza la alisa con una pata, como quien arropa a un niño."

    a "¿La está... protegiendo?"
    "Nagi susurra sin mover los labios, con los nudillos blancos sobre el bate."
    n "Son nodrizas. Mientras no toquemos a las crías, quizás no nos..."

    stop music
    stop sound
    play sound gunshot volume 0.6 # Sonido lejano, con eco
    with shake
    queue sound gunshot volume 0.3
    queue sound gunshot volume 0.1
    pause 1
    "{i}¡BAAANG!{/i}"

    "Llega desde muy abajo, deformado por el hormigón y las cañerías. Pero Luz lo reconoce: lo tuvo en las manos."
    l "(en un hilo) La pistola... Está vivo. Está..."

    #show avispa_guardia alert with vpunch
    play ambient larvcry volume 2.5
    pause 1
    "Las larvas comienzan a chillar. Un sonido agudo, como llanto de bebé distorsionado."
    "Todas las bocas que llevaban rato abriéndose en silencio, de pronto, tienen voz. El chillido se contagia de mesa en mesa, cada vez más agudo, hasta ser un solo sonido que entra por los oídos y se instala detrás de los ojos."
    
    play music chase
    "La Avispa Nodriza se gira hacia el grupo. Sus ojos multifacéticos se tornan rojos de furia."
    "El instinto maternal se convierte en instinto asesino."
    
    n "¡CORRAN! ¡A LA PUERTA!"
    
    scene cocina_puerta with vpunch
    
    "Nagi y Cutipye se lanzan contra la puerta pesada del fondo."
    
    n "¡Ayudenme! ¡Está atascada con esa cera!"
    
    scene cocina_puerta2 with vpunch
    "Luz y Azura empujan."
    
    play sound "sfx/wasp_screech_attack.mp3"
    "Detrás de ellos, tres avispas más descienden, aguijones listos."
    
    play sound door_slam
    "Logran abrirla, cruzan el umbral y Nagi intenta cerrarla de golpe."
    
    n "¡CIERREN! ¡CIERREN!"
    
    "La puerta se cierra... casi."
    
    stop ambient fadeout 0.3
    play sound "sfx/metal_crunch.mp3"
    with shake
    
    "Un brazo quitinoso y una cabeza zumbante se meten en la brecha."
    "Una de las avispas lograba entrar antes del bloqueo."
    
    n "¡Mierda! ¡Se metió una!"
    
    scene pasillo_servicio_lucha
    play sound "sfx/wasp_wings.mp3" fadein 1.0
    show avispa_zangano at center with moveinright
    
    "El Zángano se libera, aleteando furiosamente en el espacio cerrado del pasillo."
    "Bloquea el camino hacia el sótano."
    "Va a atacar a Azura."
    
    l "¡Azura, abajo!"    
    call screen qte_wasp_1

label exito_qte_1:
    # Resultado visual Fase 1
    play sound "sfx/throw_object.mp3"
    show cutipye throw # "¡CLANG!"
    play sound "sfx/metal_hit_chitin.mp3"
    with vpunch
    show avispa_zangano at right with moveinleft
    "El extintor golpea la cabeza del zángano. La criatura se sacude, aturdida por un segundo."
    
    # --- FASE 2: NAGI (GOLPEAR) ---
    show nagi angry at right
    n "¡Ahora verás!"
    
    call screen qte_wasp_2

label exito_qte_2:
    # Resultado visual Fase 2
    play sound "sfx/bat_swing.mp3"
    "Nagi carga el bate con todas sus fuerzas."
    
    play sound "sfx/bat_hit_hard.mp3"
    with shake
    show avispa_zangano at left with moveinright
    "¡CRACK!"
    "El golpe destroza el ala derecha. La avispa chilla y cae al suelo, expuesta."
    
    # --- FASE 3: LUZ (REMATAR) ---
    show luz angry at left
    l "¡MUERE!"
    
    call screen qte_wasp_3

label combate_ganado:
    
    play sound "sfx/metal_swing.mp3"
    "Luz levanta la barra por encima de su cabeza, temblando -no de miedo, sino de adrenalina pura."

    with hpunch
    play sound "sfx/metal_crush.mp3"
    "¡CLANG!"

    "El metal impacta contra el tórax abierto del zángano."

    with vpunch
    play sound "sfx/splat.mp3"
    "El exoesqueleto cede con un crujido viscoso."
    "Icor verde salpica el suelo y parte de la pared."
    "La criatura se retuerce violentamente."

    play sound "sfx/metal_crush.mp3"
    with hpunch
    "Luz golpea otra vez."

    l "¡MUERE! ¡MUERE!"

    "El tercer impacto atraviesa lo que queda del caparazón."

    scene avispa_dead with dissolve
    "La criatura cae, convulsionando una última vez antes de quedar inmóvil."
    stop ambient fadeout 2.0
    stop music fadeout 2.0
    
    "El silencio vuelve al pasillo, roto solo por los jadeos descompasados del grupo."
    
    c "¿La... matamos?"
    n "Si..."
    
    "Nagi observa a Luz."
    "Ella sigue sosteniendo la barra."
    "No la suelta."
    pause 1
    "Luego, cuando la adrenalina comienza a bajar, Azura observa a su alrededor, anunciando con voz temblorosa:"

    a "Miren... ahí."
    
    scene cuarto_maquinas_puerta with dissolve
    "Al final del pasillo, una puerta de acero. La válvula está girada desde dentro."
    "Hay abolladuras recientes en el metal. Marcas de garras por fuera."
    
    l "¡[nombre_jugador!c]!"
    
    play sound "sfx/valve_turn.mp3"
    "Luz corre y gira la válvula con fuerza. La puerta se abre con un chirrido."
    
    scene bg_cuarto_maquinas
    play music main_menu fadein 2.0
    
    "El cuarto está oscuro, iluminado solo por las luces de emergencia."
    "En el rincón, una figura sentada contra la pared."
    
    show rodrigo shock_state at center, shaking with dissolve
    "Está cubierto de polvo y sangre. Tiene la mirada perdida en la pistola vacía que sostiene en su regazo."
    "Tiembla ligeramente."
    
    l "[apodo_jugador]..."
    
    "Él levanta la vista lentamente. Tarda un segundo en reconocerla."
    
    r "Luz..."
    r "Ella... ella no muere..."
    
    scene luz_hug_rodrigo with dissolve
    "Luz se lanza a abrazarlo, ignorando la sangre. El resto del grupo se queda en la puerta, viendo la escena."
    
    n "Está vivo. Ese bastardo duro de matar está vivo."
    pause 1.5
    
    call chapter_complete("Capítulo 5")
    jump cap_6

label game_over_wasp:
    scene pasillo_servicio_lucha
    play sound slash
    show avispa_zangano attack with zoomin
    play music curse
    
    "Fueron una fracción de segundo demasiado lentos."
    
    play sound "sfx/body_slam_squish.mp3"
    show avispa_zangano attack at truecenter with vpunch
    "El zumbido se convirtió en un rugido ensordecedor cuando el zángano ignoró a Nagi y a Luz, abalanzándose directamente sobre Azura con todo su peso."
    
    scene death_wasp with shake
    play sound slash
    a "¡¡AAAGH!!"
    
    n "¡SUÉLTALA, MIERDA!"
    
    "Nagi golpeó el caparazón con el bate con todas sus fuerzas. Luz disparó al aire, gritando."
    
    play sound "sfx/metal_hit_chitin_hard.mp3"
    with shake # Sacudida general por el caos
    
    "No sirvió de nada. La bestia estaba ciega de furia, en un estado de frenesí defensivo."
    
    "Sus patas quitinosas y dentadas se aferraron a los hombros de Azura como ganchos de carnicero, desgarrando la ropa y la piel para ganar palanca, manteniéndola inmovilizada contra el suelo."
    
    #play sound "sfx/wet_stab_repeated.mp3" # Sonido húmedo y repetitivo
    
    play sound slash
    with vpunch 
    "El abdomen de la criatura se arqueó violentamente."
    
    with vpunch
    play sound slash
    "El aguijón descendió. Una vez."
    
    with vpunch
    play sound slash
    "Dos veces."
    
    with vpunch
    play sound slash
    "Tres veces."
    
    "No fue una picadura limpia. Fue una carnicería."
    
    "El enorme aguijón entraba y salía del pecho de Azura con un sonido húmedo y repugnante, inyectando litros de veneno corrosivo mientras ella se convulsionaba bajo el peso del insecto."
    
    l "¡¡AZURA!! ¡¡NO!!"
    
    "Los gritos de Azura se ahogaron rápidamente en un gorgoteo sangriento."
    
    "Incluso cuando dejó de moverse, la avispa no se detuvo. Seguía atacando el cadáver, movida por puro instinto asesino, defendiendo su colmena de la intrusa."
    pause 2
    
    scene gameover_screen with dissolve
    pause(2)
    menu:
        "Cargar partida":
            jump load_screen
        "Volver al menú principal":
            return

screen qte_wasp_1():
    modal True
    # 3 segundos para reaccionar
    timer 3.0 action Jump("game_over_wasp") 
    
    vbox:
        xalign 0.2 # Botón a la izquierda (Cutipye)
        yalign 0.5
        spacing 20
        
        text "¡CUTIPYE! ¡DISTRÁELA!" color "#fff" outlines [(2, "#000", 0, 0)] at transform_blink
        
        textbutton "LANZAR EXTINTOR" style "button_panic" action Jump("exito_qte_1") text_size 40 text_color "#fff"

screen qte_wasp_2():
    modal True
    # 2.5 segundos (Más rápido)
    timer 2.5 action Jump("game_over_wasp") 
    
    vbox:
        xalign 0.8 # Botón a la derecha (Nagi)
        yalign 0.5
        spacing 20
        
        text "¡NAGI! ¡GOLPEA!" color "#fff" outlines [(2, "#000", 0, 0)] at transform_blink
        
        textbutton "BATEAR" style "button_panic" action Jump("exito_qte_2") text_size 50 text_color "#fff"

screen qte_wasp_3():
    modal True
    # 2 segundos (Muy rápido, decisión final)
    timer 2.0 action Jump("game_over_wasp") 
    
    vbox:
        xalign 0.5 # Botón al centro (Luz)
        yalign 0.5
        spacing 20
        
        text "¡LUZ! ¡REMATA!" color "#f00" outlines [(2, "#000", 0, 0)] size 50 at transform_blink
        
        textbutton "¡GOLPEA!" style "button_panic" action Jump("combate_ganado") text_size 70 text_color "#fff" text_bold True

label qte_wasp_4:
    # Resultado visual Fase 2
    play sound "sfx/bat_swing.mp3"
    "Nagi carga el bate con todas sus fuerzas."
    
    play sound "sfx/bat_hit_hard.mp3"
    with shake
    "¡CRACK!"
    "El golpe destroza el ala derecha. La avispa chilla y cae al suelo, expuesta."
    
    # --- FASE 3: LUZ (REMATAR) ---
    show luz angry at center
    "Entre los escombros, Luz agarra una barra metálica desprendida de una banca rota."

    l "¡Hazte a un lado!"
    
    call screen combate_ganado