################
#    ACTO 2    #
################
label cap_6:

    scene black with fade
    stop music fadeout 2.0
    
    centered "{i}Tres años atrás...{/i}"

    scene scn_casa_fb_1 at sepia_filter with fade
    
    play music "music/party_chill.mp3" fadein 2.0 volume 0.6
    play sound "sfx/glass_clink.mp3"

    "La casa de Cutipye olía a perfume caro y aperitivos horneados. Era una reunión pequeña, pero el lujo se notaba en cada rincón."
    "Cortinas de lino filtrando la luz de media tarde. Un piso de madera tan pulido que devolvía los reflejos. Y, en algún lugar del pasillo, un reloj de péndulo que contaba los segundos con una puntualidad casi insolente."

    "Las sillas de la sala estaban dispuestas en semicírculo, todas mirando hacia la entrada."
    "Como para recibir a un invitado de honor. O para escuchar una declaración."

    "Cutipye acomodó por tercera vez el mismo cojín. Miró hacia el pasillo, donde el reloj marcaba los últimos minutos, y volvió a acomodarlo con impaciencia."
    
    c "Ya casi es la hora. Lucien fue muy específico."
    "Lo había sido. La hora exacta, todos presentes, sin excusas."

    a "Todavía me cuesta creer que por fin haya vuelto a la ciudad... ¿Cuánto tiempo pasó desde que sus padres se lo llevaron a estudiar fuera? ¿Casi un año?"

    c "Diez meses y dos semanas, para ser exactos. Diez meses sobreviviendo a base de puros mensajes de texto y excusas cada vez que queríamos hacer videollamada."

    a "Es extraño... Lucien no suele ser así de reservado. Antes nos contaba absolutamente todo, pero estos últimos meses sentí que guardaba un secreto enorme."

    "Azura sostenía su teléfono con las dos manos, releyendo el último mensaje del chat grupal por enésima vez."
    "«Ya estoy de vuelta. Hoy a las cinco en punto, en casa de Cuty. Vengan todos, tengo algo importante que mostrarles. Por favor, sean puntuales.»"

    a "Ni un solo emoji. Lucien jamás escribe sin emojis. Y ni siquiera quiso mandarnos un audio para avisar que ya había llegado."

    c "Lleva meses raro en el chat. Ayer le escribí para preguntarle si todo había salido bien con su regreso y solo me respondió: «Mejor que nunca. Mañana por fin me verán de verdad»."
    c "Sin stickers, sin fotos, sin nada. Quedé más confundida que antes."

    a "A mí me dio la impresión de que llevaba muchísimo tiempo esperando este día."

    n "Bah, le están dando demasiadas vueltas. No debe ser la gran cosa."
    
    "Nagi se echó un puñado de papas fritas a la boca, despreocupado, apoyándose muy cerca de Cutipye. En la otra mano sostenía un vaso de refresco al que aún no había dado ni un sorbo."
    
    n "Seguro se hizo un tatuaje horrible en otra ciudad, o ganó la lotería, o lo reclutó una secta durante el viaje."
    c "Que sea la lotería, por favor. No pienso visitar a nadie en una comuna hippy."
    n "Con suerte, es una secta con buenos postres."
    
    "Cutipye soltó una risa corta. Azura no."

    n "En serio, relájense. ¿Qué es lo peor que puede pasar después de casi un año sin vernos? ¿Que aparezca con pareja? Ojalá, así deja de ser el tercero en discordia."

    play sound "sfx/doorbell.mp3"
    "El timbre sonó antes de que pudieran reírse del chiste."
    pause 1.0
    
    "Murmullos en la entrada. Dos voces."
    "Una era la de Cutipye. La otra era baja, apenas un hilo, y no se parecía en nada a la de Lucien."
    "Nagi alzó una ceja, confundido."

    play sound door_close
    c "Pasa, pasa... chicos, miren quién llegó primero."

    scene casa_fb_3 at sepia_filter with dissolve

    "Detrás de ella, una sombra poco familiar."
    "Cabello desordenado, hombros encogidos, manos en los bolsillos como si quisiera esconderlas."
    "[nombre_jugador!c]. El chico callado del fondo del salón."
    "No miraba a nadie. Su atención, en cambio, se desviaba una y otra vez hacia el pasillo, hacia la puerta de entrada, como si esperara oírla abrirse en cualquier momento."

    # La tensión social
    "El silencio fue instantáneo."

    n "¿Eh? ¿Te equivocaste de biblioteca, amigo?"
    n "El club de ajedrez es los martes."

    c "¡Nagi! Cierra la boca."

    "Cutipye le dio un codazo nada sutil a Nagi antes de sonreírle a [nombre_jugador!c], aunque con un toque de duda en sus ojos."

    c "Ignóralo, [apodo_jugador]. Bienvenido. Aunque... ¿Lucien te invitó?"

    r "Sí... Lucien me dijo que tenía que estar aquí a esta hora."
    r "Dijo que era importante."

    scene scn_casa_fb_4 at sepia_filter with dissolve
    "Azura dio un paso al frente, con esa sonrisa que podía desarmar cualquier tensión."
    
    a "Hola, [nombre_jugador!c]. Soy Azura. Nos sentamos a dos bancos de distancia en Historia."
    a "Si Lucien te pidió venir, eres bienvenido."

    r "Gracias..."

    # La espera
    "Hubo un silencio incómodo. De esos en los que todos se miran, pero nadie mira a quien debería."
    "Azura le señaló un lugar en el sofá. [nombre_jugador!c] se sentó en la punta, con la espalda recta y las manos entre las rodillas."

    scene casa_fb_3 at sepia_filter with dissolve
    n "Entonces... ¿de dónde conoces a Lucien?"
    r "...De hace mucho."
    n "¿Cuánto es mucho?"
    "[nombre_jugador!c] se encogió de hombros. No era una respuesta."

    c "Qué raro. Creí que Lucien nos había presentado a todos sus amigos."
    "Lo dijo con ligereza, pero la frase quedó flotando en el aire."
    "Nadie dijo lo que todos estaban pensando: que quizá Lucien no se lo había contado todo."

    n "¿Y sabes de qué va esto?"
    "[nombre_jugador!c] sostuvo la mirada de Nagi un segundo de más. Luego la desvió hacia el pasillo."
    n "Genial. Un misterio dentro del misterio."

    "Pasaron tres minutos. Luego cinco."
    "Desde la cocina llegó el pitido del horno. Nadie se levantó a apagarlo."

    "El teléfono de Azura vibró contra la mesa."
    a "Es Lucien."
    "Todos se inclinaron hacia la pantalla."
    "«Estoy llegando. Gracias por esperarme.»"
    n "Lucien nunca da las gracias por esperar. Lucien llega tarde y manda un meme."
    c "Lo sé."

    stop music fadeout 2.0
    "Nadie bromeó después de eso."
    "Sin la música, la casa se volvió más grande. Se oía el refrigerador zumbando en la cocina, el hielo asentándose en los vasos, el péndulo del pasillo."
    "Nagi apretó su vaso con los dedos."

    # La llegada
    "Entonces, el reloj empezó a dar la hora."

    play sound door_open
    "Una campanada. Y, junto con ella, la puerta principal abriéndose."
    "Lucien nunca tocaba el timbre. Entraba como si la casa fuera suya, gritando un «¡ya llegué!» desde el recibidor."
    "Esta vez no gritó."
    pause 1.0
    "Otra campanada. Un paso."
    "Suave. Decidido. Pero distinto: Lucien siempre arrastraba las zapatillas, y estos pisaban con cuidado, uno por uno, como quien cruza un puente que teme romper."
    "Otra campanada. Otro paso."

    c "¿Lucien? ¿Eres tú? Estamos en la sala."

    pause 1.5
    "Ninguna respuesta. La última campanada se apagó."
    "Una figura apareció bajo el marco de la puerta, a contraluz del pasillo."

    "No era Lucien."
    "O al menos, no el que ellos recordaban."

    scene scn_casa_fb_5 at sepia_filter with dissolve
    pause 1.5

    "Solo una silueta contra la luz: hombros rectos, manos entrelazadas, el borde de una tela moviéndose con el aire."
    "Dudó en el umbral. Un segundo. Dos. Y luego dio el último paso hacia adentro."

    scene scn_casa_fb_6 at sepia_filter with dissolve
    
    "Llevaba un vestido sencillo de color pastel, el cabello suelto cayendo sobre sus hombros y un maquillaje ligero que resaltaba sus ojos."

    play sound thud volume 0.4
    "Nagi soltó su vaso. Cayó sobre la alfombra sin romperse y nadie lo miró."
    "Azura se cubrió la boca."

    n "¿Pero qué...?"
    c "¿Lucien...?"

    l "Hola, chicos."

    "Su voz temblaba un poco, pero su mirada estaba firme."
    pause 0.8

    l "Lamento no haberles dicho nada antes. Sé que... es una sorpresa."

    "Nadie respondió. Nagi había abierto la boca para soltar algún chiste, y no encontró ninguno."

    "Luz respiró hondo, entrelazando sus dedos frente a ella."

    l "Llevo mucho tiempo sintiendo que vivía la vida de alguien más. Y hoy... quería dejar de hacerlo."
    l "Quiero dar un comienzo fresco a mi vida. A quien soy realmente."

    scene casa_fb_7 at sepia_filter with dissolve
    l "Y no podía empezar ese camino sin mis personas más queridas."

    "Miró a Cutipye. A Nagi. A Azura."

    l "Mis mejores amigos..."

    "Y luego, giró la cabeza hacia la derecha, buscando los ojos del chico callado."
    pause 1.5

    l "...y mi novio."

    scene casa_fb_8 at sepia_filter with dissolve

    "Todas las miradas se dispararon hacia [nombre_jugador!c]."
    "Él no parecía sorprendido por la ropa de Luz. Solo... le sonrió. Una sonrisa pequeña, privada y llena de orgullo."

    r "Te ves hermosa, Luz."

    scene black with fade
    stop music fadeout 3.0
    show layer master at default # Quitar filtro Sepia
    
    pause 2.0
    
    play music main_menu fadein 2.0
    scene luz_hug_rodrigo with dissolve
    # afinidad_luz tiene un valor entre 2 y 5 para este punto
    
    "El recuerdo cálido de aquella tarde se disipó, reemplazado de golpe por el hedor a óxido, sangre y aceite rancio."
    "Luz seguía abrazándolo con fuerza contra su pecho, temblando, muy lejos ya de ser aquella chica tímida con vestido pastel."
    
    l "Te tengo, [apodo_jugador]... Ya pasó, estoy aquí contigo."

    "Alrededor de ambos, el resto del grupo soltó el aire que parecían haber estado conteniendo desde que el piso cedió en el segundo nivel."

    n "Carajo, amigo... Cuando vimos ese agujero pensamos que te habías partido el cuello en el acto."
    c "Casi me da un infarto cuando escuchamos los disparos aquí abajo, idiota. No vuelvas a darnos un susto así."
    a "Menos mal que lograste encerrarte a tiempo... No sé qué habríamos hecho si llegábamos tarde."

    "Sus voces sonaban atropelladas, cargadas de ese alivio torpe y ruidoso de quienes acaban de ganarle un segundo a la muerte."
    "Pero [nombre_jugador!c] apenas podía seguirles el hilo. Su propia respiración le resultaba pesada, ajena."
    "Había un sabor extraño impregnado en su paladar."
    "{cps=15}Dulce. Metálico.{/cps}"

    r "...Luz... Espera..."

    scene bg_cuarto_maquinas
    show rodrigo shock_state at right
    show luz worry at centro_derecha
    show nagi smile at centro_izquierda
    show cutipye neutral at left
    with dissolve

    "[nombre_jugador!c] se apartó unos centímetros con manos temblorosas. El costado derecho le ardía con un calor espeso, casi febril. Bajó la mirada un instante y apartó la tela desgarrada de su chaqueta."
    
    "Donde minutos antes los cortes de las garras manaban sangre sin control, ahora la tela solo estaba húmeda y fría... y la carne debajo parecía haberse cerrado hasta ser poco más que un par de rasguños pálidos."
    "Demasiado superficiales para el dolor que recordaba."

    r "...No estaba así..."
    r "Ella me abrió el costado... Yo tenía la mano llena de sangre, no estaba así..."

    "Las sonrisas de alivio de Nagi y Cutipye se congelaron poco a poco. El ambiente en el cuarto de máquinas cambió de peso."

    show nagi neutral at centro_izquierda
    n "¿De qué hablas, [apodo_jugador]? Si es solo un rasponazo, mejor para nosotros, ¿no?"

    r "No, no me entienden... Me dio de lleno en la escalera, yo sentí cómo—"

    pause 0.4

    "Un latido sordo le golpeó detrás de los tímpanos, seguido por la sensación de dedos helados cosiendo su carne desde adentro."

    play ambient "sfx/wet_whisper.mp3" fadein 0.3
    "{color=#390169}{font=fonts/HelpMe.ttf}{cps=16}No iba a dejar que te desangraras tan rápido, [apodo_jugador]~{/cps}{/font}{/color}"
    "{color=#390169}{font=fonts/HelpMe.ttf}{cps=15}Apenas me estoy acomodando ahí dentro~{/cps}{/font}{/color}"
    stop ambient fadeout 0.5

    show rodrigo alert at right with vpunch
    "[nombre_jugador!c] dio un respingo violento, parpadeando con fuerza y girando la cabeza hacia los conductos oscuros del techo."

    r "¿Escucharon eso...? ¡Está aquí! ¡Está en los ductos!"

    if estado_mental >= 6:
        show luz worry at centro_derecha
        show cutipye worried at left
        show nagi worry at centro_izquierda
        show azura worried at right behind rodrigo
        with dissolve
        
        "Nadie se movió. El único sonido en la sala era el goteo lento y distante de una tubería oxidada."
        "El alivio de hace unos segundos había desaparecido por completo; ahora los cuatro lo miraban en un silencio tenso, tratando de descifrar qué le ocurría."

        n "Ey, ey... Baja el arma, hombre. Escúchame. Aquí no hay nadie más que nosotros."
        c "[apodo_jugador], me estás asustando... No se oyó absolutamente nada."

        "Los otros se inclinaron levemente hacia él, con los rostros marcados por el desconcierto al ver cómo le temblaban las manos y cómo su mirada rebotaba de una esquina a otra."
        "Algo en su voz —quebrada, paranoica y fuera de ritmo— les dejó claro que aquello no era el simple aturdimiento de una caída; tenía el pánico clavado hasta los huesos."
        
        n "Mírame un segundo. ¿Qué fue lo que viste allá afuera antes de encerrarte?"
        c "Trata de respirar lento, ¿sí? Estamos acá contigo. La puerta de acero está cerrada."

    else:
        show luz worry at centro_derecha
        show cutipye worried at left
        show nagi serio at centro_izquierda
        with dissolve
        
        "Durante un par de segundos, todos contuvieron el aliento mirando hacia el techo... pero el único sonido seguía siendo ese goteo distante."
        "La ligereza del reencuentro se esfumó, dejando paso a una preocupación silenciosa mientras observaban el sudor frío en la frente de [nombre_jugador!c]."

        n "Tranquilo, hermano... No se escuchó nada. Ese cuarto es una caja fuerte, aquí no entró nadie."
        c "Todavía estás temblando entero. Seguro es la adrenalina y el golpe de la caída jugándote una mala pasada."
        
        show azura worried at right behind rodrigo with dissolve
        a "Ven, no intentes levantarte de golpe. Apóyate un segundo más y trata de recuperar el aire."

        "Lo rodearon con cautela, hablándole en voz baja como quien intenta traer de vuelta a la tierra a alguien que sigue atrapado en medio de la pesadilla."

    "Luz le sujetó el rostro con ambas manos para obligarlo a mirarla, pero apenas sus dedos rozaron sus mejillas, frunció el ceño."

    l "[apodo_jugador]... estás helado. Tienes la piel como el hielo."

    "Al apoyar la palma en el suelo sucio para terminar de incorporarse, [nombre_jugador!c] notó pequeñas motas oscuras adheridas a las yemas de sus dedos."
    "Parecían ceniza húmeda… o algo que había brotado de sus propios poros."

    "Las frotó instintivamente contra su pantalón antes de que alguien más bajara la vista."
    "Desaparecieron."
    "Pero dejaron una sensación espesa y pegajosa que no se iba."

    "Por un segundo —solo un segundo— el brillo tenue de la lámpara de emergencia le resultó insoportable."
    "Su pupila se contrajo en un destello vertical… de una forma que su propio cuerpo no reconoció."

    pause 0.8

    show rodrigo incomodo at right with dissolve
    "Parpadeó con fuerza, tragando esa saliva dulce y ferrosa."
    "Todo volvió a la normalidad."

    "Tal vez tenían razón y solo era la contusión."
    "Tal vez era el miedo haciéndole escuchar el eco de esa voz."

    "Tal vez..."

    stop music fadeout 0.7
    pause 1.5

    scene pasillo_abandonado with fade
    play sound wood_creak loop
    show luz worry at centro_derecha
    show azura worried at right
    show nagi serio at centro_izquierda
    show cutipye disgust at left
    show rodrigo neutral at center
    with dissolve

    "El grupo avanzó a paso lento. El orfanato se sentía más cerrado, como si los pasillos respiraran con ellos."
    
    n "Hay una ala administrativa por aquí. Si hay planos o salidas, estarán ahí."
    c "¿Y si es una trampa? Ya vimos lo que hay cuando nos metemos más adentro."
    n "No podemos quedarnos dando vueltas. Información nos da ventaja."
    c "O podemos irnos y vivir otro día. Yo prefiero no 'arriesgar ventaja'."
    stop sound fadeout 0.4

    show rodrigo nervioso at center with dissolve
    "[nombre_jugador!c] notó la discusión."
    "El sonido de sus voces le parecía lejano, como si viniera desde el fondo de un túnel."

    "Su pecho apretó nuevamente."
    "La punta de los dedos le vibró con esa sensación extraña, apenas perceptible."

    r "(No... no ahora.)"

    "Ambos lo miraron casi al mismo tiempo."
    pause 0.6
    show rodrigo neutral with dissolve
    r "¿Qué?"
    r "¿Ahora soy el comité ejecutivo?"

    "Intentó sonar ligero."
    "No lo logró del todo."

    r "A ver si entiendo."
    r "O nos metemos más profundo en el edificio embrujado buscando planos que probablemente estén mascados por algo..."
    r "O retrocedemos por el mismo camino por donde casi nos matan hace veinte minutos."

    pause 0.5
    show rodrigo incomodo with dissolve
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
            show rodrigo neutral with dissolve
            r "Si vamos a morir, prefiero hacerlo con un mapa en la mano."

            show rodrigo molesto with dissolve
            r "Al menos así podremos decir que fue una muerte organizada."
            "Su voz fue seca."
            "Demasiado seca."
            "No estaba intentando ser gracioso."
            jump ir_administracion
            
        "Cuty tiene razón. No podemos seguir adentrándonos.":
            $ afinidad_cutipye += 1
            $ estado_mental -= 1
            show rodrigo neutral with dissolve
            r "Ya tuvimos suficiente turismo oscuro por hoy."
            r "Retirarse no es cobardía."

            show rodrigo incomodo with dissolve
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
    "No miraba a [nombre_jugador!c] para lanzarle uno de sus típicos:"
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
    "No hubo exageración teatral ni golpes con el bate contra la palma de su mano."

    "Solo una frase corta."
    "Directa."

    "[nombre_jugador!c] sintió esa ausencia más que cualquier grito."

    "Mientras las chicas revisaban los archivadores del fondo, Nagi se acercó a la mesa donde descansaba el mapa."
    show nagi serio at centro_izquierda with move
    "Y luego, sin decir nada, se colocó justo al lado de [nombre_jugador!c]."

    show nagi worried at centro_izquierda with dissolve
    
    "No invadió su espacio. No le pasó un brazo por el cuello ni lo llamó 'fantasma' o 'poeta deprimido'."
    "Solo se quedó ahí, apoyando los nudillos sobre la madera polvorienta mientras lo miraba de reojo."

    n "Oye..."

    pause 0.5

    n "Suelta el aire, ermitaño. Llevas medio minuto sin parpadear."

    "No fue una orden burlona."
    "Su voz sonó baja. Casi cautelosa."

    "[nombre_jugador!c] tensó la mandíbula y evitó mirarlo, fijando la vista en las líneas borrosas del plano."
    "El sabor dulce y metálico volvió a subir por su lengua."

    show rodrigo incomodo with dissolve
    r "Solo estoy viendo por dónde salir."

    show nagi serio at centro_izquierda
    n "Ajá. Claro."
    
    "Nagi soltó un bufido corto, sin humor, y cruzó los brazos."
    n "Llevo aguantándote la cara de funeral desde secundaria, [apodo_jugador]. Sé perfectamente cómo te ves cuando estás pensando o cuando solo quieres que todos se callen."
    
    show nagi worried at centro_izquierda
    n "Normalmente ya habrías puesto los ojos en blanco o habrías soltado algún comentario de mierda sobre cómo vamos a morir todos por mi culpa."
    n "Pero desde que salimos de ese cuarto de máquinas... ni siquiera parece que estés aquí."
    n "Estás raro, amigo. Incluso para tus estándares."

    "Eso tampoco era normal en Nagi."
    "Por lo general, cuando notaba que [nombre_jugador!c] se encerraba en sí mismo, lo empujaba. Lo provocaba hasta obligarlo a reaccionar."
    "Era su equilibrio de siempre: el chico ruidoso arrastrando al callado fuera de su caparazón."

    "Pero ahora no estaba tirando de él hacia afuera."
    "Estaba tanteando el terreno... como si temiera que, si empujaba demasiado fuerte, algo se fuera a quebrar."

    menu:
        "Estoy bien.":
            $ estado_mental -= 1
            r "Estoy bien, Nagi. En serio. Solo... tengo el golpe de la caída encima. Necesito un minuto."
            
            show nagi serio at centro_izquierda
            "Nagi lo sostuvo en la mirada un par de segundos más, claramente sin tragarse el cuento del todo, pero decidió no presionar frente a las demás."
            
            n "Vale. Te compro el minuto."
            show nagi worried at centro_izquierda
            n "Pero no te hagas el duro conmigo si te empiezas a caer a pedazos, ¿me oyes? No pienso cargarte todo el camino de vuelta."

        "Creo que algo no está bien conmigo.":
            $ afinidad_nagi += 2
            $ estado_mental += 1
            show rodrigo nervioso with dissolve
            r "No lo sé, Nagi... Siento el cuerpo extraño desde que caí. Creo que algo no está bien conmigo."
            
            show nagi worried at centro_izquierda
            "La poca ligereza que Nagi intentaba fingir desapareció de golpe. Se inclinó un poco más hacia él, bajando aún más la voz para no alarmar a Luz ni a Azura."
            
            n "¿Te mareas? ¿Crees que te rompiste una costilla al caer o qué?"
            n "Dime qué sientes y vemos cómo lo parchamos, pero no te me quedes ido, que me pones más nervioso que esos bichos."

    "Nagi dio medio paso más cerca."
    "Instintivamente, con la misma postura que adoptaba siempre antes de soltar una broma pesada para aligerar el ambiente."
    "Pero esta vez el chiste se le quedó atascado en la garganta."

    "Sus ojos púrpura recorrían el rostro pálido de [nombre_jugador!c], bajando brevemente hacia la mancha de sangre seca en su ropa."
    "Analizando."
    "Intuyendo que algo había cambiado allá abajo, aunque todavía no supiera cómo llamarlo."

    n "¿Ella te hizo algo?"

    "La pregunta quedó suspendida en el aire."

    "[nombre_jugador!c] apoyó la mano en el borde del mapa para no tambalearse."

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
    "Era el tono de alguien que, por primera vez, no estaba intentando sacar a [nombre_jugador!c] al mundo…"
    "Sino impedir que algo se lo llevara."

    $ afinidad_nagi += 1

    "Revisaron archivadores y encontraron planos parciales del edificio."
    "Suficientes para trazar una ruta tentativa de salida."

    "Pero cuando [nombre_jugador!c] miró el mapa otra vez…"
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

    "[nombre_jugador!c] caminaba en silencio."
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
    c "¿Ni una sonrisa irónica, [nombre_jugador!c]? Eso sí que me preocupa."

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

    "[nombre_jugador!c] notó cómo sus manos estaban tensas."
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

    "[nombre_jugador!c] sintió un pequeño zumbido eléctrico en la punta de los dedos."
    "Un impulso extraño, casi muscular."
    "Un deseo breve y absurdo de… apoyar las manos contra los escombros y empujarlos con una fuerza que sabía perfectamente que no tenía."

    r "(No. Cálmate.)"

    "A unos metros por delante, Luz y Azura revisaban las uniones del corredor con Nagi, pero Cutipye fue acortando el paso poco a poco hasta quedar rezagada junto a él."

    show cutipye neutral at center with move
    show rodrigo sorprendido at vjump
    pause 0.1
    show rodrigo neutral at right
    
    c "Oye."

    "No sonó como el inicio de un chiste ni tuvo su habitual tono de superioridad."
    "Caminaba con los brazos cruzados contra el frío del pasillo, mirándolo de reojo mientras el resto del grupo avanzaba unos pasos más allá."

    c "Es curioso, ¿no? Te abrí la puerta de mi casa hace tres años y creo que desde esa tarde nunca habíamos tenido un segundo para hablar así, de tú a tú."
    c "Siempre está Luz en medio, o Nagi haciendo ruido."

    r "Bueno... tampoco es que yo sea el tipo más conversador del mundo."

    c "Justamente por eso."

    pause 0.4

    c "¿Sabes cuál es la parte buena de que siempre seas tan callado, [apodo_jugador]?"
    c "Que cuando te quedas más callado de lo normal… se nota a kilómetros."

    show rodrigo incomodo at right with dissolve
    "[nombre_jugador!c] tensó los hombros y desvió la mirada hacia las baldosas rotas."

    c "Ey, no me mires como si te estuviera pasando lista."
    c "No voy a darte un discurso motivacional ni a darte palmaditas en la espalda. Ese es territorio de Nagi."

    "Intentó curvar los labios en una de sus sonrisas despreocupadas."
    "No le salió del todo."
    "Disminuyó aún más la voz, asegurándose de que la conversación quedara solo entre los dos."

    c "Pero allá abajo nos pegaste un susto de muerte. Así que deja de hacerte el misterioso conmigo un segundo y solo… dime si estás aquí. Conmigo."

    menu:
        "No voy a dejar que nadie más se lastime.":
            $ afinidad_cutipye += 1
            show rodrigo serio at right
            r "Estoy aquí, Cuty. Y no voy a dejar que nadie más salga lastimado en este lugar."
            
            "Cutipye lo observó durante un segundo más largo de lo habitual, como si buscara grietas detrás de esa respuesta automática."
            
            show cutipye soft at center with dissolve
            c "Lo sé. Sé que siempre te pones en medio."
            c "Pero baja el escudo un rato, ¿sí? No te toca cargar con todo el peso de esta noche tú solo."
            c "No eres el guardaespaldas oficial del grupo, [apodo_jugador]."
            c "Solo eres tú. Nuestro amigo. Y con que salgas entero de aquí con nosotros ya es más que suficiente."

        "Tengo miedo, Cutipye.":
            $ afinidad_cutipye += 2
            $ estado_mental += 1
            show rodrigo incomodo at right
            r "Tengo miedo, Cuty. No sé qué mierda está pasando aquí abajo y tengo miedo."
            
            "La confesión salió más baja de lo que esperaba. Casi un susurro."
            "Más honesta de lo que se había permitido sonar frente a nadie en toda la noche."
            
            show cutipye soft at center with dissolve
            "En lugar de burlarse o incomodarse, la expresión de Cutipye se suavizó por completo. Dio medio paso hacia él, rozando brevemente su hombro con el suyo mientras caminaban."
            
            c "Bien."
            c "Eso significa que todavía tienes cordura y que quieres salir de aquí tanto como yo."
            c "Porque te voy a confesar un secreto: yo también estoy muerta de miedo."
            c "Pero prefiero mil veces tener miedo contigo, hablando claro, que seguir fingiendo que soy la valiente yo sola."

    "Durante un breve segundo, la opresión del pasillo pareció ceder. El aire frío dejó de sentirse tan irrespirable."

    "Sin embargo, un repentino mareo le nubló el borde de la vista. [nombre_jugador!c] extendió el brazo y apoyó la palma contra la pared para estabilizarse."

    show rodrigo shocked at vjump

    "Al despegar los dedos, una leve marca oscura quedó impresa sobre el concreto húmedo."
    "Pequeña. Espesa."
    "Casi como hollín mezclado con aceite."

    "Se apresuró a frotarla con la manga de su chaqueta para borrarla."

    show cutipye serious at center with dissolve
    "Pero Cutipye ya se había detenido. Frunció el ceño, clavando la vista primero en la pared y luego en la mano que él intentaba esconder."

    pause 0.5

    c "Espera... ¿Te manchaste con algo allá abajo o te volvió a sangrar la herida?"

    menu:
        "Es polvo. Nada más.":
            $ estado_mental -= 1
            show rodrigo neutral at right
            r "Es solo polvo viejo de la pared. Nada más."
            
            "Cutipye sostuvo la mirada en su manga un instante más. Sabía que le estaba ocultando algo, pero respetó el código tácito que acababan de formar y no lo acorraló."
            
            show cutipye neutral at center
            c "Ajá. Claro."
            c "Polvo misterioso y grasiento de edificio maldito. Justo mi favorito para arruinar la ropa."
            c "Camina, anda. No te me quedes atrás."

        "No lo sé.":
            $ afinidad_cutipye += 1
            $ estado_mental += 1
            show rodrigo nervioso at right
            r "La verdad... no lo sé, Cuty. Desde que salí de ese cuarto siento las manos raras."
            
            show cutipye worried at center with dissolve
            "Cutipye no retrocedió ni puso cara de asco. Tomó aire en silencio, asimilando la respuesta con una madurez que rara vez dejaba ver."
            
            c "Vale. Gracias por no mentirme."
            c "Entonces nos mantenemos cerca y lo vigilamos entre los dos, ¿de acuerdo?"
            c "No te voy a dejar convertirte en…"
            
            "Hizo una pausa, buscando una palabra que no sonara tan aterradora en la penumbra."
            
            c "Bueno. En algo raro sin que al menos me avises primero."

            "Intentó que el remate sonara ligero, casi como una de sus bromas habituales."
            "No lo logró del todo, pero no se apartó de su lado en el resto del trayecto."
            
    play sound door_open
    scene lavanderia_abandonada with dissolve

    "Al final del corredor apareció por fin la vieja lavandería por donde habían entrado horas atrás."
    "La luz fluorescente parpadeaba con un zumbido agónico sobre la puerta metálica."

    "El olor a detergente rancio y humedad estancada les golpeó de frente."

    "[nombre_jugador!c] sintió un tirón helado en la boca del estómago al cruzar el umbral."
    "Como si algo anclado detrás de sus costillas rechazara la idea de acercarse a la salida."

    "Parpadeó con fuerza."
    "La sensación se disipó en la penumbra."

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
    with dissolve

    "El edificio ya no se sentía igual."
    "El aire era más denso, cargado de un polvo rancio que se pegaba a la garganta."
    "Y las paredes parecían haberse estrechado un par de centímetros más."

    if label_nagi == True:

        "Nagi se detuvo en seco bajo el marco corroído del corredor. Bajó la linterna hacia el mapa que llevaba en la mano y luego volvió a alumbrar hacia el frente, con la mandíbula tensa."
        "El plano marcaba una escalera de servicio y un acceso directo al patio exterior."
        "Frente a ellos solo había un muro de ladrillo sellado con concreto viejo y tuberías oxidadas."

        show nagi annoyed at centro_izquierda
        n "No... No tiene ningún puto sentido. ¡Esto no estaba aquí!"
        
        "Sacudió el papel con brusquedad, casi rasgándolo por los bordes, como si darle la vuelta fuera a cambiar la arquitectura del pasillo."
        
        n "Conté las puertas desde el archivo, [apodo_jugador]. ¡La salida de emergencia tendría que estar justo detrás de esta pared!"

        show cutipye angry at left
        c "¡Te lo dije, Nagi! ¡Te dije que meternos más adentro era una estupidez!"
        c "¡Nos hiciste bajar a la boca del lobo por un pedazo de papel que ni siquiera sirve porque remodelaron esta pocilga hace décadas!"

        show nagi angry at centro_izquierda
        n "¡Al menos yo intenté buscar una ruta en vez de correr a ciegas, Cuty!"

        show azura worried at right
        a "¡Basta, chicos, por favor! ¡Si gritamos así nos van a escuchar desde abajo!"
        
        show luz worry at centro_derecha
        l "Azura tiene razón... No ganamos nada peleando ahora. El plano debe ser anterior a que clausuraran el subsuelo. Tenemos que seguir buscando otra puerta que conecte con el vestíbulo."

        $ ruta_anterior = "nagi"

    else:

        "Al cruzar el umbral de la lavandería, el alivio que habían sentido segundos atrás se les heló en el estómago."
        "La ventana alta por la que habían saltado horas antes ya no era accesible."
        "Una montaña de vigas podridas, escombros del segundo piso y mampostería colapsada sepultaba toda la pared exterior hasta el techo."

        show cutipye shocked at left
        c "No… no, no, no. ¡Esto no estaba así cuando entramos!"
        
        "Cutipye se adelantó tropezando y empujó un bloque de concreto con ambas manos, raspándose las palmas sin lograr moverlo ni un milímetro."
        
        show cutipye scared at left
        c "¡Hace un par de horas saltamos por ahí mismo! ¡Estaba despejado! ¡¿En qué momento se cayó todo esto sin que escucháramos nada?!"

        show nagi serio at centro_izquierda
        n "Cuando el piso cedió bajo los pies de [apodo_jugador] en el segundo nivel... Toda esa ala vieja debió venirse abajo en cadena."
        n "O la estructura se está desplomando sola… o esa cosa sabe exactamente por dónde queríamos escapar y nos acaba de cerrar la jaula."

        show azura scared at right
        a "No puede ser... ¿Estamos enterrados? ¿Y si el resto del techo también se viene abajo?"

        show luz worry at centro_derecha
        l "¡No nos vamos a quedar encerrados aquí! Escúchenme, este edificio tenía salidas de carga y patios internos. Si la ventana ya no sirve, buscaremos cómo rodear el derrumbe por los pasillos interiores."

        $ ruta_anterior = "cuty"


    "Nadie alcanzó a responderle."
    "Un estruendo metálico, seco y descomunal, retumbó justo sobre sus cabezas."

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

    "Los tubos fluorescentes chisporrotearon una última vez y se apagaron de golpe."

    c "¡¿Qué fue eso?!"
    a "¡Mi linterna no prende! ¡Nagi!"
    l "¡¿[apodo_jugador]?! ¡¿Dónde estás?! ¡No te sueltes de mí!"

    pause 1.0
    play music ambiental fadein 1.0 volume 0.6

    "Pero las voces de sus amigos empezaron a sonar lejanas, amortiguadas, como si hablaran detrás de un cristal grueso bajo el agua."
    "Oscuridad total."

    hide rodrigo
    show rodrigo shock_state at center
    with dissolve

    "En medio de esa ceguera absoluta, lo único nítido era el calor palpitando en su costado... y el roce de un aliento helado paseándose con calma alrededor de su nuca."

    play sound "sfx/wet_whisper.mp3"
    "{color=#390169}{font=fonts/HelpMe.ttf}{cps=14}[apodo_jugador]…~{/cps}{/font}{/color}"

    pause 0.5

    "{color=#390169}{font=fonts/HelpMe.ttf}{cps=16}Míralos dar vueltas en la oscuridad, buscando puertas que ya no existen.{/cps}{/font}{/color}"
    "{color=#390169}{font=fonts/HelpMe.ttf}{cps=15}Qué agotador debe ser fingir que todavía eres igual a ellos, ¿no?~{/cps}{/font}{/color}"

    r "(¿Quién—? ¡Sal de mi cabeza!)"

    "{color=#390169}{font=fonts/HelpMe.ttf}{cps=16}Shhh... No gastes saliva con ellos. Ellos no lo entienden.{/cps}{/font}{/color}"
    "{color=#390169}{font=fonts/HelpMe.ttf}{cps=15}Creen que el monstruo es algo que acecha afuera en los pasillos...{/cps}{/font}{/color}"
    "{color=#390169}{font=fonts/HelpMe.ttf}{cps=14}Siempre tan ruidosos, tan llenos de promesas bonitas cuando tienen miedo.{/cps}{/font}{/color}"
    "{color=#390169}{font=fonts/HelpMe.ttf}{cps=14}Pero tú y yo siempre supimos mirar desde el rincón, ¿verdad, [apodo_jugador]?{/cps}{/font}{/color}"
    "{color=#390169}{font=fonts/HelpMe.ttf}{cps=12}Yo también me aferré a esa esperanza inútil alguna vez... Ven un poquito más cerca y te mostraré cuánto vale~{/cps}{/font}{/color}"

    r "¿Qué quieres de mí...?"

    play sound "sfx/lights_back.mp3"
    scene pasillo_intermedio
    show luz worry at centro_derecha
    show azura worried at right
    show nagi serio at centro_izquierda
    show cutipye serious at left
    show rodrigo shock_state at center
    with flash

    "Los focos volvieron a encenderse con un chasquido eléctrico, devolviéndolo de golpe al pasillo polvoriento."
    "Había dicho esa última frase en voz alta."

    l "[apodo_jugador], ¿con quién hablabas? ¿Estás bien?"

    menu:
        "La escuché otra vez.":
            $ estado_mental += 1
            r "Sí... la escuché otra vez."
            r "Estaba hablándome aquí mismo cuando se fue la luz. Juro que no me lo estoy inventando."

            if ruta_anterior == "nagi":
                show cutipye worried at left
                $ afinidad_cutipye += 2
                c "¿La voz de esa cosa?"
                c "Tranquilo, [apodo_jugador]. Yo te creo."
                c "Después de lo que vimos allá abajo, sé que no te lo estás inventando."
                r "Gracias, Cuty. Solo... siento que me estoy volviendo loco."
                r "Necesitaba saber que no estoy perdiendo la cabeza yo solo."
            else:
                show nagi worried at centro_izquierda
                $ afinidad_nagi += 2
                n "Vale. Bien. Respira."
                n "Te creo, hermano. No estás loco."
                n "Esa cabrona está jugando contigo desde que salimos del sótano."
                r "No sé si solo está jugando, Nagi..."
                r "Siento como si me estuviera observando desde adentro."

            "Los demás intercambiaron una mirada tensa, asintiendo con gravedad."
            n "Si necesitas que estemos más atentos, no te vamos a soltar ni un segundo."
            c "No estás solo en esto, [apodo_jugador]."

        "Nada. Vámonos.":
            $ estado_mental -= 1
            r "No es nada. Solo pensé en voz alta por el ruido del techo."
            r "Dejemos de perder el tiempo aquí. Si avanzamos, se me pasará."

            if ruta_anterior == "nagi":
                $ afinidad_cutipye += 1
                show cutipye serious at left
                "Cutipye apretó los labios y frunció el ceño ligeramente; su silencio era una mezcla pesada de incredulidad y dolor al ver que volvía a cerrarse."
            else:
                $ afinidad_nagi += 1
                show nagi serio at centro_izquierda
                "Nagi frunció el ceño y negó lentamente con la cabeza, sin molestarse en disimular que no se había creído ni una palabra."

            "Nadie insistió."
            "Pero el aire entre los cinco pareció volverse de plomo mientras cada uno procesaba la mentira a su modo."


    "Sin más opciones a sus espaldas, decidieron avanzar hacia una puerta semiabierta al final del corredor."

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

    "[nombre_jugador!c] observó la vieja Biblia entre las manos de Nagi."

    "Varias páginas estaban amarillentas, gastadas por el roce obsesivo de unos dedos pequeños."
    "Marcadas."
    "Subrayadas con trazos temblorosos que parecían haber perdido la cordura a mitad de camino."

    show azura worried at right with dissolve
    a "Miren ahí... Hay una esquina doblada."

    "Nagi pasó las hojas con inusual cuidado hasta detenerse en el pliegue."

    pause 0.5
    play sound paper_flip
    show nagi surprised at centro_izquierda with dissolve
    pause 0.5

    n "«¿Es mi heredad para mí como hiena manchada? ¿No están contra ella las aves de rapiña en derredor?»"
    n "«Venid, reuníos, vosotras las fieras del campo, venid a devorarla.»"

    "La palabra 'hiena' estaba subrayada una y otra vez."
    "Con tanta saña que el grafito del lápiz había terminado por rasgar el papel."

    pause 0.5
    play sound "sfx/wet_whisper.mp3"

    "{color=#390169}{font=fonts/HelpMe.ttf}{cps=16}¿Lo ves ahora, [apodo_jugador]?~{/cps}{/font}{/color}"
    "{color=#390169}{font=fonts/HelpMe.ttf}{cps=16}Qué tierna era, ¿verdad? Gasto tanto lápiz por nada~{/cps}{/font}{/color}"

    show rodrigo tenso at center with dissolve
    "[nombre_jugador!c] tensó la mandíbula. Un escalofrío le recorrió la nuca, justo donde la piel le ardía."

    r "(Cállate. No estás aquí.)"

    "Pero la risita resonó directamente detrás de sus tímpanos, cálida, húmeda y terriblemente divertida."

    "{color=#390169}{font=fonts/HelpMe.ttf}{cps=15}Yo también junté las manitos y recé, ¿sabes?{/cps}{/font}{/color}"
    "{color=#390169}{font=fonts/HelpMe.ttf}{cps=15}Pedí tan fuerte que alguien viniera a salvarme...{/cps}{/font}{/color}"
    "{color=#390169}{font=fonts/HelpMe.ttf}{cps=14}Pero como nadie bajó del cielo, decidí que ser la hiena era mucho más divertido~{/cps}{/font}{/color}"

    show rodrigo molesto with dissolve
    r "(Genial. Ahora el parásito en mi cabeza también da sermones de catecismo.)"
    r "(Solo es fiebre... Es la maldita infección jugándome una mala pasada.)"

    "{color=#390169}{font=fonts/HelpMe.ttf}{cps=16}Oh, vamos, no pongas esa cara de funeral~{/cps}{/font}{/color}"
    "{color=#390169}{font=fonts/HelpMe.ttf}{cps=15}Tú y yo sabemos leer entre líneas, [apodo_jugador].{/cps}{/font}{/color}"

    "El aire de la habitación se volvió denso, casi irrespirable, cargado con ese repentino olor a hierro y azúcar fermentada."
    "[nombre_jugador!c] apartó la mirada de la Biblia de golpe, clavando las uñas en las palmas de sus manos para anclarse a la realidad."

    r "(Es solo tinta vieja en el libro de una niña traumatizada.)"
    r "(No significa una mierda. No tiene nada que ver conmigo.)"

    pause 0.8

    "Sin embargo, su costado herido palpitó al compás de la voz de ella, como una segunda boca dándole la razón."

    "{color=#390169}{font=fonts/HelpMe.ttf}{cps=14}Sigue repitiéndotelo si te hace sentir mejor~{/cps}{/font}{/color}"
    "{color=#390169}{font=fonts/HelpMe.ttf}{cps=12}«Venid… reunid a todas las fieras del campo…»{/cps}{/font}{/color}"
    "{color=#390169}{font=fonts/HelpMe.ttf}{cps=10}Veamos quién termina devorando a quién~{/cps}{/font}{/color}"

    stop music fadeout 1.0
    pause 1.5
    scene habitacion_abandonada at slight_zoom with fade
    play music rodtheme fadein 3.0 volume 0.65
    play ambient forest fadein 3.0

    "El grupo se quedó en silencio varios minutos."
    "Nadie quería ser el primero en admitir que no sabían qué hacer después."

    scene rodrigo_cig_balcony with dissolve

    "[nombre_jugador!c] se acercó al balcón oxidado buscando aire."
    "El metal crujió bajo su peso, pero aguantó."

    "Afuera, la noche era absoluta."
    "Ni una luz. Ni un coche lejano. Ni siquiera el rumor del viento entre los árboles."
    "Solo negrura."

    r "(Esto no es normal… incluso para un bosque tan profundo.)"

    "Miró de reojo hacia el interior de la habitación a través del marco corroído."
    "Nadie dormía. Nagi tenía el bate apoyado sobre las rodillas, Cutipye se frotaba los brazos contra el frío y Azura miraba el suelo en silencio, con una mano aún cerca del bolsillo de su abrigo."
    "Llevaban horas mirándolo de reojo."
    "Desde que lo encontraron en aquel cuarto de máquinas gritándole a los conductos vacíos, desde las manchas oscuras en sus dedos y su sobresalto cuando se apagaron las luces en el pasillo... todos sabían que algo en él no encajaba."

    "Se llevó una mano al costado sin darse cuenta."
    "Bajo la tela manchada de sangre seca, la carne cerrada palpitaba, pero no dolía como debería."
    "Era más bien… una presión tibia. Algo que se expandía y contraía muy despacio."

    play sound heartbeat volume 0.8
    "Latido."
    
    play sound heartbeat volume 0.8
    "Latido."

    play sound heartbeat volume 0.8
    "Latido."

    "No era el suyo."

    r "…"

    "Tenía cuatro pares de ojos agotados a su espalda esperando una respuesta que él mismo temía pronunciar."

    menu:
        "Confesar que sientes la influencia.":
            $ afinidad_luz += 2
            $ afinidad_azura += 2
            $ afinidad_cutipye += 2
            $ afinidad_nagi += 2

            r "(Ya vieron demasiado. Si sigo fingiendo que es solo el golpe de la caída, los voy a poner en peligro.)"
            r "(Merecen saber qué tienen al lado antes de que esto empeore.)"
            jump confesion_rodrigo
        
        "Mantenerlo en secreto.":
            $ estado_mental += 2
            r "(No. Están al límite. Si les digo que tengo esa mierda adentro, el grupo se va a romper aquí mismo.)"
            r "(Necesitan creer que solo estoy aturdido por la caída. Y no voy a darles una razón para que me miren como a las cosas de allá abajo.)"

            "[nombre_jugador!c] dio una calada profunda a su cigarrillo, obligando a sus hombros a destensarse y dejando que el humo amargo tapara el sabor dulce y metálico en su lengua."
            "El latido ajeno dentro de su pecho pareció desacelerarse."
            "O tal vez solo se acomodó detrás de su mentira."
            jump ocultar_influencia

