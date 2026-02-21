# Personajes
define r = Character("Rodrigo", color="#0c0472")
define l = Character("Luz", color="#fd5353")
define c = Character("Cutipye", color="#2dff5a")
define a = Character("Azura", color="#0f8028")
define n = Character("Nagi", color="#7b2cbf")
define g = Character("Galaxia", what_font="fonts/HelpMe.ttf", color="#390169")
define sujeto = Character("Sujeto")
define ln = Character("Lucien", color="#fd5353")

# Variables y definiciones
default afinidad_luz = 0
default afinidad_azura = 0
default afinidad_cutipye = 0
default afinidad_nagi = 0
default estado_mental = 0
default tiempo_escape = 0

style button_panic is button:
    background "#5a0000"
    hover_background "#ff0000"

style button_panic_text is text:
    size 60
    color "#ffffff"
    bold True
    outlines [(3, "#000000", 0, 0)]

transform slow_scroll:
    yalign -1.1
    xalign 0.5
    linear 130.0 yalign 1.2

transform fadein_center:
    alpha 0.0
    zoom 0.8
    linear 1.5 alpha 1.0 zoom 1.0

transform heartbeat:
    zoom 1.0
    linear 0.1 zoom 1.02
    linear 0.1 zoom 1.0
    pause 0.5
    repeat

transform transform_blink:
    alpha 1.0
    linear 0.1 alpha 0.2
    linear 0.1 alpha 1.0
    repeat

transform sepia_filter:
    matrixcolor SepiaMatrix()

define flash = Fade(.25, 0.0, .75, color="#fff")

define shake = hpunch

transform centro_izquierda:
    xalign 0.35
    yalign 1.0

transform blanco_y_negro:
    matrixcolor SaturationMatrix(0.0)

transform centro_derecha:
    xalign 0.65
    yalign 1.0

transform shaking:
    linear 0.05 xoffset -2 yoffset 2
    linear 0.05 xoffset 3 yoffset -3
    linear 0.05 xoffset 2 yoffset -2
    linear 0.05 xoffset -3 yoffset 3
    linear 0.05 xoffset 0 yoffset 0
    repeat

## Fondos
image mainmenubg = "bg/main_menu.png"
image gameover_screen = "bg/game_over.jpg"
image foreboding_1 = "bg/pasillo_oscuro.jpg"
image escape_1 = "bg/pasillo_corriendo.jpg"
image puerta_abierta_sotano = "bg/puerta_oxidada.png"
# Muertes
image spdr1 = "game_over/death_spdr_1.png"

## Escenarios
### image bg clase = "escenarios/sala_clases.jpg"
image bg_pasillo_scroll:
    "bg_pasillo.png"
    linear 5.0 xpos -500

## Sprites
# Rodrigo
image rodrigo neutral = "images/sprites/Rodri.png" 
image rodrigo soft = "images/sprites/Rodri.png"
image rodrigo molesto = "images/sprites/Rodri.png"
image rodrigo serio = "images/sprites/Rodri.png"
image rodrigo frustrado = "images/sprites/Rodri.png"
image rodrigo nervioso = "images/sprites/Rodri.png"
image rodrigo sorprendido = "images/sprites/Rodri.png"
image rodrigo pain = "images/sprites/Rodri.png"
image rodrigo scared = "images/sprites/Rodri.png"
image rodrigo alert = "images/sprites/Rodri.png"
image rodrigo linterna = "images/sprites/Rodri.png"
image rodrigo shocked = "images/sprites/Rodri.png"
image rodrigo aim_gun = "images/sprites/Rodri.png"
image rodrigo injured = "images/sprites/Rodri.png" # herido
image rodrigo shock_state = "images/sprites/Rodri.png"
image rodrigo bleeding_wall = "images/sprites/Rodri.png" # sangrando en la pared
image rodrigo casual_young_shy = "images/sprites/Rodri.png"
image rodrigo casual_young_blush = "images/sprites/Rodri.png"


