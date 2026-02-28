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