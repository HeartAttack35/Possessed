# NOTA: Para activar/desactivar el contador HUD desde la consola (Shift+O):
# - Escribe: mostrar_hud = True  (para mostrarlo)
# - Escribe: mostrar_hud = False (para ocultarlo)

label start:
    show screen hud_stats

################
#    ACTO 1
################

    scene bosque_tarde with fade
    play music forest fadein 2

    "Una fría tarde de otoño, el grupo de amigos se encontraba caminando en medio del bosque, kilómetros más allá de la autopista."
    "Los árboles a su alrededor danzaban al suave ritmo del viento. A medida que se abrían paso a través del sendero, la conversación inevitablemente retornó al motivo de aquella junta."

    show rodrigo neutral at center with dissolve
    "Rodrigo ajustó la navaja oculta en su cinturón. Esperaba no tener que usarla, pero la paranoia era un viejo hábito difícil de romper."
    r "¿Están seguras de que quieren hacer esto...? Hay formas menos estúpidas de ser buscados por la policía..."

    show cutipye smile at right
    show rodrigo at left
    with moveinright
    c "Vamos, Rodri, no seas tan agüafiestas. Además, solo está a unos diez minutos de aquí."

    menu:
        "Respondes con sarcasmo":
            r "Tch, estoy seguro de que solo encontraremos insectos y poco más..."
            r "Solo es un orfanato abandonado. ¿Qué es tan especial sobre este lugar?"
            $ afinidad_cutipye += 1
            
            show azura smile with dissolve
            a "No es solamente un orfanato abandonado, Rodri."

        "Aceptas de mala gana":
            r "Está bien... Pero si nos arrestan, no pienso correr."
            $ afinidad_cutipye += 2
            
            show azura smile with dissolve
            a "No creo que debas preocuparte por eso, el lugar fue desalojado hace mucho tiempo."
            a "Es más."

        "No dices nada":
            "Rodrigo simplemente suspira, resignado."
            pause 1
            show azura smile with dissolve
            a "Si sirve de algo..."
    
    a "Hay rumores de que en la época de la dictadura fue usado como centro de tortura."

    menu:
        "Te burlas del rumor":
            r "Vaya giro de guión. Qué conveniente."
            r "¿También hay una niña de pelo largo que aparece en los espejos o eso viene en el DLC de pago?"
            $ afinidad_azura -= 1

        "Te muestras incómodo":
            r "...Ok, eso sí fue un poco más turbio de lo que esperaba."
            $ afinidad_azura += 1
            $ estado_mental += 1

        "Guardas silencio":
            "Rodrigo se limitó a fruncir el ceño sin responder, su mueca una clara muestra de desapruebo."

    show azura at centro_derecha with moveinright
    show nagi smug with dissolve
    
    n "¿Acaso vas a acobardarte ahora que todos estamos de acuerdo?"

    show luz smile at left
    show rodrigo at centro_izquierda
    with moveinleft
    "Antes de que Rodrigo pudiera responder, la suave y cálida mano de la pelirroja rodeó la suya con gentileza..."
    "Su celeste mirada acompañada por una leve sonrisa, aquella mueca siendo suficiente para calmar el impulso del castaño."

    show rodrigo soft with dissolve
    r "Y, en todo caso, ¿cómo tienen pensado entrar?"

    hide rodrigo
    hide luz
    hide nagi
    hide azura
    hide cutipye
    with dissolve
    "Como respuesta, Nagi simplemente extendió su sonrisa y se adelantó unos cuantos pasos..."

    scene orfanato_exterior1 at center with fade
    play sound walk
    "Al cabo de unos diez minutos, el grupo fue capaz de entrar al orfanato a través de una brecha en la enorme cerca de acero."
    
    scene orfanato_exterior2 with fade
    show rodrigo neutral
    stop sound
    r "Bien, llegamos... Entonces tomamos unas cuantas fotos y nos vamos."

    show nagi smile at right with dissolve
    n "No creas que te escaparás tan fácil, cobarde."

    "Acto seguido, Nagi se quitó la mochila para sujetar su apenas escondido bate de béisbol."
    
    n  "De aquí no te irás sin acompañarnos."
    show nagi smug
    n "Y nos quedaremos un buen rato."
    
    hide rodrigo
    hide nagi
    pause 1

    play sound break_glass volume 0.7
    scene orfanato_exterior2 at shake
    "Nagi alzó su bate y lo estrelló contra una ventanilla, destrozando el vidrio antes de bajar."

    stop music fadeout 1
    play sound "sfx/land.mp3"
    queue sound "sfx/land.mp3"
    queue sound "sfx/land.mp3"
    queue sound "sfx/land.mp3"
    
    "Uno a uno, saltaron al interior. El sonido de sus botas contra el suelo resonó con un eco seco."
    "Una vez bajaron todos, Rodrigo se mantuvo de pie observando a sus amigos, quienes comenzaban a explorar lo que parecía ser una lavandería."
    
    pause 0.8
    r "Tch, hasta acá llega el olor a muerto..."

    scene lavanderia_abandonada with fade
    play sound land
    show rodrigo neutral

    "El grupo comenzó a explorar aquel lugar, encendiendo sus linternas."

    scene pasillo_oscuro with dissolve
    play sound walk
    "Rodrigo, por su lado, se adentró en una de las habitaciones en el pasillo..."
    "En el suelo, algunas muñecas antiguas y deshechas. A pesar de parecer aleatorias, algo no cuadraba."

    show rodrigo neutral
    r "¿...?"

    play music melody
    play sound "pasos_susurro.ogg"
    "Rodrigo comenzó a notar un sonido leve y sutil, como pasos pequeños..."

    show rodrigo molesto
    r "Chicas, esto no es gracioso..."

    pause(1.5)
    show rodrigo neutral
    r "¿Chicas?"
    pause(1.5)
    
    "Al no recibir respuesta, Rodrigo decidió dar marcha atrás, esta vez enfocado en encontrar a alguna de sus amigas, quien sea."
    
    scene pasillo_oscuro
    play sound run
    "Puerta tras puerta, Rodrigo buscó a sus amigas. Mientras más merodeaba, menos opciones tenía."
    
    "Su una vez lento y cuidadoso caminar se volvió un ligero trote."
    
    scene puerta_oxidada
    "Las opciones se acababan en aquel primer pasillo, hasta que el castaño trató de abrir un de las puertas."
    "Pero antes de poder intentarlo nuevamente..."

    stop music
    play sound scream1
    scene puerta_oxidada at truecenter with moveinbottom
    pause 1
    r "¿¡Luz!?"

    "Acto seguido, Rodrigo esprintó hacia la puerta, la cual debido a lo oxidada que estaba, no cooperaba con su frágil corazón."
    play sound door_slam
    with vpunch
    "Golpeó una vez."
    play sound door_slam
    with vpunch
    "Dos veces."
    play sound door_break volume 0.8
    with hpunch
    "Al tercer embate, la cerradura cedió con un chasquido metálico."
    
    scene foreboding_1 with fade
    show luz scared at left
    show rodrigo alert at right
    pause 1.3
    
    "Luz estaba pálida, sus pupilas contraídas en dos puntos negros que temblaban al compás de su respiración entrecortada."

    "El castaño, pese al miedo, estaba decidido a ver lo que Luz había encontrado."
    "Se giró hacia la puerta frente a ella, abriéndola lentamente."
    
    play sound door_open
    scene black
    pause(0.5)
    "Rodrigo entra a la habitación, pero la falta de iluminación le impide ver..."
    "Lenta y torpemente, desliza su mano por el contorno de la puerta para buscar el interruptor..."
    "...y lo que ve lo deja paralizado."
    
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
    "Acto seguido, subieron la vista."

    scene scene_spdr with dissolve
    pause 0.7
    play music chase fadein 0.5
    
    "En el techo, desafiando la gravedad, algo que alguna vez fue humano los observaba."
    "Rodrigo dió un paso atrás, manteniendo su arma en alto mientras contempla sus opciones."
    
    menu:
        "Intentas atacar a la criatura":
            r "¡Atrás!" 
            "Rodrigo sacudió su daga con más fuerza, avanzando un paso desafiante..."
            $ estado_mental += 2

            l "¡Rodri, no!"

            menu:
                "Huyes con Luz":
                    "El grito de Luz lo trajo a la realidad. No podía ganar esto."
                    jump escapar_araña

                "Insistes en atacar":
                    "Contrario a su sentido común, Rodrigo se decidió a atacar."
                    r "¡Tú vete! ¡Yo te daré tiempo!"
                    "Rodrigo arremetió contra la criatura con todas sus fuerzas."
                    jump game_over_spdr

        "Sigues retrocediendo, sin atacar":
            r "...Esto no vale la pena."
            "Rodrigo mantuvo su daga en alto, pero dio pasos hacia atrás sin atacar."
            $ estado_mental += 1
            jump escapar_araña

        "Sales corriendo sin mirar atrás":
            "El miedo pudo más. Rodrigo giró y corrió sin pensarlo."
            $ estado_mental += 3
            jump escapar_araña
        