# Azura
image azura neutral = "images/sprites/Azura.png"
image azura smile = "images/sprites/Azura.png"
image azura temblor = "images/sprites/Azura.png"
image azura emocion = "images/sprites/Azura.png"
image azura scared = "images/sprites/Azura.png"
image azura casual_young = "images/sprites/Azura.png"
image azura casual_young_smile = "images/sprites/Azura.png"

# Cutipye
image cutipye smile = "images/sprites/Cutipye.png"
image cutipye scared = "images/sprites/Cutipye.png"
image cutipye disgust = "images/sprites/Cutipye.png"
image cutipye casual_young = "images/sprites/Cutipye.png"
image cutipye throw = "images/sprites/Cutipye.png"

# Nagi
image nagi smug = "images/sprites/Nagi.png"
image nagi smile = "images/sprites/Nagi.png"
image nagi serio = "images/sprites/Nagi.png"
image nagi angry = "images/sprites/Nagi.png"
image nagi scared = "images/sprites/Nagi.png"
image nagi casual_young = "images/sprites/Nagi.png"
image nagi casual_young_molesto = "images/sprites/Nagi.png"
image nagi casual_young_shock = "images/sprites/Nagi.png"

# Luz
image luz smile = "images/sprites/Luz.png"
image luz scared = "images/sprites/Luz.png"
image luz worry = "images/sprites/Luz.png"
image luz neutral = "images/sprites/Luz.png"
image luz surprised = "images/sprites/Luz.png"
image luz determined = "images/sprites/Luz.png"
image luz aim = "images/sprites/Luz.png"
image luz pre_transition_shy = "images/sprites/Luz.png"
image luz pre_transition_smile_tears = "images/sprites/Luz.png"

# Galaxia
image galaxia walk_creepy = "images/sprites/Galaxia.png"
image galaxia smile = "images/sprites/Galaxia.png"
image galaxia half_smile = "images/sprites/Galaxia.png"
image galaxia shadow_eyes = "images/sprites/Galaxia.png"
image galaxia laugh = "images/sprites/Galaxia.png"
image galaxia regen = "images/sprites/Galaxia.png"
image galaxia healed = "images/sprites/Galaxia.png"
image galaxia headshot = "images/sprites/Galaxia.png"


# Otros
image sujeto_herido = "images/sprites/Sujeto_Herido.png"

# Objetos
image cuaderno_bitacora = "images/objects/obj_cuaderno.png"
image item_gun = "images/objects/obj-gun.png"



##Sonidos
define shock = "sfx/shock.mp3"
define slash = "sfx/slash.mp3"
define run = "sfx/run.mp3"
define flies = "sfx/flies.mp3"
define crack = "sfx/crack-and-crunch.mp3"
define walk0 = "sfx/walking_intro.mp3"
define break_glass = "sfx/break-glass.mp3"
define break_wood = "sfx/break-wood.mp3"
define wood_creak = "sfx/wood-creak.mp3"
define door_break = "sfx/door-break.mp3" # bajar volumen a 0.6
define door_slam = "sfx/door-slam.mp3"
define thud = "sfx/thud.mp3"
define door_open = "sfx/door-open.mp3"
define door_close = "sfx/door-close.mp3"
define scream1 = "sfx/scream-echo.mp3"
define chptr_cmplt ="sfx/chapter-clear.mp3"
define glx_laugh = "sfx/laugh.mp3"
define paper_flip = "sfx/paper-flip.mp3"
define alarm = "sfx/alarm.mp3" #bajar volumen a 0.7"
define gunshot = "sfx/gunshot.mp3"
define walk = "sfx/walking.mp3"
define land = "sfx/land.mp3"
define objfall = "sfx/object-fall.mp3"
define nailtap = "sfx/nails-tapping.mp3"
define larvcry = "sfx/larvae_cry.mp3"