# ==========================================================
# RUTA A: CONFESAR LA INFLUENCIA
# ==========================================================
label confesion_rodrigo:
    scene rodrigo_cig_balcony_2 with dissolve

    "Apagó el cigarrillo contra la baranda oxidada y se giró hacia el interior de la habitación."

    r "Chicos."

    "Todos alzaron la vista casi al mismo tiempo."
    "No hizo falta que levantara la voz; la forma en que sostenía su propio costado les dijo exactamente de qué iba a hablar."

    r "Si vamos a descansar aquí, tenemos que hacerlo por turnos."
    r "Y necesito que el que haga guardia no me quite los ojos de encima."

    "No hubo preguntas ingenuas."
    "Nagi no soltó ningún chiste, y Cutipye dejó de juguetear con el cierre de su chaqueta."
    "En el fondo, todos habían visto su herida cerrarse demasiado rápido en el cuarto de máquinas, el hollín grasiento en sus manos y la forma en que hablaba solo cuando las luces se apagaron."

    show nagi serio at left with dissolve
    n "Habla claro, [apodo_jugador]."
    n "No es por la contusión de cuando caíste del segundo piso, ¿verdad?"

    r "No."

    pause 1.0

    r "Abajo, antes de subir por esa escotilla... ella me alcanzó."
    r "Y desde entonces siento que algo me sigue el rastro. Pero no viene por los pasillos."

    "[nombre_jugador!c] bajó la mirada hacia su propia mano, cerrando los dedos con lentitud para disimular el temblor."

    r "Está adentro."

    show luz worry at right with dissolve
    l "[apodo_jugador]…"

    r "Sé cómo suena. Pero les juro que lo del cuarto de máquinas y lo del pasillo no fue el pánico haciéndome oír cosas."
    r "La escucho. Todo el maldito rato. Es como tener un segundo pulso detrás de los oídos... o algo respirando dentro de mi propia caja torácica cada vez que tomo aire."
    r "Y mi herida... ni siquiera duele como debería. Se siente caliente. Viva."

    show azura worried at centro_derecha with dissolve
    "Azura se abrazó a sí misma, rozando inconscientemente el bolsillo donde había escondido el informe médico de los Huéspedes."

    a "Dios mío, [apodo_jugador]..."

    r "No se los digo para que me tengan lástima. Se los digo porque todavía soy yo el que está hablando."
    r "Pero no sé cuánto tiempo más va a durar eso. Y como estamos encerrados en la misma trampa..."

    show nagi worried at left
    n "Estás infectado."

    "Nagi no lo dijo como una acusación, sino como quien termina de leer un diagnóstico que llevaba horas evitando mirar."
    "La palabra cayó en medio del cuarto como un bloque de plomo."

    l "¡Nagi, cállate!"

    n "No lo digo para joderlo, Luz. Míralo, él mismo nos lo está diciendo."
    n "Todos vimos los papeles allá abajo y vimos lo que había en esa cocina. Sabemos lo que hace esta mierda."
    
    "Nagi apretó la mandíbula, mirando a [nombre_jugador!c] directamente a los ojos, sin retroceder."

    n "Nos metimos juntos en este agujero. Así que no vamos a fingir que estás bien hasta que sea demasiado tarde para todos."

    r "Exacto."
    r "Por eso necesito que estemos de acuerdo desde ahora. Si en algún punto dejo de responder... o si notan que ya no los reconozco..."

    "Dejó la frase colgando en el aire frío. Nadie necesitaba que la terminara."
    "El grupo intercambió una mirada silenciosa, pesada, cargada con el agotamiento de quienes ya no tienen espacio para negarlo."

    show cutipye serious at centro_izquierda with dissolve
    c "A ver, frena ahí. Escúchame bien, [apodo_jugador]."
    
    "Cutipye dio un paso al frente, cruzándose de brazos con una firmeza que rara vez mostraba cuando todo iba bien."

    c "Primero: baja ese tono de despedida, porque nadie aquí va a dispararte, apuñalarte ni dejarte tirado en un rincón."
    c "Entramos los cinco a esta basura de lugar y el problema es de los cinco, nos guste o no."
    c "Segundo: vamos a vigilarte. Todos. Por turnos, como pediste."
    c "Tercero: al primer síntoma raro que sientas, por estúpido que sea, abres la boca y nos avisas. Nada de hacerte el mártir callado."
    
    show cutipye worried at centro_izquierda
    c "Y cuarto…"

    "Deshizo el cruce de brazos y se acercó a él muy despacio, hasta quedar a medio metro."

    c "Si esa cosa quiere meterse en tu cabeza, le vas a hacer la vida imposible. Prométeme que vas a pelear con todo lo que tengas antes de cederle un solo centímetro."
    c "Porque no pienso perderte hoy sin que al menos le des pelea."

    "La determinación en los ojos de Cutipye, respaldada por el asentimiento silencioso de Nagi y Azura detrás de ella, le quitó un peso helado de los hombros."
    "Seguía teniendo un monstruo germinando bajo la piel. Pero al menos ya no lo estaba cargando a escondidas."

    r "…Lo intentaré. Se los prometo."

    "No era una garantía."
    "Pero en un lugar como ese, era lo más honesto que tenía para darles."

    jump escena_luz_balcon_confesion

