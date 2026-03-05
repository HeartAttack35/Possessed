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
    scene bg_cuarto_maquinas
    show rodrigo shock_state at right
    show luz worry at left
    with dissolve

    "El costado le ardía. Bajó la mirada un instante."
    
    "Donde antes la sangre empapaba su ropa, ahora la tela estaba húmeda... Pero la herida parecía menos profunda."
    "Demasiado menos profunda."

    r "...No estaba así..."

    pause 0.5

    play ambient "sfx/wet_whisper.mp3" fadein 0.3
    centered "{cps=15}{color=#390169}{i}Casi... casi mía...{/i}{/color}{/cps}"
    stop ambient fadeout 0.5

    "Rodrigo parpadeó con fuerza."

    r "¿Escucharon eso...?"

    if estado_mental >= 6:
        show luz worry at centro_derecha with move
        show cutipye worried at left
        show nagi worried at centro_izquierda
        with moveinleft
        "Pero el único sonido era el goteo distante del lugar."

        n "Ey... Cálmate, hombre. No hay nada."
        c "No sobrepienses las cosas. Solo es el estrés."

        "Los otros se inclinaron hacia él como si esperaran una explicación, sus rostros marcados por la preocupación y el desconcierto."
        "Algo en su voz —tensa y quebrada— les hizo pensar que había más que un simple golpe; parecía un estado de shock."
        n "¿Te acuerdas de quién... o qué dijiste?"
        c "Respira, Rodri. Estamos acá."

    else:
        show luz worry at centro_derecha with move
        show cutipye neutral at left
        show nagi neutral at centro_izquierda
        with moveinleft
        "El único sonido seguía siendo ese goteo distante."

        n "Ok, tranquilo, no pasa nada."
        c "Probablemente fue el golpe, tómalo con calma."
        a "Ven, recuéstate un segundo."

        "Lo rodearon más suavemente, intentando reconfortarlo después del susto, como quien cuida a alguien que tuvo un mal rato."

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

    play music rodtheme fadein 1.5

    r "La verdad es que ambas opciones suenan como el comienzo de una historia que termina mal."
    r "Pero supongo que elegir no hacer nada tampoco nos va a teletransportar mágicamente afuera."

    "Mantuvo la mirada baja unos segundos más de lo normal."

    r "Así que sí."
    r "Vamos a hacer algo estúpido."
    r "Solo decidamos qué tipo de estupidez."

    menu:
        "Nagi tiene razón. Necesitamos información.":
            $ label_nagi = True
            $ afinidad_nagi += 1
            $ estado_mental += 1
            show rodrigo serio
            r "Si vamos a morir, prefiero hacerlo con un mapa en la mano."
            r "Al menos así podremos decir que fue una muerte organizada."
            "Su voz fue seca."
            "Demasiado seca."
            "No estaba intentando ser gracioso."
            jump ir_administracion
            
        "Cuty tiene razón. No podemos seguir adentrándonos.":
            $ afinidad_cutipye += 1
            $ estado_mental -= 1
            show rodrigo serio
            r "Ya tuvimos suficiente turismo oscuro por hoy."
            r "Retirarse no es cobardía."
            r "Es… estrategia con pulso funcional."
            "Forzó una media sonrisa."
            "Duró menos de un segundo."
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
            
    play sound door_open
    scene lavanderia_abandonada with dissolve

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

    if label_nagi == True:
        scene pasillo_intermedio with dissolve
    else:
        scene lavanderia_abandonada with dissolve
    play ambient "sfx/low_drone.mp3" fadein 1.5

    show rodrigo neutral at center
    show luz worry at centro_derecha
    show azura worried at right
    show nagi serio at centro_izquierda
    show cutipye serious at left

    "El edificio ya no se sentía igual."
    "El aire era más denso."
    "Más estrecho."

    if label_nagi == True:

        "El mapa que Nagi llevaba en la mano ya no coincidía del todo con el pasillo frente a ellos."

        show nagi annoyed
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
    scene pasillo_oscuridad
    show rodrigo neutral at center, oscuro
    show luz worry at centro_derecha, oscuro
    show azura worried at right, oscuro
    show nagi serio at centro_izquierda, oscuro
    show cutipye serious at left, oscuro
    with vpunch

    stop ambient
    play ambient "sfx/ringing.mp3"

    "Las luces se apagaron."

    l "¿Rodri?"

    pause 1.0
    play music ambiental fadein 1.0 volume 0.6

    "Oscuridad total."

    hide rodrigo
    show rodrigo shock_state at center
    with dissolve

    "{cps=10}{color=#390169}{i}Rodrigo…{/i}{/color}{/cps}"

    pause 0.5

    "{cps=12}{color=#390169}{i}Ellos no lo entienden…{/i}{/color}{/cps}"

    r "¿Quién—?"

    play sound "sfx/lights_back.mp3"
    scene pasillo_intermedio
    show luz worry at centro_derecha
    show azura worried at right
    show nagi serio at centro_izquierda
    show cutipye serious at left
    show rodrigo shock_state at center
    with flash

    l "Rodri, ¿estás bien?"

    menu:
        "La escuché otra vez.":
            $ estado_mental += 1
            r "Sí... la escuché."
            r "No estoy inventando esto."

            if ruta_anterior == "nagi":
                show cutipye worried
                $ afinidad_cutipye += 2
                c "¿La voz?"
                c "Yo te creo."
                c "No estás inventándolo."
                r "Gracias, Cuty. Sólo... no quiero parecer un loco."
                r "Necesito que alguien más lo confirme."
            else:
                show nagi worried
                $ afinidad_nagi += 2
                n "Vale. Bien."
                n "Entonces no estás loco."
                n "Algo está jugando contigo."
                r "¿Algo... o alguien?"
                r "Me da la sensación de que me observan."

            "Los demás se miraron entre sí, asintiendo con seriedad."
            n "Si necesitás que estemos más atentos, lo estaremos."
            c "No estás solo en esto."

        "Nada. Vámonos.":
            $ estado_mental -= 1
            r "No es nada. Fue un ruido."
            r "Si nos vamos, quizá nos calme."

            if ruta_anterior == "nagi":
                $ afinidad_cutipye += 1
                show cutipye serious
                "Cutipye apretó los labios y frunció el seño ligeramente; su silencio era una mezcla de incredulidad y dolor."
            else:
                $ afinidad_nagi += 1
                show nagi serio
                "Nagi frunció el ceño y negó con exageración, su expresión abierta de falta de creencia."

            "Nadie dijo nada más."
            "El aire pareció volverse más pesado mientras cada uno procesaba a su modo."


    "Decidieron avanzar hacia una puerta semiabierta al fondo del pasillo."

    scene habitacion_abandonada with fade
    play ambient "sfx/room_tone.mp3"

    "Camas oxidadas. Un crucifijo torcido colgando de la pared. Un pequeño balcón al fondo."

    show azura neutral at right

    "Azura se apartó del grupo, revisando un archivador metálico."

    play sound paper_flip

    show azura shocked

    "Sus dedos encontraron una carpeta etiquetada como:"
    """
    {cps=20}{b}Entrada 09 – Día 28{/b}{/cps}
    \n
    {cps=20}Cinco sujetos han mostrado una tolerancia parcial al patógeno. Los llamamos Huéspedes Activos.
    Presentan signos de mutación adaptativa: aumento de masa muscular, endurecimiento dérmico y cambios oculares.{/cps}
    """

    play sound paper_flip
    """
    {cps=20}También muestran comportamientos erráticos, violentos, territoriales.
    Uno de ellos arrancó el rostro de un investigador por mirarlo fijamente durante más de tres segundos. Protocolos de seguridad revisados.{/cps}
    """

    show azura worried

    "Azura dobló el papel."
    "No dijo nada."
    "Lo guardó en su bolsillo."

    "Mientras tanto, Nagi levantó una vieja Biblia del suelo."

    show nagi neutral at centro_izquierda

    n "Tiene un nombre escrito aquí."

    pause 0.5

    n "No es Galaxia."
    n "Dice... Shio Katashi."

    show cutipye serious at left

    c "Entonces… ese no era su nombre real."

    "Un cuaderno infantil cayó al abrir el cajón."

    l "Ella… vivía aquí."

    show luz sad at centro_derecha

    n "Era una interna."

    pause 0.5

    c "...Era una huérfana."

    "Silencio."

    n "¿Y si la hicieron así?"
    c "¿Y si no tuvo opción?"

    show rodrigo neutral at center

    "Rodrigo observó la Biblia en las manos de Nagi."

    "Varias páginas estaban gastadas."
    "Marcadas."
    "Subrayadas con trazos temblorosos."

    a "Hay una página doblada..."

    "Nagi la abrió con cuidado."

    pause 0.5
    play sound paper_flip
    show nagi surprised at centro_izquierda
    pause 0.5

    n '“¿Es mi heredad para mí como hiena manchada?'
    n "¿Están las aves de rapiña contra ella en derredor?"
    n "Venid, reunid todas las fieras del campo,"
    n 'venid a devorarla.”'

    "La palabra 'hiena' estaba subrayada una y otra vez."
    "La presión del lápiz había rasgado levemente el papel."

    pause 0.5

    "{cps=12}{color=#390169}{i}¿Lo ves ahora, Rodrigo?{/i}{/color}{/cps}"
    "{cps=12}{color=#390169}{i}Siempre estuvo escrito.{/i}{/color}{/cps}"

    r "(No.)"

    "{cps=12}{color=#390169}{i}Yo también recé…{/i}{/color}{/cps}"
    "{cps=12}{color=#390169}{i}Pedí ser salvada.{/i}{/color}{/cps}"
    "{cps=12}{color=#390169}{i}Pero Él me convirtió en la hiena.{/i}{/color}{/cps}"

    "El aire de la habitación se volvió pesado."
    "Rodrigo apartó la mirada del texto."

    r "(Es solo un versículo.)"
    r "(No significa nada.)"

    pause 0.8

    "{cps=12}{color=#390169}{i}Venid… reunid todas las fieras del campo…{/i}{/color}{/cps}"
    "{cps=12}{color=#390169}{i}Venid a devorarla.{/i}{/color}{/cps}"

    stop music fadeout 1.0

    scene habitacion_abandonada at slight_zoom with fade
    play music rodtheme fadein 3.0 volume 0.65
    play ambient forest fadein 3.0

    "El grupo se quedó en silencio varios minutos."
    "Nadie quería ser el primero en admitir que no sabían qué hacer después."

    scene rodrigo_cig_balcony with dissolve

    "Rodrigo se acercó al balcón oxidado."
    "El metal crujió bajo su peso, pero aguantó."

    "Afuera, la noche era absoluta."
    "Ni una luz. Ni un coche lejano. Ni siquiera el rumor del viento entre los árboles."

    "Solo negrura."

    r "(Esto no es normal… incluso para un bosque tan profundo.)"

    "Se llevó una mano al costado sin darse cuenta."
    "La herida palpitaba, pero no dolía como debería."
    "Era más bien… una presión. Algo que se expandía y contraía muy despacio."

    play sound heartbeat volume 0.8
    "Latido."
    
    play sound heartbeat volume 0.8
    "Latido."

    play sound heartbeat volume 0.8
    "Latido."

    "No era el suyo."

    r "…"

    menu:
        "Confesar que sientes la influencia.":
            $ afinidad_luz += 2
            $ afinidad_azura += 2
            $ afinidad_cutipye += 2
            $ afinidad_nagi += 2

            r "(Si me lo guardo... Puede que empeore.)"
            r "(No puedo arrastrarlos a esto sin decir nada.)"
            jump confesion_rodrigo
        
        "Mantenerlo en secreto.":
            $ estado_mental += 2
            r "(No.)"
            r "(Si lo digo en voz alta, se vuelve real.)"
            r "(Y no voy a darles una razón para que me miren como a los otros.)"

            "Rodrigo dió una fuerte calada a su cigarrillo, esperando que el tabaco calmara la presión en su pecho."
            "El latido dentro de su pecho se desaceleró."
            "O tal vez solo se acostumbró a él por un momento."
            jump ocultar_influencia