# Música
define audio.main_menu = "<loop 28.25>music/menu.ogg"
define audio.forest = "music/bosque.mp3"
define audio.melody = "music/melodia.ogg"
define audio.story = "<loop 41.53>music/historia.ogg"
define audio.curse = "music/maldicion.ogg"
define audio.chase = "<loop 62.8>music/persecucion.ogg"
define audio.chase1 = "<loop 34.5>music/persecucion (galaxia).ogg"
define audio.flashback = "<loop 28.00>music/flashback.ogg"
define audio.credits = "music/creditos.mp3"
define audio.rodtheme = "music/rodtheme.ogg" #DEFINIR LOOP

label start:
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
    #show rodrigo neutral at left with moveinleft
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
            $ afinidad_cutipye += 0
            pause 1
            show azura smile with dissolve
            a "Si sirve de algo..."
    
    a "Hay rumores de que en la época de la dictadura fue usado como centro de tortura."

    menu:
        "Te burlas del rumor":
            r "Sí, claro, y probablemente también hay un monstruo bajo cada cama, ¿no?"
            $ afinidad_azura -= 1

        "Te muestras incómodo":
            r "...Ok, eso sí fue un poco más turbio de lo que esperaba."
            $ afinidad_azura += 1
            $ estado_mental += 1

        "Guardas silencio":
            "Rodrigo se limitó a fruncir el ceño sin responder, su mueca una clara muestra de desapruebo."
            $ afinidad_azura += 0

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
                    $ estado_mental += 1
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

    jump cap_1_cmplt

label cap_1_cmplt:

    stop music fadeout 1.5
    scene black with fade
    pause(1.0)

    ### TERMINA CAPÍTULO 1
    play sound chptr_cmplt fadein 1.5
    show text "{size=50}Capítulo 1 Completado{/size}" at truecenter with dissolve
    pause(2.5)
    hide text with fade

    pause(0.5)

    show text "¿Deseas guardar tu progreso antes de continuar?" at truecenter with dissolve
    pause(1.0)

    menu:
        "Guardar y Continuar":
            $ renpy.save("1-1", "Capítulo 1 Completado")
            "Progreso guardado."
            jump cap_2
        "Continuar sin guardar":
            jump cap_2


label cap_2:

    scene sotano_inicial with fade
    play sound wood_creak loop volume 0.5
    "Los escalones crujían bajo sus pies con cada paso que daban. Una humedad densa impregnaba el aire; y el frío del sótano era diferente: no era solo temperatura... era abandono."

    show rodrigo linterna at left
    show luz worry at right

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

    scene sala_h127 with fade

    "El olor golpeó primero. Agrio. Metálico. Animal."
    show sujeto_herido at center with dissolve

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
    "Rodrigo entró en una habitación de literas oxidadas. Su linterna parpadeó."

    play sound nailtap
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

    play sound "sfx/garra_pared.wav"
    "Entonces, un chasquido metálico, seguido del raspado de una garra recorriendo la pared..."
    
    play sound door_open
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
    
    $ estado_mental += 1
    "Rodrigo cayó al suelo, temblando. Había estado a centímetros."
    pause (1)
    "Finalmente respira."
    
    "Sus manos tiritaban."
    
    r "Esa cosa... Me buscaba..."
    r "Sabía lo que hacía..."
    
    "Cuando por fin se incorporó, su espalda crujió y soltó un suspiro contenido."
    "Abrió la puerta de la habitación lentamente, asomandose al pasillo."
    
    scene pasillo with fade
    "Vacío."
    
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

    scene reunion_luz with fade
    show luz smile with dissolve
    play music menu
    l "¡Rodri!"
    "Él se giró en seco, instintivamente alzando el brazo con el que sostenía su daga, aunque sin intención real de atacar."
    
    l "¡Te estaba buscando! ¡Encontré algo genial!"
    
    "Rodrigo apenas pudo contestar, atónito por el contraste."
    
    "Luz estaba limpia. Demasiado limpia. Y esa sonrisa..."
        
    menu:
        "¿Estás bien?":
            r "¿Estás bien?"
            l "¡Si, mejor que nunca! Me siento... Ligera."
            $afinidad_luz +=1
    
        "¿Eres realmente tú?":
            "Todavía incrédulo por el contraste, el castaño se acercó titubeando a la pelirroja."
            r "Luz... Tu voz..."
            l "¿Qué pasa, tontito? ¿El miedo te comió la lengua?"
        
            "La voz de Luz no parecía estar preocupada... Más bien, estaba feliz... Demasiado feliz..."
            $ estado_mental +=1
    
    l "Ven, quiero mostrarte esto."
    "Sin esperar respuesta, lo tomó de la mano, apretándola fuerte, arrastrándolo con ella."

    scene pasaje_secreto with dissolve
    
    r "No había visto ese rincón antes..."
    pause(0.4)
    r "¿Estaba oculto?"
    l "Si... Hasta que cayó una tabla y escuché una corriente de aire."
    l "Da al otro lado del ala sur. Puede que haya una salida... O al menos, más espacio."
    "Rodrigo asintió, por primera vez en mucho tiempo..."
    "...sintiendo que las cosas van a mejorar."
    r "Vamos."

    jump cap_2_cmplt

