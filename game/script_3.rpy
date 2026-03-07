label creditos:
    $ _skipping = False
    $ renpy.block_rollback()
    
    if persistent.credits_seen:
        $ _skipping = True

    play music credits fadein 1.5 noloop
    show expression Solid("#0006") as oscurecer
    with dissolve

    python:
        splashes = []

        splashes.append("{size=+20}{b}{i}POSSESSED{/i}{/b}{/size}")

        # Crédito 1
        splashes.append("Historia y Dirección:\nHeartAttack51\n\nProgramación:\nHeartAttack51")

        # Epílogo de Nagi
        if ending_type == "bad1":
            splashes.append(("nagi dead", "La familia de Nagi gastó todos sus recursos en una búsqueda desesperada.\nSin cuerpo ni pistas, su habitación permanece intacta, esperando un regreso que nunca ocurrirá."))
        elif nagi_dead:
            splashes.append(("nagi dead", "Luego de semanas, la familia de Nagi inició una búsqueda para encontrarlo.\nSin embargo, nunca lograron dar con su paradero."))
        else:
            splashes.append(("nagi smug", "Nagi Katashi sobrevivió a la experiencia, gracias a la ayuda de sus amigos.\nSin embargo, nunca volvió a ser el mismo."))

        # Crédito 2
        splashes.append("Música:\nHuman Entertainment\nCapcom\nRenegade Kid LLC\n{a=https://youtube.com/@Jambus8550}@Jambus8550{/a}\n{a=https://www.youtube.com/@ryukaiiee}ryuka{/a}")

        # Epílogo de Cutipye
        if ending_type == "bad1":
            splashes.append(("cutipye dead", "La desaparición de Cutipye fue tratada con absoluto hermetismo por su familia.\nSe mudaron de la ciudad poco después, dejando atrás un misterio sin resolver."))
        elif cuty_dead:
            splashes.append(("cutipye dead", "El padre de Cutipye organizó un funeral privado, al que solo asistieron sus familiares y amigos más cercanos.\nSin embargo, la familia de Cutipye se negó a hablar del tema con la prensa, y no se inició una investigación formal."))
        else:
            splashes.append(("cutipye smile", "Cutipye, aunque sobrevivió a la experiencia, no pudo superar el trauma.\nSe volvió una persona retraída y distante, y eventualmente se mudó a otra ciudad para alejarse de los recuerdos."))

        # Crédito 3
        splashes.append("Ilustraciones:\nUraku\nVins2099\nArtistas libres de derechos")

        # Epílogo de Azura
        if ending_type == "bad1":
            splashes.append(("azura dead", "La desaparición de Azura dejó un vacío irremplazable.\nSu familia aún espera su regreso, aferrándose al recuerdo de su inagotable optimismo en una casa que ahora se siente demasiado silenciosa."))
        elif ending_type == "bad2":
            splashes.append(("azura shocked", "Azura trató de mantener una actitud positiva, pero asiste a terapia sin lograr superar el trauma.\nActualmente usa esa aplastante experiencia como motor para su música."))
        else:
            splashes.append(("azura smile", "Azura logró mantener una actitud positiva tras los sucesos.\nCon el apoyo de sus padres y amigos, pudo superar el trauma y seguir adelante con su vida."))

        # Crédito 4
        splashes.append("Efectos de sonido:\nRenegade Kid LLC\nHeartAttack51\nArtistas libres de derechos")

        # Epílogo de Luz
        if ending_type == "bad1":
            splashes.append(("luz dead", "La desaparición de Luz sumió a su familia en la desesperación.\nLas autoridades cerraron el caso por falta de pruebas, dejándolos sin un cierre ni un lugar donde llorarla."))
        elif afinidad_luz >= 5:
            splashes.append(("luz smile", "La familia de Luz inició una investigación, la cual sigue abierta para este momento.\nLos sobrevivientes asistieron a su funeral."))
        else:
            splashes.append(("luz sad", "La familia de Luz inició una investigación, la cual sigue abierta para este momento.\nLos sobrevivientes asistieron a su funeral.\nSe sugiere que la relación distante de Rodrigo con Luz contribuyó a su trágico destino."))

        # Crédito 5
        splashes.append("Personajes:\nAzura: AlliTati\nCutipye: Uraku\nDr. Edgar: HeartAttack51\nGalaxia: HeartAttack51\nLuz: Michi_tamagotchi\nNagi: HeartAttack51\nRodrigo: HeartAttack51")

        # Epílogo de Rodrigo
        if ending_type == "bad1":
            splashes.append(("rodrigo dead", "La familia de Rodrigo aceptó su desaparición en completo silencio.\nSu padre lo dio por fugado, su madre no volvió a mencionarlo, y nadie se molestó en buscarlo."))
        else:
            splashes.append(("rodrigo neutral", "La familia de Rodrigo no inició una investigación.\nSu padre lo atribuye a una desaparición voluntaria, mientras que su madre se niega a hablar del tema.\nSin embargo, sus amigos saben la verdad."))

        # --- INFO. RELEVANTE SOBRE LA PARTIDA (Estadísticas Dinámicas) ---
        texto_stats = "{size=+10}Resumen de la Partida{/size}\n\n"
        
        if afinidad_nagi >= 5:
            texto_stats += "Tu relación con Nagi fue buena.\n"
        else:
            texto_stats += "Tu relación con Nagi fue distante.\n"
            
        if afinidad_cutipye >= 5:
            texto_stats += "Tu relación con Cutipye fue buena.\n"
        else:
            texto_stats += "Tu relación con Cutipye fue distante.\n"

        if afinidad_azura >= 5:
            texto_stats += "Tu relación con Azura fue buena.\n"
        else:
            texto_stats += "Tu relación con Azura fue distante.\n"
            
        if afinidad_luz >= 5:
            texto_stats += "Tu relación con Luz fue buena.\n\n"
        else:
            texto_stats += "Tu relación con Luz fue distante.\n\n"

        if estado_mental <= 10:
            texto_stats += "Rodrigo mantuvo la calma.\n\n"
        elif estado_mental <= 15:
            texto_stats += "Rodrigo estuvo bajo presión.\n\n"
        else:
            texto_stats += "Rodrigo sucumbió al estrés.\n\n"

        texto_stats += "Final obtenido: " + str(ending_type)
        splashes.append(texto_stats)

        # --- EPÍLOGO GENERAL ---
        if ending_type == "bad1":
            splashes.append(
            "El incendio consumió el orfanato durante la madrugada.\n\n"
            "Cuando las autoridades llegaron, no encontraron sobrevivientes.\n\n"
            "Los nombres de Rodrigo y sus amigos fueron añadidos a la lista de personas desaparecidas.\n\n"
            "El lugar donde alguna vez se alzó el orfanato quedó reducido a cenizas.\n\n"
            "Pero algunos vecinos aseguran que, en las noches más silenciosas,\n"
            "aún pueden oír algo moviéndose entre los restos calcinados."
            )
        elif ending_type == "bad2":
            splashes.append(
            "El incendio borró casi todo rastro del orfanato.\n\n"
            "Azura fue la única que logró salir con vida.\n\n"
            "Durante semanas apenas pudo dormir.\n"
            "Cada vez que cerraba los ojos recordaba los pasillos, los gritos... y a sus amigos.\n\n"
            "A veces se pregunta si realmente escapó.\n"
            "O si una parte de ella todavía sigue atrapada en aquel lugar."
            )
        elif ending_type == "neutral1":
            splashes.append(
            "Desde la distancia, observaron cómo el fuego devoraba el edificio.\n\n"
            "Nadie dijo una palabra.\n"
            "No hacía falta.\n\n"
            "Lo que ocurrió dentro del orfanato sería algo que cargarían el resto de sus vidas.\n\n"
            "Cuando finalmente llegaron las sirenas, los sobrevivientes ya se habían marchado.\n\n"
            "Algunas historias son demasiado horribles para contarlas."
            )
        elif ending_type == "neutral2":
            splashes.append(
            "El incendio acabó con el orfanato antes del amanecer.\n\n"
            "Las autoridades atribuyeron la tragedia a un accidente.\n\n"
            "Los tres sobrevivientes nunca intentaron corregir esa versión.\n\n"
            "Después de lo que vieron aquella noche,\n"
            "sabían que nadie les creería.\n\n"
            "Y quizás era mejor así."
            )
        elif ending_type == "good":
            splashes.append(
            "El incendio arrasó con el orfanato hasta no dejar nada en pie.\n\n"
            "Cuando todo terminó, solo quedaron ruinas y silencio.\n\n"
            "Azura, Nagi y Cutipye sobrevivieron.\n"
            "Pero alguien más se quedó atrás.\n\n"
            "A veces, cuando el viento sopla fuerte entre los árboles,\n"
            "juran escuchar el eco de unas alas agitándose entre las llamas.\n\n"
            "Como si algo aún protegiera aquel lugar."
            )
        else:
            # ESTO TE AYUDARÁ A DETECTAR EL ERROR:
            splashes.append("ERROR: No se encontró un epílogo para el ending_type: " + str(ending_type) + ". Por favor, revisa tus variables.")

        # --- AGRADECIMIENTOS (Ahora va al final de la lista) ---
        splashes.append("Agradecimientos:\nLa gente que fue parte del proyecto.\nCanela la perrita.\n\nA todos los que no atacaron a la primera criatura.")

        # Recálculo de tiempo
        tiempo_por_splash = (168.0 / len(splashes))
        tiempo_espera = tiempo_por_splash - 1.0

    # BUCLE DE VISUALIZACIÓN
    $ i = 0
    $ num_splashes = len(splashes)

    while i < num_splashes:
        $ current_info = splashes[i]

        if isinstance(current_info, tuple):
            $ sprite = current_info[0]
            $ texto = current_info[1]

            show expression sprite as credit_sprite at credit_sprite_left
            show expression Text(texto, xmaximum=500, text_align=0.0) as credit_text:
                xalign 0.75
                yalign 0.5
        else:
            show text "[current_info]" at truecenter

        with dissolve

        if not persistent.credits_seen:
            $ renpy.pause(tiempo_espera, hard=True)
        else:
            $ renpy.pause(tiempo_espera)

        if isinstance(current_info, tuple):
            hide credit_sprite
            hide credit_text
        else:
            hide text
            
        with dissolve

        $ i += 1

    # Pantalla final
    hide oscurecer
    scene black
    show text "{size=+30}Fin.{/size}" at truecenter
    with slow_dissolve

    if not persistent.credits_seen:
        $ renpy.pause(4.0, hard=True)
    else:
        $ renpy.pause(4.0)
        
    hide text
    with slow_dissolve 

    $ persistent.credits_seen = True
    $ _skipping = True
    return