label confesion_rodrigo:
    scene rodrigo_cig_balcony_2 with dissolve

    "Se giró hacia el grupo."

    r "Chicos."

    "Todos alzaron la vista al mismo tiempo."
    "Algo en su tono los alertó antes de que dijera otra palabra."

    r "Creo que… deberíamos dormir por turnos."
    r "Y alguien tiene que quedarse despierto conmigo todo el tiempo."

    n "¿Por qué solo contigo?"

    r "Porque…"

    pause 1.2

    r "Porque creo que algo me está siguiendo."
    r "Y no está afuera."

    "Silencio."

    l "Rodri…"

    r "No estoy alucinando."
    r "O… quizás sí."
    r "Pero si estoy alucinando, entonces es mejor que alguien me vigile."
    r "Y si no estoy alucinando…"

    "Dejó la frase colgando."

    c "¿Qué sientes exactamente?"

    "Rodrigo dudó."
    "Buscó las palabras."

    r "Como si… alguien respirara dentro de mi caja torácica."
    r "Y cada vez que respiro yo… respira también."
    r "Al mismo tiempo."

    "Azura se abrazó a sí misma."

    a "Eso suena…"

    r "A locura. Lo sé."

    n "No."
    n "Suena a que estás infectado."

    "La palabra cayó como plomo."

    l "¡Nagi!"

    n "No lo digo para herirlo."
    n "Lo digo porque ya vimos qué les pasa a los que se infectan."
    n "Y si él está empezando…"

    r "Entonces hay que decidir qué hacemos conmigo antes de que sea tarde."

    "El grupo se miró entre sí."
    "Nadie quería decirlo en voz alta."

    c "Primero: nadie va a dispararte, apuñalarte ni dejarte tirado."
    c "Segundo: vamos a vigilarte. Todos."
    c "Tercero: si en algún momento empiezas a… cambiar… nos avisas."
    c "Y cuarto…"

    "Se acercó a él. Muy despacio."

    c "Si llega ese momento… prométeme que lucharás contra eso con todo lo que tengas."
    c "Porque no pienso perderte sin que al menos lo intentes."

    r "…Lo intentaré."

    "No era una promesa muy sólida."
    "Pero era lo único que podía dar."
    jump escena_luz_balcon_confesion

label ocultar_influencia:
    scene rodrigo_cig_balcony_2 with dissolve

    "Se giró hacia el grupo."

    r "Chicos."

    "Todos alzaron la vista."

    r "Deberíamos dormir por turnos."
    r "Este lugar no es seguro."

    n "Eso ya lo sabemos."
    n "¿Algo más?"

    r "No."
    r "Solo… eso."

    "Nagi lo observó unos segundos más."
    "Como si esperara que dijera algo adicional."

    "Rodrigo sostuvo la mirada."
    "No parpadeó."

    "El latido volvió."

    play sound heartbeat fadein 1.0 loop

    "{cps=9}{color=#390169}{i}Mentiroso…{/i}{/color}{/cps}"

    r "(Cállate.)"

    "Mientras el grupo discutía rutas de escape y posibles salidas del orfanato…"

    c "Si encontramos el ala administrativa, quizá haya planos."
    n "O una salida trasera que no esté bloqueada."
    l "Tenemos que movernos antes del amanecer."

    "Rodrigo apenas escuchaba."

    "La conversación se sentía lejana."
    "Como si estuviera ocurriendo al final de un túnel."

    "{cps=9}{color=#390169}{i}No necesitan saberlo todavía…{/i}{/color}{/cps}"

    r "(No estoy perdiendo el control.)"
    r "(Todavía no.)"

    stop sound fadeout 1.0

    jump escena_luz_balcon_oculta

label escena_luz_balcon_confesion:
    scene balcon_abandonado_night
    show rodrigo worried at centro_derecha
    with dissolve

    "Más tarde."

    "Rodrigo seguía en el balcón."
    "Luz se sentó a su lado, hombro con hombro."

    show luz sad at centro_izquierda
    with moveinleft

    l "No tienes que cargar con esto solo."

    r "No quiero que me vean… cuando pase."

    l "Entonces no mires hacia otro lado cuando me mires a mí."
    l "Mírame ahora."

    "Rodrigo giró la cabeza con lentitud."

    "Los ojos de Luz brillaban bajo la luz mortecina."
    "No había miedo en ellos."
    "Solo determinación."

    l "Sea lo que sea que esté intentando meterse en ti…"
    l "Va a tener que pasar por encima de mí primero."

    "Rodrigo dejó escapar una risa rota."

    r "Eres terrible mintiendo."

    l "No estoy mintiendo."
    l "Estoy amenazando a un parásito."

    "Se quedaron en silencio."

    "El viento trajo un olor extraño."
    "Dulce. Metálico. Familiar."

    play sound "sfx/drip_distant.mp3"

    "Una gota cayó desde el techo del balcón."
    "Aterrizó en el dorso de la mano de Rodrigo."

    "No era agua."

    show rodrigo scared

    "Era negra."
    "Y se movía."

    "Muy despacio."
    "Como si tuviera intención."

    r "Luz…"

    "Ella ya lo estaba viendo."

    l "No te muevas."

    "La gota se deslizó hacia su muñeca."
    "Y desapareció bajo la piel."
    "Sin dejar marca."

    "Rodrigo cerró los ojos con fuerza."

    "{cps=9}{color=#390169}{i}Shhh…{/i}{/color}{/cps}"
    "{cps=9}{color=#390169}{i}Ya casi estamos en casa…{/i}{/color}{/cps}"

    "Cuando volvió a abrir los ojos…"

    "La gota ya no estaba."

    "Pero su mano temblaba."

    "Y por primera vez…"
    "No estaba seguro de quién la estaba moviendo."

    scene black with fade
    stop music fadeout 4.0
    stop ambient fadeout 2.0

    call chapter_complete("Capítulo 7")
    jump cap_8