label game_over_mnts_1:
    "Rodrigo avanzó con cautela, su linterna apagada, guiado solamente por instinto."
    scene black with fade
    "Pero no había tiempo para dudar."
    
    play sound "sfx/garra_pared.wav"
    "Una figura se abalanzó desde las sombras, dos hojas brillantes descendieron."
    play music curse
    scene death_mnts_1 with fade
    
    "Por un momento, la aterrada mirada de Rodrigo se encontró con los seis ojos de aquella criatura, pero antes de poder siquiera gritar por ayuda..."
    scene death_mnts_2
    play sound slash
    pause 3
    "{cps=20}.{/cps}"
    pause 3
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
    
    play sound "sfx/garra_pared.wav"
    "Una garra raspa el suelo... Luego la cama."
    
    
    pause (1.5)
    play music curse
    play sound slash
    "Sin aviso, la hoja atraviesa el colchón y su torso."
    
    play sound "sfx/ultimo_aliento.wav"
    scene gameover_screen with dissolve
    pause(2)
    menu:
        "Cargar partida":
            jump load_screen
        "Volver al menú principal":
            return



label cap_2_cmplt:

    stop music fadeout 1.5
    scene black with fade
    pause(1.0)

    ### TERMINA CAPÍTULO 2
    play sound chptr_cmplt fadein 1.5

    show text "{size=40}Capítulo 2 Completado{/size}" at truecenter with dissolve
    pause 3.0
    hide text with fade

    pause(0.5)

    show text "¿Deseas guardar tu progreso antes de continuar?" at truecenter with dissolve
    pause(1.0)

    menu:
        "Sí, guardar ahora":
            $ renpy.save("1-1", "Capítulo 2 Completado")
            "Progreso guardado."
            jump cap_3
        "No, continuar sin guardar":
            jump cap_3