# ==========================================================
# RUTA B: MANTENERLO EN SECRETO
# ==========================================================
label ocultar_influencia:
    scene rodrigo_cig_balcony_2 with dissolve

    "Apagó el cigarrillo contra el metal húmedo, compuso su expresión más neutra y se giró hacia el grupo."

    r "Chicos."

    "Todos alzaron la vista de inmediato, tensos, como si llevaran rato esperando que por fin hablara."

    r "Deberíamos descansar un par de horas, pero hay que hacerlo por turnos."
    r "Este piso tampoco es seguro."

    show nagi serio at left with dissolve
    n "Eso ya lo sabemos."
    
    "Nagi no apartó la vista de él. Apoyó los codos sobre las rodillas, escrutándolo en la penumbra."

    n "¿Y tú en qué turno piensas dormir? Porque llevas desde el cuarto de máquinas viendo sombras en el techo y saltando cada vez que parpadea un foco."
    n "¿Vas a decirnos qué te pasa o seguimos haciendo como que no vimos nada?"

    show cutipye serious at centro_izquierda with dissolve
    c "Nagi tiene razón, [apodo_jugador]. Tienes la piel helada, apenas hablas y hace un rato en el pasillo..."

    show luz worry at right with dissolve
    l "Déjenlo respirar un segundo, por favor. Cayó desde un segundo piso y tuvo a esa cosa encima."

    "[nombre_jugador!c] aprovechó el salvavidas de Luz sin parpadear."

    r "Es solo eso."
    r "Me golpeé la cabeza al caer por el derrumbe y perdí sangre en la escalera. Estoy aturdido, tengo los oídos zumbando por los disparos en el sótano y llevo toda la noche con la adrenalina al cuello."
    r "Si me vieron raro allá atrás, es porque apenas puedo mantenerme en pie del cansancio. Nada más."

    show azura worried at centro_derecha with dissolve
    "Azura apretó los labios. Sus dedos rozaron el bolsillo de su abrigo donde guardaba la Entrada 09, debatiéndose en silencio entre hablar o creer en la excusa más sencilla."
    "Nagi sostuvo la mirada de [nombre_jugador!c] durante varios segundos interminables."
    "No le creía del todo. Pero el agotamiento en el cuarto era tan denso que nadie tenía fuerzas para iniciar un interrogatorio."

    show nagi worried at left
    n "…Vale. Como quieras, ermitaño."
    n "Pero si te vuelves a marear o escuchas ruidos, despiertas al que esté de guardia antes de ponerte a disparar a oscuras."

    r "Hecho."

    "El grupo desvió la mirada poco a poco, aferrándose a esa mentira porque era mucho más fácil de digerir que la alternativa."
    "Volvieron a discutir en voz baja sobre rutas de escape y posibles salidas del orfanato…"

    c "Si cruzamos por el vestíbulo al amanecer, quizá encontremos una ventana baja que ceda."
    n "O la puerta de carga trasera. Con algo de luz será más fácil no caer en otra trampa."
    l "Sí... solo tenemos que aguantar hasta que salga el sol."

    play sound heartbeat fadein 1.0 loop

    "Pero el latido ajeno volvió a golpear contra sus costillas."
    "Más lento. Más profundo."

    "[nombre_jugador!c] apenas los escuchaba."
    "Las voces de sus amigos empezaron a sentirse lejanas, amortiguadas, como si hablaran desde el otro extremo de un túnel sumergido."

    "{color=#390169}{font=fonts/HelpMe.ttf}{cps=12}{i}Mentiroso~{/i}{/cps}{/font}{/color}"

    r "(Cállate.)"

    "{color=#390169}{font=fonts/HelpMe.ttf}{cps=14}{i}Míralos qué rápido aceptan tu excusa... Prefieren fingir que estás sano antes que mirarte de verdad~{/i}{/cps}{/font}{/color}"
    "{color=#390169}{font=fonts/HelpMe.ttf}{cps=12}{i}No necesitan saberlo todavía. Que sea nuestro secreto un ratito más~{/i}{/cps}{/font}{/color}"

    "[nombre_jugador!c] apretó los dientes, dándoles la espalda otra vez hacia la baranda helada."

    r "(No estoy perdiendo el control.)"
    r "(Todavía puedo manejarlo yo solo.)"

    stop sound fadeout 1.0

    jump escena_luz_balcon_oculta