label escena_luz_balcon_oculta:

    scene balcon_abandonado_night
    show rodrigo worried at centro_derecha
    with dissolve

    "Más tarde."

    "Rodrigo seguía en el balcón."
    "Tenía los brazos apoyados en la baranda, rígido."
    "Demasiado quieto."

    show luz serious at centro_izquierda
    with moveinleft

    l "Rodri."

    "Él no respondió."

    l "No hagas eso."

    r "¿Qué cosa?"

    l "Desaparecer aunque estés aquí."

    pause 0.5

    r "Estoy bien."

    l "No."
    l "Estás funcionando."
    l "Que no es lo mismo."

    "Rodrigo apretó la mandíbula."

    r "No hay nada que decir."

    l "Soy tu pareja."
    l "Merezco saber cómo te sientes."
    l "Sea bueno o malo."
    l "En especial si es más probable que sufras una crisis de pánico en cualquier momento."

    "El viento golpeó el balcón con un quejido largo."

    r "No voy a tener una crisis."

    l "Te conozco."
    l "Cuando te muerdes el interior de la mejilla así…"
    l "Es porque estás conteniendo algo."

    pause 0.5

    l "No tienes que protegerme de lo que te pasa."
    l "No soy de cristal."

    r "No intento protegerte."

    l "Entonces ¿qué haces?"

    "Silencio."

    play sound "sfx/heart_slow.mp3" fadein 1.5 loop

    "Latido."

    "Rodrigo cerró los ojos un segundo de más."

    "{cps=9}{color=#390169}{i}Díselo.{/i}{/color}{/cps}"

    "{cps=9}{color=#390169}{i}Quiero ver su cara cuando lo entienda…{/i}{/color}{/cps}"

    r "(Cállate.)"

    l "¿Qué dijiste?"

    r "Nada."

    "Luz dio un paso más cerca."

    l "Rodrigo."
    l "Si te estás quebrando por dentro, prefiero saberlo."
    l "Prefiero sostenerte ahora que recoger los pedazos después."

    "Sus ojos brillaban, pero esta vez sí había algo más."
    "Miedo."

    l "No me excluyas."
    l "No me castigues con silencio."

    "Rodrigo la miró."
    "Por un momento pareció que iba a hablar."

    pause 1.0

    r "Si empiezo a perder el control…"
    r "No quiero que tu última imagen mía sea esa."

    l "Entonces dame algo mejor que recordar ahora."

    "El aire se volvió denso."

    play sound "sfx/drip_distant.mp3"

    "Una gota cayó desde el techo del balcón."
    "Aterrizó en el dorso de la mano de Rodrigo."

    show rodrigo scared

    l "…Rodri."

    "La sustancia era negra."
    "Y se movía."

    "Muy despacio."

    l "No te muevas."

    "La gota avanzó hacia su muñeca."
    "Y desapareció bajo la piel."

    stop sound fadeout 1.0

    "Rodrigo contuvo el aliento."

    "{cps=9}{color=#390169}{i}¿Ves?{/i}{/color}{/cps}"
    "{cps=9}{color=#390169}{i}Ni siquiera ahora puedes decírselo todo…{/i}{/color}{/cps}"

    "Luz tomó su mano con fuerza."

    l "Mírame."
    l "Respira conmigo."

    "Inhalaron."
    "Exhalaron."

    "Otra vez."

    "La mano de Rodrigo temblaba."

    r "No sé si…"
    r "No sé si soy solo yo aquí dentro."

    "Luz no soltó su mano."

    l "Entonces vamos a averiguarlo juntos."

    "Pero esta vez…"

    "Rodrigo no estaba seguro de si eso seguía siendo verdad."

    scene black with fade
    stop music fadeout 4.0
    stop ambient fadeout 2.0

    call chapter_complete("Capítulo 7")
    jump cap_8