label cap_3:
    scene white with fade
    
    centered "{i}...Estático. Luz cálida. Voces infantiles a lo lejos...{/i}"
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
        "Preguntas si está bien.":
            $ afinidad_azura += 2
            r "¿Estás herida?"
            
            a "No... solo asustada. No quise separarme, pero… algo nos forzó a dispersarnos."    
            a "Fue... el ruido."
            "Se seca una lágrima rápidamente y se endereza."
        
        "Preguntas por lo que ocurrió":
            $ afinidad_azura += 1
            r "¿Qué ocurrió? ¿Donde están los otros?"
         
            a "No lo sé. Corrimos en direcciones opuestas. Nagi y Cuty subieron al segundo piso."
        
        "Te quedas callado":
            $ estado_mental += 1
            r "..."
            "Rodrigo solo miraba las sombras. ¿Estarán vivos? La imagen de sus cuerpos rotos invadía su mente."
            a "Rodrigo..."
            "Él parpadeó, volviendo a la realidad."

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

    "En el fondo, en un perchero, cuelga un abrigo viejo. Un olor a humedad y tinta seca impregna el ambiente."

    a "Es raro... Alguien cuidaba este lugar.."

    "Sus ojos esmeralda se dirigen a los cuadros mientras da un par de pasos hacia ellos."

    show luz smile with dissolve
    "Luz revisaba los cajones de un escritorio en busca de información útil."

    l "¡Rodri! ¡Mira esto!"

    "Luz sacó un pañuelo de un cajón. Dentro, el metal frío brilló bajo la linterna."
    
    show pistola_primer_plano with dissolve
    "Una pistola. Vieja, pero aceitada. Y una caja de balas."
    
    hide pistola_primer_plano with dissolve
    
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

    scene galaxia_ventana with dissolve
    play ambient "sfx/susurro_cercano.wav"
    play music melody

    "Una voz femenina se desliza entre las paredes, suave, casi cantarina, con un tono juguetón que hiela la sangre."

    g "Sé que están ahí~"

    "Azura se cubre la boca con ambas manos, retrocediendo."
    "Luz gira lentamente hacia la ventana, donde una silueta se asoma."

    show galaxia_sombra at center # Asumiendo sprite silueta
    
    "En la ventana. Una silueta con orejas de gato y una sonrisa demasiado ancha."
    
    g "¿Ya juegan al escondite? Me encanta ese juego..."

    "Rodrigo baja el rostro, dientes apretados."

    play sound "sfx/bang_window.mp3" volume 2.0
    with vpunch 
    
    g "Pero yo siempre gano."
    
    r "Vámonos. ¡YA!"
    
    play sound "sfx/rasguño_vidrio.wav"
    "Un chirrido agudo de garras contra el cristal los persiguió mientras huían."
    
    scene pasillo_oscuro with dissolve
    play sound run
    "Cuando finalmente abandonan la habitación y cierran la puerta con suavidad, el grupo suelta el aire contenido."

    show rodrigo alert
    "Rodrigo, aún en tensión, no mira atrás. Solo camina al frente."

    "Pero por un momento... su sombra parece temblar."

    "Como si algo dentro de él empezara a agitar"
    
    scene pasillo_polvoriento with fade
    play sound walk loop
    stop music fadeout 1.5
    play ambient wood_creak

    "Los tres avanzaban con pasos medidos. La linterna de Rodrigo barre el pasillo, revelando capas de polvo, trozos de pintura descascarada, y puertas cerradas con placas oxidadas."
    "A cada paso, el crujido del suelo de madera hace eco, forzándolos a contener la respiración."

    a "¿Siempre fue así de frágil...?"
    r "No es solo viejo... Está a punto de ceder..."
    l "Entonces vayamos más lento... Por las orillas si es posible."

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

    play sound break_wood
    scene derrumbe with vpunch
    play music shock noloop
    pause 0.5
    
    "Demasiado tarde."

    "El suelo desapareció."

    "Azura y Luz logran aferrarse a los bordes, gritando al hacerlo, pero Rodrigo —el más cercano al centro— desaparece en la penumbra, tragado por el derrumbe."

    show luz scared at right
    l "¡RODRIGOOOO!"

    show azura scared at left
    a "¡No... no, no, no!"

    scene polvo_niebla with dissolve
    "El polvo cubre todo. Desde el piso superior sólo se ve el vacío, y el eco lejano del cuerpo de Rodrigo golpeando estructuras al caer."

    play ambient "dust_and_echo.ogg"
    pause 2

    hide azura
    hide luz

    jump cap_3_cmplt