label escena_luz_balcon_confesion:
    scene balcon_abandonado_night
    show rodrigo worried at centro_derecha
    with dissolve

    "Más tarde."

    "[nombre_jugador!c] seguía en el balcón."
    "Luz se sentó a su lado, hombro con hombro."

    show luz sad at centro_izquierda
    with moveinleft

    l "No tienes que cargar con esto solo."

    r "No quiero que me vean… cuando pase."

    l "Entonces no mires hacia otro lado cuando me mires a mí."
    l "Mírame ahora."

    "[nombre_jugador!c] giró la cabeza con lentitud."

    "Los ojos de Luz brillaban bajo la luz mortecina."
    "No había miedo en ellos."
    "Solo determinación."

    l "Sea lo que sea que esté intentando meterse en ti…"
    l "Va a tener que pasar por encima de mí primero."

    "[nombre_jugador!c] dejó escapar una risa rota."

    r "Eres terrible mintiendo."

    l "No estoy mintiendo."
    l "Estoy amenazando a un parásito."

    "Se quedaron en silencio."

    "El viento trajo un olor extraño."
    "Dulce. Metálico. Familiar."

    play sound "sfx/drip_distant.mp3"

    "Una gota cayó desde el techo del balcón."
    "Aterrizó en el dorso de la mano de [nombre_jugador!c]."

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

    "[nombre_jugador!c] cerró los ojos con fuerza."

    "{cps=9}{color=#390169}{i}Shhh…{/i}{/color}{/cps}"
    "{cps=9}{color=#390169}{i}Ya casi estamos en casa…{/i}{/color}{/cps}"

    "Cuando volvió a abrir los ojos…"

    "La gota ya no estaba."

    "Pero su mano temblaba."

    "Y por primera vez…"
    "No estaba seguro de quién la estaba moviendo."
    
    pause 1.5
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

    "[nombre_jugador!c] seguía en el balcón."
    "Tenía los brazos apoyados en la baranda, rígido."
    "Demasiado quieto."

    show luz serious at centro_izquierda
    with moveinleft

    l "[apodo_jugador]."

    "Él no respondió."

    l "No hagas eso."

    r "¿Qué cosa?"

    l "Desaparecer aunque estés aquí."

    pause 0.5

    r "Estoy bien."

    l "No."
    l "Estás funcionando."
    l "Que no es lo mismo."

    show rodrigo molesto with dissolve
    "[nombre_jugador!c] apretó la mandíbula."

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

    "[nombre_jugador!c] cerró los ojos un segundo de más."

    "{cps=9}{color=#390169}{i}Díselo.{/i}{/color}{/cps}"

    "{cps=9}{color=#390169}{i}Quiero ver su cara cuando lo entienda…{/i}{/color}{/cps}"

    r "(Cállate.)"

    l "¿Qué dijiste?"

    r "Nada."

    "Luz dio un paso más cerca."

    l "[nombre_jugador!c]."
    l "Si te estás quebrando por dentro, prefiero saberlo."
    l "Prefiero sostenerte ahora que recoger los pedazos después."

    "Sus ojos brillaban, pero esta vez sí había algo más."
    "Miedo."

    l "No me excluyas."
    l "No me castigues con silencio."

    "[nombre_jugador!c] la miró."
    "Por un momento pareció que iba a hablar."

    pause 1.0

    r "Si empiezo a perder el control…"
    r "No quiero que tu última imagen mía sea esa."

    l "Entonces dame algo mejor que recordar ahora."

    "El aire se volvió denso."

    play sound "sfx/drip_distant.mp3"

    "Una gota cayó desde el techo del balcón."
    "Aterrizó en el dorso de la mano de [nombre_jugador!c]."

    show rodrigo scared

    l "…[apodo_jugador]."

    "La sustancia era negra."
    "Y se movía."

    "Muy despacio."

    l "No te muevas."

    "La gota avanzó hacia su muñeca."
    "Y desapareció bajo la piel."

    stop sound fadeout 1.0

    "[nombre_jugador!c] contuvo el aliento."

    "{cps=9}{color=#390169}{i}¿Ves?{/i}{/color}{/cps}"
    "{cps=9}{color=#390169}{i}Ni siquiera ahora puedes decírselo todo…{/i}{/color}{/cps}"

    "Luz tomó su mano con fuerza."

    l "Mírame."
    l "Respira conmigo."

    "Inhalaron."
    "Exhalaron."

    "Otra vez."

    "La mano de [nombre_jugador!c] temblaba."

    show rodrigo nervioso with dissolve
    r "No sé si…"
    r "No sé si soy solo yo aquí dentro."

    "Luz no soltó su mano."

    l "Entonces vamos a averiguarlo juntos."

    "Pero esta vez…"

    "[nombre_jugador!c] no estaba seguro de si eso seguía siendo verdad."
    pause 1

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

    "Pero [nombre_jugador!c] y [min_afinidad_personaje!c]…"

    "Aún no se movían."
    "Como si el sueño los hubiera retenido un poco más."

    show rodrigo neutral at center with dissolve

    "[nombre_jugador!c] abrió los ojos. No hubo el parpadeo perezoso de quien despierta de un sueño, sino la apertura súbita de una lente."
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
        l "[apodo_jugador]…"
        l "¿Dormiste algo?"

    "[nombre_jugador!c] no respondió de inmediato."
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

    "[nombre_jugador!c] caminaba al frente, pero sus pasos eran irregulares."
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
    "[nombre_jugador!c] parpadeaba menos."
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
    "El vacío central del vestíbulo parecía llamar a [nombre_jugador!c]. Sus ojos escaneaban las barandillas del piso superior con una precisión casi geométrica."

    show cutipye neutral at left
    c "Dividámonos para cubrir más—"

    hide rodrigo
    show rodrigo neutral at center with moveinright  # Ya se mueve

    "Pero [nombre_jugador!c] no esperó. Sus pasos eran silenciosos, apoyando primero la punta del pie, como si evitara alertar a algo que todavía no veía."

    l "¿[apodo_jugador]?"
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
        l "¡[apodo_jugador]!"

    stop music
    play music chase fadein 0.5

    if estado_mental < 10:  # COMBATE HUMANO
        scene vestibulo_fight_normal with dissolve
        play sound "sfx/human_scream.mp3"
        
        "La criatura saltó. [nombre_jugador!c] reaccionó con la torpeza del miedo, lanzándose desde el rellano hacia el cuerpo del mutante."
        "Cayeron en un revoltijo de extremidades y polvo. [nombre_jugador!c] forcejeaba, sintiendo el aliento fétido y caliente de la rata contra su cuello."
        
        r "¡Atrás! ¡Hijo de puta!"

        "Enterró la daga en el hombro de la bestia. No fue un golpe limpio. Fue un tajo desesperado que apenas logró separarlos."
        "[nombre_jugador!c] retrocedió jadeando, la adrenalina quemándole las venas mientras veía a la criatura lamerse la herida con una lengua negra y bífida."
        
        play sound "sfx/stab.mp3"
        with vpunch

    elif estado_mental < 15:  # COMBATE SINTETIZADO (Crow vs Rat)
        show layer master at distortion_light # ACTIVAR DISTORSIÓN LIGERA
        scene vestibulo_fight_saturated with dissolve
        play sound "sfx/beast_growl.mp3"

        "El mundo se volvió más brillante, más nítido. Los colores de la sangre y el moho saltaron a la vista de [nombre_jugador!c] con una intensidad violenta."
        "La criatura se lanzó hacia [min_afinidad_personaje!c], pero [nombre_jugador!c] ya estaba en el aire."

        "No fue un salto humano. Fue un picado."
        "[nombre_jugador!c] aterrizó sobre la espalda del mutante, sus pies buscando instintivamente los puntos de apoyo en los omóplatos. La daga bajó como un pico, buscando los ojos, buscando la base del cráneo."

        r "(Ciega al rastrero. Quiebra sus patas.)"

        "El mutante chilló y se revolvió, pero [nombre_jugador!c] se mantenía pegado a su espalda con una agilidad antinatural, girando la cabeza con movimientos rápidos y espasmódicos."
        
        play sound "sfx/slash_rough.mp3"
        with shake

    else:  # COMBATE BRUTAL / PREDADOR (The Raven's Feast)
        show layer master at distortion_heavy # ACTIVAR DISTORSIÓN PESADA
        scene vestibulo_fight_glitch with dissolve
        play sound "sfx/primal_screech.mp3"

        "La realidad se fracturó. La tonalidad del mundo viró hacia un espectro enfermo, donde el calor de la presa era lo único que importaba."
        "[nombre_jugador!c] no gritó. Emitió un chasquido seco desde el fondo de su garganta mientras se lanzaba desde la barandilla."

        "El impacto contra el huésped-ratón fue brutal. El sonido de los huesos de la criatura rompiéndose bajo el peso de [nombre_jugador!c] resonó en todo el vestíbulo."
        "Fue una ejecución, no una pelea."

        "[nombre_jugador!c] sujetó la cabeza del mutante con una mano, forzándola hacia atrás para exponer el cuello, mientras su otra mano hundía la daga una, dos, tres veces. Movimientos cortos. Precisos. Despiadados."
        "Como un cuervo destripando a una rata en un callejón, [nombre_jugador!c] no se detuvo cuando la criatura dejó de luchar. Sus ojos estaban fijos, sin parpadear, reflejando una sed que no era suya."

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

    "[nombre_jugador!c] permanecía en cuclillas sobre el cadáver."
    "Sus dedos goteaban icor. Sus pulmones trabajaban con un ritmo mecánico, pesado."

    "El grupo lo miró. Nadie se acercó."

    if min_afinidad_personaje == "nagi":
        show nagi shocked at centro_izquierda
        n "[apodo_jugador]... eso no fue defenderse. Eso fue... carnicería."
    elif min_afinidad_personaje == "cutipye":
        show cutipye shocked at left
        c "Parecías... disfrutándolo. Tu cara..."
    elif min_afinidad_personaje == "azura":
        show azura shocked at right
        "Azura se tapó la boca con la mano, sus ojos fijos en la forma en que [nombre_jugador!c] inclinaba la cabeza, examinando los restos."
    elif min_afinidad_personaje == "luz":
        show luz shocked at centro_derecha
        l "…¿[nombre_jugador!c]? Por favor, mírame."

    "[nombre_jugador!c] levantó la mirada."
    "Por una fracción de segundo, la luz del amanecer incidió en sus pupilas, revelando un brillo aceitoso, negro, que devoraba cualquier rastro de humanidad."
    
    r "Está muerto. Es lo que importa."

    scene black with fade
    stop ambient fadeout 2.0

    call chapter_complete("Capítulo 8")
    jump cap_9