label cap_8:

    scene black with fade
    stop music fadeout 2.0

    scene habitacion_abandonada_dawn with dissolve
    play ambient forest fadein 3.0 volume 0.4

    "El amanecer se filtró a través de las ventanas rotas como un velo gris, cargado de partículas de polvo que bailaban en el aire estancado."
    "No traía calidez. Solo una luz fría que hacía las sombras más largas."

    "El grupo yacía disperso en el suelo polvoriento."
    "Agotados. Inmóviles."
    "Como si el orfanato los hubiera drenado durante la noche."
    python:
        afinidades = {
            "nagi": afinidad_nagi,
            "cutipye": afinidad_cutipye,
            "azura": afinidad_azura,
            "luz": afinidad_luz
        }
        # Prioridad en empates: nagi, cutipye, azura, luz
        prioridad = {"nagi": 0, "cutipye": 1, "azura": 2, "luz": 3}
        min_afinidad_personaje = min(afinidades.keys(), key=lambda k: (afinidades[k], prioridad.get(k, 999)))

    if min_afinidad_personaje != "luz": # Raro, pero posible si afinidad baja
        show luz neutral at centro_derecha
    if min_afinidad_personaje != "azura":
        show azura neutral at right
    if min_afinidad_personaje != "nagi":
        show nagi neutral at centro_izquierda
    if min_afinidad_personaje != "cutipye":
        show cutipye neutral at left
    with dissolve

    "Uno a uno, comenzaron a moverse."
    "Luz se incorporó primero, frotándose los ojos."
    "Azura murmuró algo sobre un sueño extraño."
    "Nagi estiró los brazos con un gruñido."
    "Cutipye se sentó, revisando su mochila instintivamente."

    "Pero Rodrigo y [min_afinidad_personaje!c]…"

    "Aún no se movían."
    "Como si el sueño los hubiera retenido un poco más."

    show rodrigo neutral at center with dissolve

    "Rodrigo abrió los ojos. No hubo el parpadeo perezoso de quien despierta de un sueño, sino la apertura súbita de una lente."
    "Su mirada no buscó a sus compañeros, ni la salida. Se clavó en las vigas del techo, donde la madera se astillaba hacia la oscuridad del ático."

    r "(Demasiado expuesto abajo…)"
    r "(En el suelo eres vulnerable. En el suelo eres comida.)"

    "Sentía una extraña rigidez en la nuca, un impulso eléctrico que le recorría los omóplatos, como si sus músculos recordaran una anatomía que nunca habían tenido."

    $ estado_mental += 1

    if min_afinidad_personaje == "nagi":
        show nagi tired at centro_izquierda with dissolve
        n "Ugh… ¿Ya amaneció?"
        n "Siento como si me hubieran pisoteado."
    elif min_afinidad_personaje == "cutipye":
        show cutipye tired at left with dissolve
        c "¿Qué hora es?"
        c "Esto no fue una buena idea para dormir."
    elif min_afinidad_personaje == "azura":
        show azura tired at right with dissolve
        a "…Mi cabeza."
        a "Tuve un sueño horrible."
    elif min_afinidad_personaje == "luz":
        show luz tired at centro_derecha with dissolve
        l "Rodri…"
        l "¿Dormiste algo?"

    "Rodrigo no respondió de inmediato."
    "Solo se levantó con un movimiento fluido."
    "Demasiado fluido para alguien que acababa de caer de un derrumbe el día anterior."

    r "Vamos."
    r "Hay que moverse."

    "Su voz era seca, carente de la inflexión de preocupación que solía tener."
    "Pero sus ojos seguían volviendo al techo."
    
    stop ambient fadeout 1
    scene pasillo_dawn with fade
    play sound walk loop volume 0.6
    play music "music/tense_exploration.mp3" fadein 2.0 volume 0.5

    "El grupo reanudó la búsqueda de una salida."
    "Los pasillos parecían más laberínticos bajo la luz diurna."
    "Como si el orfanato se reorganizara mientras dormían."

    show rodrigo neutral at center
    show luz neutral at centro_derecha
    show azura neutral at right
    show nagi neutral at centro_izquierda
    show cutipye neutral at left
    with dissolve

    "Rodrigo caminaba al frente, pero sus pasos eran irregulares."
    "Se detenía de pronto, inclinando la cabeza ligeramente."
    "Como si escuchara algo que nadie más percibía."

    play sound "sfx/distant_scratch.mp3" volume 0.3

    r "…"
    l "¿Qué pasa?"

    if estado_mental < 4:  # Bajo: Racionaliza
        r "Nada. Solo… el viento."
        r "(Fatiga. Eso es todo.)"
        $ estado_mental += 1

    elif estado_mental < 11:  # Medio: Sensación mixta
        r "Escuché algo."
        r "Arriba."
        r "(Ligero… como si pudiera flotar sobre eso.)"
        $ estado_mental += 1

    else:  # Alto: Disfruta claridad
        r "Está en las paredes. Se arrastra. Puedo oler el almizcle de su pelaje."
        r "(Puedo escuchar… todo.)"
        $ estado_mental += 2

    "Continuaron."
    "Rodrigo parpadeaba menos."
    "Sus ojos se fijaban en detalles altos: grietas en el techo, lámparas colgantes."

    "En un momento, ante una escalera derruida…"

    r "Subamos."
    n "¿Para qué? La salida está abajo."
    r "…"

    "Sintió un impulso."
    "Estirar la espalda."
    "Sentir el aire desde arriba."
    "Ligereza en los huesos."

    if estado_mental < 10:
        r "Mejor no. Sigamos."
    else:
        $ estado_mental += 1
        r "(Arriba… seguro.)"

    stop sound fadeout 1.0

    scene vestibulo_dawn with fade

    "Llegaron al vestíbulo principal."
    "Un espacio cavernoso donde el aire circulaba con un silbido gélido."
    "Dos pisos de altura, escaleras curvadas a los lados."
    "El vacío central del vestíbulo parecía llamar a Rodrigo. Sus ojos escaneaban las barandillas del piso superior con una precisión casi geométrica."

    show cutipye neutral at left
    c "Dividámonos para cubrir más—"

    hide rodrigo
    show rodrigo neutral at center with moveinright  # Ya se mueve

    "Pero Rodrigo no esperó. Sus pasos eran silenciosos, apoyando primero la punta del pie, como si evitara alertar a algo que todavía no veía."

    l "¿Rodri?"
    r "Necesito altura. Mejor vista."

    "Simple. Seco. Funcional."

    "Pero en su mente…"
    "(Sentinela. Vigilar. Alto.)"

    $ estado_mental += 1

    "Subió al segundo piso. Sus manos rozaron la madera de la bandilla y sus dedos se curvaron, casi como garras buscando tracción."
    "Mirando abajo, evaluando distancias."

    play sound "sfx/scratch_wood.mp3" volume 0.8

    "Un sonido."
    "Uñas contra madera."
    "Espasmódico. Rápido."

    show rata_mutant at right with moveinbottom  # Emerge de las sombras

    "La criatura surgió de una puerta lateral."
    "No era una rata. No era un hombre. Era un monstruo de piel estirada y espinazos expuestos."
    "Sus ojos, dos puntos de rubí podrido, se fijaron en [min_afinidad_personaje!c]."
    "La criatura emitió un chirrido agudo, un sonido que vibró en los dientes de todos los presentes. Se agazapó, sus patas traseras -demasiado largas para su torso- se tensaron para el salto."

    # Ataca al de menor afinidad
    if min_afinidad_personaje == "nagi":
        show rata_mutant at centro_izquierda with moveinright
        n "¡Mierda!"
    elif min_afinidad_personaje == "cutipye":
        show rata_mutant at left with moveinright
        c "¡Atrás!"
    elif min_afinidad_personaje == "azura":
        show rata_mutant at right with moveinright
        a "¡No!"
    elif min_afinidad_personaje == "luz":
        show rata_mutant at centro_derecha with moveinright
        l "¡Rodri!"

    stop music
    play music chase fadein 0.5

    if estado_mental < 10:  # COMBATE HUMANO
        scene vestibulo_fight_normal with dissolve
        play sound "sfx/human_scream.mp3"
        
        "La criatura saltó. Rodrigo reaccionó con la torpeza del miedo, lanzándose desde el rellano hacia el cuerpo del mutante."
        "Cayeron en un revoltijo de extremidades y polvo. Rodrigo forcejeaba, sintiendo el aliento fétido y caliente de la rata contra su cuello."
        
        r "¡Atrás! ¡Hijo de puta!"

        "Enterró la daga en el hombro de la bestia. No fue un golpe limpio. Fue un tajo desesperado que apenas logró separarlos."
        "Rodrigo retrocedió jadeando, la adrenalina quemándole las venas mientras veía a la criatura lamerse la herida con una lengua negra y bífida."
        
        play sound "sfx/stab.mp3"
        with vpunch

    elif estado_mental < 15:  # COMBATE SINTETIZADO (Crow vs Rat)
        show layer master at distortion_light # ACTIVAR DISTORSIÓN LIGERA
        scene vestibulo_fight_saturated with dissolve
        play sound "sfx/beast_growl.mp3"

        "El mundo se volvió más brillante, más nítido. Los colores de la sangre y el moho saltaron a la vista de Rodrigo con una intensidad violenta."
        "La criatura se lanzó hacia [min_afinidad_personaje!c], pero Rodrigo ya estaba en el aire."

        "No fue un salto humano. Fue un picado."
        "Rodrigo aterrizó sobre la espalda del mutante, sus pies buscando instintivamente los puntos de apoyo en los omóplatos. La daga bajó como un pico, buscando los ojos, buscando la base del cráneo."

        r "(Ciega al rastrero. Quiebra sus patas.)"

        "El mutante chilló y se revolvió, pero Rodrigo se mantenía pegado a su espalda con una agilidad antinatural, girando la cabeza con movimientos rápidos y espasmódicos."
        
        play sound "sfx/slash_rough.mp3"
        with shake

    else:  # COMBATE BRUTAL / PREDADOR (The Raven's Feast)
        show layer master at distortion_heavy # ACTIVAR DISTORSIÓN PESADA
        scene vestibulo_fight_glitch with dissolve
        play sound "sfx/primal_screech.mp3"

        "La realidad se fracturó. La tonalidad del mundo viró hacia un espectro enfermo, donde el calor de la presa era lo único que importaba."
        "Rodrigo no gritó. Emitió un chasquido seco desde el fondo de su garganta mientras se lanzaba desde la barandilla."

        "El impacto contra el huésped-ratón fue brutal. El sonido de los huesos de la criatura rompiéndose bajo el peso de Rodrigo resonó en todo el vestíbulo."
        "Fue una ejecución, no una pelea."

        "Rodrigo sujetó la cabeza del mutante con una mano, forzándola hacia atrás para exponer el cuello, mientras su otra mano hundía la daga una, dos, tres veces. Movimientos cortos. Precisos. Despiadados."
        "Como un cuervo destripando a una rata en un callejón, Rodrigo no se detuvo cuando la criatura dejó de luchar. Sus ojos estaban fijos, sin parpadear, reflejando una sed que no era suya."

        play sound "sfx/impact_heavy.mp3"
        with hpunch
        play sound "sfx/stab_repeated.mp3"
        with vpunch

    show layer master
    scene vestibulo_aftermath with fade
    stop music fadeout 2.0
    play ambient "sfx/heavy_breathing.mp3" loop

    "El silencio que siguió fue peor que el ruido de la pelea."
    "La criatura era una masa irreconocible de carne y pelaje negro. La sangre se filtraba entre las tablas del suelo, goteando hacia el piso inferior."

    show rodrigo bloodied at center with dissolve

    "Rodrigo permanecía en cuclillas sobre el cadáver."
    "Sus dedos goteaban icor. Sus pulmones trabajaban con un ritmo mecánico, pesado."

    "El grupo lo miró. Nadie se acercó."

    if min_afinidad_personaje == "nagi":
        show nagi shocked at centro_izquierda
        n "Rodri... eso no fue defenderse. Eso fue... carnicería."
    elif min_afinidad_personaje == "cutipye":
        show cutipye shocked at left
        c "Parecías... disfrutándolo. Tu cara..."
    elif min_afinidad_personaje == "azura":
        show azura shocked at right
        "Azura se tapó la boca con la mano, sus ojos fijos en la forma en que Rodrigo inclinaba la cabeza, examinando los restos."
    elif min_afinidad_personaje == "luz":
        show luz shocked at centro_derecha
        l "…¿Rodrigo? Por favor, mírame."

    "Rodrigo levantó la mirada."
    "Por una fracción de segundo, la luz del amanecer incidió en sus pupilas, revelando un brillo aceitoso, negro, que devoraba cualquier rastro de humanidad."
    
    r "Está muerto. Es lo que importa."

    scene black with fade
    stop ambient fadeout 2.0

    call chapter_complete("Capítulo 8")
    jump cap_9