label cap_3_cmplt:

    stop music fadeout 1.5
    scene black with fade
    pause(1.0)

    ### TERMINA CAPÍTULO 3
    play sound chptr_cmplt fadein 1.5

    show text "{size=40}Capítulo 3 Completado{/size}" at truecenter with dissolve
    pause 3.0
    hide text with fade

    pause(0.5)

    show text "¿Deseas guardar tu progreso antes de continuar?" at truecenter with dissolve
    pause(1.0)

    menu:
        "Sí, guardar ahora":
            $ renpy.save("1-1", "Capítulo 3 Completado")
            "Progreso guardado."
            jump cap_4
        "No, continuar sin guardar":
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

    scene bg_bodega_dark with fade
    show rodrigo injured at center with dissolve

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

    scene bg_bodega_pan
    "Observa a su alrededor."
    "Estanterías corroídas, cajas desechas, frascos vacíos y algunos envases sellados con etiquetas ilegibles."
    "El lugar parece una bodega metálica olvidada, húmeda y colapsada en varias secciones."

    "Silencio."
    "Solo el lejano goteo de agua."

    scene bg_bodega_walk with dissolve
    show rodrigo move_slow
    play sound walk loop
    "Rodrigo da unos pasos con lentitud, examinando la habitación. Se apoya contra una pared y para mantener el equilibrio."
    "Por unos instantes, se permite respirar."

    r "Podría ser peor... Podría estar atrapado con uno de esos monstruos..."

    pause 1.5

    stop sound
    stop music
    play sound "sfx/claw_drag_concrete.mp3"
    "CRRRK..."
    "Un sonido rasposo. Uñas largas contra el hormigón."
    
    play sound glx_laugh
    "Y una risita baja, gutural."

    show rodrigo tense
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
    
    scene bg_pasillo_scroll with vpunch
    play sound run
    show rodrigo run_panic at center
    
    "Rodrigo giró y corrió por el pasillo de la izquierda."
    
    play sound "sfx/monster_parkour.ogg" # Sonido de rebotes
    "Detrás de él, no había pasos humanos. Había una bestia cazando."
    "Clic-clic-clic."
    "Impactos pesados contra las paredes y el techo."

    scene bg_almacen_medico with fade
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
    scene galaxia headshot with vpunch
    "El impacto fue brutal. Un tiro limpio en la frente."
    
    scene gal_dead_floor
    play sound "sfx/body_fall_glass.mp3"
    
    "El cuerpo cayó pesadamente entre los cristales."
    
    scene bg_almacen_medico
    show rodrigo shocked at center
    with dissolve
    
    r "Dios... Se acabó."
    
    "Rodrigo bajó el arma, temblando. Exhaló. Necesitaba salir."
    "Se giró para buscar otra salida, dándole la espalda al cuerpo."
    
    play sound "sfx/wet_whisper.mp3" volume 2.0 # Sonido fuerte y cercano
    g "{size=+10}{cps=5}Oye...{/cps}{/size}"

    show rodrigo scared with vpunch
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
    
    scene bg_pasillo_escombros with vpunch
    
    g "¡CORRE, CORRE, CORRE!"
    
    "Ya no había coquetería. Solo hambre."
    
    show rodrigo run_panic
    "Rodrigo volcó un archivador."
    play sound "sfx/metal_crash.mp3"
    
    "No sirvió. Ella saltó sobre él, rebotando en las paredes."
    
    r "¡Aléjate, monstruo!"
    play sound "sfx/brick_throw.mp3"
    "Lanzó un ladrillo. Ella ni se inmutó."
    
    # QTE (Quick Time Event)
    "Una escotilla elevada al final del pasillo. Su única oportunidad."
    
    call screen qte_escalera

label continue_escape_ladder:
    scene bg_escalera_mano
    
    "Rodrigo puso un pie en el peldaño."
    
    play sound slash
    show rodrigo pain with vpunch
    r "¡¡AAAGH!!"
    
    "Garras en su costado. Ardor lacerante."
    "Lo estampó contra la pared. Rostro regenerado a centímetros del suyo."
    
    g "Te tengo."
    
    show rodrigo gun_point_blank
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

    jump cap_4_cmplt

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
    
    scene death_spdr_1 with fade
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

label cap_4_cmplt:

    stop music fadeout 1.5
    scene black with fade
    pause(1.0)

    ### TERMINA CAPÍTULO 4
    play sound chptr_cmplt fadein 1.5

    show text "{size=40}Capítulo 4 Completado{/size}" at truecenter with dissolve
    pause 3.0
    hide text with fade

    pause(0.5)

    show text "¿Deseas guardar tu progreso antes de continuar?" at truecenter with dissolve
    pause(1.0)

    menu:
        "Sí, guardar ahora":
            $ renpy.save("1-1", "Capítulo 4 Completado")
            "Progreso guardado."
            jump cap_5
        "No, continuar sin guardar":
            jump cap_5
            