label cap_9:

    scene black with fade
    "Antes de todo esto..."
    "Antes del orfanato, antes del miedo constante..."
    "Hubo tiempos más simples."
    "Una noche cualquiera."

    scene fiesta_flashback1 with dissolve  # Imagen de una fiesta animada, perhaps en un salón o casa.
    show layer master at sepia_filter
    play ambient "bgm/nostalgic_party.mp3" fadein 1.0
    "Luces cálidas colgaban del techo del pequeño salón."
    "La música rebotaba contra las paredes mientras grupos de jóvenes reían, gritaban y bailaban sin preocuparse demasiado por el mañana."

    "Entre la multitud, Luz tiraba suavemente del brazo de [nombre_jugador!c], abriéndose paso entre la gente."

    l "¡Anda, [apodo_jugador]! ¡Apúrate!"
    "[nombre_jugador!c] avanzaba detrás de ella con visible incomodidad, mirando a su alrededor."
    "Demasiadas caras desconocidas."
    "Demasiado ruido."
    "Demasiado... Todo."
    l "¡Nagi organizó esto para todos, y me costó convencerlo de que te dejara ir!"
    "Se gira hacia el con una sonrisa radiante."
    l "¡Va a ser genial!"

    menu:
        "Aceptar con entusiasmo":
            $ afinidad_luz += 2
            r "No soy muy de fiestas, pero si tú vas... No veo por qué no."
            "[nombre_jugador!c] se encoge de hombros con una leve sonrisa."

            r "Hagámoslo."
            l "¡Así me gusta!"

            "Luz levanta el puño victoriosa."
            l "¡Prometo que no te vas a arrepentir!"
        "Aceptar a regañadientes":
            $ afinidad_luz += 1
            r "Sabes que no es lo mío, Luz..."

            "[nombre_jugador!c] observa el lugar con desconfianza."
            r "...pero bueno, iré por tí."

            "Luz suspira exageradamente."
            l "Ay, ¡Qué amargado!"
            
            "Luego le da un pequeño empujón juguetón."
            l "Pero gracias por hacer el esfuerzo"
            l "De verdad."

    scene fiesta_flashback2 with dissolve
    "El interior de la casa estaba aún más lleno de lo que parecía desde afuera."
    "La música vibraba en el suelo."
    "El aire estaba cargado con olor a alcohol, perfume barato y calor humano."
    "[nombre_jugador!c] frunce ligeramente el ceño."
    "Su instinto le decía que aquel lugar no era para él."
    "Antes de que pudiera decir algo, dos figuras conocidas aparecieron entre la multitud."

    show nagi smile at left
    show cutipye smile at right
    with dissolve

    n "¡Pero miren quien llegó!" 
    "Nagi levanta su vaso en señal de saludo."

    n "El intelectual del grupo."
    n "¡Suelta ese ceño fruncido, [apodo_jugador]!"
    
    c "Sí, relájate un poco."
    "Cutipye le ofrece un vaso."
    c "Un par de tragos no matan a nadie."
    c "Ayúdanos a que el ambiente prenda."

    "[nombre_jugador!c] mira el vaso."
    "Luego mira a Luz."

    menu:
        "Aceptar el trago sin dudar":
            $ afinidad_nagi += 2
            $ afinidad_cutipye += 2
            r "Bueno..."
            "[nombre_jugador!c] giró el vaso entre sus dedos."

            r "No creo que a Luz le moleste si bebo un par..."

            pause 0.5
            "Hace una pausa."
            "Luego se encoge de hombros."
            r "Bah, qué mierda."
            r "¡Vamos por unos tragos!"

            "Nagi soltó una carcajada como respuesta."
            n "¡Ese es el espíritu!"

            "El primer vaso desaparece rápido."
            "Luego viene otro."
            "Y otro más."

        "Dudar, pero aceptar":
            $ afinidad_nagi += 1
            $ afinidad_cutipye += 1
            r "{cps=20}Bieeen...{/cps}"
            "[nombre_jugador!c] suspiró."

            r "Pero solo para entrar en calor."
            n "¡Ese es el espíritu!"
            n "Vas a ver que te vas a relajar, hermano."

            "El vaso llega a su mano."
            "Y la noche comienza a rodar."

    scene fiesta_flashback3 with dissolve
    "La música subía."
    "Las risas se mezclaban con gritos y conversaciones superpuestas."
    "Un vaso se convirtió en dos."
    "Luego en tres."
    "Y de alguna forma..."

    "[nombre_jugador!c] empezó a sentirse cómodo."
    "Demasiado cómodo."

    "Las conversaciones fluían."
    "Las bromas salían solas."

    "Por primera vez en mucho tiempo, [nombre_jugador!c] no estaba pensando."

    "Solo estaba... viviendo."

    "En algún punto, incluso olvidó dónde estaba Luz."
    "Olvidó a Azura."
    "Olvidó todo."

    show nagi smile at centro_izquierda with dissolve
    "Nagi se acercó, sus ojos brillando de una forma distinta."
    "Sacó algo fino de detrás de su oreja, acercandolo al inexperto chico."
    
    "Nagi reaparece a su lado."

    "Sus ojos brillan con una energía distinta."

    "Con un movimiento rápido, saca algo fino de detrás de su oreja."

    n "Oye, [nombre_jugador!c]..."
    r "¿Hmm?"
    n "¿Quieres probar algo más..."

    "Nagi sonríe."

    n "...elevado?"

    "[nombre_jugador!c] parpadea."

    r "¿Fumar?"
    n "Te enseñaré."
    n "Es fácil."

    menu:
        "Seguirle el juego":
            $ afinidad_nagi += 3
            r "Nunca lo he hecho..."

            "[nombre_jugador!c] observó el porro improvisado."
            r "Pero qué más da. Enséñame."

            "Nagi ríe."

            n "Así se habla."

            "El primer intento es torpe."
            "El humo le quema los pulmones."

            "[nombre_jugador!c] tose."
            "Nagi se ríe."

            "Pero después..."
            "Algo cambia."
            "El mundo empieza a sentirse... diferente."

            $ riesgo_salud = True
        "Aceptar por presión":
            $ afinidad_nagi += 2
            $ afinidad_cutipye += 1

            r "No sé si sea buena idea..."
            r "Pero no quiero ser el único aburrido aquí."

            "Nagi sonríe como si hubiera ganado una apuesta."
            "[nombre_jugador!c] lo intenta."
            "Tose."
            "Nagi se burla."

            n "¡Respira, hombre!"

            "El humo llena su cabeza de estática."

            $ riesgo_salud = False
    
    stop music fadeout 1.0
    scene bg_fiesta_borrosa with flash
    play sound heartbeat loop

    "De pronto..."
    "El mundo se inclinó."

    "Las luces comenzaron a girar."
    "La música ya no era música."
    "Era ruido."
    "Ruido aplastando su cabeza."

    "La memoria de [nombre_jugador!c] se volvió fragmentos sueltos."
    "Imágenes inconexas."

    "Risas."
    "Luces."
    "Sombras."

    "Su corazón latía demasiado rápido."
    "Demasiado fuerte."

    r "{cps=20}C-Cuty...{/cps}"

    "[nombre_jugador!c] intenta ponerse de pie."
    "Las piernas no responden."

    r "{cps=20}Algo...{/cps}"

    "El suelo se acerca peligrosamente."

    r "{cps=20}Algo no está bien...{/cps}"

    "El sabor ácido del vómito invade su boca."
    "El mundo se apaga."
    
    stop sound
    scene black with fade

    "Silencio."
    "Voces lejanas."
    "Pasos."
    "Agua corriendo."
    "Órdenes."

    show azura neutral at center with dissolve
    "La voz de Azura llega desde el teléfono."
    "Calmada."
    "Firme."
    "Como si nada pudiera sacarla de su centro."

    a "Escuchen bien."
    a "Nagi. Cutipye."
    a "Dejen de entrar en pánico."

    "Un breve silencio."

    a "Denle té de manzanilla."
    a "Y báñenlo ahora mismo con agua templada."
    a "Necesitamos bajar su ritmo cardíaco."
    a "Luz ya viene en camino."
    a "Ella se encargará del resto."

    pause 1.5

    scene bg_habitacion_luz with dissolve
    "La mañana llega demasiado pronto."

    "La luz que entra por la ventana es un cuchillo en los ojos de [nombre_jugador!c]."
    "Su cabeza late."
    "Su garganta está seca."
    "Su cuerpo pesa toneladas."

    "Lentamente abre los ojos."
    "Mira alrededor."
    "Una habitación que no reconoce."
    "Mantas que no son suyas."
    "Ropa que definitivamente no es suya."

    "El olor a manzanilla flota en el aire."

    scene bg_habitacion_luz1 with dissolve

    "Antes de que pueda reaccionar..."
    play music flashback fadein 1.5
    "Luz se lanza sobre él."

    l "¡[nombre_jugador!c]!"

    "Sus brazos lo rodean con fuerza."

    l "¡Dios mío, pensé que te perdía!"
    l "¡No vuelvas a hacerme algo así!"

    menu:
        "Sarcasmo clásico":
            $ afinidad_luz += 2

            "[nombre_jugador!c] parpadea."
            "Todavía confundido."

            r "Oye..."
            r "¿Esta pijama es de tu papá?"

            "Se mira la manga."
            r "Me queda un poco ajustada de los hombros..."

            "Luz se queda en silencio."
            "Luego lo golpea suavemente."
            l "¡Eres un idiota!"

            "{i}Llora y ríe al mismo tiempo.{/i}"

        "Sinceridad vulnerable":
            $ afinidad_luz += 4
            r "Perdóname, Luz..."

            "[nombre_jugador!c] evita su mirada."
            r "Me pasé de la raya."
            r "No debí dejarme llevar así."

            "Luz lo abraza más fuerte."
            "Como si todavía necesitara comprobar que está vivo."

    scene black with fade
    "En aquel entonces..."
    "Parecía solo una mala noche."
    "Una anécdota vergonzosa."
    "Un susto pasajero."

    stop music fadeout 2.0
    "Ahora..."
    "Esos recuerdos se sienten como ecos de otro mundo."
    "Uno donde todavía existía algo parecido a la normalidad."

    scene vestibulo_dawn
    show rodrigo frustrado at center
    show luz worry at centro_derecha
    show azura worried at right
    show nagi serio at centro_izquierda
    show cutipye serious at left
    with fade  # Escena del vestíbulo después de la pelea, con el mutante derrotado en el suelo.
    #play music "bgm/tense_confrontation.mp3" fadein 1.0
    play music ambiental fadein 1.0

    "El vestíbulo huele a óxido caliente, bilis y carne abierta."
    "El cuerpo de la criatura yace a unos metros. Demasiado destrozado."
    "{cps=15}Demasiado... irreconocible.{/cps}"

    play sound "sfx/heavy_breathing.mp3" loop volume 0.5
    "Las manos de [nombre_jugador!c] todavía tiemblan."
    "Siente los dedos extrañamente livianos, fríos, como si toda la sangre se le hubiera escurrido hacia los codos y una baja de presión le estuviera vaciando las palmas."
    "Aprieta el mango de la daga, pero apenas percibe el tacto del metal contra su piel adormecida."
    "Y en el fondo de su estómago, revuelto de náuseas, no sabe si tiembla por el esfuerzo brutal..."
    "...o por el segundo exacto en que disfrutó escuchar cómo cedía el hueso."

    show nagi scared at left with dissolve
    n "¡¿Qué mierda ha sido eso?! ¡El ratón de biblioteca que conozco no habría acabado con esa bestia ni con toda la adrenalina de la muerte encima, y mucho menos habría dejado su cráneo como un maldito queso suizo!"
    
    "Nagi señala el cadáver con el bate tembloroso. Evita mirar directamente a [nombre_jugador!c] a los ojos."

    show azura worried at right with dissolve
    a "¿No creen que... tras todo lo que ha pasado, tenga sentido que empiece a decir que 'escucha voces'?"
    a "O sea, dudo que le esté dando exactamente lo mismo que a las bestias del orfanato... Podría ser solo el colapso nervioso o el pánico acumulado."
    a "...¿O no, Cuty?"

    pause 1.0

    show cutipye serious at centro_izquierda with dissolve
    c "Miren, ya no tiene ningún caso discutir si [nombre_jugador!c] tenía razón o no. Venir a este orfanato fue una idea estúpida desde el principio y tenemos que largarnos de aquí cuanto antes."

    "Nadie da un paso hacia él."
    "Sin darse cuenta, han formado un semicírculo a varios metros de distancia."
    "Como si acorralaran al siguiente peligro de la habitación."

    show luz worry at centro_derecha with dissolve
    l "¡Esperen! ¡[nombre_jugador!c] no es un monstruo... él solo nos protegió! ¡No lo miren así!"
    
    show nagi angry at left
    n "¡Pero míralo, Luz! ¡Está bañado en sangre y nos mira como un animal acorralado!"
    
    l "¡No me importa! ¡Es nuestro amigo, y lo que hizo fue para que esa cosa no nos matara! ¡Denle aunque sea un segundo para respirar y explicarse!"

    pause 1.2

    "[nombre_jugador!c] intentó darles la razón. Intentó decirles que seguía ahí dentro."
    "Pero al tragar saliva, su garganta ardió como si hubiera tragado vidrio molido."
    "Las puntas de sus dedos habían perdido toda sensibilidad; un hormigueo helado le trepaba por las muñecas hasta los hombros, entumeciéndole la piel."

    r "Yo... Chicos, yo no quise—"

    # --- INICIO DEL COLAPSO SENSORIAL Y ATAQUE DE PÁNICO ---
    show screen screen_distortion_light
    play sound "sfx/voices_overlapping.mp3"
    play ambient "sfx/ringing.mp3" fadein 1.0
    with hpunch

    "El sonido de su propia voz se quebró, ahogado por un zumbido agudo que le perforó los tímpanos."
    "Las voces de sus amigos empezaron a superponerse unas sobre otras, desfasadas, rebotando contra las paredes como estática rota."
    "Demasiado fuertes."
    "Demasiado cerca."

    play sound glx_laugh
    "{color=#390169}{font=fonts/HelpMe.ttf}{cps=16}Ja, ja, ja... ¿Lo ves, [apodo_jugador]?~{/cps}{/font}{/color}"
    "{color=#390169}{font=fonts/HelpMe.ttf}{cps=15}Míralos bien. Tus 'amigos' se mueren de miedo de ti. Son tan frágiles~{/cps}{/font}{/color}"

    show nagi angry at left, panic_saturate_jitter
    show cutipye serious at centro_izquierda, panic_saturate_jitter
    show luz worry at centro_derecha, panic_saturate_jitter
    show azura worried at right, panic_saturate_jitter
    with vpunch

    "Su visión parpadea con violencia."
    "El suelo del vestíbulo parece inclinarse hacia un lado, robándole el equilibrio."
    "Los bordes de todo lo que mira se saturan hasta quemar la retina; los colores se deforman, chillones e irreales, como si el mundo físico no soportara la velocidad a la que se disparan sus pensamientos."

    "Un calor húmedo e insoportable le inunda los ojos de golpe."
    "Quiere contener las lágrimas, aprieta los párpados con rabia para no llorar frente a ellos, pero el nudo en su tráquea es tan grande que le impide pasar el aire."

    play sound "sfx/heart_slow.mp3" loop
    "Su pulso golpea contra sus costillas. Desbocado. Hueco."
    "Toma una bocanada de aire corta, desesperada, pero sus pulmones se sienten cerrados."
    "Algo empuja desde el fondo de su esternón, abriéndose paso a codazos entre sus órganos."
    "Algo que quiere salir."

    a "Tal vez sea el estrés acumulado, pero esto no es normal..."
    c "Luz, aléjate de él, esto es peligroso. Debemos irnos antes de que... algo peor pase."
    l "¡Basta! ¡[nombre_jugador!c] ha pasado por un infierno! ¡Todos lo hemos hecho! ¡Apóyenlo en vez de tratarlo así!"
    l "¡No lo abandonaremos! ¡Él nos necesita!"

    play sound "sfx/low_drone.mp3"
    with vpunch
    "La palabra {b}'abandonar'{/b} se despega del resto de la frase."
    "Retumba en su cráneo."
    "Se deforma en medio de la estática, estirándose como un alarido metálico hasta borrar todo lo demás."

    hide screen screen_distortion_light
    show screen screen_distortion_heavy
    
    # Los sprites de los amigos comienzan a corromperse visualmente
    show nagi angry at left, sprite_corrupt_glitch
    show cutipye serious at centro_izquierda, sprite_corrupt_glitch
    show azura worried at right, sprite_corrupt_glitch
    with hpunch

    "La risa de Galaxia ya no suena en la habitación; resuena dentro de su propia médula, pegada a su nuca, respirando por su misma boca."

    "{color=#390169}{font=fonts/HelpMe.ttf}{cps=14}Hazlo. Termina de romperte y demuéstrales lo que eres~{/cps}{/font}{/color}"

    r "(¡No! ¡Cállate!)"
    r "(¡No quiero! ¡Yo no soy eso!)"

    play sound "sfx/beast_growl.mp3"
    "Intenta gritarles que se tapen los oídos, que él sigue aquí, pero lo que escapa de su garganta cerrada no suena a palabras."
    "Suena como un gruñido ronco, animal y quebrado de llanto bajo su pecho."

    "A través del velo borroso de las lágrimas que se le escapan sin permiso, [nombre_jugador!c] recorre las siluetas distorsionadas frente a él."
    "Sus rostros parecen parpadear, desfigurados por sombras negras y trazos de estática."
    "Nagi retrocede medio paso, alzando el bate."
    "Azura aprieta los labios, temblando."
    "Cutipye tensa las piernas, calculando la distancia hacia la puerta."
    "Y Luz... Luz se adelanta."

    "Tienen miedo."
    "Ya no tienen miedo por él."
    "{b}Tienen miedo de él.{/b}"

    "La culpa y el pánico le aplastan el pecho como una losa de plomo."
    "Ya no siente sus propias manos. No siente el suelo bajo sus botas. Solo escucha el jadeo frenético, superficial y asfixiante de su propia hiperventilación."

    centered "{color=#ff0033}{cps=25}¿En qué mierda te estás convirtiendo?{/cps}{/color}"
    centered "{color=#ff0033}{cps=25}¿Y si Galaxia tiene razón?{/cps}{/color}"
    centered "{color=#ff0033}{cps=25}¿Y si ya cruzaste la línea y ni siquiera te diste cuenta?{/cps}{/color}"

    "Su respiración se acelera hasta marearlo. Corta. Entrecortada. Insuficiente."
    "Las paredes del vestíbulo laten al ritmo de la estática."
    "El mundo entero empieza a girar demasiado rápido para sus ojos... o es su cuerpo el que se está moviendo más rápido que el mundo."
    "Ya no puede distinguir la diferencia."

    show luz worry at center, sprite_corrupt_glitch with move
    "En medio del ruido ensordecedor, una de las figuras da un paso más hacia su punto ciego."
    "Extiende una extremidad pálida con cuidado."
    "Como quien intenta tocar a una bestia rabiosa y herida."

    l "[apodo_jugador]... mírame, tranquilo... Estoy aquí contigo."

    "Los dedos cálidos de ella rozan el hombro de [nombre_jugador!c]."

    # --- EL IMPACTO ---
    show luz scared at center, threat_shadow_corrupt
    play sound slash
    stop music
    stop ambient
    with hpunch
    scene black with flashred

    "El contacto le quema la piel como hierro al rojo vivo."

    r "¡¡N-NO ME TO—!!"

    "Su cerebro saturado de pánico no registra el rostro de Luz."
    "Su pupila contraída solo procesa una silueta negra invadiendo su cuello."
    "Una amenaza directa."
    "Un ataque."

    "El cuerpo infectado de [nombre_jugador!c] actuó medio segundo antes que su conciencia."
    "Un espasmo ciego. Un reflejo puramente depredador nacido del terror absoluto."
    "Una embestida desesperada para quitarse el peligro de encima."

    # --- EL SILENCIO POSTERIOR ---
    hide screen screen_distortion_heavy
    play sound "sfx/thud.mp3"
    with vpunch

    "El golpe seco de un cuerpo cayendo de espaldas resuena en todo el vestíbulo."
    "Pesado."
    "Hueco."

    pause 1.5

    "Y de pronto, la estática desaparece."
    "La risa de Galaxia se apaga de golpe. No vuelve."
    "No hace falta. El silencio que deja detrás es infinitamente peor."

    scene vestibulo_sangre with fade
    play music rodtheme fadein 2.0
    
    show cutipye shocked at left
    show nagi shocked at centro_izquierda
    show azura desesperada at right
    with dissolve

    c "¡¡Luz!! ¡¡NO!!"
    n "¡Joder, no! ¡¡Dios mío!!"
    a "¿Qué... qué has hecho...?"

    "La niebla ácida se disipa de sus ojos de un solo golpe, devolviéndole el tacto en las manos, el peso de su cuerpo y la nitidez cruel de la mañana."
    "A sus pies, un charco escarlata comienza a extenderse lentamente sobre las baldosas sucias bajo el pecho de ella."
    "Rojo. Brillante."
    "Imposible de negar."

    "El tiempo recupera su velocidad normal."
    "Y encierra a [nombre_jugador!c] dentro de lo que acaba de hacer."

    show rodrigo shock_state at center with dissolve
    r "(No...)"
    r "(No, no, no, por favor, no...)"

    "Sus rodillas ceden. Las lágrimas que había intentado retener le caen de golpe por las mejillas heladas mientras mira hacia abajo."

    centered "{cps=15}Tus manos.{/cps}"
    centered "{cps=10}{b}Tus malditas manos.{/b}{/cps}"

    scene closeup_luz_dying with dissolve  # Close-up de Luz herida.
    if afinidad_luz >= 13:
        l "Te quiero... [nombre_jugador!c]. No olvides nuestros momentos... vive por mí."  # Máximo afecto: Amor y legado. Muy raro.
    elif afinidad_luz >= 10:
        l "[apodo_jugador]... Amor... siempre estaré contigo en espíritu."  # Alto afecto, conexión emocional.
    elif afinidad_luz >= 7:
        l "Te... aprecio tanto... no dejes que esto te destruya."  # Afecto moderado, preocupación por él.
    elif afinidad_luz >= 5:
        l "[nombre_jugador!c], no te culpes... fuiste fuerte por nosotros."  # Empieza a mostrar apoyo.
    elif afinidad_luz >= 3:
        l "No... fue un accidente... lo sé..."  # Ligeramente más comprensiva.
    else:
        l "[nombre_jugador!c]... duele... ¿por qué?"  # Mínimo afecto: Confusión y dolor. Más probable.

    if afinidad_luz >= 10:
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

        "Ella fue quien integró a [nombre_jugador!c] al grupo."
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

    "Las lágrimas de [nombre_jugador!c] caían sobre el rostro de Luz."
    "Pero ella ya no responde."

    "La risa de Galaxia no vuelve."
    "No hace falta."
    "El silencio es peor."

    pause 2

    scene black with fade
    stop music fadeout 2.0
    stop ambient fadeout 2.0

    call chapter_complete("Capítulo 9")
    jump cap_10