label cap_9:

    # Transición al flashback: Un recuerdo de una fiesta pasada para "farmear" afinidades.
    scene black with fade
    "Antes de todo esto, en tiempos más simples..."
    scene fiesta_flashback with dissolve  # Imagen de una fiesta animada, perhaps en un salón o casa.
    play music "bgm/nostalgic_party.mp3" fadein 1.0

    # Escena 1: Interacción con Nagi – Energía juguetona, incrementa afinidad.
    "Nagi bailaba con energía, arrastrándote al centro de la pista. Su risa era contagiosa, y por un momento, olvidaste tus libros."
    $ afinidad_nagi += 2  # Incremento: Refleja conexión divertida.

    # Escena 2: Interacción con Azura – Conversación profunda, incrementa afinidad.
    "Azura compartía un rincón tranquilo, hablando de estrellas y sueños. Sus palabras te hicieron sentir comprendido."
    $ afinidad_azura += 1  # Incremento: Refleja empatía intelectual.

    # Escena 3: Interacción con Cutipye – Ayuda práctica, incrementa afinidad.
    "Cutipye te ayudó a preparar bebidas, su enfoque meticuloso complementaba tu torpeza. Fue un equipo silencioso pero efectivo."
    $ afinidad_cutipye += 2  # Incremento: Refleja confianza práctica.

    # Escena 4: Interacción con Luz – Momento tierno, incrementa afinidad (más enfocado, ya que es clave).
    "Luz te tomó de la mano durante un juego, su calidez te hizo sonreír. En esa fiesta, todo parecía posible."
    $ afinidad_luz += 1  # Incremento moderado: Mantiene el rango 2-7 asumiendo progresión previa.

    # Fin del flashback: Desvanecimiento nostálgico.
    "Pero esos recuerdos ahora parecen lejanos, eclipsados por el horror del orfanato."
    stop music fadeout 2.0
    scene vestibulo_dawn
    show rodrigo frustrado at center
    show luz worry at centro_derecha
    show azura worried at right
    show nagi serio at centro_izquierda
    show cutipye serious at left
    with fade  # Escena del vestíbulo después de la pelea, con el mutante derrotado en el suelo.
    #play music "bgm/tense_confrontation.mp3" fadein 1.0
    play music ambiental fadein 1.0

    "El vestíbulo huele a óxido y carne abierta."
    "El cuerpo de la criatura yace a unos metros. Demasiado destrozado."
    "{cps=15}Demasiado... Irreconocible...{/cps}"

    "Las manos de Rodrigo todavía tiemblan."
    "No sabía bien si era por el esfuerzo..."
    "...o por lo que disfrutó durante un segundo."

    n "¡¿Qué ha sido eso?! ¡El ratón de biblioteca que conozco no hubiera acabado con esa bestia ni con la adrenalina de la muerte encima, mucho menos dejar su cráneo como queso suizo!"
    "Nagi señala el cadáver. Evita mirar directamente a Rodrigo."

    a "¿No creen que tras lo que haya pasado tenga sentido que empiece a decir que 'escucha voces'? O sea, dudo que le esté dando lo mismo que a las bestias del orfanato, podría ser solo la adrenalina o el pánico."

    a "...o no, Cuty?"

    pause 1.0

    c "Miren, ya no tiene tanto caso el decir si Rodrigo tenía razón o no, venir a este orfanato fue una idea estúpida y debemos irnos cuanto antes."

    "No se acercan a él."
    "Forman un semicírculo."
    "Como si fuera el siguiente peligro."

    l "¡Esperen! Rodrigo no es así... él solo nos protegió. No lo juzguen tan rápido."
    n "¡Pero míralo, Luz! Está cubierto de sangre, como un animal!"
    l "¡No! Es nuestro amigo, y lo que hizo fue por nosotros. Denle una oportunidad de explicarse."

    pause 1.5

    "Rodrigo trató de hablar."
    pause 0.7
    "Su garganta arde."

    r "Yo... yo no-"

    show screen screen_distortion_light   # (placeholder visual)
    play sound "sfx/voices_overlapping.mp3"  # Voces distorsionadas de amigos.
    play ambient glx_laugh loop  # Risa descarada de Galaxia, en loop bajo.
    with hpunch
    "Las voces se superponen."
    "Demasiado fuertes."
    "Demasiado cerca."

    g "Ja ja ja... ¿Ves? Tus 'amigos' te temen ahora. Son tan frágiles~"
    "Tu visión parpadea."
    "El vestíbulo parece inclinarse."
    "Los bordes de la imágen se saturan."
    "Los colores se intensifican hasta hacerse irreales."
    "Como si el mundo no soportara la velocidad de sus pensamientos."

    play sound heartbeat loop
    "El pulso del castaño se dispara."
    play sound heartbeat loop
    "Algo empezó a empujar desde dentro."
    play sound heartbeat loop
    "Algo quiere salir."

    a "Tal vez sea el estrés acumulado, pero esto no es normal."
    c "Luz, esto es peligroso. Debemos irnos antes de que... algo peor pase."
    l "¡Basta! Rodrigo ha pasado por mucho. Todos lo hemos hecho. Apóyenlo en vez de atacarlo."
    l "¡No lo abandonaremos! Él nos necesita."

    "La palabra 'abandonar' retumba."
    "Se deforma."
    "Se estira."
    "Se convierte en eco."

    hide screen screen_distortion_light
    show screen screen_distortion_heavy

    "La risa de Galaxia se vuelve más clara."
    "Más cercana."
    "Como si respirara tras del cuello de Rodrigo."

    centered "Hazlo. Demuéstrales lo que eres."

    centered "No."
    centered "No quiero."
    centered "No soy eso."

    "Pero el miedo no suena humano."
    "Suena como un gruñido bajo su pecho."

    "La mirada de Rodrigo recorrió la de los demás."
    "Nagi retrocede medio paso."
    "Azura aprieta los labios."
    "Cutipye calcula distancias."
    "Luz... se acerca."

    "Ellos tienen miedo."
    "Por él."
    "{b}De él.{/b}"

    "La culpa cae como plomo en su estómago."
    centered "¿En qué te estás convirtiendo?"
    centered "¿Y si Galaxia tiene razón?"
    centered "¿Y si ya cruzaste una línea invisible?"

    "Su respiración se acelera."
    "Demasiado rápido."
    "Demasiado fuerte."

    "El mundo comienza a ir más rápido que él."
    "O él más rápido que el mundo."
    "No lo sabe."

    "Luz da un paso más."
    "Extiende la mano con cuidado."
    "Como si se acercara a un animal herido."

    l "Rodrigo... tranquilo... estamos contigo."

    "Su mano toca a Rodrigo por el hombro."

    #play sound "sfx/violent_reaction.mp3"
    play sound slash
    stop music
    with hpunch
    "El contaxto quema."

    r "¡N-no to-!"

    "No ve a Luz."
    "Ve una sombra acercarse."
    "Una amenaza."
    "Un ataque."

    "El cuerpo de Rodrigo reaccionó antes que su mente."
    "Un reflejo primitivo."
    "Una embestida desesperada."

    stop ambient fadeout 0.7  # Detiene la risa de Galaxia abruptamente.
    play sound thud
    hide screen screen_distortion_heavy

    "El golpe resuena en el vestíbulo."
    "Seco."
    "Hueco."

    # Reacciones horrorizadas de todos.
    play music rodtheme fadein 1.5
    c "¡Luz! ¡No!"
    n "¡Dios mío!"
    a "Qué... Has hecho..."

    "La sangre comienza a extenderse bajo ella."
    "Roja."
    "Imposible de ignorar."

    "El tiempo vuelve a su velocidad normal."
    "Y con Rodrigo dentro."

    r "(No...)"
    r "(No no no no...)"

    centered "Tus manos."
    centered "{cps=10}{b}Tus malditas manos.{/b}{/cps}"

    scene closeup_luz_dying with dissolve  # Close-up de Luz herida.
    if afinidad_luz < 3:
        l "Rodrigo... duele... ¿por qué?"  # Mínimo afecto: Confusión y dolor.
    elif afinidad_luz == 4:
        l "No... fue un accidente... lo sé..."  # Ligeramente más comprensiva.
    elif afinidad_luz == 5:
        l "Rodrigo, no te culpes... fuiste fuerte por nosotros."  # Empieza a mostrar apoyo.
    elif afinidad_luz == 6:
        l "Te... aprecio tanto... no dejes que esto te destruya."  # Afecto moderado, preocupación por él.
    elif afinidad_luz == 7:
        l "Rodri... Amor... siempre estaré contigo en espíritu."  # Alto afecto, conexión emocional.
    elif afinidad_luz == 8:
        l "Te quiero... Rodrigo. No olvides nuestros momentos... vive por mí."  # Máximo afecto: Amor y legado.

    if afinidad_luz >= 6:
        "Sus dedos buscan los de él."
        "Incluso ahora."
        "Incluso mientras la vida se le escapa."

        pause 1

        "Recuerda su risa en la escuela."
        "Las tardes estudiando juntos."
        "Las caminatas bajo la lluvia."
        "Cómo fingía molestarse cuando la llamaba exagerada."
        "Cómo lo miraba cuando creía que no la veía."

        pause 1

        "Ella fue quien integró a Rodrigo al grupo."
        "Quien insistió en que era más que sus silencios."
        "Quien creyó en él incluso cuando él no lo hacía."

        pause 1

        "Y ahora..."
        "La está sosteniendo mientras su luz se apaga."

    # Fin: Rodrigo llora sosteniéndola.
    play sound "sfx/crying.mp3"
    "Su peso se siente distinto."
    "Más frágil."
    "Más... Final..."
    r "¡Luz! ¡Díme algo... por favor!"
    r "¡No me dejes... no así...!"

    "Las lágrimas de Rodrigo caían sobre el rostro de Luz."
    "Pero ella ya no responde."

    "La risa de Galaxia no vuelve."
    "No hace falta."
    "El silencio es peor."

    pause 1

    scene black with fade
    stop music fadeout 2.0
    stop ambient fadeout 2.0

    call chapter_complete("Capítulo 9")
    jump cap_10