label cap_5:
    scene polvo_niebla with fade
    stop music fadeout 2.0
    
    show luz scared at right
    show azura scared at left
    
    l "¡RODRIGO! ¡RESPONDE!"
    
    "El grito de Luz se pierde en la oscuridad del agujero. El polvo tarda en asentarse."
    
    play sound "sfx/rocks_falling_echo.mp3"
    "Solo se escucha el eco lejano de piedras cayendo. Y luego... nada."
    
    show nagi serio at center with dissolve
    n "Mierda... El suelo estaba podrido."
    
    show cutipye scared at centro_derecha behind nagi with dissolve
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
    
    scene cocina_infestada with dissolve
    
    "Al empujar las puertas vaivén de la cocina, se detienen en seco."
    
    "Lo que alguna vez fue una cocina industrial ahora es un nido."
    
    show nidos_larvas at truecenter with dissolve
    "Las mesas de metal están cubiertas de una sustancia cerosa y amarillenta."
    "Y sobre ella... cosas."
    
    c "Dios... son..."
    
    "Larvas. Del tamaño de perros grandes. Pálidas, húmedas, retorciéndose lentamente."
    "Pero tienen rasgos. Pequeñas manos atrofiadas. Rostros humanos a medio formar que boquean en silencio."
    
    l "No miren. Solo... busquemos la salida al fondo."
    
    play sound "sfx/wasp_wings.mp3" fadein 1.0
    
    "Un aleteo pesado desciende del techo."
    
    show avispa_guardia at center with dissolve
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
    
    show avispa_guardia alert with vpunch
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
    show avispa_zangano attack at center with moveinright
    
    "El Zángano se libera, aleteando furiosamente en el espacio cerrado del pasillo."
    "Bloquea el camino hacia el sótano."
    "Va a atacar a Azura."
    
    l "¡Azura, abajo!"
    
    "El tiempo se ralentiza. Tienen que actuar en equipo o morirán."
    
    call screen qte_wasp_1

label exito_qte_1:
    # Resultado visual Fase 1
    play sound "sfx/throw_object.mp3"
    show cutipye throw
    "¡CLANG!"
    
    play sound "sfx/metal_hit_chitin.mp3"
    with vpunch
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
    "¡CRACK!"
    "El golpe destroza el ala derecha. La avispa chilla y cae al suelo, expuesta."
    
    # --- FASE 3: LUZ (REMATAR) ---
    show luz aim at left
    l "¡MUERE!"
    
    call screen qte_wasp_3

label combate_ganado:
    
    play sound gunshot
    with flash
    
    play sound "sfx/insect_splat.mp3"
    "La bala atraviesa el tórax de la avispa, explotando en una lluvia de icor verde."
    
    scene avispa_dead with dissolve
    "La criatura cae, convulsionando una última vez antes de quedar inmóvil."
    
    stop music fadeout 2.0
    
    "El silencio vuelve al pasillo, roto solo por los jadeos del grupo."
    
    c "¿La... matamos?"
    n "Eso parece."
    
    "Nagi se limpia una mancha de sangre verde de la mejilla, mirando su bate abollado."
    
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
    
    jump cap_5_cmplt

label game_over_wasp:
    scene pasillo_servicio_lucha
    play sound slash
    show avispa_zangano attack with zoomin
    play music curse
    
    "Fueron una fracción de segundo demasiado lentos."
    
    play sound "sfx/body_slam_squish.mp3"
    show avispa_zangano attack at truecenter with vpunch
    "El zumbido se convirtió en un rugido ensordecedor cuando el zángano ignoró a Nagi y a Luz, abalanzándose directamente sobre Azura con todo su peso."
    
    scene game_over_wasp_1
    play sound slash
    a "¡¡AAAGH!!"
    
    show luz scared at left
    show nagi scared at right
    
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
    
    scene game_over_wasp_2 with fade
    
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
        
        textbutton "¡DISPARAR!" style "button_panic" action Jump("combate_ganado") text_size 70 text_color "#fff" text_bold True