label cap_10:

    scene bg pasillo_derruido with fade
    play music "audio/ambience/pasillo_tenso.ogg" fadein 2.0 loop   # música de fondo tensa opcional

    "El pasillo administrativo está medio derrumbado. El techo cruje. Las luces parpadean con ese zumbido eléctrico insoportable."

    "[nombre_jugador!c] camina último."
    "Sus pasos son más pesados que antes."
    "Respira mal."
    "Se detiene cada cierto tiempo, como si estuviera escuchando algo que los demás no oyen."

    show azura worried at left with dissolve

    "Azura se volvió hacia él con miedo reflejado en sus ojos esmeralda."
    a "[apodo_jugador]… Dime que estás bien. Por favor."

    "[nombre_jugador!c] tarda en responder. Su voz sale rasposa."
    "Cuando lo hizo, su voz salió con la espereza del papel de lija."
    r "Sí. Solo… sigan caminando. No se separen."

    "Mientras hablñaba, su mano derecha se hundió en su pecho, sus uñas raspando la tela de su camisa en un tic nervioso del que parecía no ser consciente."

    show cutipye at centro_izquierda with dissolve

    c "(en voz baja) Está empeorando… Lo ves en sus ojos, ¿Verdad?"

    "Nagi se detiene en seco, sus botas rechinando contra el suelo sucio."
    "Se giró con una violencia repentina, enfrentando a [nombre_jugador!c] con una mezcla de pavor y furia contenida."

    if afinidad_nagi < 3:
        jump traicion_nagi
    else:
        jump nagi_no_traiciona

label traicion_nagi:

    "Nagi estalló, agitando los brazos con desesperación."
    n "¿¡Sabes qué!? ¡Ya basta!"

    "El grupo se congeló en el sitio. La tensión era casi sólida."
    a "¿Nagi…?"

    "Él señaló a [nombre_jugador!c] con un dedo tembloroso, acusándolo frente a todos."
    n "Desde que entramos en este jodido lugar, todo gira en torno a él."
    n "Sus ataques."
    n "Sus cambios de humor."
    n "Sus… Malditas cosas raras."

    "[nombre_jugador!c] baja la mirada, incapaz de sostenerle el juicio."
    "Intenta hablar, pero su mandíbula se tensa antes de que pueda articular bien."

    r "No estoy… perdiendo el control, Nagi. No todavía."

    "Sin embargo, incluso mientras hablaba, su pupila se dilató hasta casi devorar el iris."
    "Dió un paso al frente, un movimiento rígido y forzado."
    r "Escuchen bien."
    r "No pedí nada de esto."
    r "Ni las voces, ni el hambre, ni el frío."

    "Traga saliva con dificultad, y su voz descendió una octava, volviendose algo más grave."

    r "Pero si nos dividimos, estamos muertos."
    r "Galaxia nos cazará uno a uno.."
    r "Solo... Manténganse cerca."
    r "Si pierdo el control… me detienen."
    r "Pero no se vayan."

    "El silencio que siguió fue sepulcral."
    "Azura y Cutipye lo miraban con una compasión dolorosa, pero Nagi soltó una carcajada seca que sonó a cristales rotos."

    n "¿Aguantar?"
    n "Llevas diciendo eso horas mientras te transformas en un monstruo frente a todos."

    "Da un paso hacia [nombre_jugador!c]."

    n "Te tiemblan las manos."
    n "Nos miras como si fuéramos comida."
    n "{cps=15}Mataste a—{/cps}"

    "Se detiene antes de terminar la frase."
    "Silencio pesado."

    "[nombre_jugador!c] hundió la cabeza entre los hombros."

    n "¿Sabes qué? Siempre has sido así."
    n "Un pozo sin fondo de problemas."

    # Flashback breve
    scene bg flashback_rodrigo_borracho with dissolve
    "[nombre_jugador!c] inconsciente. Vomitando."
    "Luz llorando."
    "Nagi sosteniéndolo para que no se ahogara."
    scene bg pasillo_derruido with dissolve

    "Nagi escupió las palabras con una rabia que le quebraba la voz."
    n "¡Debí dejar que te ahogaras en tu vómito esa noche, animal!"

    "El golpe emocional fue más letal que cualquier herida física."

    a "¡Nagi!"

    "[nombre_jugador!c] no responde."
    "No puede."
    "Sus uñas atraviesan la piel de su brazo, dibujando hilos rojos sobre la manga."

    n "Siempre hay que salvarte."
    n "Siempre hay que cuidarte."
    n "Siempre hay que entenderte."

    "Mira al resto."

    n "¿Y quién nos salva a nosotros?"

    "Silencio."
    "Nadie responde."

    n 'Yo no voy a morir aquí porque él no puede "contener a su demonio interno".'

    "Da media vuelta, decidido."

    n "Si quieren seguir con este retrasado, adelante."
    n "¡Pero yo me largo!"
    r "¡Nagi, espera!"
    n "¡Cállate! ¡No quiero volver a oír tu voz!"
    
    "Azura corrió tras él, sujetando del brazo en un intento desesperado por detener la ruptura."
    a "¡No hagas esto! ¡No ahora, por favor!"

    "Nagi la apartó con una brusquedad que ocultaba su propio miedo."
    n "Zu-chan… míralo."
    n "Ya no es el chico con el que crecimos."

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

    "Mira a [nombre_jugador!c]."
    "No con odio."
    "Con tristeza."

    c "No sé si podamos detenerlo si se transforma del todo."

    "Ese comentario duele más que el grito de Nagi."
    "[nombre_jugador!c] lo sabe."
    pause 1.0

    "Nagi asintió, dándole la espalda al grupo definitivamente."
    n "Gracias."
    n "No voy a arrastrarlos conmigo."
    n "Pero tampoco voy a quedarme esperando a que él termine lo que empezó esa cosa."

    "Sus pasos se alejaron hacia la oscuridad del ala izquierda, perdiéndose en un eco solitario."
    scene bg pasillo_oscuro with dissolve
    play sound "audio/sfx/pasos_lejanos_fade.ogg" fadeout 3.0

    "Oscuridad."
    "El sonido de sus pasos alejándose."

    "Un silencio tenso."

    "[nombre_jugador!c] cerró los ojos. El aire a su alrededor parecía vibrar con una premonición funesta."
    r "...No."
    r "...Esto no puede terminar así."

    play ambient slash volume 0.6 noloop
    play sound "audio/sfx/grito_nagi.ogg"
    "Un grito desgarrador cortó el aire."

    play sound "audio/sfx/golpe_pared.ogg"
    "Luego, el impacto seco de un cuerpo contra la pared y el sonido de algo arrastrándose sobre el concreto."

    a "¡NAGI!"

    "Cutipye intentó correr hacia el origen del ruido, pero [nombre_jugador!c] la frenó con una mano que ardía de fiebre."
    "Desde el vacío, la voz de Galaxia llegó como un susurro juguetón."

    g "Siempre se separan…"
    g "Es tan previsible que casi me da lástima."
    g "Nunca aprenden."

    play sound "audio/sfx/arrastre_humedo.ogg"

    "Un sonido viscoso dominó el ambiente antes de que el silencio volviera a reclamar el pasillo."
    "Azura se cubrió la boca para no gritar. Cutipye apretó los puños hasta que sus nudillos blanquearon."
    "[nombre_jugador!c] no dijo nada, pero algo dentro de él crujó. No fue un hueso; fue su última pizca de voluntad humana rompiéndose."

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
    play music chase1

    n "(fuera de escena) ¡¿Qué—?! ¡Suélt—!"

    play sound "audio/sfx/golpe_pared_fuerte.ogg"

    "El sonido de algo arrastrándose."

    "Luz se lleva la mano a la boca."
    "Azura corre un paso adelante."
    "[nombre_jugador!c] ya está en movimiento."

    g "(fuera de escena, juguetona) Siempre es el mismo error…"
    g "Alejarse del rebaño."

    play sound "audio/sfx/levantado_suelo_humedo.ogg"

    "El grupo dobla la esquina del pasillo."

    scene bg pasillo_intermitente with flash   # luz intermitente

    "Al final, bajo una luz intermitente, la ven."
    "Galaxia sostiene a Nagi del cuello, elevado apenas del suelo."
    "Sus piernas patean en el aire."
    "Nagi aún tiene rabia en los ojos."

    n "...Púdrete."

    "Reúne saliva."
    "Le escupe directo al rostro."

    "El tiempo parece congelarse."

    "Luz contiene el aliento."
    "Azura aprieta los puños."
    r "Ngh..."

    "Galaxia parpadea."
    "Se limpia la mejilla lentamente con los dedos."
    "Luego sonríe."

    g "(dulcemente burlona) Supongo que debo estar agradecida…"
    g "Empezaba a tener hambre~"

    "Inclina la cabeza."
    "Sus ojos se tornan más oscuros."

    g "Y tú te ofreciste solito."

    "Nagi forcejea."

    n "¡[nombre_jugador!c]—!"

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

    "[nombre_jugador!c] da un paso al frente."
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

    "La bestia arremete contra [nombre_jugador!c], estrellándolo contra la pared."
    "El impacto hace crujir el concreto."

    # (continúa el combate con descripciones similares; para brevidad, salto al final)

    # Final del combate
    play sound "audio/sfx/puerta_metallica_cerrar.ogg"

    "La puerta metálica al fondo se cierra de golpe."
    stop music fadeout 1.5
    "Silencio."

    "No hay más gritos."
    "No hay más voces."
    "Solo el eco distante de pasos arrastrándose."

    "[nombre_jugador!c] queda de rodillas."
    "Su transformación se retrae lentamente."
    "Demasiado tarde."

    a "(quebrada) …No lo logramos."

    "Azura mira la puerta cerrada."

    a "Nos estaban esperando."

    "Cutipye no dice nada."
    "Solo observa a [nombre_jugador!c]."

    "[nombre_jugador!c] aprieta los puños hasta que sangran."
    "No llora."
    "Esta vez no."

    "Sus ojos se tornaron negros, reflejando una oscuridad absoluta."
    r "Fue mi culpa. Todo es mi culpa."

    $ nagi_dead = True
    call chapter_complete("Capítulo 10")
    jump cap_11

label nagi_no_traiciona:
    scene bg pasillo_derruido with dissolve
    play music "audio/ambience/pasillo_tenso.ogg" fadein 2.0 loop

    "Nagi se detuvo, bufando con una frustración que no podía ocultar más."
    n "¡Ya basta! ¡Esto es ridículo!"
    a "Nagi, por favor, no empieces..."
    n "¡Míralo! Desde que entramos, el mundo gira en torno a sus crisis."
    n "¡Maldita sea, [apodo_jugador], pareces un zombi con esteroides!"

    "[nombre_jugador!c] agachó la cabeza. La influencia de Galaxia era evidente en el brillo antinatural de su mirada."
    r "No estoy… perdiendo el control. Todavía no."

    "Avanzó un paso, luchando contra una marea interna que amenazaba con devorarlo."

    r "Escuchen."
    r "No me gusta esto tampoco."
    r "No pedí… nada de esto."
    r "Pero si nos dividimos, estamos muertos."
    r "Galaxia quiere eso."
    r "Separarnos."

    "Se apoyó contra la pared, respirando con una dificultad que asustaba."

    r "Yo puedo aguantar."
    r "Solo… manténganse cerca."
    r "Si pierdo el control… me detienen."
    r "Pero no se vayan."

    "Por un segundo, hay silencio."
    "Azura lo mira con lágrimas contenidas."
    "Cutipye también."
    "Nagi cruza los brazos, pero no se mueve."

    "Nagi suelta una risa seca, pero esta vez con un matiz de frustración compartida en vez de rechazo total."

    n "¿Aguantar?"
    n "Te tiemblan las manos."
    n "Nos miras como si fuéramos comida."
    n "Mataste a—"

    "Se detiene antes de terminar la frase. Silencio pesado."
    pause 0.5
    "Da un paso hacia [nombre_jugador!c], pero no agresivo —más como un amigo que quiere zarandearlo para despertarlo."
    "[nombre_jugador!c] baja la cabeza, y sus uñas raspan más fuerte la tela, dejando marcas visibles."

    n "¿Sabes qué? Siempre has sido así, ¿eh? Recuerdan esa vez que se emborrachó hasta casi morirse?"

    # Flashback breve
    scene bg flashback_rodrigo_borracho with dissolve
    "[nombre_jugador!c] inconsciente. Vomitando."
    "Azura y Cutipye preocupadas."
    "Nagi sosteniéndolo para que no se ahogara."
    scene bg pasillo_derruido with dissolve

    n "(con rabia, pero ahora con un toque de nostalgia forzada) ¡Y ahí estaba yo, salvándote el trasero como siempre! ¡No voy a dejar que nos mates a todos ahora, pero tampoco voy a largarme solo!"

    "El golpe emocional es fuerte, pero Nagi no lo remata con insultos. En cambio, mira al grupo."

    a "(amable, interviniendo con cuidado) Nagi, por favor... Entiendo tu miedo. Todos lo sentimos. [apodo_jugador] está luchando, y Galaxia lo está... cambiando. Pero separarnos no ayudará. ¿Y si hablamos de irnos cuanto antes? Encontrar una salida rápida, juntos."

    "Azura pone una mano suave en el brazo de Nagi, su voz cuidadosa y empática, como una mediadora que prioriza la unión."

    c "(con ligereza, intentando aligerar) Sí, ¡vamos! Como en esas películas donde todos corren y nadie se queda atrás. [apodo_jugador], si te transformas, te doy un beso para que vuelvas... o un golpe, lo que funcione primero. ¡Je!"

    "Pero su risa es nerviosa, y mira a [nombre_jugador!c] con una mezcla de cariño y temor real."

    n "(extrovertido, respondiendo con energía) ¡Eso! ¡Irnos cuanto antes! No me quedo aquí esperando que [apodo_jugador] se convierta en el monstruo principal. Pero solos, somos carnada fácil para esa loca de Galaxia. ¡Vamos, grupo! ¿Quién dice que corramos como si nos persiguiera el diablo?"

    "[nombre_jugador!c] levanta la mirada, sus pupilas aún dilatadas, pero asiente lentamente. La influencia de Galaxia hace que su voz suene un poco distorsionada."

    r "De acuerdo... Irnos cuanto antes. No... no quiero lastimarlos."
    a "(sonríe débilmente, cuidadosa como siempre) Entonces, sigamos. Juntos. Busquemos esa salida, pero con cuidado. [apodo_jugador], si sientes que empeora... avísanos."
    c "(asiente, ligera pero solidaria) ¡Equipo invencible! O al menos... equipo que no se rinde."

    "Nagi da una palmada en la espalda de [nombre_jugador!c] —fuerte, extrovertida—."

    n "¡Eso es! No te voy a dejar solo, idiota. Pero apúrate, o te cargo yo mismo."

    "El grupo avanza, más unido por ahora, pero la tensión persiste. [nombre_jugador!c] siente la influencia de Galaxia creciendo, un susurro en su mente que promete caos si no se apresuran."

    pause 2.0

    "Un silencio tenso, pero no roto."
    "Algo no está bien."
    "Demasiado silencio."
    "Pero esta vez, no hay grito. Solo el eco de sus pasos sincronizados, apresurados hacia la salida."

    "La cámara cierra en el ojo de [nombre_jugador!c]."
    "Aún oscuro, pero resistiendo... por ahora."

    stop music fadeout 4.0

    call chapter_complete("Capítulo 10")
    jump cap_11