label cap_10:

    # Fondo: pasillo derruido, luces parpadeando (deberías tener una imagen o varias para variación)
    scene bg pasillo_derruido with fade
    play music "audio/ambience/pasillo_tenso.ogg" fadein 2.0 loop   # música de fondo tensa opcional

    "El pasillo administrativo está medio derrumbado. El techo cruje. Las luces parpadean con ese zumbido eléctrico insoportable."

    "Rodrigo camina último."
    "Sus pasos son más pesados que antes."
    "Respira mal."
    "Se detiene cada cierto tiempo, como si estuviera escuchando algo que los demás no oyen."

    show azura worried at left with dissolve

    a "Rodri… ¿estás bien?"

    "Rodrigo tarda en responder. Su voz sale rasposa."

    r "Sí. Solo… sigan caminando. No se separen."

    "Se lleva una mano al pecho. Las uñas raspan la tela de su ropa sin que él lo note."

    show cutipye at right with dissolve

    c "(en voz baja) Está empeorando…"

    "Nagi se detiene en seco."
    "Se gira."
    "Lo mira con una mezcla de miedo y rabia contenida."

    # Aquí empieza la decisión clave
    if afinidad_nagi < 3:
        jump traicion_nagi
    else:
        # Ruta alternativa: Nagi se queja pero no abandona (o lo que decidas)
        jump nagi_no_traiciona

label traicion_nagi:

    n "¿Sabes qué? Ya basta."

    "El grupo se detiene."

    a "¿Nagi…?"

    n "(señalando a Rodrigo) Desde que esto empezó, todo gira en torno a él."
    n "Sus ataques."
    n "Sus cambios de humor."
    n "Sus… cosas raras."

    "Rodrigo baja la mirada."
    "Intenta hablar, pero su mandíbula se tensa antes de que pueda articular bien."

    r "No estoy… perdiendo el control."

    "Pero incluso mientras lo dice, su pupila parece dilatarse un poco más."

    "Da un paso al frente. Uno lento. Forzado."

    r "Escuchen."
    r "No me gusta esto tampoco."
    r "No pedí… nada de esto."

    "Traga saliva."
    "Su voz suena más grave por momentos."

    r "Pero si nos dividimos, estamos muertos."
    r "Galaxia quiere eso."
    r "Separarnos."

    "Se apoya contra la pared."
    "Respira profundo."

    r "(casi suplicando) Yo puedo aguantar."
    r "Solo… manténganse cerca."
    r "Si pierdo el control… me detienen."
    r "Pero no se vayan."

    "Por un segundo, hay silencio."
    "Azura lo mira con lágrimas contenidas."
    "Cutipye también."
    "Pero Nagi no."

    "Nagi suelta una risa seca."

    n "¿Aguantar?"
    n "¿Eso dices desde hace horas?"

    "Da un paso hacia Rodrigo."

    n "Te tiemblan las manos."
    n "Nos miras como si fuéramos comida."
    n "Mataste a—"

    "Se detiene antes de terminar la frase."
    "Silencio pesado."

    "Rodrigo baja la cabeza."

    n "¿Sabes qué? Siempre has sido así."

    "Todos lo miran, confundidos."

    n "¿Recuerdan esa vez que se emborrachó hasta casi morirse?"

    # Flashback breve
    scene bg flashback_rodrigo_borracho with dissolve
    "Rodrigo inconsciente. Vomitando."
    "Luz llorando."
    "Nagi sosteniéndolo para que no se ahogara."
    scene bg pasillo_derruido with dissolve

    n "(voz quebrada de rabia) ¡Debí dejar que te ahogaras en tu vómito, animal!"

    "El golpe emocional es brutal."

    a "¡Nagi!"

    "Rodrigo no responde."
    "No puede."
    "Sus uñas ahora sí atraviesan la tela de su manga."

    n "Siempre hay que salvarte."
    n "Siempre hay que cuidarte."
    n "Siempre hay que entenderte."

    "Mira al resto."

    n "¿Y quién nos salva a nosotros?"

    "Silencio."
    "Nadie responde."

    n "(más bajo) Yo no voy a morir porque él no puede controlarse."

    "Da media vuelta."

    n "Si quieren seguir con este retrasado, bien."
    n "¡Pero yo me voy!"

    # Reacciones
    r "(forzando la voz) ¡Nagi, espera!"

    n "(sin girarse) ¡Cállate!"

    a "(corriendo hacia él) ¡No hagas esto! ¡No ahora!"

    "Lo sujeta del brazo."
    "Nagi la aparta con brusquedad, pero sin violencia."

    n "Luz… míralo."
    n "No es él."

    a "Podemos buscar otra ruta."
    a "Podemos… atarlo si es necesario."
    a "Pero no nos dejes."

    "Nagi duda."
    "Por un segundo, realmente duda."

    c "Tiene razón."

    "Todos la miran."
    "Incluso Nagi."

    c "Yo lo quiero…"
    c "Pero también tengo miedo."

    "Mira a Rodrigo."
    "No con odio."
    "Con tristeza."

    c "No sé si podamos detenerlo si se transforma del todo."

    "Ese comentario duele más que el grito de Nagi."
    "Rodrigo lo sabe."

    n "Gracias."

    "Se suelta de Azura."   # corregí "Luz" por Azura según tu texto reciente

    n "No voy a arrastrarlos conmigo."
    n "Pero tampoco voy a quedarme esperando a que él termine lo que empezó esa cosa."

    "Se adentra solo en el ala izquierda del pasillo."

    scene bg pasillo_oscuro with dissolve

    "Oscuridad."
    "El sonido de sus pasos alejándose."

    play sound "audio/sfx/pasos_lejanos_fade.ogg" fadeout 3.0

    "Un silencio tenso."

    "Rodrigo cierra los ojos."
    "Algo no está bien."
    "Demasiado silencio."

    r "(susurrando) …No."

    "Un grito corta el aire."

    n "(a lo lejos) ¡¿Qué—?!"

    play sound "audio/sfx/grito_nagi.ogg"

    "Un golpe seco."
    play sound "audio/sfx/golpe_pared.ogg"

    "Algo arrastrándose."

    a "¡Nagi!"

    "Cutipye corre hacia el pasillo."
    "Rodrigo la detiene con una mano temblorosa."

    g "(fuera de escena, suave, casi divertida) Siempre se separan…"
    g "Nunca aprenden."

    play sound "audio/sfx/arrastre_humedo.ogg"

    "Un sonido húmedo."
    "Un arrastre."
    "Y silencio."

    "Luz cae de rodillas."
    "Azura cubre su boca."
    "Cutipye aprieta los puños."

    "Rodrigo no dice nada."
    "Pero algo dentro de él cruje."
    "No como hueso."
    "Como voluntad."

    # Zoom dramático posible con ATL o simplemente narración
    "La cámara podría cerrar en su ojo."
    "Más oscuro que antes."

    # Segunda parte: descubrimiento del cuerpo capturado
    "El eco de los pasos de Nagi se pierde en el pasillo."
    "Silencio."
    "Demasiado silencio."

    r "(susurrando) …No."

    "Un grito desgarrador rompe el aire."

    play sound "audio/sfx/grito_desgarrador_nagi.ogg"

    n "(fuera de escena) ¡¿Qué—?! ¡Suélt—!"

    play sound "audio/sfx/golpe_pared_fuerte.ogg"

    "El sonido de algo arrastrándose."

    "Luz se lleva la mano a la boca."
    "Azura corre un paso adelante."
    "Rodrigo ya está en movimiento."

    r "(fuera de escena, juguetona) Siempre es el mismo error…"
    r "Alejarse del rebaño."

    play sound "audio/sfx/levantado_suelo_humedo.ogg"

    "El grupo dobla la esquina del pasillo."

    scene bg pasillo_intermitente with flash   # luz intermitente

    "Al final, bajo una luz intermitente, la ven."
    "Galaxia sostiene a Nagi del cuello, elevado apenas del suelo."
    "Sus piernas patean en el aire."
    "Nagi aún tiene rabia en los ojos."

    n "(ahogado, desafiante) …Púdrete."

    "Reúne saliva."
    "Le escupe directo al rostro."

    "El tiempo parece congelarse."

    "Luz contiene el aliento."
    "Azura aprieta los puños."
    r "(ruge por lo bajo)"

    "Galaxia parpadea."
    "Se limpia la mejilla lentamente con los dedos."
    "Luego sonríe."

    g "(dulcemente burlona) Supongo que debo estar agradecida…"
    g "Empezaba a tener hambre~"

    "Inclina la cabeza."
    "Sus ojos se tornan más oscuros."

    g "Y tú te ofreciste solito."

    "Nagi forcejea."

    n "¡Rodrigo—!"

    "Pero Galaxia lo arrastra hacia atrás, hacia una puerta metálica entreabierta."

    # Guardián
    play sound "audio/sfx/caida_techo_pesado.ogg"

    "Antes de que el grupo pueda avanzar—"
    "Algo cae del techo."

    scene bg centinela_quitinoso with vpunch   # shake para impacto

    "Un cuerpo enorme bloquea el pasillo."
    "Mitad humano. Mitad cucaracha."
    "Su espalda está cubierta por un caparazón grueso y brillante."
    "Las patas traseras raspan el suelo con un sonido repugnante."
    "Sus antenas vibran."
    "Emite un chasquido seco."

    play sound "audio/sfx/chasquido_antenas.ogg"

    a "…No nos va a dejar pasar."

    "Rodrigo da un paso al frente."
    "Sus brazos se tensan."
    "Las venas se marcan bajo la piel."

    # Combate (puedes expandirlo con menús de elección si quieres interactividad)
    "El infectado embiste primero."
    "Rápido. Sorprendentemente rápido."

    n "(fuera de escena) ¡Suéltenme! ¡Maldita—!"

    play sound "audio/sfx/golpe_galaxia.ogg"

    g "(regañando, como a un niño) ¡Deja de moverte!"

    "El grupo vacila un segundo."
    "Error."

    play sound "audio/sfx/embestida_concreto.ogg"
    with vpunch

    "La bestia arremete contra Rodrigo, estrellándolo contra la pared."
    "El impacto hace crujir el concreto."

    # (continúa el combate con descripciones similares; para brevidad, salto al final)

    # Final del combate
    play sound "audio/sfx/puerta_metallica_cerrar.ogg"

    "La puerta metálica al fondo se cierra de golpe."
    "Silencio."

    "No hay más gritos."
    "No hay más voces."
    "Solo el eco distante de pasos arrastrándose."

    "Rodrigo queda de rodillas."
    "Su transformación se retrae lentamente."
    "Demasiado tarde."

    a "(quebrada) …No lo logramos."

    "Azura mira la puerta cerrada."

    a "Nos estaban esperando."

    "Cutipye no dice nada."
    "Solo observa a Rodrigo."

    "Rodrigo aprieta los puños hasta que sangran."
    "No llora."
    "Esta vez no."

    r "(susurra, voz rota) Fue mi culpa."

    "Y por primera vez, nadie lo contradice."

    stop music fadeout 4.0

    # Transición a siguiente label o fin de capítulo
    $ nagi_dead = True
    call chapter_complete("Capítulo 10")
    jump cap_11