label qte_wasp_4:
    # Resultado visual Fase 2
    play sound "sfx/bat_swing.mp3"
    "Nagi carga el bate con todas sus fuerzas."
    
    play sound "sfx/bat_hit_hard.mp3"
    with shake
    "¡CRACK!"
    "El golpe destroza el ala derecha. La avispa chilla y cae al suelo, expuesta."
    
    # --- FASE 3: LUZ (REMATAR) ---
    show luz aim at center
    l "¡MUERE!"
    
    call screen combate_ganado

label cap_5_cmplt:

    stop music fadeout 1.5
    scene black with fade
    pause(1.0)

    ### TERMINA CAPÍTULO 5
    play sound chptr_cmplt fadein 1.5

    show text "{size=40}Capítulo 5 Completado{/size}" at truecenter with dissolve
    pause 3.0
    hide text with fade

    pause(0.5)

    show text "¿Deseas guardar tu progreso antes de continuar?" at truecenter with dissolve
    pause(1.0)

    menu:
        "Sí, guardar ahora":
            $ renpy.save("1-1", "Capítulo 5 Completado")
            "Progreso guardado."
            jump cap_6
        "No, continuar sin guardar":
            jump cap_6


label cap_6:

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
    
    c "Pasen, pasen... chicos, miren quién llegó primero."

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
    scene bg_cuarto_maquinas with dissolve
    
    scene luz_hug_rodrigo at center
    
    "El recuerdo se disipó, reemplazado por el olor a sangre y aceite."
    "Luz seguía abrazándolo, temblando, pero ya no era aquella chica tímida con vestido pastel."
    "Ahora sostenía una pistola vacía y tenía la ropa sucia de escombros."
    
    l "Te tengo, Rodri... Estoy aquí."

    # Continuar historia...
    
label cap_6_cmplt:

    stop music fadeout 1.5
    scene black with fade
    pause(1.0)

    ### TERMINA CAPÍTULO 6
    play sound chptr_cmplt fadein 1.5

    show text "{size=40}Capítulo 6 Completado{/size}" at truecenter with dissolve
    pause 3.0
    hide text with fade

    pause(0.5)

    show text "¿Deseas guardar tu progreso antes de continuar?" at truecenter with dissolve
    pause(1.0)

    menu:
        "Sí, guardar ahora":
            $ renpy.save("1-1", "Capítulo 6 Completado")
            "Progreso guardado."
            jump cap_7
        "No, continuar sin guardar":
            jump cap_7


label cap_7:
    return





label creditos:

    play music credits fadein 1.5
    scene black with fade

    $ credits_text = '''
    POSSESSED


    Historia y Dirección:
    HeartAttack51
    Vins2099


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
    A todos los que no huyeron a la primera criatura.
    '''
    
    show text credits_text at slow_scroll
    pause 140
    hide text

    pause 3
    show text "Fin." with fade
    pause 4
    return




###label splashscreen:    scene black    with Pause(1)    $ splash_text = """{size=+10}{color=#FF0000}ADVERTENCIA{/color}{/size}                                    Este juego contiene lenguaje fuerte, y escenas de violencia explícita y gore.    Se recomienda discreción."""    show text splash_text at fadein_center    with dissolve        pause 5    hide splash_text    scene black with dissolve        with fade    return

label splashscreen:
    scene mainmenubg at blanco_y_negro
    with dissolve
    pause 0.5
    
    $ splash_text = """{size=+10}{color=#FF0000}ADVERTENCIA{/color}{/size}
    Este juego contiene lenguaje fuerte, y escenas de violencia explícita y gore.
    Se recomienda discreción."""
    
    show text Text(splash_text, outlines=[(4, "#000000", 0 ,0)], text_align=0.5) at fadein_center with dissolve
    
    pause 5
    hide text
    scene black
    with dissolve
    pause 1
    return


label intro:
    stop music fadeout 0.5
    play sound door_open
    scene black
    with fade
    pause 1
    play sound door_close
    pause 2
    jump start