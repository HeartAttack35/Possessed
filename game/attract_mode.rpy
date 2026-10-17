################################################################
#  ATTRACT MODE: opening tras inactividad en el menú principal
################################################################

define ATTRACT_IDLE_SECONDS = 15.0   # usa 3.0 para probar
define ATTRACT_POLL = 0.5

image attract_gota = Solid("#000")

transform attract_gota_anim:
    xalign 0.5
    yalign 0.0
    alpha 0.0
    zoom 0.0
    linear 0.4 alpha 1.0 zoom 0.1       # a small drop appears at the top
    linear 2.6 yalign 0.5 zoom 8.0      # it falls and expands to cover the screen
    linear 0.2 alpha 1.0

transform attract_fade:
    on show:
        alpha 0.0
        linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0.0

# Hilo de tinta que cae desde arriba y se expande (placeholder: cámbialo
# por una imagen de gota si tienes una)
init python:
    import time
    import pygame_sdl2 as pygame

    class AttractState(object):
        last_activity = 0.0
        last_tick = 0.0
        last_pos = None
        running = False

    ATTRACT_ACTIVITY_EVENTS = tuple(
        getattr(pygame, n) for n in
        ("KEYDOWN", "MOUSEBUTTONDOWN", "JOYBUTTONDOWN",
         "CONTROLLERBUTTONDOWN", "FINGERDOWN")
        if hasattr(pygame, n)
    )

    class AttractIdleWatcher(renpy.Displayable):
        """Displayable invisible: registra la última actividad del jugador."""
        def render(self, width, height, st, at):
            return renpy.Render(width, height)

        def event(self, ev, x, y, st):
            S = AttractState
            if ev.type == pygame.MOUSEMOTION:
                if S.last_pos != (x, y):
                    S.last_pos = (x, y)
                    S.last_activity = time.time()
            elif ev.type in ATTRACT_ACTIVITY_EVENTS:
                S.last_activity = time.time()
            return None

    def attract_tick():
        S = AttractState
        now = time.time()

        if now - S.last_tick > ATTRACT_POLL * 4:
            S.last_activity = now
        S.last_tick = now

        if renpy.get_screen("confirm"):
            S.last_activity = now
            return

        if S.running or (now - S.last_activity) < ATTRACT_IDLE_SECONDS:
            return

        S.running = True
        try:
            renpy.call_in_new_context("attract_opening")
        finally:
            S.running = False
            S.last_activity = S.last_tick = time.time()

        music = config.main_menu_music or getattr(audio, "main_menu", None)
        if music:
            renpy.music.play(music, channel="music", fadein=1.0, if_changed=True)
        renpy.restart_interaction()

    def attract_pause(seconds):
        """Pausa. Cualquier tecla/click interrumpe TODO el attract mode."""
        if renpy.pause(seconds):
            renpy.jump("attract_exit")

    def attract_entry(titulo, cuerpo):
        """Muestra una entrada de bitácora y espera según su longitud."""
        renpy.show_screen("attract_entrada", titulo=titulo, cuerpo=cuerpo)
        attract_pause(1.8 + len(cuerpo) / 25.0)
        renpy.hide_screen("attract_entrada")

## ── El opening ─────────────────────────────────────────────────

label attract_opening:

    python:
        attract_qm_prev = getattr(store, "quick_menu", None)
        if attract_qm_prev is not None:
            quick_menu = False

    show screen attract_guard
    stop music fadeout 1.5

    # ── 0–5 s: la gota negra infecta el fondo del menú ──
    scene mainmenubg
    show attract_gota at attract_gota_anim
    $ attract_pause(3.2)
    scene black with flash
    play music audio.chase2 fadein 1.0 volume 0.5
    $ attract_pause(0.6)

    # ── Entrada 01 ──
    play sound paper_flip
    scene sala_proyector with dissolve
    show layer master at sepia_filter
    $ attract_entry("REGISTRO RECUPERADO — ENTRADA 01 · DÍA 0", "Los niños refugiados del orfanato, sin lazos familiares y desahuciados por la sociedad, han sido seleccionados como sujetos ideales. Sus historiales los hacen prescindibles.")

    # ── Entrada 04 (empieza el latido) ──
    $ renpy.music.set_volume(0.15, channel="ambient")
    play ambient heartbeat fadein 1.0
    play sound paper_flip
    scene pasillo_lab with dissolve
    show layer master at sepia_filter
    $ attract_entry("ENTRADA 04 · DÍA 11", "El 60 por ciento de los primeros sujetos han fallecido. Los cuerpos se deforman en masas amorfas, aún respirando en algunos casos por horas.")

    # ── Entrada 17 (el latido crece, el nombre va tachado) ──
    $ renpy.music.set_volume(0.5, delay=4.0, channel="ambient")
    play sound paper_flip
    scene sala_h127_1 with dissolve
    show layer master at distortion_light
    $ attract_entry("ENTRADA 17 · DÍA 49", "{color=#b02020}[[REDACTADO]{/color} ya no responde a los protocolos. Se comunica con los demás huéspedes mediante gestos, sonidos guturales y golpes en los muros. Coordinación. Intención. No somos los domadores aquí. Somos la presa.")

    # ── Entrada 20 (la última) ──
    $ renpy.music.set_volume(0.9, delay=4.0, channel="ambient")
    play sound paper_flip
    scene pasillo_oscuro with dissolve
    show layer master at distortion_heavy
    $ attract_entry("ENTRADA 20 · DÍA 55", "Estoy oculto en el archivo subterráneo. Escucho sus pasos. {color=#b02020}[[REDACTADO]{/color} me busca, pero aún no me encuentra. Quizá desea que lo escriba todo, que lo deje registrado. Como advertencia. Como burla.")

    # ── Corte seco, logo y risa lejana ──
    stop ambient
    show layer master
    scene black
    $ attract_pause(1.2)

    show text "{size=80}{color=#fd5353}{font=fonts/HelpMe.ttf}POSSESSED{/font}{/color}{/size}" at truecenter with dissolve
    show layer master at distortion_heavy
    play sound glx_laugh volume 0.2
    $ attract_pause(3.0)
    hide text with dissolve
    show layer master

    # ── Texto final sobre negro ──
    stop music fadeout 6
    scene black with dissolve
    show expression Text(
        "{i}“No seas vencido de lo malo, sino vence con el bien el mal.”{/i}\n\n"
        "{size=-12}{color=#8a8a8a}(Romanos 12:21){/color}{/size}",
        size=46, xmaximum=1300, text_align=0.5
    ) as versiculo at truecenter with Dissolve(1.5)
    $ attract_pause(7.0)
    hide versiculo with Dissolve(1.5)
    $ attract_pause(0.5)

    # (si termina normal, cae directo a la limpieza)

label attract_exit:
    hide screen attract_guard
    hide screen attract_entrada
    stop sound
    stop ambient fadeout 0.5
    $ renpy.music.set_volume(1.0, channel="ambient")
    show layer master
    python:
        if attract_qm_prev is not None:
            quick_menu = attract_qm_prev
    return