label nagi_no_traiciona:

    # Fondo y música similar
    scene bg pasillo_derruido with dissolve
    play music "audio/ambience/pasillo_tenso.ogg" fadein 2.0 loop

    n "¿Sabes qué? Ya basta."

    "El grupo se detiene."

    a "¿Nagi…?"
    
    n "(señalando a Rodrigo) Desde que esto empezó, todo gira en torno a él."
    n "Sus ataques."
    n "Sus cambios de humor."
    n "Sus… cosas raras."

    "Rodrigo baja la mirada."
    "Intenta hablar, pero su mandíbula se tensa antes de que pueda articular bien."

    r "No estoy… perdiendo el control."

    "Pero incluso mientras lo dice, su pupila parece dilatarse un poco más. La influencia de Galaxia se nota en el brillo antinatural de sus ojos, como si algo ajeno estuviera susurrando en su mente."

    "Da un paso al frente. Uno lento. Forzado."

    r "Escuchen."
    r "No me gusta esto tampoco."
    r "No pedí… nada de esto."

    "Traga saliva."
    "Su voz suena más grave por momentos, como si Galaxia estuviera tirando de hilos invisibles en su garganta."

    r "Pero si nos dividimos, estamos muertos."
    r "Galaxia quiere eso."
    r "El Científico quería eso."
    r "Separarnos."

    "Se apoya contra la pared."
    "Respira profundo, pero irregular, como si luchara contra una ola interna."

    r "(casi suplicando) Yo puedo aguantar."
    r "Solo… manténganse cerca."
    r "Si pierdo el control… me detienen."
    r "Pero no se vayan."

    "Por un segundo, hay silencio."
    "Azura lo mira con lágrimas contenidas."
    "Cutipye también."
    "Nagi cruza los brazos, pero no se mueve."

    "Nagi suelta una risa seca, pero esta vez con un matiz de frustración compartida en vez de rechazo total."

    n "¿Aguantar? ¿Eso dices desde hace horas? ¡Maldita sea, Rodri, pareces un zombie con esteroides!"

    "Da un paso hacia Rodrigo, pero no agresivo —más como un amigo que quiere zarandearlo para despertarlo."

    n "Te tiemblan las manos."
    n "Nos miras como si fuéramos comida."
    n "Casi matas a—"

    "Se detiene antes de terminar la frase. Silencio pesado."

    "Rodrigo baja la cabeza, y sus uñas raspan más fuerte la tela, dejando marcas visibles."

    n "¿Sabes qué? Siempre has sido así, ¿eh? Recuerdan esa vez que se emborrachó hasta casi morirse?"

    # Flashback breve
    scene bg flashback_rodrigo_borracho with dissolve
    "Rodrigo inconsciente. Vomitando."
    "Azura y Cutipye preocupadas."
    "Nagi sosteniéndolo para que no se ahogara."
    scene bg pasillo_derruido with dissolve

    n "(con rabia, pero ahora con un toque de nostalgia forzada) ¡Y ahí estaba yo, salvándote el trasero como siempre! ¡No voy a dejar que nos mates a todos ahora, pero tampoco voy a largarme solo!"

    "El golpe emocional es fuerte, pero Nagi no lo remata con insultos. En cambio, mira al grupo."

    a "(amable, interviniendo con cuidado) Nagi, por favor... Entiendo tu miedo. Todos lo sentimos. Rodri está luchando, y Galaxia lo está... cambiando. Pero separarnos no ayudará. ¿Y si hablamos de irnos cuanto antes? Encontrar una salida rápida, juntos."

    "Azura pone una mano suave en el brazo de Nagi, su voz cuidadosa y empática, como una mediadora que prioriza la unión."

    c "(con ligereza, intentando aligerar) Sí, ¡vamos! Como en esas películas donde todos corren y nadie se queda atrás. Rodri, si te transformas, te doy un beso para que vuelvas... o un golpe, lo que funcione primero. ¡Je!"

    "Pero su risa es nerviosa, y mira a Rodrigo con una mezcla de cariño y temor real."

    n "(extrovertido, respondiendo con energía) ¡Eso! ¡Irnos cuanto antes! No me quedo aquí esperando que Rodri se convierta en el monstruo principal. Pero solos, somos carnada fácil para esa loca de Galaxia. ¡Vamos, grupo! ¿Quién dice que corramos como si nos persiguiera el diablo?"

    "Rodrigo levanta la mirada, sus pupilas aún dilatadas, pero asiente lentamente. La influencia de Galaxia hace que su voz suene un poco distorsionada."

    r "De acuerdo... Irnos cuanto antes. No... no quiero lastimarlos."

    a "(sonríe débilmente, cuidadosa como siempre) Entonces, sigamos. Juntos. Busquemos esa salida, pero con cuidado. Rodri, si sientes que empeora... avísanos."

    c "(asiente, ligera pero solidaria) ¡Equipo invencible! O al menos... equipo que no se rinde."

    "Nagi da una palmada en la espalda de Rodrigo —fuerte, extrovertida—."

    n "¡Eso es! No te voy a dejar solo, idiota. Pero apúrate, o te cargo yo mismo."

    "El grupo avanza, más unido por ahora, pero la tensión persiste. Rodrigo siente la influencia de Galaxia creciendo, un susurro en su mente que promete caos si no se apresuran."

    pause 2.0  # Pausa dramática

    "Un silencio tenso, pero no roto."
    "Algo no está bien."
    "Demasiado silencio."
    "Pero esta vez, no hay grito. Solo el eco de sus pasos sincronizados, apresurados hacia la salida."

    "La cámara cierra en el ojo de Rodrigo."
    "Aún oscuro, pero resistiendo... por ahora."

    stop music fadeout 4.0

    call chapter_complete("Capítulo 10")
    jump cap_11