label cap_11:
    if afinidad_cutipye < 4:
        scene bg_enfermeria_abandonada with dissolve
        
        "El descanso en la enfermería abandonada no trajo alivio. El aire estaba cargado de un olor metálico a sangre vieja y medicamentos podridos."
        "[nombre_jugador!c] se hundió en el suelo, pegando la espalda a la pared fría. Sus hombros sufrían espasmos y entrelazaba sus dedos con fuerza, como si tratara de evitar que sus manos se convirtieran en algo más."
        "El silencio era una losa, hasta que Cutipye lo rompió con un tono afilado."

        show cutipye half_smile at right
        c "Es fascinante, ¿No? Como siempre logras que todo sea un caos absoluto."

        if not nagi_dead:
            show nagi ceja_levantada at left
            "Nagi la observó con una ceja levantada, detectando el veneno en sus palabras."
        
        c "Primero el orfanato. Después los monstruos. Después las mutaciones."
        
        show cutipye mirada_reojo
        c "Algunas personas simplemente… no saben cuándo parar."
        
        "[nombre_jugador!c] hundió la barbilla en el pecho, su voz apenas un hilo de voz."
        r "Cuty… no estoy haciendo esto a propósito."
        
        show cutipye feign_surprise
        c "¿Oh? ¿Entonces sí sabes lo que haces?"

        if not nagi_dead:
            n "Oye, tranquila. Nadie está en su mejor momento ahora…"
            show cutipye seria
            c "No lo defiendas, Nagi. Quiero que me mire a la cara y me lo diga."
        else:
            "El silencio de la sala hace que las palabras de Cutipye corten como cuchillas."

        "Cutipye se pone de pie y camina lentamente frente a [nombre_jugador!c]."
        
        c "Siempre tienes el consejo perfecto para los demás. 'Relájate', dices. 'Estás exagerando', dices."
        
        show cutipye disgust
        c "Pero ahora que tú eres el que tiene un monstruo en las tripas… todos tenemos que ser comprensivos contigo."
        
        "[nombre_jugador!c] la mira. Sus ojos están brillosos. No de rabia, sino de contención."
        
        c "Te da miedo todo. Miedo el ruido. Miedo la oscuridad..."
        c "{cps=15}Te da miedo convertirte en lo que siempre has sido en el fondo.{/cps}"
        
        "Los dedos de [nombre_jugador!c] se curvaron, transformándose involuntariamente en garras por un segundo antes de que él volviera a apretar los puños."
        
        a "Cutipye…"
        a "Basta."
        
        "Pero no suena a orden. Suena a ruego débil."
        
        r "¡Estoy intentando no hacerles daño! ¡Estoy luchando cada segundo!"
        
        "Unas plumas negras brotaron sutilmente en su cuello antes de retraerse. La lucha interna era feroz."
        
        c "Ese es tu problema, [apodo_jugador]. Siempre estás 'intentando', pero nunca logras nada. Solo das lástima."
        
        "Él se quedó inmóvil, como si le hubieran arrancado el alma de un golpe."
        c "¿Quieres que confiemos en ti? Ni tú mismo lo haces. Nos miras como si fuéramos presas y luego lloras para que te perdonemos."

        if not nagi_dead:
            show nagi worried
            n "Bueno, técnicamente llorar es una respuesta emocional saludable, ¿no? O sea, peor sería que—"
            c "No estoy bromeando."
            "Nagi se calla de inmediato."

        c "Eres un monstruo porque eliges comportarte como uno cuando tienes miedo."
        
        "[nombre_jugador!c] ya no responde. Solo llora en silencio, sin defenderse."

        show cutipye tired
        c "No puedo más. Necesito aire antes de que yo también me vuelva loca."
        
        hide cutipye with moveoutright
    else:
        # === CAP 11 — RUTA NORMAL (afinidad_cutipye >= 4) ===
        # Cutipye no traiciona. Llega todavía intentando sostener al grupo.
        # La caída emocional es genuina porque parte del humor, no del rencor.

        scene bg_enfermeria_abandonada with dissolve
        stop music fadeout 2.0
        play music audio.story fadein 2.0

        "El peso de los últimas horas había convertido el aire de la enfermería en algo denso, casi imposible de respirar."
        "Nadie hablaba. El único sonido era la respiración entrecortada del grupo y el goteo distante de una tubería rota."

        show cutipye smile_nervous at left with dissolve
        "Cutipye entró la última. Hizo lo que siempre hacía: buscó algo en qué apoyarse para mantener al grupo en pie."

        c "Bueno, miren el lado positivo: si esto fuera una película, ya estaríamos en el tercer acto. Casi llegamos, gente."

        "El chiste no aterrizó."
        "Silencio."

        if not nagi_dead:
            show nagi tired at right with dissolve
            "Nagi, que normalmente habría respondido con algo sarcástico, solo bajó la mirada."

        show azura tired at centro_derecha with dissolve
        "Azura apretó los labios. [nombre_jugador!c] no levantó la vista."

        show cutipye worried
        "Cutipye notó el silencio antes que el jugador. Lo midió. Entendió exactamente lo que significaba."

        "Se quedó de pie en el centro de la habitación, sin saber muy bien adónde poner las manos."

        # --- LA GRIETA ---
        "Sus ojos recorrieron la enfermería, buscando algo en qué posarse."
        "Se detuvieron en su propia mochila, tirada en el suelo junto a la pared."
        "La abrió sin pensar demasiado. Por hacer algo con las manos."
        "Y sacó el cuaderno."

        show cutipye soft
        "Lo sostuvo un momento sin decir nada, pasando los dedos sobre la tapa."

        c "Yo dibujaba esto... antes de venir. El orfanato. Como referencia. Pensé que sería—"

        "No terminó la frase."
        "Era la primera vez en todo el capítulo que Cutipye no cerraba una idea. No la remató con un chiste. No la rescató."
        "La dejó colgada en el aire."

        "[nombre_jugador!c] levantó la vista por primera vez."
        if not nagi_dead:
            "Nagi también."

        # --- NEGACIÓN ---
        show cutipye smile_nervous
        c "Da igual. No es momento para nostalgia de arte."

        "Intentó sonreír. Guardó el cuaderno."
        "Nadie llenó el silencio por ella."
        "Azura no dijo 'no, cuéntanos'. [nombre_jugador!c] no cambió de tema para darle una salida. Nagi no hizo un chiste que la rescatara del momento."
        "Solo el silencio. Quieto. Sin rescate social."

        show cutipye tired
        "Cutipye miró el cuaderno cerrado entre sus manos."

        c "..."

        # --- LA CONFESIÓN ---
        "Cuando volvió a hablar, la voz le salió diferente. Sin control de escenario. Sin timing."

        c "Fui yo."

        "Pausa."

        c "La idea del orfanato. La dije como si fuera una broma en el grupo de chat... 'busquemos algo emocionante para el finde'."
        c "Ni siquiera lo pensé en serio."

        show cutipye scared
        "Tragó saliva."

        c "Y ahora Luz no está."

        if not nagi_dead:
            c "Y Nagi casi no vuelve."
        else:
            c "Y Nagi... ya no está."

        c "Y yo sigo haciendo chistes porque si me detengo un segundo, tengo que pensar en que esto es mi culpa."

        "La última frase le salió más rápido que las demás, como si hubiera esperado demasiado para decirla y ya no pudiera frenarse."

        "Silencio."

        # --- REACCIÓN DEL GRUPO ---
        show azura worried
        "Azura fue la primera en moverse. No corrió hacia ella. Solo dio un paso al frente, despacio."

        a "Eso no es cierto."
        a "O sí lo es, pero no importa. Nadie te obligó a nadie a entrar."

        show cutipye shocked
        c "Pero yo—"

        a "Lo sé. Pero la culpa no funciona así."

        "[nombre_jugador!c] no dijo nada largo. No era su estilo."
        show rodrigo soft at right with dissolve
        r "Yo también dije que sí."

        "Dos frases. Nada más."
        "Pero algo en la habitación cambió."

        if not nagi_dead:
            show nagi soft
            "Nagi se limpió la cara con el dorso de la mano."
            n "Yo también."
            n "Todos dijimos que sí."
            "Se encogió de hombros, con la voz un tono más baja que de costumbre."
            n "Así que si quieres cargar la culpa, vas a tener que hacer fila."

        "La culpa no desapareció. No era el tipo de cosa que desapareciera con dos frases."
        "Pero el peso ya no lo llevaba solo uno."

        # --- CIERRE: LA MÁSCARA VUELVE, YA DISTINTA ---
        show cutipye tired
        "Cutipye dejó escapar un largo suspiro por la nariz."
        "Guardó el cuaderno en la mochila. Cerró el cierre."

        c "...Bueno."

        "Pausa corta."

        c "Sigo pensando que la próxima vez, elijo el minigolf."

        "Esta vez el grupo sí rió."
        "Poco. Cansado. Pero real."
        "La primera risa del capítulo había fallado. Esta no."

        if not nagi_dead:
            show nagi smile
            n "El minigolf es aburrido."
            c "¡Exactamente, ese es el punto!"

        show azura smile
        "Azura se tapó la boca con la mano, conteniendo algo entre la risa y las ganas de llorar."

        hide cutipye
        hide azura
        if not nagi_dead:
            hide nagi
        hide rodrigo

        call chapter_complete("Capítulo 11")
        jump cap_12
        

label escena_traicion_cutipye:
    scene bg_pasillo_oscuro with dissolve
    "Los pasos de Cutipye se alejaron hasta ser solo un eco. La oscuridad la envolvió rápidamente."
    "Caminaba apoyándose en las paredes, respirando de forma entrecortada mientras intentaba recomponerse."
    
    c "No soy así… no soy así…"
    c "Yo no quería decirle esas cosas..."
    
    pause 1.0
    "Una voz suave y melosa se filtró desde las grietas de las paredes."
    
    g "Claro que no… Solo estás empezando a ser honesta contigo misma. Es liberador, ¿verdad?"
    
    "Cutipye abrió los ojos de par en par, pero fue tarde."
    "Una mano fría la empujó contra la pared y algo afilado acarició su yugular."

    scene bg_enfermeria_abandonada with flash
    "En la enfermería, [nombre_jugador!c] se tensó de golpe. Sus instintos de depredador le enviaron una señal de alarma que le heló la sangre."
    r "…Cutipye. Algo va mal."
    
    "Un grito ahogado rerebota por las paredes del pasillo."
    a "¡Cutipye!"
    
    if not nagi_dead:
        "Nagi maldice en voz baja mientras su agarre en su arma se tensa, corriendo hacia la oscuridad."

    scene bg_habitacion_limpia with dissolve
    "Cutipye tropezó al entrar en la habitación, cerrando la puerta tras de sí con desesperación."
    "Se quedó atónita. El lugar estaba impecable: papel tapiz floral, juguetes antiguos en estantes perfectos y un reloj de pared que marcaba el tiempo con precisión suiza."
    
    c "¿Qué es este lugar?"
    
    "El clic metálico del seguro de la puerta sonó con la contundencia de una sentencia de muerte."
    
    g "Pensé que vendrían todos juntos... Pero supongo que tú servirás para empezar el juego."
    
    show galaxia sentada_sonriendo with dissolve
    play music chase1
    
    "Galaxia estaba sentada en una pequeña silla de mimbre, balanceando las piernas con inocencia macabra."
    g "¿Tú sabes dónde están los demás?"
    
    "Cutipye sacó el arma que le había quitado a [nombre_jugador!c], apuntando con manos que no dejaban de temblar."
    c "Están lejos de ti."
    
    play sound gunshot
    "El disparo retumbó en la habitación. La bala impactó en la pierna de Galaxia, pero la herida comenzó a supurar un humo negro y a cerrarse antes de que la sangre tocara el suelo."
    
    g "Oh. Vaya. Ahora entiendo por qué [nombre_jugador!c] estaba tan asustado."
    
    play sound gunshot
    queue sound gunshot
    queue sound gunshot
    "Cutipye disparó una, dos, tres veces. Hombro, torso, cuello. Galaxia se tambaleaba con cada impacto, pero seguía sonriendo."
    
    play sound "sfx/gunshot.mp3"
    pause 0.6
    "El cargador estaba vacío. El silencio que siguió fue aterrador."
    
    g "Eso no ha sido nada amable. Y yo que quería ser tu amiga."
    
    "Cutipye retrocedió hasta chocar con la pared. No había salida."
    g "Si dejas de gritar, prometo que no dolerá tanto."
    
    "Galaxia se levantó y acarició la mejilla de Cutipye con una garra suave."

    play sound glx_laugh fadeout 2.5
    "Entonces, soltó una risa aguda y descompuesta que llenó cada rincón de la habitación impecable."
    scene black with dissolve
    show death_cutipye at center with blood_splash
    
    "Un grito ensordecedor se cortó en seco."
    pause 1.0
    "Una mancha de sangre salpicó el papel tapiz floral. Luego otra."
    stop music fadeout 1.5
    pause 1.5
    
    "{cps=20}Silencio{/cps}."
    "El reloj siguió su curso imperturbable."
    "{cps=15}Tic. Tic. Tic.{/cps}"

    $ cutipye_dead = True
    call chapter_complete("Capítulo 11")
    jump cap_12

label cap_12:
    # === CAP 12 — "EL FINAL" ===
    # Confrontación definitiva con Galaxia. Incendio. Endings.

    scene bg_pasillo_primer_piso with dissolve
    stop music fadeout 2.0
    play music audio.story fadein 2.5

    "La ruta de salida era visible por primera vez desde que entraron."
    "Una puerta lateral, pesada, con el candado oxidado hasta el punto de partirse. La cerradura cedería con un golpe limpio."
    "Estaban a veinte metros."

    show rodrigo worried at left with dissolve
    if not nagi_dead:
        show nagi scared at centro_izquierda with dissolve
    if not cuty_dead:
        show cutipye scared at right with dissolve
    show azura worried at centro_derecha with dissolve

    r "Ahí. Esa es."

    if not nagi_dead:
        n "No hay criaturas. Está despejado."

    if not cuty_dead:
        c "No corran todavía. Esperen."

    show azura shocked
    a "...[nombre_jugador!c]."

    "El tono de Azura lo detuvo antes de que diera el primer paso."
    "Al final del pasillo, bloqueando la puerta de salida, estaba Galaxia."
    "No corría. No acechaba desde las sombras."
    "Solo estaba parada ahí, con los brazos cruzados y la cabeza ladeada, como si llevara un rato esperándolos."

    stop music fadeout 1.5
    play music audio.chase1 fadein 0.5

    show galaxia smile at center with dissolve

    g "Pensé que les llevaría más tiempo."
    g "¿Ya se quieren ir~? Pero si apenas llegaron."

    hide rodrigo
    hide azura
    if not nagi_dead:
        hide nagi
    if not cuty_dead:
        hide cutipye

    # --- CONFRONTACIÓN ---
    "[nombre_jugador!c] buscó la pistola. Vacía. La había vaciado Cutipye en el Cap 11."
    "Nagi apretó el bate. Los nudillos blancos."
    "Azura no se movió. Sus ojos esmeralda recorrieron la habitación: las paredes, el techo, el suelo. Calculando."

    if not cuty_dead:
        show cutipye serious at left with dissolve
        c "Las balas no funcionan. Ya lo sabemos."
        c "Azura. El edificio."
        show azura worried at right with dissolve
        "Azura entendió al instante. Asintió sin decir nada."
        a "Las paredes son de madera vieja. El piso también. Y el techo..."
        a "Todo esto tiene más de cincuenta años."
    else:
        show azura worried at left with dissolve
        a "Las balas no funcionan. Pero el fuego sí. Lo sabemos desde el Cap 4."
        a "Este edificio tiene más de cincuenta años. Madera, pintura vieja, alfombra podrida..."
        a "Solo necesitamos una chispa."

    "Galaxia inclinó la cabeza al otro lado. Seguía sonriendo, pero algo en su postura cambió. Un instinto."

    show galaxia half_smile
    g "Oh. Oh, eso es... interesante."
    g "Nunca habían llegado tan lejos. Normalmente para este punto ya estaban llorando en el suelo."

    "El tiempo se comprimió."

    # --- LA CHISPA ---
    play sound break_wood
    "Azura arrancó un trozo de madera podrida del marco de una ventana con un golpe seco."

    if not cuty_dead:
        play sound shock
        "Cutipye encontró en el suelo un encendedor oxidado — probablemente de alguno de los visitantes anteriores que nunca salieron."
        "Hizo clic una vez. Dos veces. A la tercera, la llama apareció."
        c "¡Vámonos!"
    else:
        play sound shock
        "[nombre_jugador!c] sacó el encendedor que llevaba desde el principio. Lo usaba para ver en los cuartos sin linterna."
        "Hizo clic. La llama apareció."
        r "¡Vámonos!"

    scene bg_enfermeria_abandonada with flash
    play music audio.chase fadein 0.3

    "El fuego prendió más rápido de lo que esperaban."
    "La madera seca del suelo fue lo primero. Luego el papel tapiz de los pasillos adyacentes. Luego el techo."
    "El humo empezó a descender."

    show galaxia walk_creepy at center with dissolve
    "Galaxia no huyó del fuego. Se quedó parada en el pasillo, observando cómo las llamas reptaban por las paredes."
    "Los otros Huéspedes, en cambio, sí."

    "Algo en el edificio cambió: crujidos en las paredes, un aullido lejano, el sonido pesado de algo grande que derribaba una puerta."
    "Las criaturas no respondían a sus órdenes. Respondían al instinto de supervivencia."
    "El control territorial de Galaxia se fracturaba."

    play sound scream1
    "[nombre_jugador!c] escuchó la araña chillando a dos pisos de distancia."
    "No venía hacia ellos. Iba hacia afuera."

    # ============================================================
    # PERSECUCIÓN FINAL — SECUENCIA DE QTEs CON LÍMITE DE TIEMPO
    # ============================================================
    # El timer global es de 90 segundos (1:30) en tiempo real.
    # La pantalla hud_reloj_persecucion descuenta 1s por segundo automáticamente,
    # sin importar en qué menú o diálogo esté el jugador.
    # Las decisiones del jugador NO penalizan el tiempo — solo el reloj.
    # Si timer_persecucion llega a 0 → jump escape_tiempo_agotado → bad1.
    # ============================================================

    $ renpy.block_rollback()
    $ timer_persecucion = 90
    $ opciones_agotadas = set()

    show screen hud_reloj_persecucion("escape_tiempo_agotado")
    with dissolve

    jump persecucion_qte_inicio


