################
#    ACTO 2    #
################
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
    scene pasillo_lab
    play sound walk loop
    show nagi smug at centro_izquierda
    show cutipye neutral at left
    show luz worry at centro_derecha
    show azura worried at right
    show rodrigo nervioso at center
    with dissolve

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

    show nagi serio at left
    show rodrigo nervioso at centro_derecha
    with dissolve

    n "Aquí debería haber algo útil."

    "No hubo sonrisa."
    "No hubo exageración teatral."

    "Solo una frase corta."
    "Directa."

    "Rodrigo sintió esa ausencia más que cualquier grito."

    "Mientras los demás revisaban cajones, Nagi se acercó al mapa."
    show nagi serio at centro_izquierda with move
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

    scene pasillo_servicio
    show cutipye determined at left
    show nagi annoyed at centro_izquierda
    show luz worry at centro_derecha
    show azura scared at right
    show rodrigo nervioso at center
    with fade
    play sound walk loop

    "El grupo retrocedió hacia la lavandería por donde habían entrado."
    "El aire parecía más frío en esa dirección, como si el edificio exhalara detrás de ellos."

    "Rodrigo caminaba en silencio."
    "El sabor dulce volvió a su lengua."
    "{cps=15}Dulce. Metálico.{/cps}"

    "Cutipye notó el silencio."
    "Demasiado silencio."

    c "Bueno… miren el lado positivo."

    pause 0.5

    c "Si sobrevivimos, jamás volveremos a quejarnos de una prueba sorpresa."

    pause 0.5

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

    #scene pasillo_servicio_dim with dissolve
    stop sound fadeout 1.6
    scene bodega_gal_shadow with dissolve

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

    scene lavanderia_abandonada with dissolve
    play sound door_open

    "Al final del corredor apareció la lavandería por donde habían entrado."
    "La luz fluorescente parpadeaba sobre la puerta metálica."

    "El olor a detergente viejo y humedad les golpeó de frente."

    "Rodrigo sintió algo extraño al cruzar el umbral."
    "Como si una parte de él no quisiera salir."

    "Parpadeó."
    "La sensación desapareció."

    call chapter_complete("Capítulo 6")
    jump cap_7