label cap_11:
    if afinidad_cutipye < 4:
        scene bg_enfermeria_abandonada with dissolve
        
        "El grupo descansa en una sala de enfermería abandonada. El ambiente es sofocante."
        "El aire huele a metal y polvo."
        
        "Rodrigo está sentado en el suelo, espalda contra la pared. Sus hombros tiemblan levemente."
        "Tiene las manos entrelazadas, como si estuviera tratando de impedir que crezcan."
        
        "Nadie habla. Hasta que—"

        show cutipye media_sonrisa at right
        c "Qué curioso… Las cosas siempre se salen de control aquí."
        
        "Silencio."

        if not nagi_dead:
            show nagi ceja_levantada at left
            "Nagi levanta una ceja, observándola con cautela."
        
        c "Primero el orfanato. Después los monstruos. Después las mutaciones."
        
        show cutipye mirada_reojo
        c "Algunas personas simplemente… no saben cuándo parar."
        
        "Rodrigo baja aún más la cabeza."
        
        r "No lo hago a propósito..."
        
        show cutipye sorpresa_fingida
        c "¿Oh? ¿Entonces sí sabes lo que haces?"

        if not nagi_dead:
            n "Hey… bueno, nadie está en su mejor versión ahora mismo—"
            show cutipye seria
            c "No, no, déjalo. Me interesa escuchar esto."
        else:
            "El silencio de la sala hace que las palabras de Cutipye corten como cuchillas."

        "Cutipye se pone de pie y camina lentamente frente a Rodrigo."
        
        c "¿Sabes qué es lo gracioso? Siempre tienes un comentario listo cuando alguien más mete la pata."
        c "(Imitando a Rodrigo) 'Relájate.' 'No es para tanto.' 'Estás exagerando.'"
        
        show cutipye fria
        c "Pero cuando eres tú el que pierde el control… tenemos que entenderte."
        
        "Rodrigo la mira. Sus ojos están brillosos. No de rabia, sino de contención."
        
        c "Te da miedo todo. Miedo el ruido. Miedo la oscuridad. Miedo convertirte en lo que ya eres."
        
        "Rodrigo traga saliva. Sus dedos se curvan como garras involuntarias."
        
        l "Cutipye…"
        az "Basta."
        
        "Pero no suena a orden. Suena a ruego débil."
        
        r "Estoy intentando… ¡Estoy intentando no hacerles daño!"
        
        "Las plumas negras asoman sutilmente en su cuello antes de retraerse. Está luchando."
        
        c "Ese es el problema. Siempre estás intentando. Nunca estás logrando."
        
        "Rodrigo queda inmóvil, como si le hubieran vaciado el aire."
        
        c "¿Quieres que confiemos en ti? Ni tú confías en ti mismo."
        c "Nos miras como si fueras a atacarnos… y luego lloras para que sintamos pena."

        if not nagi_dead:
            n "Bueno, técnicamente llorar es una respuesta emocional saludable, ¿no? O sea, peor sería que—"
            c "No estoy bromeando."
            "Nagi se calla de inmediato."

        c "Eres un monstruo porque eliges comportarte como uno cuando tienes miedo."
        
        "Rodrigo ya no responde. Solo llora en silencio, sin defenderse."

        show cutipye cansada
        c "Necesito aire."
        
        hide cutipye with moveoutright
    else:
        # Placeholder para afinidad alta
        "Luz mira hacia la puerta por donde salió Cutipye, pero Rodrigo le hace una señal para que se quede."
        "A pesar de la tensión, la conexión del grupo con Cutipye es lo suficientemente fuerte como para no dejarla ir sola."
        # label_placeholder_continuacion_normal
        return
        

label escena_traicion_cutipye:
    scene bg_pasillo_oscuro with dissolve
    "Pasos alejándose. Oscuridad."
    "Cutipye respira agitado mientras camina sola, apoyándose contra la pared."
    
    c "No soy así… no soy así…"
    
    "Una voz suave. Cercana. Demasiado cercana."
    
    voice_galaxia "Claro que no… Solo estás aprendiendo a ser honesta."
    
    "Cutipye abre los ojos. Demasiado tarde."
    "Una mano la empuja contra la pared. Algo afilado roza su garganta."

    # --- Corte paralelo ---
    scene bg_enfermeria_abandonada with flash
    "Rodrigo deja de llorar de golpe. Algo en su instinto lo alerta."
    
    r "…Cutipye."
    
    "Un grito ahogado resuena por el pasillo."
    
    l "¡Cutipye!"
    
    if not nagi_dead:
        "Nagi maldice en voz baja mientras desenfunda su arma."

    # --- Escena: La Habitación que No Envejece ---
    scene bg_habitacion_limpia with dissolve
    
    "Cutipye cierra la puerta detrás de ella. Respira agitada."
    "El lugar está intacto. Papel mural perfecto, juguetes ordenados. Un reloj que funciona."
    
    c "¿Qué es este lugar?"
    
    "El clic del seguro de la puerta resuena como un disparo."
    
    voice_galaxia "Pensé que vendrían todos juntos…"
    
    show galaxia sentada_sonriendo with dissolve
    
    g "¿Tú sabes dónde están mis juguetes?"
    
    "Cutipye, recordando el arma que le quitó a Rodrigo, apunta con manos temblorosas."
    
    c "Están lejos de ti."
    
    play sound "sfx_disparo"
    "El balazo impacta en la pierna de Galaxia. La carne empieza a cerrarse ante sus ojos."
    
    g "Oh. Ahora entiendo lo que él intentaba decirles."
    
    play sound "sfx_disparo_repetido"
    "Cutipye vacía el cargador. Hombro. Torso. Cuello. Galaxia retrocede, pero no cae."
    "Las heridas se abren y se cierran en un ciclo grotesco."
    
    play sound "sfx_click_vacio"
    "Click. Vacío. Silencio."
    
    g "Eso fue grosero. No tienes que mentirme."
    
    "Cutipye choca contra la pared. No hay más espacio."
    
    g "Si cooperas… prometo no romperlos tan rápido."
    
    "Galaxia toca la mejilla de Cutipye con suavidad. Y entonces— ríe."
    "Una risa aguda, descompuesta, maniática."

    # Final visual
    scene black with dissolve
    show siluetas_muerte_cutipye at center with blood_splash
    
    "Un grito ensordecedor atraviesa la escena."
    "Una mancha oscura salpica la pared. Luego otra."
    "El grito se corta abruptamente."
    
    "Silencio."
    "El reloj sigue funcionando."
    "Tic. Tic. Tic."

    $ cutipye_dead = True

    call chapter_complete("Capítulo 11")
    jump cap_12

label cap_12:
    return