# ============================================================
# LABEL DE ENTRADA — establece la escena antes del primer QTE
# ============================================================
label persecucion_qte_inicio:

    scene pasillo_huida with flash
    play sound run

    "No había tiempo para pensar."
    "El pasillo delante de ellos escupía humo desde el techo."
    "Galaxia no perseguía — esperaba. Sabía que el edificio haría el trabajo por ella."

    if not nagi_dead:
        n "¡Por aquí, la escalera!"

    if not cuty_dead:
        c "¡No paren!"

    jump persecucion_qte_1


# ============================================================
# QTE 1 — El suelo cede
# ============================================================
label persecucion_qte_1:

    scene pasillo_huida with vpunch
    play sound wood_creak

    "Una sección del suelo cedió con un crujido sordo."
    "El agujero se abrió en menos de un segundo — madera negra y llamas abajo."

    menu:
        "[[ SALTAR ]]":
            play sound land
            "[nombre_jugador!c] saltó el hueco sin detenerse a medir la distancia."
            "El impacto le sacudió las rodillas, pero siguió corriendo."
            jump persecucion_qte_2

        "[[ RODEAR ]]":
            play sound walk
            "El rodeo costó segundos que no tenían."
            "El humo ganó terreno."
            jump persecucion_qte_2


# ============================================================
# QTE 2 — Una viga en llamas bloquea el pasillo
# ============================================================
label persecucion_qte_2:

    scene escape_1 with vpunch
    play sound crack

    "Una viga del techo cayó delante de ellos, atravesando el pasillo en diagonal."
    "Las llamas la recorrían de extremo a extremo."
    "Había un metro libre en el lado izquierdo."

    if not nagi_dead:
        n "¡Izquierda! ¡Hay espacio!"

    menu:
        "[[ PASAR POR LA IZQUIERDA ]]":
            play sound slash
            "El calor les golpeó la cara al pasar."
            "[nombre_jugador!c] sintió el brazo rozar las llamas. Siguió corriendo."
            jump persecucion_qte_3

        "[[ ROMPER LA VIGA ]]":
            play sound break_wood
            "La viga no cedió como esperaban."
            "Fueron segundos de golpes inútiles antes de encontrar el espacio."
            jump persecucion_qte_3


# ============================================================
# QTE 3 — Galaxia aparece en el cruce
# ============================================================
label persecucion_qte_3:

    scene escape_1 with flash
    stop music fadeout 0.3
    play sound glx_laugh

    show galaxia walk_creepy at center with dissolve

    "En el cruce del pasillo central, Galaxia."
    "No corría. Solo estaba ahí, en el centro del corredor, con las manos abiertas."
    "Las llamas detrás de ella la silueteaban."

    g "¿A dónde van con tanta prisa~?"

    play music audio.chase1 fadein 0.2

    menu:
        "[[ ESQUIVAR — IR POR LA DERECHA ]]":
            play sound run
            "[nombre_jugador!c] giró sin frenar."
            "Galaxia extendió una garra — rozó el aire donde estaba su cabeza un instante antes."
            hide galaxia
            jump persecucion_qte_4

        "[[ ENFRENTARLA — EMPUJARLA ]]":
            play sound thud
            "[nombre_jugador!c] la golpeó con el hombro con todo lo que tenía."
            "Galaxia retrocedió tres pasos — sorprendida, no herida."
            play sound shock
            "El impacto le costó el equilibrio. Azura lo agarró del brazo."
            if not nagi_dead:
                n "¡Muévete!"
            hide galaxia
            jump persecucion_qte_4


# ============================================================
# QTE 4 — Escalera con peldaños quemados
# ============================================================
label persecucion_qte_4:

    scene pasillo_huida with dissolve
    play sound wood_creak

    "La escalera hacia la salida tenía los primeros tres peldaños en llamas."
    "El cuarto aguantaba. El quinto también."
    "Había que calcular bien el primer salto."

    if not cuty_dead:
        c "¡El cuarto escalón! ¡Directamente al cuarto!"

    menu:
        "[[ SALTAR AL CUARTO PELDAÑO ]]":
            play sound land
            "El peldaño aguantó."
            "Subieron los últimos metros en segundos."
            jump persecucion_qte_5

        "[[ BUSCAR OTRO CAMINO ]]":
            play sound walk
            "El rodeo por el ala este costó varios segundos."
            "El techo allí ya crujía."
            jump persecucion_qte_5


# ============================================================
# QTE 5 — La puerta de salida
# ============================================================
label persecucion_qte_5:

    scene bg_pasillo_primer_piso with vpunch
    play sound thud

    "La puerta de salida estaba a tres metros."
    "El candado. Oxidado. [nombre_jugador!c] lo recordaba desde el principio del capítulo."

    "El humo ya tapaba el techo. Quedaban segundos antes de que el pasillo fuera irrespirable."

    play sound door_slam

    menu:
        "[[ GOLPEAR EL CANDADO ]]":
            play sound break_glass
            play sound door_break
            "El candado cedió al tercer golpe."
            "La puerta se abrió hacia fuera."
            "El aire frío de la noche golpeó sus caras."
            hide screen hud_reloj_persecucion
            jump persecucion_exitosa

        "[[ PATEAR LA PUERTA ]]":
            play sound door_break
            "La puerta cedió hacia afuera con el segundo golpe."
            "Salieron tropezando."
            hide screen hud_reloj_persecucion
            jump persecucion_exitosa


# ============================================================
# PERSECUCIÓN EXITOSA — bifurca según estado_mental
# ============================================================
label persecucion_exitosa:

    $ renpy.block_rollback()
    scene black with flash
    stop music fadeout 0.5

    "Afuera."
    "El aire frío."
    "El cielo aún oscuro."

    # Bifurcación final según estado_mental
    if estado_mental >= 16:
        jump ending_bad1_rodrigo
    elif estado_mental >= 11:
        jump ending_neutral_rodrigo
    else:
        jump ending_good_rodrigo


# ============================================================
# TIEMPO AGOTADO — no escaparon a tiempo
# ============================================================
label escape_tiempo_agotado:

    $ renpy.block_rollback()
    hide screen hud_reloj_persecucion
    $ ending_type = "bad1"

    scene black with slow_dissolve
    stop music fadeout 2.0

    pause 1.5

    "El fuego llegó antes que ellos."
    pause 0.8
    "El pasillo de salida colapsó. El techo. Las paredes."
    pause 0.8
    "No había otro camino."
    pause 1.0

    "{cps=15}No escaparon a tiempo.{/cps}"

    pause 1.5
    jump creditos


# --- ENDING GOOD: Rodrigo resiste, retiene a Galaxia ---
label ending_good_rodrigo:

    stop music fadeout 1.0

    show galaxia walk_creepy at left with dissolve
    show rodrigo worried at right with dissolve

    "Galaxia se giró hacia [nombre_jugador!c]."
    "El resto del grupo ya estaba moviéndose hacia la salida. Solo [nombre_jugador!c] no se había movido."

    g "¿Por qué no corres~?"

    show rodrigo serio
    "[nombre_jugador!c] no respondió con palabras."
    "Sus pies ya no eran del todo suyos. La transformación avanzaba desde que el humo empezó a llenar sus pulmones."
    "Pero todavía era él quien decidía adónde ir."

    r "Porque si no te retengo, llegas a la salida antes que ellos."

    show galaxia half_smile
    g "Oh. Eso es lo más interesante que has dicho en toda la noche."

    "Se lanzó hacia él."

    play sound slash
    scene black with flash

    "[nombre_jugador!c] no esquivó."
    "La golpeó de frente, usó su peso y el impulso de ella para estamparla contra la pared opuesta."
    "Las garras le abrieron el costado. No lo soltó."

    play sound thud
    "El humo descendía. El calor subía."

    "En la puerta, Azura se detuvo. Miró hacia atrás."
    if not nagi_dead:
        "Nagi la alcanzó por el brazo."
        n "¡Azura! ¡No podemos—!"
    if not cuty_dead:
        "Cutipye vio la silueta de [nombre_jugador!c] a través del humo."
        c "...[apodo_jugador]."

    "[nombre_jugador!c] no miró hacia atrás."
    "Oyó sus pasos alejarse."

    play music audio.rodtheme fadein 2.0

    "La transformación terminó de cerrarse en sus dedos, en sus hombros, en su espina dorsal."
    "Pero sus brazos seguían apretando."
    "Galaxia dejó de reír."

    show galaxia regen
    g "...Shio."

    "Una palabra. La primera vez que pronunció ese nombre en quince años."
    "No para [nombre_jugador!c]. Para ella misma."

    "El techo cedió a tres metros de ellos."
    "Las llamas lo cubrieron todo."

    scene black with slow_dissolve
    stop music fadeout 3.0

    $ ending_type = "good"
    jump epilogo_exterior




# --- ENDING BAD1: Rodrigo sucumbe, ataca a los suyos — QTEs de combate ---
label ending_bad1_rodrigo:

    $ renpy.block_rollback()
    play music audio.chase1 fadein 0.3

    "El humo negro del incendio llenó los pulmones de [nombre_jugador!c]."
    "No fue el calor lo que lo quebró. Fue el instinto."
    "Un susurro que ya no era de Galaxia — era de él mismo."

    show rodrigo shocked at center with dissolve

    "[nombre_jugador!c] sintió cómo su cuerpo dejaba de pedir permiso para actuar."
    "Se giró hacia el grupo."
    "Ya no los reconoció."

    # -----------------------------------------------
    # QTE DE COMBATE 1 — Rodrigo ataca a Nagi
    # -----------------------------------------------
    if not nagi_dead:
        show nagi scared at left with dissolve
        n "[nombre_jugador!c]. [nombre_jugador!c], míranos. Estamos aquí."

        show rodrigo molesto
        "Los ojos de [nombre_jugador!c] se posaron en Nagi."
        "No lo vio como su amigo."
        "Lo vio como una amenaza."

        # Los sobrevivientes intentan esquivar / defenderse
        "Nagi levantó el bate. Manos temblorosas."

        menu:
            "[[ ESQUIVAR EL GOLPE — Nagi se aparta ]]":
                play sound slash
                play sound thud
                scene black with flash
                n "¡RODRIGO, PARA!"
                "Nagi esquivó el primer golpe."
                "Pero el segundo llegó antes de que pudiera reaccionar."
                scene pasillo_huida with flash
                show nagi scared at left
                "El bate cayó al suelo."
                "Nagi no."

            "[[ AGUANTAR — Nagi intenta sujetarlo ]]":
                play sound slash
                play sound thud
                scene black with flash
                "Nagi no pudo sujetarlo."
                "[nombre_jugador!c] era demasiado rápido."
                scene pasillo_huida with flash
                "El bate cayó al suelo."

        $ nagi_dead = True

    # -----------------------------------------------
    # QTE DE COMBATE 2 — Rodrigo ataca a Cutipye
    # -----------------------------------------------
    if not cuty_dead:
        show cutipye scared at right with dissolve
        c "¡Azura, corre! ¡No lo mires!"

        "Cutipye no corrió."
        "Se quedó entre [nombre_jugador!c] y Azura."

        menu:
            "[[ AZURA DISTRAE A RODRIGO ]]":
                show azura shocked at centro_izquierda with dissolve
                a "¡[nombre_jugador!c]! ¡Soy yo! ¡Soy Azura!"
                play sound shock
                "[nombre_jugador!c] vaciló — un segundo, solo un segundo."
                "Fue suficiente para que Cutipye empujara a Azura hacia la puerta."
                play sound slash
                scene black with flash
                "[nombre_jugador!c] no la siguió a ella."

                $ cuty_dead = True
                scene pasillo_huida with flash

            "[[ CUTIPYE CORRE ]]":
                #CAMBIAR - Cutipye sobrevive
                play sound run
                play sound slash
                scene black with flash
                "No fue suficientemente rápida."
                scene pasillo_huida with flash

    # -----------------------------------------------
    # QTE DE COMBATE 3 — Rodrigo y Azura, solo una sale
    # -----------------------------------------------
    show azura shocked at center with dissolve

    "Azura era la única que quedaba entre él y la salida."
    "No tenía arma. No tenía plan."
    "Solo tenía el nombre de él."

    a "[nombre_jugador!c]."

    "Sin grito. Sin pánico. Solo su nombre, dicho en voz baja."
    "Como aquella primera vez en Historia, cuando lo integró al grupo."

    show rodrigo shocked
    "[nombre_jugador!c] se detuvo."
    "Un segundo."
    "Dos."

    menu:
        "[[ RODRIGO AVANZA — Azura esquiva y corre ]]":
            play sound run
            "Azura no esperó el tercero."
            "Se lanzó hacia la puerta lateral mientras [nombre_jugador!c] avanzaba hacia donde ella había estado."
            "El humo la cubrió."
            play sound door_break
            "La puerta cedió."
            "Azura salió."

        "[[ RODRIGO BLOQUEA LA SALIDA ]]":
            play sound slash
            scene black with flash
            "Azura no llegó a la puerta."
            pause 0.5
            "..."
            pause 0.5
            "Pero el fuego sí llegó a [nombre_jugador!c]."
            pause 0.5
            "Y Azura encontró otra salida."
            scene pasillo_huida with flash

    "Azura fue la única que llegó a la noche."
    "No miró hacia atrás."
    "El incendio la siguió de cerca, pero la noche la tragó antes de que el edificio colapsara."

    scene black with slow_dissolve
    stop music fadeout 3.0

    $ ending_type = "bad1"
    jump epilogo_exterior


# --- ENDING NEUTRAL: Rodrigo desaparece durante la huida ---
label ending_neutral_rodrigo:

    play music audio.curse fadein 1.0

    "[nombre_jugador!c] mantuvo el paso con el grupo hasta el pasillo final."
    "Luego no lo mantuvieron."

    show rodrigo nervioso at left with dissolve
    if not cuty_dead:
        show cutipye scared at right with dissolve
    show azura worried at centro_derecha with dissolve

    "Una pared de humo cortó el pasillo."
    "El grupo corrió."

    if not cuty_dead:
        c "¡[nombre_jugador!c], por aquí!"

    "[nombre_jugador!c] giró en la dirección equivocada."
    "No por accidente."

    show rodrigo shocked
    "Había algo al fondo del pasillo. No Galaxia. No una criatura."
    "Solo sus propias manos, a contraluz de las llamas."
    "No reconoció lo que vio."

    scene black with dissolve
    stop music fadeout 2.0
    "Azura lo llamó dos veces más desde el otro lado del humo."
    "No hubo respuesta."

    # Determinar cuántos sobrevivientes hay para asignar el ending correcto
    python:
        sobrevivientes = 0
        if not nagi_dead:
            sobrevivientes += 1
        if not cuty_dead:
            sobrevivientes += 1
        # Azura siempre sobrevive en la ruta neutral si llegó a este punto
        sobrevivientes += 1

        if sobrevivientes >= 3:
            ending_type = "neutral1"
        else:
            ending_type = "neutral2"

    jump epilogo_exterior


# === EPÍLOGO — EXTERIOR DEL ORFANATO (COMPARTIDO) ===
label epilogo_exterior:

    scene ending with slow_dissolve
    stop music fadeout 3.0

    "El orfanato ardía desde el interior."
    "Las ventanas del segundo piso soltaban columnas de humo negro. El fuego ya había alcanzado el tejado."

    # Quién está presente varía según el ending
    if ending_type == "good":
        show azura shocked at left with dissolve
        if not nagi_dead:
            show nagi soft at centro_izquierda with dissolve
        if not cuty_dead:
            show cutipye tired at right with dissolve

        "Nadie habló."
        "Las sirenas empezaban a sonar lejos, en la carretera."

        if not cuty_dead:
            show cutipye scared
            "Cutipye se abrazó a sí misma. El mecanismo del humor había dejado de funcionar del todo."
            "No lloró en voz alta. Solo temblaba, mirando las llamas."

        if not nagi_dead:
            show nagi soft
            "Nagi se colocó a su lado, sin decir nada. Le puso una mano en el hombro."
            "No era gesto de él. Era uno nuevo."
            "Pero era suyo."

        show azura shocked
        "Azura tenía los ojos fijos en el edificio."
        "En algún punto dejó de buscar la silueta de [nombre_jugador!c] entre las ventanas."

        play sound "sfx/crack-and-crunch.mp3"
        "El tejado cedió con un crujido que se oyó desde el bosque."
        stop music

    elif ending_type == "bad1":
        scene black with slow_dissolve
        "El incendio consumió el orfanato durante la madrugada."
        "Cuando las autoridades llegaron, no encontraron sobrevivientes."

    elif ending_type == "bad2":
        show azura shocked at center with dissolve
        "Azura salió sola."
        "Se sentó en el borde del camino de tierra y esperó. No sabía qué más hacer."
        "El edificio ardía a su espalda."
        "Se preguntó, con una claridad extraña para ese momento, si realmente había escapado."
        "O si una parte de ella seguía en algún pasillo, corriendo sin llegar nunca a ningún lado."

    elif ending_type == "neutral1" or ending_type == "neutral2":
        show azura tired at left with dissolve
        if not nagi_dead:
            show nagi tired at centro_izquierda with dissolve
        if not cuty_dead:
            show cutipye tired at right with dissolve

        "Desde la distancia, observaron cómo el fuego devoraba el edificio."
        "Nadie dijo una palabra."
        "No hacía falta."

        "Cuando finalmente llegaron las sirenas, los sobrevivientes ya se habían marchado."

    # --- TRANSICIÓN A CRÉDITOS ---
    pause 2.0
    jump creditos