label cap_7:

    scene black with fade
    stop music fadeout 2.0

    scene pasillo_intermedio with dissolve
    play ambient "sfx/low_drone.mp3" fadein 1.5

    show rodrigo neutral at center
    show luz worry at centro_derecha
    show azura worried at right
    show nagi serio at centro_izquierda
    show cutipye serious at left

    "El edificio ya no se sentía igual."
    "El aire era más denso."
    "Más estrecho."

    if _last_label == "ir_administracion":

        "El mapa que Nagi llevaba en la mano ya no coincidía del todo con el pasillo frente a ellos."

        show nagi frustrated
        n "No tiene sentido… esto no estaba aquí."

        show cutipye serious
        c "Te dije que meternos más adentro era mala idea."

        $ ruta_anterior = "nagi"

    else:

        "La lavandería por donde habían entrado ya no era accesible."
        "Un derrumbe reciente bloqueaba el regreso."

        show cutipye shocked
        c "No… no, no, no. Esto no estaba así."

        show nagi serio
        n "El edificio se está moviendo… o algo lo está moviendo."

        $ ruta_anterior = "cuty"


    "Un golpe metálico resonó en el techo."

    play sound "sfx/metal_impact.mp3"
    scene pasillo_oscuridad with vpunch

    stop ambient
    play ambient "sfx/ringing.mp3"

    "Las luces se apagaron."

    l "¿Rodri?"

    pause 1.0

    "Oscuridad total."

    show rodrigo shock_state at center

    "{cps=10}{color=#390169}{i}Rodrigo…{/i}{/color}{/cps}"

    pause 0.5

    "{cps=12}{color=#390169}{i}Ellos no lo entienden…{/i}{/color}{/cps}"

    $ estado_mental += 1

    r "¿Quién—?"

    play sound "sfx/lights_back.mp3"
    scene pasillo_intermedio with flash

    show luz worry at centro_derecha
    show azura worried at right
    show nagi serio at centro_izquierda
    show cutipye serious at left
    show rodrigo shock_state at center

    l "Rodri, ¿estás bien?"

    menu:
        "La escuché otra vez.":
            $ estado_mental += 1

            if ruta_anterior == "nagi":
                # Farmea con Cutipye
                show cutipye worried
                c "¿La voz?"
                c "Yo te creo."
                c "No estás inventándolo."

                $ afinidad_cutipye += 2

            else:
                # Farmea con Nagi
                show nagi worried
                n "Vale. Bien."
                n "Entonces no estás loco."
                n "Algo está jugando contigo."

                $ afinidad_nagi += 2

        "Nada. Vámonos.":
            $ estado_mental -= 1
            r "Nada. Fue el ruido."

            if ruta_anterior == "nagi":
                show cutipye serious
                c "No me mientas."
                $ afinidad_cutipye += 1
            else:
                show nagi serio
                n "No me apartes, Rodrigo."
                $ afinidad_nagi += 1


    "Decidieron avanzar hacia una puerta semiabierta al fondo del pasillo."

    scene habitacion_abandonada with fade
    play ambient "sfx/room_tone.mp3"

    "Camas oxidadas."
    "Un crucifijo torcido colgando de la pared."
    "Un pequeño balcón al fondo."

    show azura neutral at right

    "Azura se apartó del grupo, revisando un archivador metálico."

    play sound "sfx/paper_pick.mp3"

    show azura shocked

    "Sus dedos encontraron una carpeta etiquetada como:"
    "{i}Proyecto Huésped – Casos Especiales{/i}"

    "Leyó en silencio."

    "{cps=18}Sujeto 12-A demuestra compatibilidad superior.
    No presenta rechazo celular.
    Adaptación progresiva.
    Posible simbiosis estable bajo control emocional.{/cps}"

    show azura worried

    "Azura dobló el papel."
    "No dijo nada."
    "Lo guardó en su bolsillo."

    "Mientras tanto, Nagi levantó una vieja Biblia del suelo."

    show nagi neutral

    n "Tiene un nombre escrito aquí."

    pause 0.5

    n "No es Galaxia."

    show cutipye serious

    c "Entonces… ese no era su nombre real."

    "Un cuaderno infantil cayó al abrir el cajón."

    l "Ella… vivía aquí."

    show luz sad

    n "Era una interna."

    pause 0.5

    c "...Era una huérfana."

    silencio

    n "¿Y si la hicieron así?"

    c "¿Y si no tuvo opción?"

    show rodrigo neutral at center

    "{cps=12}{color=#390169}{i}Yo también recé…{/i}{/color}{/cps}"

    $ estado_mental += 1

    r "(No.)"

    if ruta_anterior == "nagi":

        # Escena íntima con Cutipye
        show cutipye soft at center with move

        c "No quiero volver a perder a alguien."
        c "Ya es suficiente."

        r "No me voy a romper tan fácil."

        c "No me prometas eso."
        c "Prométeme que me vas a decir cuando empiece a pasar."

        $ afinidad_cutipye += 2

    else:

        # Escena íntima con Nagi
        show nagi soft at center with move

        n "Si algo te pasa, yo…"

        pause 0.5

        n "No soy bueno diciendo esto."
        n "Pero no pienso dejar que algo te arrastre."

        r "No soy tan fácil de arrastrar."

        n "Eso espero."

        $ afinidad_nagi += 2


    # --- ESCENA FINAL ---

    scene habitacion_abandonada_noche with fade
    stop ambient fadeout 2.0
    play music "music/quiet_night.mp3" fadein 2.0

    "Horas después."

    "El grupo descansaba en silencio."

    scene balcon_abandonado with dissolve

    show rodrigo neutral at center

    "Rodrigo salió al balcón oxidado."

    play sound "sfx/lighter.mp3"

    "Encendió un cigarrillo."

    "Su mano temblaba."

    show rodrigo shock_state

    "No por frío."

    "El humo se elevó…"
    "Y por un segundo pareció mezclarse con algo más oscuro."

    "{cps=10}{color=#390169}{i}Todavía no…{/i}{/color}{/cps}"

    $ estado_mental += 1

    "Rodrigo exhaló lentamente."
    "Pero su pulso no se estabilizó."

    scene black with fade

    call chapter_complete("Capítulo 7")

    return