label game_over_spdr:
    stop sound
    scene black with fade
    
    "Pero..."
    
    play music curse
    scene spdr1 with fade
    pause(1)
    "La criatura fue más rápida, más fuerte, más letal de lo que Rodrigo jamás pudo anticipar."
    "Su acto de valentía solo resultó en una muerte sin gloria."
    pause(1)
    "{cps=15}Rodrigo murió como un idiota...{/cps}"

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
    "Rodrigo y Luz corrieron por los pasillos sin mirar atrás."
    "El pasillo se convertía en un túnel borroso mientras sus pulmones ardían."

    scene escape_1
    show rodrigo scared at right:
        linear 0.5 xalign 0.4
        linear 0.5 xalign 0.3
        repeat

    show luz scared at left:
        linear 0.5 xalign 0.6
        linear 0.5 xalign 0.7
        repeat
    
    r "¿¡Donde están las demás!?"
    
    l "¡No lo se! ¡Nos separamos y las perdí de vista!"
    
    pause 1.0
    stop music fadeout 2.0
    
    "Rodrigo y Luz siguieron corriendo durante un rato, hasta que finalmente encontraron un lugar que parecía ser seguro."
    
    scene sala_espera_abandonada with dissolve
    play music "ambiente_tenso.ogg" fadein 2.0
    stop sound fadeout 1.5

    "Ambos se sentaron en unas viejas sillas de madera, tratando de recuperar el aliento."

    show luz scared at left
    show rodrigo nervioso at right
    with dissolve
    r "Oh mierda, oh mierda, oh mierda..."
    r "Sabía que era una pésima idea..."
    
    "Luz se sentó en el suelo, abrazando sus piernas con la mirada perdida."
    
    show rodrigo serio
    "Rodrigo la observó en silencio. Sabía que no podían quedarse ahí para siempre, pero ella necesitaba algo..."

    menu:
        "Reconfortas a Luz":
            r "Hey... vamos a salir de esta, cariño."
            pause 1
            l "¿Me lo prometes...?"
            
            "Al notar que Luz estaba incluso más afligida que el mismo, no tuvo más remedio que responder sincera y afectivamente."
            show rodrigo soft
            r "Con mi vida..."
            "Rodrigo se sentó junto a ella, apoyando una mano en su hombro. Luz no respondió al principio, pero su respiración se volvió más lenta."
            "Por un momento, el silencio dejó de ser tan pesado."
            $ afinidad_luz += 2

        "Piensas en opciones":
            r "Tenemos que movernos... Debe haber una salida."
            "Rodrigo se quedó de pie, analizando el entorno, forzándose a no pensar en el miedo. Cada minuto que pasaba ahí era un riesgo."
            
            r "Enfoquémonos en encontrar a las demás, ¿Si?"
            "Luz solo asintió."
            $ estado_mental -= 1
    
    "El silencio reinaba en aquella sala de espera, interrumpido únicamente por el sonido entrecortado de la respiración de ambos jóvenes."
    pause(1.0)
    "El tiempo parecía haberse detenido..."
    
    pause(0.5)
    play sound wood_creak volume 0.7
    show rodrigo serio at right
    show luz worry at left
    pause(0.5)
    "Hasta que un leve crujido de madera, proveniente del techo, los obligó a intercambiar miradas."

    r "No puede ser... ¿Otra vez?"
    l "Rodri... Tenemos que buscar a los demás..."

    "Él asintió con desgano, poniéndose de pie primero, ayudando a Luz segundos después."
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

    "Rodrigo se acercó con rapidez, reconociendo los pines personalizados en la tela negra."

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

    scene sotano_inicial with fade
    play sound wood_creak loop volume 0.5
    "Los escalones crujían bajo sus pies con cada paso que daban. Una humedad densa impregnaba el aire; y el frío del sótano era diferente: no era solo temperatura... era abandono."

    show rodrigo linterna at left
    show luz worry at right
    with dissolve

    "La linterna de Rodrigo iluminaba paredes de concreto agrietado, cables expuestos, y manchas que no sabían si eran óxido o sangre vieja."

    stop sound fadeout 1
    l "¿Qué es este lugar...? No parece parte del orfanato."
    r "Un laboratorio... O eso parece."

    scene pasillo_lab with dissolve
    play sound walk
    window hide
    scene pasillo_lab with flash
    pause 0.1
    scene pasillo_lab with flash
    window show
    show rodrigo linterna at left
    show luz neutral at right
    
    "Frente a ellos, un pasillo estrecho con varias salas numeradas."
    "Mientras se abrían paso, las miradas de Rodrigo y Luz se tornaban hacia sus alrededores, observando detenidamente las puertas metálicas."
    "A medida que avanzaban, lentamente se apegaban el uno al otro sin decir una sola palabra, instintivamente buscando la compañía del otro."

    r "Jamás pensé que terminaríamos perdidos en un lugar así..."
    show luz smile at right
    l "Siendo honesta... Si me hubieran dicho que terminaría en una casita de terror con el callado del salón... Tampoco me lo hubiera creído."
    $ afinidad_luz += 1
    
    scene sala_proyector with fade
    "Dentro, viejos escritorios, archivos húmedos, y en la esquina, un proyector cubierto de polvo. En las paredes, fotografías clínicas de niños con la piel... Incorrecta."
    "Sobre uno de los escritorios, una hoja de cuaderno intacto dentro de una caja metálica sellada, con el símbolo de una organización desconocida."

    show cuaderno_bitacora at center with dissolve
    play sound paper_flip
    play music story
    "Rodrigo abre el cuaderno."

    """
    {cps=20}{b}Bitácora del proyecto H-127: SUJETOS HUÉSPEDES{/b}{/cps}\n
    
    {cps=20}Responsable: Dr. Édgar L. Montané{/cps}\n
    
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
    
    hide cuaderno_bitacora with dissolve
    hide text
    
    show luz worry at right
    show rodrigo frustrado at left
    pause (2)
    
    r "..."
    
    pause (1)
    
    r "Usaron a los niños como ratas de laboratorio..."
    l "Entonces..."
    
    pause 1
    
    l "Esa cosa que vimos... ¿Era uno de ellos?"
    "Rodrigo cerró el cuaderno de golpe, con los nudillos blancos por la ira."
    
    stop music fadeout 3
    scene puerta_h127 with dissolve
    "Una puerta entreabierta. Un letrero corroído: {b}H-127{/b}."
    
    l "¿No es ese el número que decía en la bitácora?"
    "Rodrigo asintió."
    r "Vamos."

    play sound door_open
    scene sala_h127
    show sujeto_herido at right
    with fade

    "El olor golpeó primero. Agrio. Metálico. Animal."
    show luz surprised at left
    show rodrigo alert at centro_izquierda
    with moveinleft

    l "¿E... Está vivo?"
    
    "El hombre alzó una mano con esfuezo, sus dedos manchados de sangre temblaban sin control."
    sujeto "N-no... No deberían... Estar aquí..."
    
    r "¿Quién eres? ¿Quién te hizo esto?"
    
    "El hombre soltó una risa húmeda, ahogándose en su propia saliva."
    sujeto "Ella... Ella no es como los otros... Ella lo disfruta..."
    
    pause 1
    "La pareja intercambió una mirada, sus corazones acelerándose ante aquella declaración."
    
    l "¿Ella...? ¿Te refieres a una de las criaturas?"
    scene sala_h127_1
    show sujeto_herido at center
    with dissolve
    pause (1)
    sujeto "Galaxia... su nombre... es Galaxia..."
    pause (1)
    "Silencio."
    sujeto "Por favor... Huyan... Ella no quiere que se vayan..."
    sujeto "No..."
    sujeto "No deja que nadie se vaya..."

    stop music
    
    sujeto "{size=+10}{cps=5}Galaxia.{/cps}{/size}"
    
    "El nombre flotó en el aire como una maldición."
    
    play sound door_close
    scene puerta_cerrandose with shake
    r "¿¡Quién anda ahí!?"

    centered "{cps=15}{color=#390169}Jueguen mientras puedan...{/color}{/cps}"
    
    "Rodrigo sujetó firmemente la mano de Luz."
    r "Tenemos que irnos. Ya."
    
    play sound run fadeout 1.5
    scene sala_h127 with fade
    show sujeto_herido at center
    sujeto "No se puede huir de ella..."
    pause (0.5)
    sujeto "No se puede huir de ella..."
    pause (0.5)
    sujeto "No se puede huir de ella..."

    scene pasillo_huida with fade
    play sound run
    play music melody

    "Corrieron. El pasillo parecía estirarse."
    
    scene escombros_bloqueo with dissolve
    stop sound
    "¡Bloqueado!"
    
    play sound door_slam
    with shake
    r "¡Mierda!"
    r "¡Debimos tomar esa ruta antes...!"
    l "No tenemos tiempo, Rodri."
    l "¡Separémonos! ¡Grita si ves una salida!"
    "Fue una mala idea. Rodrigo lo sabía. Pero el pánico decidía por ellos."
    
    stop music fadeout 2
    scene foreboding_2 with fade
    stop sound
    $ renpy.save("1-1", "Encuentro 2")
    show rodrigo neutral at center
    "Rodrigo entró en una habitación de literas oxidadas. Su linterna parpadeó."

    play sound nailtap
    show rodrigo alert at vjump
    "Clic. Clic. Clic."
    "Garras sobre el linóleo."
    
    play music chase
    "Rodrigo notó que algo olfateaba cerca del suelo, buscando bajo los muebles..."
    
    menu:
        "Te acercas a comprobar":
            jump game_over_mnts_1
        "Te escondes bajo una de las camas":
            jump game_over_mnts_2
        "Te escondes tras el armario":
            jump escape_mnts
    
label escape_mnts:
    "Rodrigo apagó la linterna y se pegó a la pared, tras el armario, conteniendo el aliento hasta que le dolieron los pulmones."

    scene foreboding_2 with dissolve
    play sound "sfx/claw_drag_concrete.mp3"
    "Entonces, un chasquido metálico, seguido del raspado de una garra recorriendo la pared..."
    
    play sound door_open fadein 0.3
    "...y el crujido de la puerta abriéndose."
    scene habitacion_mantis with dissolve
    
    $ estado_mental += 1
    centered "{cps=10}La criatura te está buscando.{/cps}"
    
    "La Mantis entró. Sus antenas vibraban, captando el miedo en el aire."
    
    "Se acercó muy lentamente."
    
    "Un brazo se alza, una hoja afilada..."
    
    "Una."
    
    "Dos veces."
    
    "Rodrigo sostuvo el aire, un solo movimiento en falso y era hombre muerto."
    
    "La Mantis pasó de largo frente a las camas, ignorando el armario alto."
    pause (2.5)
    stop music fadeout 1.5
    play sound alarm volume 0.2 loop
    "¡BEEEEEP! ¡BEEEEEP!"
    
    "Una alarma lejana distrajo a la bestia. Con un chillido, la criatura salió disparada."
    stop sound fadeout 2.0
    scene foreboding_2
    show rodrigo scared at center
    with dissolve
    
    $ estado_mental += 1
    "Rodrigo cayó al suelo, temblando. Había estado a centímetros."
    pause (1)
    "Finalmente respira."
    
    "Sus manos tiritaban."
    
    r "Esa cosa... Me buscaba..."
    r "Sabía lo que hacía..."
    
    "Cuando por fin se incorporó, su espalda crujió y soltó un suspiro contenido."
    "Abrió la puerta de la habitación lentamente, asomandose al pasillo."
    
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
    l "¡Rodri!"
    "Él se giró en seco, instintivamente alzando el brazo con el que sostenía su daga, aunque sin intención real de atacar."
    
    l "¡Te estaba buscando! ¡Encontré algo genial!"
    
    "Rodrigo apenas pudo contestar, atónito por el contraste."
    
    "Luz estaba limpia. Demasiado limpia. Y esa sonrisa..."
        
    menu:
        "Abrazarla sin pensar":
            "El alivio le ganó al orgullo."
            "Antes de poder analizarlo, Rodrigo avanzó y la rodeó con los brazos con más fuerza de la que pretendía."
            
            l "¿R-Rodri?"
            
            "Su cuerpo estaba tibio. Real. No había rigidez antinatural. No había trampa."
            
            r "Esa cosa estaba cerca..."
            r "Pensé que..."
            
            "No terminó la frase."
            
            "Luz, todavía sorprendida por lo inusualmente físico del gesto —porque Rodrigo rara vez iniciaba contacto así—, dudó apenas un segundo antes de corresponder."
            
            l "...Estoy aquí."
            
            "Sus manos se apoyaron en su espalda, suaves. Firmes."
            
            "Después de unos segundos, fue ella quien se separó primero, mirándolo con una mezcla de ternura y preocupación."
            
            l "Debió ser horrible."
            
            $ afinidad_luz += 2
            $ estado_mental -= 1


        "Comprobar si está bien":
            "Rodrigo se acercó sin decir nada."
            "Sus manos se alzaron y sostuvieron el rostro de Luz entre sus dedos, examinando cada rasgo con intensidad."
            
            l "¿Qué haces?"
            
            "Bajó las manos por su cuello, palpando con cuidado, como buscando marcas invisibles."
            
            r "Quédate quieta."
            
            "No había suavidad en su voz. Solo tensión."
            "Sus ojos recorrían su piel en busca de heridas… o algo peor."
            pause 0.5
            "Nada."
            "La piel estaba limpia. Demasiado limpia."
            "Entonces, como si recién recordara lo extraño de su actitud, Rodrigo inclinó el rostro y dejó un beso breve en sus labios."
            
            r "...Solo quería asegurarme."
            
            "Luz parpadeó, confundida, pero sonrió."
            
            l "Podías haber empezado por ahí, paranoico."
            
            $ afinidad_luz += 1
            $ estado_mental += 1


        "Cuestionar a Luz":
            "Rodrigo no se movió."
            
            r "¿Por qué estás tan tranquila?"
            r "Y limpia."
            
            "La sonrisa de Luz vaciló apenas."
            
            l "¿Eh?"
            
            r "Hemos visto un fenómeno araña colgar del techo."
            r "No pareces... afectada."
            
            "Por un momento, el silencio pesó entre ambos."
            "Luego, la expresión de Luz se suavizó."
            
            l "Rodri..."
            l "Tuvimos suerte. No nos encontró."
            l "Y si no sonrío, me pongo a temblar."
            
            "Antes de que él pudiera responder, ella dio un paso al frente y lo abrazó."
            "Esta vez fue ella quien lo sostuvo con fuerza."
            
            l "Estás tenso."
            
            "Rodrigo tardó un segundo en corresponder."
            
            r "...Estoy bien."
            
            "Mentía."
            "Luz se separó con suavidad, pero su mirada permaneció atenta."
            
            $ estado_mental += 2
            $ afinidad_luz += 1
    
    l "Ven, quiero mostrarte esto."
    "Sin esperar respuesta, lo tomó de la mano, apretándola fuerte, arrastrándolo con ella."

    scene pasaje_secreto with dissolve
    pause (0.7)
    
    r "No había visto ese rincón antes..."
    pause(0.4)
    r "¿Estaba oculto?"
    l "Si... Hasta que cayó una tabla y escuché una corriente de aire."
    l "Da al otro lado del ala sur. Puede que haya una salida... O al menos, más espacio."
    "Rodrigo asintió, por primera vez en mucho tiempo..."
    "...sintiendo que las cosas van a mejorar."
    r "Vamos."

    call chapter_complete("Capítulo 2")
    jump cap_3

label game_over_mnts_1:
    "Rodrigo avanzó con cautela, su linterna apagada, guiado solamente por instinto."
    scene black with fade
    "Pero no había tiempo para dudar."
    
    play sound "sfx/claw_drag_concrete.mp3"
    "Una figura se abalanzó desde las sombras, dos hojas brillantes descendieron."
    play music curse
    scene death_mnts_1 with fade
    
    "Por un momento, la aterrada mirada de Rodrigo se encontró con los seis ojos de aquella criatura, pero antes de poder siquiera gritar por ayuda..."
    scene death_mnts_2 with shake
    play sound slash
    pause 3
    "{cps=20}.{/cps}"
    pause 2
    scene gameover_screen with dissolve
    pause(2)
    menu:
        "Cargar partida":
            jump load_screen
        "Volver al menú principal":
            return    

label game_over_mnts_2:
    "Rápidamente, Rodrigo se deslizó bajo una de las camas, conteniendo la respiración."
    
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
    scene expression Solid((255,255,255)) with fade
    
    centered "{i}{color=#000000}...Estático. Luz cálida. Voces infantiles a lo lejos...{/color}{/i}"
    play music flashback fadein 2
    scene luzdrigo_fb_1 with dissolve
    show layer master at sepia_filter
    "El sol de primavera caía oblicuo sobre el patio de la escuela, manchado con sombras largas el concreto rajado."
    
    scene luzdrigo_fb_2 with fade
    show layer master at sepia_filter
    "En una esquina, lejos de los juegos, los gritos, y las risas, un niño de cabello desordenado se acurrucaba contra una pared, con la mirada baja y con los brazos cruzados sobre las rodillas."
    
    "Rodrigo."
    
    "Su uniforme estaba limpio, pero arrugado. En el suelo junto a él había un cuaderno con garabatos oscuros, de formas extrañas y sin nombre. Dibujos de criaturas, de ojos tristes, de árboles secos."
    
    "No hablaba. No miraba. Solo esperaba que el recreo acabara."

    "Hasta que oyó pasos. Lentos, ligeros. Y una sombra diferente a las demás cubrió parte de su cuaderno."
    
    scene luzdrigo_fb_3 with dissolve
    show layer master at sepia_filter
    '?' "{i}¿Tú lo dibujaste?{/i}"

    "Rodrigo levantó apenas la vista. Frente a él había un niño de cabello castaño claro, suelto y algo desordenado. Sostenía una manzana a medio comer, y lo miraba sin miedo, sin burla. Solo… con interés genuino."

    '?' "{i}No está feo. Da miedo, pero es bonito.{/i}"

    "Rodrigo no respondió. Volvió a mirar el cuaderno."

    scene luzdrigo_fb_4 with dissolve
    show layer master at sepia_filter
    "El niño se sentó a su lado sin invitación."

    ln "{i}Yo soy Lucien. Tú eres el que no habla, ¿cierto?{/i}"

    "Silencio."

    "El se encogió de hombros."

    ln "{i}Está bien. No tienes que hablar. Puedo hablar yo.{/i}"

    "Y así lo hizo."

    "Le habló de su perro. De cómo su abuela hacía sopa extraña. De lo feos que eran los recreos a veces, porque los niños grandes gritaban mucho."
    
    "Le ofreció un trozo de su manzana. Rodrigo la tomó con torpeza, sorprendido de que alguien se quedara tanto rato con él."

    scene luzdrigo_fb_5 with fade
    show layer master at sepia_filter
    pause 1
    "Pasaron semanas."

    "Y cada día, Lucien encontraba una excusa para buscarlo. A veces dibujaban juntos. A veces solo se sentaban."

    "Y un día, cuando la campana sonó, Rodrigo habló por primera vez:"

    scene luzdrigo_fb_6 with dissolve
    show layer master at sepia_filter
    pause 1
    r "{i}Me llamo Rodrigo.{/i}"

    scene luzdrigo_fb_6 with dissolve
    show layer master at sepia_filter
    "Lucien lo miró con una sonrisa que iluminó más que el sol."

    ln "{i}Ya lo sabía. Pero me alegra oírlo de ti.{/i}"

    scene black with fade
    stop music fadeout 2
    pause 3
    play music "sfx/goteo_lento.wav" volume 0.5 loop
    scene pasillo_oscuro with dissolve

    "La luz del recuerdo se desvanece."
    "El aire vuelve a ser espeso. Húmedo. Muerto."

    scene corredor_amplio with dissolve
    "El pasadizo por el que Rodrigo y Luz avanzaban se abre finalmente hacia un corredor más amplio."
    "Los escombros se acumulan en las esquinas y algunas lámparas cuelgan inertes del techo."
    "A lo lejos, las puertas del vestíbulo se vislumbran a través de las sombras."

    scene vestibulo
    show azura temblor at left, shaking
    with dissolve
    play music menu fadein 1.5
    "Una figura se apoya contra la pared. Tiembla."

    show luz neutral at center with moveinright
    l "¡Azura!"

    show azura emocion
    "Azura levanta la vista de golpe, conteniendo el aliento. Al reconocerla, sus ojos se llenan de lágrimas contenidas."
    a "Luz… Rodrigo… Pensé que…"

    show rodrigo serio at right with moveinright
    menu:
        "Preguntas si está bien":
            $ afinidad_azura += 2

            show rodrigo serio at centro_izquierda
            show luz neutral at centro_derecha
            with move
            "Rodrigo acorta la distancia en dos pasos firmes."

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
            "Rodrigo asiente, pero su mandíbula permanece tensa."

            r "Nagi y Cuty."
            r "¿Los viste lastimados?"

            a "No."
            a "Corrían."

            "No dice 'están bien'. No dice 'están vivos'"
            "Solo 'corrían'."
            "Eso basta para que el silencio vuelva a pesar"
        
        "Preguntas por lo que ocurrió":
            $ afinidad_azura += 1
            "Rodrigo no se acerca."
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
            
            "Rodrigo aprieta la empuñadura de su daga."
            
            r "¿Los viste caer?"
            
            a "¡No!"
            
            "La respuesta es demasiado rápida."
            "Demasiado frágil."
            
            a "Solo... corrimos."
            
            "El vestíbulo vuelve a sentirse inmenso."
            "Y el segundo piso, peligrosamente lejano."
        
        "Te quedas callado":
            $ estado_mental += 2
            "Rodrigo no respondió."
            
            "Su mirada no estaba en Azura… sino en el espacio detrás de ella."
            
            "El vestíbulo era demasiado grande. Demasiado abierto. Demasiados lugares donde algo podía estar observándolos."
            
            a "Rodrigo…"
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
            "Rodrigo parpadea. La imagen de cuerpos mutilados desaparece lentamente."
            
            r "...Siguen vivos."
            r "Tienen que estarlo."
            
            "No suena convencido."
            
            a "Entonces vamos a encontrarlos."
            
            "Azura no sonríe. No se recompone."
            "Solo se obliga a mantenerse en pie."

    show luz worry
    "Luz mira hacia Rodrigo. Él evita la mirada por un segundo, pero luego asiente."

    l "Entonces los buscaremos. No vamos a dejarlos atrás."

    a "Gracias… De verdad."

    "Rodrigo lanza una última mirada hacia el vestíbulo. Aún bloqueado. La salida parece más lejana que nunca."

    "Sin decir nada, se gira, comenzando a avanzar hacia las escaleras con pasos firmes."

    "Azura y Luz lo siguen."

    stop music fadeout 1.5
    scene escaleras_con_sombra with fade
    "Subieron al segundo piso. El silencio era peor que los gritos."

    scene habitacion_intacta with dissolve
    pause 0.5

    "Una habitación... Limpia. Sin sangre. Sin roturas."
    show rodrigo neutral
    show luz neutral at left
    show azura neutral at right
    with dissolve

    "En el fondo, en un perchero, cuelga un abrigo viejo. Un olor a humedad y tinta seca impregna el ambiente."

    a "Es raro... Alguien cuidaba este lugar.."

    "Sus ojos esmeralda se dirigen a los cuadros mientras da un par de pasos hacia ellos."

    show luz smile with dissolve
    "Luz revisaba los cajones de un escritorio en busca de información útil."

    l "¡Rodri! ¡Mira esto!"

    "Luz sacó un pañuelo de un cajón. Dentro, el metal frío brilló bajo la linterna."
    
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
    
    "Luego, Rodrigo se dirigió al pequeño librero."

    "Entre papeles sueltos y libros de cuidado infantil, encuentra una nota amarillenta doblada cuidadosamente."

    play sound paper_flip
    play music story
    pause 0.5

    "Al abrirla, su expresión se endurece."

    "{cps=20}{b}Entrada 04 – Día 11{/b}{/cps}"

    "{cps=20}El {b}60%%{/b} de los primeros sujetos han fallecido. El proceso de mutación resultó inestable; los tejidos colapsan, los huesos se expanden sin orden y los sistemas vitales no resisten.{/cps}"
    
    "{cps=20}Los cuerpos se deforman en masas amorfas, aún respirando en algunos casos por horas. Las cámaras frías están saturadas. Se incrementó la dosis de estabilizadores para los próximos voluntarios.{/cps}"

    l "¿Y? ¿Qué encontraste?"

    "Rodrigo arrugó la nota antes de guardarla en su bolsillo."
    
    r "Nada útil... Solo... Basura vieja..."
    
    show luz neutral
    l "¿Seguro? Te vi la cara."

    l "¿No será algo importante?"

    r "No nos sirve. Vamos."

    "Incluso si no quería admitirlo, Rodrigo se estremeció por lo que leyó."

    "La sola idea le revolvía el estómago."

    a "Chicos... ¿Creen que alguien dormía aquí... sabiendo todo lo que pasaba?"

    pause 1.0
    stop music fadeout 1.5
    "El silencio reinó unos segundos."

    "Luz aún sostiene la pistola con cautela, Azura se aparta del cuadro, y Rodrigo da unos pasos hacia la puerta, cada músculo tenso."

    $ renpy.save("1-1", "Encuentro 3")
    "Rodrigo se detiene. Su mirada se dirige hacia la ventana."

    r "(Algo está mal... Demasiado silencio...)"

    l "¿Rodri...?"

    r "No se muevan."

    "Extiende su mano hacia Luz sin apartar la vista."
    
    play music melody

    "Una voz femenina se desliza entre las paredes, suave, casi cantarina, con un tono juguetón que hiela la sangre."

    play ambient "sfx/susurro_cercano.wav"
    g "Sé que están ahí~"

    "Azura se cubre la boca con ambas manos, retrocediendo."
    "Luz gira lentamente hacia la ventana, donde una silueta se asoma."

    scene galaxia_ventana with dissolve
    
    "En la ventana. Una silueta con orejas de gato y una sonrisa demasiado ancha."
    
    g "¿Ya juegan al escondite? Me encanta ese juego..."

    "Rodrigo baja el rostro, dientes apretados."

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
    "Rodrigo, aún en tensión, no mira atrás. Solo camina al frente."

    "Pero por un momento... su sombra parece temblar."

    "Como si algo dentro de él empezara a agitar"
    
    scene pasillo_abandonado
    show rodrigo serio
    show luz neutral at left
    show azura worried at right
    with fade
    play sound walk loop
    stop music fadeout 1.5
    play ambient wood_creak

    "Los tres avanzaban con pasos medidos. La linterna de Rodrigo barre el pasillo, revelando capas de polvo, trozos de pintura descascarada, y puertas cerradas con placas oxidadas."
    "A cada paso, el crujido del suelo de madera hace eco, forzándolos a contener la respiración."

    l "¿Siempre fue así de frágil...?"
    a "No es solo viejo... Está a punto de ceder..."
    r "Entonces vayamos más lento... Por las orillas si es posible."

    "Se acomodan, caminando en fila, pegados a la pared. Sus sombras oscilan con la luz, proyectándose deformadas."
    "La tensión se siente con cada movimiento."

    stop sound fadeout 1.5
    "De pronto, al fondo del pasillo, dos siluetas cruzan brevemente el marco de una puerta abierta."
    "Una de ellas voltea, mostrando el rostro de Cutipye, quien parece decir algo antes de entrar. Nagi le sigue, como si lo que encontraron fuera importante."

    show luz surprised
    l "¡Hey! ¡Cuty! ¡Nagi!"

    "Ellos voltearon. Nagi abrió la boca para gritar algo, pero el sonido fue otro."

    stop sound
    play sound crack
    "CRRRK…"
    "El piso bajo los pies del trío se agrieta. Se oye un crujido largo, siniestro."

    r "¡No se muevan!"

    play music shock noloop
    pause 0.2
    scene derrumbe with vpunch
    play sound break_wood
    pause 0.5
    
    "Demasiado tarde."

    "El suelo desapareció."

    "Azura y Luz logran aferrarse a los bordes, gritando al hacerlo, pero Rodrigo —el más cercano al centro— desaparece en la penumbra, tragado por el derrumbe."

    #show luz scared at right
    l "¡RODRIGOOOO!"

    #show azura scared at left
    a "¡No... no, no, no!"

    scene pasillo_abandonado
    show luz at centro_derecha
    show azura at right
    show nagi at centro_izquierda
    show cutipye at left
    with dissolve
    "El polvo cubre todo. Desde el piso superior sólo se ve el vacío, y el eco lejano del cuerpo de Rodrigo golpeando estructuras al caer."

    play ambient "dust_and_echo.ogg"
    pause 2

    call chapter_complete("Capítulo 3")
    jump cap_4



label cap_4:
    scene black with fade
    play music melody fadein 2
    pause 1

    "Oscuridad."
    "El polvo desciende como ceniza."
    "El aire es espeso, y el único sonido es el lento jadeo de Rodrigo."

    play sound "sfx/heavy_breathing.ogg" loop volume 0.8
    r "Estoy vivo... Creo que eso cuenta para algo..."

    scene bodega_dark
    show rodrigo injured at center
    with fade

    "El aire en el subsuelo era denso, una mezcla rancia de humedad, moho y sangre seca."
    "Rodrigo se sacudió el polvo, tosiendo. Le dolían las costillas, pero la adrenalina silenciaba el dolor con pánico frío."

    show item_gun at left with dissolve
    "A su lado, entre el polvo, algo metálico reluce."
    "La pistola."
    hide item_gun

    scene rodrigo_grab_pistol with dissolve
    "Rodrigo la toma con la mano temblorosa, recordando brevemente el rostro de Luz al encontrarla."
    "Apretando los dientes, la asegura en su cinturón improvisado."

    r "Perfecto... Un sótano oscuro en un orfanato abandonado."
    r "Solo falta una niña en triciclo y tengo el bingo del terror completo."

    scene bg_bodega_pan with dissolve
    "Observa a su alrededor."
    "Estanterías corroídas, cajas desechas, frascos vacíos y algunos envases sellados con etiquetas ilegibles."
    "El lugar parece una bodega metálica olvidada, húmeda y colapsada en varias secciones."

    "Silencio."
    "Solo el lejano goteo de agua."

    # scene bg_bodega_walk with dissolve
    show rodrigo move_slow with dissolve
    play sound walk loop
    "Rodrigo da unos pasos con lentitud, examinando la habitación. Se apoya contra una pared y para mantener el equilibrio."
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
    "Rodrigo se detiene en seco."
    "Nada visible, pero algo se movió en la penumbra."
    "Aprieta el arma."

    play music chase fadein 1
    $ renpy.save("1-1", "Encuentro 4")
    centered "{cps=20}No estás solo...{/cps}"

    "La oscuridad parece expandirse, como si algo lo observara desde más allá del ojo humano."

    scene bodega_gal_shadow with dissolve
    pause 0.7
    show galaxia shadow_eyes at center with dissolve # Solo ojos brillando
    
    g "Hueles a miedo... y a sudor frío. Me encanta."

    r "¡Déjame en paz, maldita sea!"
    
    #scene bg_pasillo_scroll with vpunch
    scene pasillo_corriendo with vpunch
    play sound run
    show rodrigo run_panic at center
    
    "Rodrigo giró y corrió por el pasillo de la izquierda."
    
    play sound "sfx/monster_parkour.ogg" # Sonido de rebotes
    "Detrás de él, no había pasos humanos. Había una bestia cazando."
    "Clic-clic-clic."
    "Impactos pesados contra las paredes y el techo."

    scene bg_almacen_medico with fade
    show rodrigo alert at left with moveinright
    play sound "sfx/glass_break_footsteps.mp3"
    
    "Derrapó en un almacén médico. Cristales rotos bajo sus rodillas. Se levantó al instante."

    g "¡Vamos, Rodri! ¡Corre más rápido!"
    g "Si te alcanzo, te doy un besito. O un mordisco~"
    
    play sound door_slam
    "Llegó al final. Puerta metálica. Cerrada."
    r "¡Mierda!"
    
    stop sound
    
    "El sonido de las garras se detuvo."
    "El silencio fue peor."

    show rodrigo aim_gun at left with dissolve
    "Rodrigo se giró lentamente, espalda contra la puerta fría."

    show galaxia walk_creepy at right with dissolve
    "De las sombras surgió ella."
    "Caminaba erguida, pero con la postura encorvada de una hiena. Ojos luminiscentes. Dientes afilados."

    g "Te acorralaste solito. Qué torpe eres."
    
    r "Aléjate. Soy alérgico al pelo de perro."

    show galaxia smile
    "Galaxia soltó una carcajada y se lanzó."
    
    show galaxia at centro_izquierda with moveinright
    play sound gunshot
    stop music
    scene black
    with flash
    
    "¡BANG!"
    
    play sound "sfx/thud.mp3"
    scene gal_dead_floor with vpunch
    "El impacto fue brutal. Un tiro limpio en la frente."
    
    play sound "sfx/body_fall_glass.mp3"
    
    "El cuerpo cayó pesadamente entre los cristales."
    
    scene bg_almacen_medico
    show rodrigo shocked at center
    with dissolve
    
    r "Dios... Se acabó."
    
    "Rodrigo bajó el arma, temblando. Exhaló. Necesitaba salir."
    scene pasillo_corriendo
    show rodrigo neutral at center
    with fade
    "Se giró para buscar otra salida, dándole la espalda al cuerpo."
    
    play sound "sfx/wet_whisper.mp3" volume 2.0 # Sonido fuerte y cercano
    g "{size=+10}{cps=5}Oye...{/cps}{/size}"

    show rodrigo scared at vjump
    "Rodrigo tropezó hacia atrás."

    play music chase1 volume 1.0 # Música frenética
    scene chase1_reprise with fade
    "Estaba de pie."
    "El lado izquierdo de su rostro era una ruina sanguinolenta y humeante."
    
    "Pero el lado derecho... sonreía. Coqueta. Viva."

    g "{b}{cps=15}Las balas no funcionan, Rodri~{/cps}{/b}"
    
    # Efecto visual de regeneración
    scene chase1_1
    show galaxia half_smile at truecenter:
        zoom 1.5
        linear 0.5 zoom 1.8
    with dissolve

    play sound "sfx/blood_drip.mp3"
    "Se acercó. Le dio un toquecito en la nariz con una garra, manchándolo de sangre."

    play sound "sfx/flesh_bubble.mp3" # Sonido asqueroso de regeneración
    
    show galaxia regen with dissolve 
    pause 0.5
    show galaxia healed with dissolve
    
    g "Vas a tener que esforzarte más si quieres romperme el corazón."

    r "¡NO!"
    
    scene bg_pasillo_escombros
    show rodrigo run_panic
    with vpunch
    
    g "¡CORRE, CORRE, CORRE!"
    
    "Ya no había coquetería. Solo hambre."
    
    play sound "sfx/heavy_bang.mp3"
    "Rodrigo volcó un archivador."
    
    "No sirvió. Ella saltó sobre él, rebotando en las paredes."
    
    r "¡Aléjate, monstruo!"
    play sound "sfx/brick_throw.mp3"
    "Lanzó un ladrillo. Ella ni se inmutó."
    
    # QTE (Quick Time Event)
    "Una escotilla elevada al final del pasillo. Su única oportunidad."
    
    call screen qte_escalera

label continue_escape_ladder:
    scene escalera_mano_1 with fade
    
    "Rodrigo puso un pie en el peldaño."
    
    scene escalera_mano_2 with shake
    play sound slash
    r "¡¡AAAGH!!"
    
    "Garras en su costado. Ardor lacerante."
    "Lo estampó contra la pared. Rostro regenerado a centímetros del suyo."
    
    g "Te tengo."
    
    #show rodrigo gun_point_blank
    r "¡Suéltame!"
    
    play sound gunshot
    with flash
    
    "Disparo a quemarropa en el abdomen."
    play sound "sfx/gal_pain_scream.mp3"
    
    "El impacto la dobló. Rodrigo trepó como una exhalación."

    scene bg_cuarto_maquinas
    play sound "sfx/hatch_slam_lock.mp3"
    
    "Cerró la escotilla. Giró la válvula."
    
    play sound "sfx/heavy_bang.mp3"
    with vpunch
    "BAM."
    
    play sound "sfx/heavy_bang.mp3"
    with vpunch
    "BAM."
    
    "Arañazos frenéticos... y luego, silencio."

    show rodrigo bleeding_wall at center with dissolve
    stop music fadeout 3.0
    
    "Rodrigo se dejó caer. Sangre caliente en sus dedos."
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

screen qte_escalera():
    modal True
    timer 3.0 action Jump("game_over_ladder") # 3 segundos para reaccionar
    
    vbox:
        xalign 0.5
        yalign 0.8
        text "{font=fonts/HelpMe.ttf}{size=50}¡LA ESCALERA! ¡AHORA!{/font}{/size}" color "#f00" at transform_blink
        textbutton "TREPAR" action Return() style "button_panic"

label game_over_ladder:
    play sound slash
    play music curse
    scene black with flash
    
    "{cps=15}Demasiado lento.{/cps}"
    
    scene death_glx_1 with fade
    g "Te dije que eras torpe~"
    
    pause(1)
    "Rodrigo sintió cómo unos dedos fríos y duros como el acero se cerraban alrededor de su tobillo."
    
    "Un tirón brutal lo arrancó de la escalera, lanzándolo contra el suelo con la fuerza de un animal salvaje jugando con su comida."
    
    "El aire escapó de sus pulmones con un gemido ahogado."
    
    play sound "sfx/bone_crack.mp3"
    
    "Antes de poder siquiera intentar levantarse, un peso inmenso le aplastó el pecho. Galaxia estaba sobre él, sus rodillas clavadas en sus brazos, inmovilizándolo con una facilidad humillante."
    
    "Ella acercó su rostro al de él, saboreando el terror en sus ojos, sus fauces abiertas goteando saliva sobre la mejilla de Rodrigo."
    
    "No hubo lucha. Solo la aceptación paralizante de una presa que sabe que el depredador ya ha ganado."
    
    play sound "sfx/bite_crunch.mp3"
    scene black with fade
    pause(1)
    
    "{cps=15}Rodrigo murió con la garganta destrozada, a centímetros de la salvación.{/cps}"
    
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
    show nagi serio at centro_izquierda
    show cutipye scared at left
    with fade
    stop music fadeout 2
    
    l "¡RODRIGO! ¡RESPONDE!"
    
    "El grito de Luz se pierde en la oscuridad del agujero. El polvo tarda en asentarse."
    
    play sound "sfx/rocks_falling_echo.mp3"
    "Solo se escucha el eco lejano de piedras cayendo. Y luego... nada."
    
    n "Mierda... El suelo estaba podrido."
    
    c "¿Se... se mató? ¿Cayó hasta el fondo?"
    
    l "¡No! ¡Él está bien! ¡Tiene que estar bien!"
    "Luz se acerca peligrosamente al borde, pero Nagi la sujeta del brazo."
    
    n "¡Atrás! Si te acercas, te vas con él. Toda esta estructura es inestable."
    
    a "¿Qué hacemos? No tenemos cuerdas... No podemos bajar."
    
    show luz determined
    l "Buscamos las escaleras. El sótano. Tiene que haber un acceso de servicio."
    l "No me voy de aquí sin él."
    
    n "Bien. Muévanse. Quedarnos aquí llorando no lo va a sacar."

    scene pasillo_servicio with fade
    play music melody fadein 2.0
    play ambient flies loop
    
    "El grupo avanza hacia el área de servicio. El aire cambia. Ya no huele a polvo viejo."
    "Huele a dulce. A carne podrida y azúcar fermentada."
    
    show cutipye disgust with dissolve
    c "Ugh... ¿Qué es esa peste?"
    
    show azura neutral at left with dissolve
    a "Suena como... ¿electricidad?"
    
    "No era electricidad. Era un zumbido orgánico."
    $ renpy.save("1-1", "Encuentro 5")
    
    scene cocina_infestada with dissolve
    
    "Al empujar las puertas vaivén de la cocina, se detienen en seco."
    
    "Lo que alguna vez fue una cocina industrial ahora es un nido."
    
    "Las mesas de metal están cubiertas de una sustancia cerosa y amarillenta."
    "Y sobre ella... cosas."
    
    c "Dios... son..."
    
    "Larvas. Del tamaño de perros grandes. Pálidas, húmedas, retorciéndose lentamente."
    "Pero tienen rasgos. Pequeñas manos atrofiadas. Rostros humanos a medio formar que boquean en silencio."
    
    l "No miren. Solo... busquemos la salida al fondo."
    
    play sound "sfx/wasp_wings.mp3" fadein 1.0
    
    "Un aleteo pesado desciende del techo."
    
    scene avispa_guardia with dissolve
    "Una criatura desciende. Mitad hombre, mitad insecto. Sus piernas son largas y quitinosas, su abdomen palpita con un aguijón rezumante."
    
    "El grupo retrocede, preparando sus armas."
    
    "Pero la criatura no ataca."
    
    "Se posa sobre una de las larvas humanoides. Acaricia su cabeza deforme con sus antenas. La limpia."
    
    a "¿La está... protegiendo?"
    n "Son nodrizas. Mientras no toquemos a las crías, quizás no nos..."
    
    stop music
    stop sound
    
    play sound gunshot volume 0.6 # Sonido lejano, con eco
    queue sound gunshot volume 0.3
    queue sound gunshot volume 0.1
    pause 1
    "{i}¡BAAANG!{/i}"
    
    #show avispa_guardia alert with vpunch
    play sound larvcry volume 2.5
    pause 1
    "Las larvas comienzan a chillar. Un sonido agudo, como llanto de bebé distorsionado."
    
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
    show luz aim at left
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
    
    stop music fadeout 2.0
    
    "El silencio vuelve al pasillo, roto solo por los jadeos descompasados del grupo."
    
    c "¿La... matamos?"
    n "Si..."
    
    "Nagi observa a Luz."
    "Ella nsigue sosteniendo la barra."
    "No la suelta."
    pause 1
    "Luego, cuando la adrenalina comienza a bajar, Azura observa a su alrededor, anunciando con voz temblorosa:"

    a "Miren... ahí."
    
    scene cuarto_maquinas_puerta with dissolve
    "Al final del pasillo, una puerta de acero. La válvula está girada desde dentro."
    "Hay abolladuras recientes en el metal. Marcas de garras por fuera."
    
    l "¡Rodrigo!"
    
    play sound "sfx/valve_turn.mp3"
    "Luz corre y gira la válvula con fuerza. La puerta se abre con un chirrido."
    
    scene bg_cuarto_maquinas
    play music main_menu fadein 2.0
    
    "El cuarto está oscuro, iluminado solo por las luces de emergencia."
    "En el rincón, una figura sentada contra la pared."
    
    show rodrigo shock_state at center with dissolve
    
    "Está cubierto de polvo y sangre. Tiene la mirada perdida en la pistola vacía que sostiene en su regazo."
    "Tiembla ligeramente."
    
    l "Rodri..."
    
    "Él levanta la vista lentamente. Tarda un segundo en reconocerla."
    
    r "Luz..."
    r "Ella... ella no muere..."
    
    scene luz_hug_rodrigo with dissolve
    "Luz se lanza a abrazarlo, ignorando la sangre. El resto del grupo se queda en la puerta, viendo la escena."
    
    n "Está vivo. Ese bastardo duro de matar está vivo."
    
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



label cap_6:

################
#    ACTO 2    #
################

    scene black with fade
    stop music fadeout 2.0
    
    centered "{i}Tres años atrás...{/i}"

    scene bg_casa_cutipye_dia with dissolve
    show layer master at sepia_filter 
    
    play music "music/party_chill.mp3" fadein 2.0
    play sound "sfx/glass_clink.mp3"

    "La casa de Cutipye olía a perfume caro y aperitivos horneados. Era una reunión pequeña, pero el lujo se notaba en cada rincón."

    scene bg_casa_cutipye_dia_interior with dissolve
    show layer master at sepia_filter
    show cutipye casual_young at center
    show nagi casual_young at right
    show azura casual_young at left

    c "Ya casi es la hora. Lucien fue muy específico."

    a "Es extraño... Lucien no suele ser así de misterioso. Siempre nos cuenta todo."
    
    n "Bah, no debe ser la gran cosa."
    "Nagi se echó un puñado de papas fritas a la boca, despreocupado, apoyándose muy cerca de Cutipye."
    
    n "¿Qué es lo peor que puede pasar? ¿Que venga con pareja? Ojalá, así deja de ser el tercero en discordia."

    play sound "sfx/doorbell.mp3"
    "El timbre sonó antes de que pudieran reírse del chiste."

    c "¡Yo abro!"

    hide cutipye with moveoutright
    pause 1.0
    
    "Murmullos en la entrada. Nagi alzó una ceja, confundido."
    
    c "Pasa, pasa... chicos, miren quién llegó primero."

    show cutipye casual_young at center with moveinright
    show nagi casual_young at centro_derecha
    show rodrigo casual_young_shy at right
    with moveinright

    "Detrás de ella, una sombra poco familiar."
    "Cabello desordenado, hombros encogidos, manos en los bolsillos como si quisiera esconderlas."
    "Rodrigo. El chico callado del fondo del salón."

    # La tensión social
    show nagi casual_young_molesto
    "El silencio fue instantáneo."

    n "¿Eh? ¿Te equivocaste de biblioteca, amigo?"
    n "El club de ajedrez es los martes."

    c "¡Nagi! Cierra la boca."
    
    "Cutipye le dio un codazo nada sutil a Nagi antes de sonreírle a Rodrigo, aunque con un toque de duda en sus ojos."
    
    c "Ignóralo, Rodri. Bienvenido. Aunque... ¿Lucien te invitó?"

    r "Sí... Lucien me dijo que tenía que estar aquí a esta hora."
    r "Dijo que era importante."

    show cutipye casual_young at left
    show nagi casual_young_molesto at centro_izquierda
    with moveinright
    show azura casual_young_smile at centro_derecha with moveinleft
    "Azura dio un paso al frente, con esa sonrisa que podía desarmar cualquier tensión."
    
    a "Hola, Rodrigo. Soy Azura. Nos sentamos a dos bancos de distancia en Historia."
    a "Si Lucien te pidió venir, eres bienvenido."

    r "Gracias..."

    play sound "sfx/door_open.mp3"
    
    "La puerta principal se abrió de nuevo. Pasos suaves. Decididos."

    c "¿Lucien? ¿Eres tú? Estamos en la sala."

    "Una figura apareció bajo el marco de la puerta."
    
    "No era Lucien."
    "O al menos, no el que ellos recordaban."

    show luz pre_transition_shy at center with moveinright
    "Llevaba un vestido sencillo de color pastel, el cabello suelto cayendo sobre sus hombros y un maquillaje ligero que resaltaba sus ojos."
    
    "Nagi soltó su vaso. Azura se cubrió la boca."
    
    n "¿Pero qué...?"
    c "¿Lucien...?"

    l "Hola, chicos."

    "Su voz temblaba un poco, pero su mirada estaba firme."

    l "Lamento no haberles dicho nada antes. Sé que... es una sorpresa."
    
    "Luz respiró hondo, entrelazando sus dedos frente a ella."

    l "Llevo mucho tiempo sintiendo que vivía la vida de alguien más. Y hoy... quería dejar de hacerlo."
    l "Quiero dar un comienzo fresco a mi vida. A quien soy realmente."
    
    show luz pre_transition_smile_tears
    l "Y no podía empezar ese camino sin mis personas más queridas."
    
    "Miró a Cutipye. A Nagi. A Azura."
    
    l "Mis mejores amigos..."
    
    "Y luego, giró la cabeza hacia la derecha, buscando los ojos del chico callado."
    
    l "...y mi novio."

    show rodrigo casual_young_blush at right
    show nagi casual_young_shock
    
    "Todas las miradas se dispararon hacia Rodrigo."
    "Él no parecía sorprendido por la ropa de Luz. Solo... le sonrió. Una sonrisa pequeña, privada y llena de orgullo."
    
    r "Te ves hermosa, Luz."
    
    scene black with fade
    stop music fadeout 3.0
    show layer master at default # Quitar filtro Sepia
    
    pause 2.0
    
    play music main_menu fadein 2.0
    scene luz_hug_rodrigo with dissolve
    # afinidad_luz tiene un valor entre 2 y 5 para este punto
    
    "El recuerdo se disipó, reemplazado por el olor a sangre y aceite."
    "Luz seguía abrazándolo, temblando, pero ya no era aquella chica tímida con vestido pastel."
    
    l "Te tengo, Rodri... Estoy aquí."

    "Rodrigo trató de contestar, pero su respiración era más pesada de lo que recordaba."
    "Había un sabor extraño en su boca."
    "{cps=15}Dulce. Metálico.{/cps}"

    r "...Luz..."
    $ estado_mental += 1
    scene bg_cuarto_maquinas
    show rodrigo shock_state at right
    show luz worry at left
    with dissolve

    "El costado le ardía. Bajó la mirada un instante."
    
    "Donde antes la sangre empapaba su ropa, ahora la tela estaba húmeda... Pero la herida parecía menos profunda."
    "Demasiado menos profunda."

    r "...No estaba así..."

    pause 0.5

    play ammbient "sfx/wet_whisper.mp3" fadein 0.3
    centered "{cps=15}{color=#390169}{i}Casi... casi mía...{/i}{/color}{/cps}"
    stop ambient fadeout 0.5
    $ estado_mental += 1

    "Rodrigo parpadeó con fuerza."

    r "¿Escucharon eso...?"

    if estado_mental >= 7:
        show luz worry at centro_derecha with move
        show cutipye worried at left
        show nagi worried at centro_izquierda
        with moveinleft
        "Pero el único sonido era el goteo distante del lugar."

        n "Ey... Cálmate, hombre. No hay nada."
        c "No sobrepienses las cosas. Solo es el estrés."

    "Luz lo miró con preocupación, sin soltarlo."

    l "Rodri... estás frío."

    "Al apoyar la mano en el suelo para incorporarse, notó pequeñas motas oscuras pegadas a sus dedos."
    "Parecían ceniza… o algo peor."

    "Las frotó instintivamente."
    "Desaparecieron."
    "Pero dejaron una sensación pegajosa que no se iba."

    $ estado_mental += 1

    "Por un segundo —solo un segundo— la luz del lugar le molestó más de lo normal."
    "Su pupila se contrajo… de una forma que no reconoció."

    pause 0.8

    "Parpadeó."
    "Todo volvió a la normalidad."

    "Tal vez era el golpe."
    "Tal vez era el miedo."

    "Tal vez..."

    stop music fadeout 0.7
    pause 1.5

    scene pasillo_abandonado with fade
    play sound wood_creak loop
    show luz worry at centro_derecha
    show azura scared at right
    show nagi serio at centro_izquierda
    show cutipye disgust at left
    show rodrigo neutral at center
    with dissolve

    "El grupo avanzó a paso lento. El orfanato se sentía más cerrado, como si los pasillos respiraran con ellos."
    
    n "Hay una ala administrativa por aquí. Si hay planos o salidas, estarán ahí."
    c "¿Y si es una trampa? Ya vimos lo que hay cuando nos metemos más adentro."
    n "No podemos quedarnos dando vueltas. Información nos da ventaja."
    c "O podemos irnos y vivir otro día. Yo prefiero no 'arriesgar ventaja'."

    show rodrigo nervioso at center
    "Rodrigo notó la discusión."
    "El sonido de sus voces le parecía lejano, como si viniera desde el fondo de un túnel."

    "Su pecho apretó nuevamente."
    "La punta de los dedos le vibró con esa sensación extraña, apenas perceptible."

    r "(No... no ahora.)"

    "Ambos lo miraron casi al mismo tiempo."
    stop sound fadeout 0.4
    pause 0.6

    r "¿Qué?"
    r "¿Ahora soy el comité ejecutivo?"

    "Intentó sonar ligero."
    "No lo logró del todo."

    r "A ver si entiendo."
    r "O nos metemos más profundo en el edificio embrujado buscando planos que probablemente estén mascados por algo..."
    r "O retrocedemos por el mismo camino por donde casi nos matan hace veinte minutos."

    pause 0.5

    r "Decisiones, decisiones."

    "Se llevó una mano al costado casi sin darse cuenta."
    "El ardor seguía ahí."
    "Constante."

    r "La verdad es que ambas opciones suenan como el comienzo de una historia que termina mal."
    r "Pero supongo que elegir no hacer nada tampoco nos va a teletransportar mágicamente afuera."

    "Mantuvo la mirada baja unos segundos más de lo normal."

    r "Así que sí."
    r "Vamos a hacer algo estúpido."
    r "Solo decidamos qué tipo de estupidez."

    menu:
        "Nagi tiene razón. Necesitamos información.":
            show rodrigo serio
            r "Si vamos a morir, prefiero hacerlo con un mapa en la mano."
            r "Al menos así podremos decir que fue una muerte organizada."
            "Su voz fue seca."
            "Demasiado seca."
            "No estaba intentando ser gracioso."
            $ afinidad_nagi += 1
            $ estado_mental += 1
            jump ir_administracion
            
        "Cuty tiene razón. No podemos seguir adentrándonos.":
            show rodrigo serio
            r "Ya tuvimos suficiente turismo oscuro por hoy."
            r "Retirarse no es cobardía."
            r "Es… estrategia con pulso funcional."
            "Forzó una media sonrisa."
            "Duró menos de un segundo."
            $ afinidad_cutipye += 1
            $ estado_mental -= 1
            jump volver_afuera

label ir_administracion:
    "Aceptaron seguir a Nagi."
    "Normalmente, eso implica escuchar un discurso motivador exagerado, una sonrisa confiada, y algún comentario sarcástico para empujar a todos a moverse."
    "Pero esta vez no hubo nada de eso."
    scene pasillo_lab with dissolve
    play sound walk loop
    show nagi smug at centro_izquierda
    show cutipye neutral at left
    show luz worry at centro_derecha
    show azura worried at right
    show rodrigo nervioso at center

    "Nagi caminaba al frente, sí... Pero no volteaba a hacer chistes."
    "No miraba a Rodrigo para lanzarle uno de sus típicos:"
    "{cps=20}\"Vamos, ermitaño, muévete o te cargo.\"{/cps}"

    "Ese era el guión de siempre."
    "El chico ruidoso arrastrando al callado fuera de su caparazón."
    "El equilibrio que habían tenido desde secundaria."

    "Ahora, Nagi bajaba el ritmo cada pocos pasos."
    "Demasiado pendiente."
    "Demasiado atento."

    scene pasillo_lab_close with dissolve

    "El olor a papel viejo y humedad aumentó conforme avanzaban."
    "El letrero corroído apareció al final del pasillo."

    "{cps=25}ADMINISTRACIÓN.{/cps}"
    play sound door_open
    scene oficina_admin with fade
    "Dentro, mesas cubiertas de polvo, archivadores volcados y un mapa clavado en la pared."
    "La luz temblorosa del techo apenas iluminaba los bordes."

    show nagi serio at centro_izquierda
    show rodrigo nervioso at center

    n "Aquí debería haber algo útil."

    "No hubo sonrisa."
    "No hubo exageración teatral."

    "Solo una frase corta."
    "Directa."

    "Rodrigo sintió esa ausencia más que cualquier grito."

    "Mientras los demás revisaban cajones, Nagi se acercó al mapa."
    "Y luego, sin decir nada, se colocó al lado de Rodrigo."

    show nagi worried at centro_izquierda with dissolve
    
    "No invadió su espacio. No le dió un golpe en el hombro. No lo llamó 'fantasma' ni 'poeta deprimido'."
    n "Oye..."

    pause 0.5

    n "Respira."

    "No fue una orden burlona."
    "Fue... suave."

    "Demasiado suave."

    "Rodrigo evitó mirarlo."
    "El sabor dulce volvió a su lengua."

    $ estado_mental += 1

    n "Te conozco."
    n "Cuando te quedas así de callado no es porque estés pensando."
    n "Es porque algo te aplasta por dentro."

    "Eso tampoco era normal."
    "Nagi no solía leerlo tan directamente."
    "Lo empujaba."
    "Lo provocaba."
    "Lo obligaba a reaccionar."

    "Pero ahora no intentaba sacarlo de su caparazón."
    "Intentaba... sostenerlo."

    #show rodrigo nervioso at center
    menu:
        "Estoy bien.":
            $ estado_mental -= 1
            r "Estoy bien. Solo... Necesito un minuto."
            n "Vale."
            n "Pero no me mientas si deja de ser verdad."

        "Creo que algo no está bien conmigo.":
            $ afinidad_nagi += 2
            $ estado_mental += 1
            show rodrigo nervioso
            r "No me siento bien, Nagi."
            show nagi worried
            n "¿Te mareas? ¿Te duele algo?"
            n "Dime dónde y vemos qué hacemos."

    "Nagi dio un paso más cerca."
    "Instintivamente, como siempre hacía cuando estaba por hacer una broma."
    "Pero esta vez no dijo nada gracioso."

    "Sus ojos recorrían el rostro de Rodrigo."
    "Analizando."
    "Buscando algo que no sabía nombrar."

    n "Ella te tocó, ¿no?"

    "La pregunta quedó suspendida en el aire."

    $ estado_mental += 1

    "Rodrigo apoyó la mano en el borde del mapa para no tambalearse."

    show rodrigo shocked at vjump

    "Una fina mancha oscura quedó marcada sobre el papel."
    "Pequeña."
    "Casi como tinta húmeda."

    "La cubrió con la manga antes de que nadie más la viera."

    "Nagi sí lo notó."

    show nagi serio

    "Pero no dijo nada."

    "Eso tampoco era normal."
    "Nagi siempre decía algo."

    pause 1.0

    n "Vamos a salir de aquí."
    n "¿Sí?"

    "No era el tono del líder empujando al grupo."
    "Era el tono de alguien que, por primera vez, no estaba intentando sacar a Rodrigo al mundo…"
    "Sino impedir que algo se lo llevara."

    $ afinidad_nagi += 1

    "Revisaron archivadores y encontraron planos parciales del edificio."
    "Suficientes para trazar una ruta tentativa de salida."

    "Pero cuando Rodrigo miró el mapa otra vez…"
    "Por una fracción de segundo, las líneas parecieron moverse."

    $ estado_mental += 1

    "Parpadeó."
    "Todo estaba quieto."

    call chapter_complete("Capítulo 6")
    jump cap_7

label volver_afuera:

    "Cutipye ganó la disputa."
    "Con pasos firmes —más firmes de lo que se sentía por dentro— giró sobre sus talones."

    scene pasillo_servicio with dissolve
    play sound walk loop

    show cutipye determined at left
    show nagi annoyed at centro_izquierda
    show luz worry at centro_derecha
    show azura scared at right
    show rodrigo nervioso at center

    "El grupo retrocedió hacia la lavandería por donde habían entrado."
    "El aire parecía más frío en esa dirección, como si el edificio exhalara detrás de ellos."

    "Rodrigo caminaba en silencio."
    "El sabor dulce volvió a su lengua."
    "{cps=15}Dulce. Metálico.{/cps}"

    $ estado_mental += 1

    "Cutipye notó el silencio."
    "Demasiado silencio."

    c "Bueno… miren el lado positivo."

    pause 0.5

    c "Si sobrevivimos, jamás volveremos a quejarnos de una prueba sorpresa."

    "Nadie respondió."

    c "...¿No?"
    c "¿Nada?"
    c "¿Ni una sonrisa irónica, Rodrigo? Eso sí que me preocupa."

    "Soltó una pequeña risa."
    "Fue corta."
    "Demasiado rápida."
    "Más parecida a un reflejo que a algo genuino."

    show cutipye smile_nervous

    c "En serio, piénsenlo. '¿Cuál fue su actividad extracurricular?'"
    c "'Ah, exploré un orfanato abandonado y casi muero tres veces.'"
    c "Eso suma puntos en la universidad, ¿no?"

    "Otra risa."
    "Esta vez más baja."
    "Más quebrada."

    "Rodrigo notó cómo sus manos estaban tensas."
    "Cómo sus dedos temblaban apenas."
    "Cómo cada vez que hacía un chiste, miraba de reojo las sombras del pasillo."

    "No estaba tratando de ser graciosa."
    "Estaba tratando de que nadie se rompiera."

    "Especialmente él."

    scene pasillo_servicio_dim with dissolve

    "Al doblar una esquina, encontraron el corredor parcialmente bloqueado por escombros recientes."
    "Polvo aún suspendido en el aire."
    "La salida directa no sería tan sencilla."

    show cutipye serious with dissolve

    c "Genial."
    c "Me encanta cuando el edificio decide redecorarse sin avisar."

    pause 0.5

    c "Vale. Rodeamos."
    c "Porque somos personas inteligentes."
    c "Personas que no vuelven al ala administrativa."
    c "Personas que toman decisiones sanas."

    "Su voz subía apenas en cada frase."
    "Como si necesitara convencerse a sí misma."

    show rodrigo nervioso at right
    show cutipye serious at left
    with dissolve

    "Rodrigo sintió un pequeño zumbido en la punta de los dedos."
    "Un impulso extraño."
    "Un deseo breve de… empujar los escombros con una fuerza que sabía que no tenía."

    r "(No.)"

    $ estado_mental += 1

    "Cutipye caminó más despacio hasta quedar a su lado."

    show cutipye neutral at center with move

    c "Oye."

    "No sonó como un chiste."

    c "¿Sabes cuál es la parte buena de que seas tan callado?"

    pause 0.5

    c "Que cuando te quedas más callado de lo normal… es muy obvio."

    "Rodrigo desvió la mirada."

    c "No me mires así."
    c "No estoy haciendo un discurso motivacional."
    c "Eso es territorio de Nagi."

    "Intentó sonreír."
    "No le salió del todo."

    "Bajó la voz."

    c "Solo… dime si estás aquí conmigo."

    menu:
        "No voy a dejar que nadie más se lastime.":
            $ afinidad_cutipye += 1
            show rodrigo serio
            r "No voy a dejar que nadie más se lastime."
            "Cutipye lo miró un segundo más de lo normal."
            c "Lo sé."
            c "Pero no te toca cargar con todo."
            c "No eres el guardaespaldas oficial del grupo."
            c "Eres Rodrigo."
            c "Y eso ya es suficiente."

        "Tengo miedo, Cutipye.":
            $ afinidad_cutipye += 2
            $ estado_mental += 1
            show rodrigo soft
            r "Tengo miedo, Cuty."
            "La confesión salió más baja de lo que esperaba."
            "Más honesta."
            show cutipye soft
            c "Bien."
            c "Eso significa que todavía quieres salir de aquí."
            c "Yo también tengo miedo."
            c "Pero prefiero tener miedo contigo que hacerme la valiente sola."

    "Durante un segundo, el pasillo dejó de sentirse tan estrecho."

    "Rodrigo apoyó la mano contra la pared para estabilizarse."

    show rodrigo shocked at vjump

    "Una leve marca oscura quedó sobre el concreto."
    "Pequeña."
    "Casi como hollín húmedo."

    "La limpió rápido con la manga."

    "Cutipye frunció el ceño."
    "Notó el gesto."

    pause 0.5

    c "¿Te manchaste con algo?"

    menu:
        "Es polvo. Nada más.":
            $ estado_mental -= 1
            r "Es polvo. Nada más."
            c "Claro."
            c "Polvo misterioso de edificio maldito."
            c "Mi favorito."

        "No lo sé.":
            $ afinidad_cutipye += 1
            $ estado_mental += 1
            r "No lo sé."
            show cutipye worried
            c "Vale."
            c "Entonces lo vigilamos."
            c "No te voy a dejar convertirte en…"
            c "Bueno."
            c "En algo raro sin avisarme."

            "Intentó que sonara ligero."
            "No lo logró del todo."

    scene lavanderia_exterior with dissolve
    #play sound door_squeak
    play sound wood_creak

    "Al final del corredor apareció la lavandería por donde habían entrado."
    "La luz fluorescente parpadeaba sobre la puerta metálica."

    "El olor a detergente viejo y humedad les golpeó de frente."

    "Rodrigo sintió algo extraño al cruzar el umbral."
    "Como si una parte de él no quisiera salir."

    $ estado_mental += 1

    "Parpadeó."
    "La sensación desapareció."

    call chapter_complete("Capítulo 6")
    jump cap_7

label cap_7:
    return



label creditos:

    play music credits fadein 1.5
    show expression Solid("#0006") as oscurecer

    $ credits_text = '''
    POSSESSED


    Historia y Dirección:
    HeartAttack51


    Programación:
    HeartAttack51


    Música:
    Human Entertainment
    Capcom
    Renegade Kid LLC
    @Jambus8550 #insertar hipervínculo


    Efectos de sonido:
    Renegade Kid LLC
    HeartAttack51
    Artistas libres de derechos


    Ilustraciones:
    ReFresh
    Vins2099
    Artistas libres de derechos


    Personajes:
    Azura: AlliTati
    Cutipye: ReFresh
    Dr. Edgar: HeartAttack51
    Galaxia: HeartAttack51
    Luz: Michi_tamagotchi
    Nagi: HeartAttack51
    Rodrigo: HeartAttack51


    Agradecimientos:
    La gente que fue parte del proyecto.
    Canela la perrita.
    A todos los que no atacaron a la primera criatura.
    '''
    
    show text credits_text at slow_scroll
    pause 140
    hide text

    pause 3
    scene black
    show text "Fin."
    with dissolve
    pause 4
    hide text
    hide oscurecer
    with fade
    return