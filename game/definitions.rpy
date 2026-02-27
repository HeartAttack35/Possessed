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
default nombre_capitulo = ""
default mostrar_hud = True

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

transform vjump:
    yoffset 0
    linear 0.08 yoffset -25
    linear 0.08 yoffset 0

## Fondos
image mainmenubg = "bg/main_menu.png"
image gameover_screen = "bg/game_over.jpg"
image foreboding_1 = "bg/pasillo_oscuro.jpg"
image escape_1 = "bg/pasillo_corriendo.jpg"
image puerta_abierta_sotano = "bg/puerta_oxidada.png"
image pasillo_lab = "bg/pasillo_abandonado.jpg"
image sala_h127_1 = "bg/sala_h127.jpg"
image puerta_cerrandose = "bg/puerta_h127.jpg"
image pasillo_huida = "bg/pasillo_corriendo.jpg"
image corredor_amplio = "bg/pasillo_corriendo.jpg"
image chase1_1 = "bg/bg_bodega_pan.jpg"
image bg_pasillo_escombros = "bg/pasillo_corriendo.jpg"
image bg_cuarto_maquinas = "bg/puerta_oxidada.png"
image pasillo_servicio = "bg/pasillo_oscuro.jpg"
image cocina_puerta = "bg/puerta_oxidada.png"
image cuarto_maquinas_puerta = "bg/bg_bodega_pan.jpg"
image pistola_primer_plano = "objects/obj-gun.png"
image pasillo_servicio_lucha = "bg/pasillo_oscuro.jpg"
image pasillo_lab_close = "bg/pasillo_corriendo.jpg"
# Muertes
image spdr1 = "game_over/death_spdr_1.png"

## Escenarios
### image bg clase = "escenarios/sala_clases.jpg"
image bg_pasillo_scroll:
    "bg/pasillo.png"
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
image rodrigo move_slow:
    "images/sprites/Rodri.png"

    yoffset 0
    xoffset 0

    block:
        linear 0.6 yoffset -6 xoffset 2
        linear 0.6 yoffset 0 xoffset 0
        linear 0.6 yoffset -6 xoffset -2
        linear 0.6 yoffset 0 xoffset 0
        repeat
image rodrigo run_panic:
    "images/sprites/Rodri.png"

    yoffset 0
    xoffset 0

    block:
        linear 0.2 yoffset -12 xoffset 4
        linear 0.2 yoffset 0 xoffset 0
        linear 0.2 yoffset -12 xoffset -4
        linear 0.2 yoffset 0 xoffset 0
        repeat


# Azura
image azura neutral = "images/sprites/Azura.png"
image azura smile = "images/sprites/Azura.png"
image azura temblor = "images/sprites/Azura.png"
image azura emocion = "images/sprites/Azura.png"
image azura scared = "images/sprites/Azura.png"
image azura worried = "images/sprites/Azura.png"
image azura casual_young = "images/sprites/Azura.png"
image azura casual_young_smile = "images/sprites/Azura.png"

# Cutipye
image cutipye neutral = "images/sprites/Cutipye.png"
image cutipye smile = "images/sprites/Cutipye.png"
image cutipye smile_nervous = "images/sprites/Cutipye.png"
image cutipye determined = "images/sprites/Cutipye.png"
image cutipye serious = "images/sprites/Cutipye.png"
image cutipye soft = "images/sprites/Cutipye.png"
image cutipye scared = "images/sprites/Cutipye.png"
image cutipye disgust = "images/sprites/Cutipye.png"
image cutipye casual_young = "images/sprites/Cutipye.png"
image cutipye throw = "images/sprites/Cutipye.png"
image cutipye worried = "images/sprites/Cutipye.png"

# Nagi
image nagi smug = "images/sprites/Nagi.png"
image nagi smile = "images/sprites/Nagi.png"
image nagi serio = "images/sprites/Nagi.png"
image nagi angry = "images/sprites/Nagi.png"
image nagi annoyed = "images/sprites/Nagi.png"
image nagi worried = "images/sprites/Nagi.png"
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
#image sujeto_herido = "images/sprites/Sujeto_Herido.png"
image sujeto_herido:
    "images/sprites/Nagi.png"
    matrixcolor TintMatrix("#000000")
image avispa_zangano = "images/sprites/avispa_zangano.png"
image avispa_zangano attack = "images/sprites/avispa_zangano.png"

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

# Pantalla HUD de afinidades y estado mental
screen hud_stats():
    if mostrar_hud:
        frame:
            xpos 10
            ypos 10
            xysize (320, 280)
            background Frame("gui/frame.png", 10, 10)
            
            vbox:
                spacing 8
                xpos 15
                ypos 15
                
                text "=== ESTADÍSTICAS ===" size 20 bold True
                
                fixed:
                    xysize (290, 30)
                    text "Luz:" align (0.0, 0.5)
                    text "[afinidad_luz]" color "#fd5353" align (0.9, 0.5)
                
                fixed:
                    xysize (290, 30)
                    text "Azura:" align (0.0, 0.5)
                    text "[afinidad_azura]" color "#0f8028" align (0.9, 0.5)
                
                fixed:
                    xysize (290, 30)
                    text "Cutipye:" align (0.0, 0.5)
                    text "[afinidad_cutipye]" color "#2dff5a" align (0.9, 0.5)
                
                fixed:
                    xysize (290, 30)
                    text "Nagi:" align (0.0, 0.5)
                    text "[afinidad_nagi]" color "#7b2cbf" align (0.9, 0.5)
                
                null height 5
                
                fixed:
                    xysize (290, 30)
                    text "Estado Mental:" align (0.0, 0.5)
                    text "[estado_mental]" color "#ffaa00" align (0.9, 0.5)

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

label chapter_complete(nombre):

    $ nombre_capitulo = nombre
    stop music fadeout 1.5
    scene black with fade
    pause(1.0)

    play sound chptr_cmplt
    show text "{size=50}[nombre_capitulo] Completado{/size}" at truecenter with dissolve
    pause(2.5)
    hide text with fade

    pause(0.5)

    show text "¿Deseas guardar tu progreso antes de continuar?" with dissolve
    pause(1.0)

    menu:
        "Guardar y Continuar":
            $ renpy.save("1-1", f"{nombre_capitulo} Completado.")
            "Progreso guardado."
            return
        "Continuar sin guardar":
            return