################################################################
#  ATTRACT MODE: opening tras inactividad en el menú principal
################################################################

define ATTRACT_IDLE_SECONDS = 15.0     # usa 3.0 para probar
define ATTRACT_POLL         = 0.5
define ATTRACT_DEBUG        = False    # True: muestra un reloj en pantalla para sincronizar con la pista

# Bloque 1 y 2
define ATTRACT_INTRO_LEN    = 14.0     # duración de chase2_begin hasta el corte seco
define ATTRACT_TITLE_LEN    = 1.0      # título en silencio antes de chase2

# Bloques 3-5: segundos medidos DESDE EL INICIO DE chase2
define ATTRACT_T_TEMPO      = 20.0     # aquí empieza a "subir el tempo"
define ATTRACT_T_FINALE     = 46.0     # aquí empieza el inicio de la historia
define ATTRACT_T_END        = 58.0     # aquí se corta la música (≈ fin de la pista)

# Bloque 6
define ATTRACT_VERSE_LEN    = 6.5

# Escala de los sprites (los PNG actuales son placeholders de tamaño desconocido).
# Si los personajes salen enormes o diminutos, cambia SOLO este número.
define ATTRACT_SPRITE_ZOOM  = 1.0

# Fuente del título (None = fuente del juego). Opcional: "fonts/HelpMe.ttf"
define ATTRACT_TITLE_FONT   = None

# Transiciones propias
define attract_flash = Fade(0.03, 0.0, 0.16, color="#ffffff")
define attract_cut   = Dissolve(0.08)


## ── IMÁGENES DE POST-PROCESO (los PNG van en game/images/attract/) ──

image attract_vignette = "images/attract/vignette.png"

image attract_grain:
    zoom 2.0 alpha 0.6
    "images/attract/grain_1.png"
    pause 0.05
    "images/attract/grain_2.png"
    pause 0.05
    "images/attract/grain_3.png"
    pause 0.05
    repeat


## ── CÓDIGO ───────────────────────────────────────────────────

# Si no definiste chase2_begin / chase2 en definitions.rpy, se crean aquí.
# Si ya existen, esto no los toca. Ajusta las rutas a tus archivos.
init 10 python:
    if not hasattr(audio, "chase2_begin"):
        audio.chase2_begin = "music/chase2_begin.ogg"
    if not hasattr(audio, "chase2"):
        audio.chase2 = "music/chase2.ogg"

init python:
    import time
    import math
    import pygame_sdl2 as pygame

    # ── Detección de inactividad (menú principal) ──

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

    class AttractInterrupter(renpy.Displayable):
        """Durante el opening: cualquier tecla o click lo corta y vuelve al menú."""
        def render(self, width, height, st, at):
            return renpy.Render(width, height)

        def event(self, ev, x, y, st):
            if ev.type in ATTRACT_ACTIVITY_EVENTS:
                return True
            return None

    def attract_tick():
        S = AttractState
        now = time.time()

        # Si el timer estuvo "dormido" (Preferences, Load...), reinicia el reloj
        if now - S.last_tick > ATTRACT_POLL * 4:
            S.last_activity = now
        S.last_tick = now

        # Un diálogo de confirmación abierto cuenta como actividad
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

        # Vuelta al menú: música + cortina negra que se disipa
        music = config.main_menu_music or getattr(audio, "main_menu", None)
        if music:
            renpy.music.play(music, channel="music", fadein=1.0, if_changed=True)
        renpy.show_screen("attract_curtain")
        renpy.restart_interaction()

    # ── Pausas sincronizadas con un reloj absoluto ──

    class AttractClock(object):
        t0 = 0.0

    def attract_clock_reset():
        AttractClock.t0 = time.time()

    def attract_now():
        return time.time() - AttractClock.t0

    def attract_pause(seconds):
        """Pausa. Si el jugador pulsa algo, se aborta TODO el opening."""
        if seconds <= 0:
            return
        if renpy.pause(seconds):
            renpy.jump("attract_exit")

    def attract_until(t):
        """Espera hasta el segundo t del reloj actual (no acumula deriva)."""
        remaining = t - attract_now()
        if remaining > 0.02:
            attract_pause(remaining)

    # ── Audio (no revienta si falta un efecto) ──

    def attract_sfx(name, vol=1.0, channel="sound"):
        f = getattr(audio, name, None)
        if f:
            renpy.music.play(f, channel=channel, relative_volume=vol)

    def attract_music(name, fadein=0.0):
        f = getattr(audio, name, None)
        if f:
            renpy.music.play(f, channel="music", loop=False, fadein=fadein)
        else:
            print("[attract] falta audio.%s" % name)

    # ── Fondos con cámara, color y comprobación de existencia ──

    def attract_bg(name, cam=None, dim=0.0, sat=None, tint=None, extra=None):
        """Equivale a `scene name` + cámara sobre toda la capa.
        cam   = (zoom_ini, zoom_fin, segundos, x_ini, x_fin, y_ini, y_fin)
        dim   = oscurece solo el fondo (0..1)     sat = saturación (0..1)
        tint  = color de tinte del fondo          extra = transforms de capa extra
        """
        renpy.scene()

        m = None
        if tint:
            m = TintMatrix(tint)
        if sat is not None:
            m = SaturationMatrix(sat) if m is None else m * SaturationMatrix(sat)
        if dim:
            m = BrightnessMatrix(-dim) if m is None else m * BrightnessMatrix(-dim)
        at = [Transform(matrixcolor=m)] if m is not None else []

        if renpy.has_image(name, exact=True):
            renpy.show(name, at_list=at)
        else:
            print("[attract] falta la imagen: %s" % name)
            renpy.show("attract_missing", what=Solid("#0b0b0b"))

        stack = []
        if cam:
            stack.append(attract_cam(*cam))
        if extra:
            stack.extend(extra)
        renpy.show_layer_at(stack, layer="master", reset=True)

    def attract_entry(titulo, cuerpo, cps=42, y=0.5):
        """Muestra una entrada de bitácora escribiéndose."""
        renpy.hide_screen("attract_entrada")
        renpy.show_screen("attract_entrada", titulo=titulo, cuerpo=cuerpo, cps=cps, ya=y)

    def attract_ambient(name, vol):
        f = getattr(audio, name, None)
        if f:
            renpy.music.play(f, channel="ambient", fadein=0.5)
            renpy.music.set_volume(vol, channel="ambient")

    def attract_preload():
        """Pide a Ren'Py que cargue de antemano los fondos del opening."""
        names = [
            "mainmenubg", "sotano_inicial", "pasillo_lab", "sala_proyector",
            "pasillo_abandonado", "pasillo_oscuro", "puerta_oxidada", "foreboding_1",
            "pasillo_corriendo", "vestibulo", "habitacion_cadaver", "scene_spdr",
            "galaxia_ventana", "sala_h127", "escape_1", "derrumbe",
            "escalera_mano_1", "escalera_mano_2", "habitacion_mantis",
            "death_mnts_1", "death_mnts_2", "death_mnts_3", "death_glx_1", "spdr1",
            "death_wasp", "avispa_dead", "avispa_guardia", "cocina_infestada",
            "bg_almacen_medico", "gal_dead_floor", "chase1_reprise", "chase1_1",
            "bosque_tarde", "orfanato_exterior1",
        ]
        ok = [n for n in names if renpy.has_image(n, exact=True)]
        if ok:
            renpy.start_predict(*ok)

    # ── Duraciones decrecientes: el "tempo que sube" ──

    def attract_ramp(n, total, first):
        """n duraciones d_i = first * r**i (r<1 acelera) que suman exactamente `total`."""
        if n <= 1:
            return [total]
        if n * first <= total:           # no puede acelerar: reparte parejo
            return [total / float(n)] * n
        lo, hi = 0.3, 1.0
        for _ in range(60):
            r = (lo + hi) / 2.0
            if sum(first * r ** i for i in range(n)) > total:
                hi = r
            else:
                lo = r
        return [first * r ** i for i in range(n)]

    # ── Jitter para efectos "corruptos" (lo usan ATL y Transform) ──

    def attract_jitter_fn(base=0, amp=6, vamp=2, period=0.045):
        def f(trans, st, at):
            trans.xoffset = base + renpy.random.randint(-amp, amp)
            trans.yoffset = renpy.random.randint(-vamp, vamp)
            return period
        return f

    attract_jf_tremble = attract_jitter_fn(0, 3, 2, 0.04)
    attract_jf_cam     = attract_jitter_fn(0, 9, 7, 0.03)
    attract_jf_menu    = attract_jitter_fn(0, 16, 4, 0.04)
    attract_jf_title_r = attract_jitter_fn(-10, 7, 2, 0.05)
    attract_jf_title_c = attract_jitter_fn(10, 7, 2, 0.05)
    attract_jf_title_w = attract_jitter_fn(0, 2, 1, 0.07)

    def attract_jf_bob(trans, st, at):
        """Rebote de carrera."""
        trans.yoffset = -int(abs(math.sin(st * 14.0)) * 28)
        return 0.02

    def attract_jf_kick(trans, st, at):
        """Pataleo de alguien levantado en el aire."""
        trans.xoffset = int(math.sin(st * 22.0) * 22)
        return 0.02

    # ── Sprites: existencia, RGB-split y siluetas ──

    def attract_disp(name):
        if renpy.has_image(name, exact=True):
            return renpy.displayable(name)
        print("[attract] falta el sprite: %s" % name)
        return Null()

    def attract_chroma(name, amp=12, **place):
        """Sprite partido en canales R/G/B que tiemblan por separado (aberración cromática).
        Solo se ve bien sobre fondo oscuro."""
        base = attract_disp(name)
        layers = []
        for i, col in enumerate(("#ff0000", "#00ff00", "#0000ff")):
            layers.append(Transform(
                base,
                matrixcolor=TintMatrix(col),
                blend="add",
                function=attract_jitter_fn((i - 1) * amp // 2, amp, max(1, amp // 4), 0.04),
                **place
            ))
        return Fixed(*layers)

    def attract_silhouette(kind, z=1.0, **place):
        """Silueta negra. Usa tu arte si existe; si no, un placeholder con los sprites actuales.
           kind: "shio"    -> images/attract/shio_silueta.png
                 "rodrigo" -> images/attract/rodrigo_mutante_silueta.png"""
        path = {"shio": "images/attract/shio_silueta.png",
                "rodrigo": "images/attract/rodrigo_mutante_silueta.png"}[kind]
        if renpy.loadable(path):
            return Transform(Image(path), zoom=z * ATTRACT_SPRITE_ZOOM, **place)
        if kind == "shio":
            # placeholder: Galaxia achicada (proporción de niña), toda negra
            return Transform(attract_disp("galaxia smile"), matrixcolor=TintMatrix("#000000"),
                             zoom=z * 0.62 * ATTRACT_SPRITE_ZOOM, **place)
        # placeholder: Rodrigo ensanchado, todo negro
        return Transform(attract_disp("rodrigo neutral"), matrixcolor=TintMatrix("#000000"),
                         xzoom=1.18, zoom=z * ATTRACT_SPRITE_ZOOM, **place)

    def attract_corrupt(who, dur=1.0, z=1.0):
        """Animación corrupta: el personaje se parte en RGB y parpadea con su silueta.
           who = "rodrigo" (→ su forma mutada)  |  "galaxia" (→ Shio, antes del H-127)"""
        if who == "rodrigo":
            base_name, sil_kind = "rodrigo shocked", "rodrigo"
        else:
            base_name, sil_kind = "galaxia laugh", "shio"

        renpy.show_layer_at([attract_cam(1.0, 1.07, dur * 1.3)], layer="master", reset=True)
        pattern = [("base", .16), ("sil", .06), ("base", .10), ("sil", .08),
                   ("base", .08), ("sil", .06), ("sil", .46)]
        for i, (what, frac) in enumerate(pattern):
            renpy.scene()
            if what == "base":
                renpy.show("attract_cbg", what=Solid("#070707"))
                renpy.show("attract_cx", what=attract_chroma(
                    base_name, amp=10 + i * 4, xalign=0.5, yalign=1.0, zoom=z * ATTRACT_SPRITE_ZOOM))
            else:
                renpy.show("attract_cbg", what=Solid("#e9e4d8"))
                renpy.show("attract_cx", what=attract_silhouette(
                    sil_kind, z, xalign=0.5, yalign=1.0))
            attract_pause(dur * frac)

    # ── Bloque 4: el montaje que acelera ──

    def attract_run_b(shots, t0, t1, first=2.0):
        durs = attract_ramp(len(shots), t1 - t0, first)
        t = t0
        for shot, d in zip(shots, durs):
            t += d
            if shot[0] == "cor":
                attract_corrupt(shot[1], max(d, 0.4))
            else:
                _, img, sfx, hit = shot
                attract_bg(img, cam=(1.04, 1.18, d + 0.3))
                if sfx:
                    attract_sfx(sfx, 0.9)
                if hit and d > 0.55:
                    renpy.with_statement(getattr(store, hit))
                elif d > 0.9:
                    renpy.with_statement(attract_flash)
            attract_until(t)

    def attract_debug_text(st, at):
        return Text("t = %.1f" % attract_now(), size=26, color="#00ff66",
                    outlines=[(2, "#000000", 0, 0)], xpos=24, ypos=150), 0.05


## ── TRANSFORMS ───────────────────────────────────────────────

# Cámara de toda la capa: empuje/paneo lento
transform attract_cam(z0=1.0, z1=1.1, d=3.0, x0=0, x1=0, y0=0, y1=0):
    xalign 0.5 yalign 0.5
    zoom z0 xoffset x0 yoffset y0
    linear d zoom z1 xoffset x1 yoffset y1

# Cámara en mano (para carreras)
transform attract_shake_cam:
    function attract_jf_cam

# El menú se corrompe y cae a negro
transform attract_menu_corrupt:
    parallel:
        function attract_jf_menu
    parallel:
        matrixcolor BrightnessMatrix(0.0)
        linear 0.9 matrixcolor BrightnessMatrix(-0.95)

transform attract_text_in:
    alpha 0.0
    linear 0.3 alpha 1.0

transform attract_verse_in:
    alpha 0.0
    linear 1.6 alpha 1.0

transform attract_title_fade:
    alpha 0.0
    linear 1.0 alpha 1.0

transform attract_title_r:
    alpha 0.75
    function attract_jf_title_r

transform attract_title_c:
    alpha 0.75
    function attract_jf_title_c

transform attract_title_w:
    function attract_jf_title_w

transform attract_curtain_out:
    alpha 1.0
    linear 1.0 alpha 0.0

transform attract_bar_top:
    yalign 0.0 yoffset -400
    easein 1.2 yoffset 0

transform attract_bar_bottom:
    yalign 1.0 yoffset 400
    easein 1.2 yoffset 0

# Personajes
transform attract_tremble:
    function attract_jf_tremble

transform attract_slide_right:
    xoffset 700 alpha 0.0
    ease 0.45 xoffset 0 alpha 1.0

transform attract_run_toward(d=1.6):
    zoom (0.5 * ATTRACT_SPRITE_ZOOM)
    parallel:
        linear d zoom (1.1 * ATTRACT_SPRITE_ZOOM)
    parallel:
        function attract_jf_bob

transform attract_lunge:
    zoom 0.95
    ease 0.5 zoom 1.2

transform attract_lifted:
    yoffset 0
    ease 0.35 yoffset -170
    function attract_jf_kick

transform attract_eyes_in:
    alpha 0.0 zoom 1.0
    parallel:
        linear 1.5 alpha 1.0
    parallel:
        linear 1.8 zoom 1.10

# Siluetas lejanas que se acercan (Azura temblando con Luz y Rodrigo al fondo)
transform attract_sil_far(x=0.8, z=0.55, grow=1.25, d=2.4):
    xalign x yalign 0.9
    zoom (z * ATTRACT_SPRITE_ZOOM)
    matrixcolor TintMatrix("#000000")
    alpha 0.85
    linear d zoom (z * grow * ATTRACT_SPRITE_ZOOM)

# Siluetas que cruzan la pantalla caminando
transform attract_walk(x0=-0.1, x1=1.3, d=5.4, z=0.55, lag=0.0):
    xalign x0 yalign 1.0
    zoom (z * ATTRACT_SPRITE_ZOOM)
    matrixcolor TintMatrix("#120d0d")
    parallel:
        linear d xalign x1
    parallel:
        pause lag
        block:
            ease 0.3 yoffset -14
            ease 0.3 yoffset 0
            repeat

# Siluetas que se alejan hacia el orfanato
transform attract_walk_away(x=0.5, d=6.5, z0=0.5, z1=0.2, lag=0.0):
    xalign x yalign 1.0
    zoom (z0 * ATTRACT_SPRITE_ZOOM)
    matrixcolor TintMatrix("#140f0f")
    parallel:
        linear d xalign 0.5 yalign 0.72 zoom (z1 * ATTRACT_SPRITE_ZOOM)
    parallel:
        pause lag
        block:
            ease 0.3 yoffset -9
            ease 0.3 yoffset 0
            repeat


## ── SCREENS ──────────────────────────────────────────────────

# Se usa desde main_menu con `use attract_watcher`
screen attract_watcher():
    add AttractIdleWatcher()
    timer ATTRACT_POLL repeat True action Function(attract_tick, _update_screens=False)

# Corta el opening con cualquier tecla/click y bloquea el menú de Esc
screen attract_guard():
    zorder 250
    add AttractInterrupter()
    key "game_menu" action Return(True)

# Viñeta + grano de película
screen attract_overlay():
    zorder 90
    if renpy.loadable("images/attract/vignette.png"):
        add "attract_vignette"
    if renpy.loadable("images/attract/grain_1.png"):
        add "attract_grain"

# Barras de cine 2.39:1
screen attract_letterbox():
    zorder 120
    $ bar = int((config.screen_height - config.screen_width / 2.39) / 2)
    add Solid("#000000") xysize (config.screen_width, bar) at attract_bar_top
    add Solid("#000000") xysize (config.screen_width, bar) at attract_bar_bottom

screen attract_entrada(titulo, cuerpo, cps=42, ya=0.5):
    zorder 100
    vbox at attract_text_in:
        xalign 0.5
        yalign ya
        xsize 1300
        spacing 30
        text titulo:
            slow_cps 70
            slow_abortable False
            size 30
            color "#c23030"
            xalign 0.5
            outlines [ (2, "#000000", 0, 0) ]
        text cuerpo:
            slow_cps cps
            slow_abortable False
            size 44
            color "#ece6d6"
            xalign 0.5
            text_align 0.5
            outlines [ (3, "#000000", 0, 0) ]

screen attract_title(glitch=True):
    zorder 110
    $ tf = (ATTRACT_TITLE_FONT or gui.text_font)
    if glitch:
        text "{b}{i}POSSESSED{/i}{/b}" font tf size 170 color "#ff2a2a" xalign 0.5 yalign 0.5 at attract_title_r
        text "{b}{i}POSSESSED{/i}{/b}" font tf size 170 color "#2af0ff" xalign 0.5 yalign 0.5 at attract_title_c
        text "{b}{i}POSSESSED{/i}{/b}" font tf size 170 color "#f2efe6" xalign 0.5 yalign 0.5 outlines [ (5, "#000000", 0, 0) ] at attract_title_w
    else:
        text "{b}{i}POSSESSED{/i}{/b}" font tf size 170 color "#f2efe6" xalign 0.5 yalign 0.5 outlines [ (5, "#000000", 0, 0) ] at attract_title_fade

screen attract_verse():
    zorder 110
    vbox at attract_verse_in:
        xalign 0.5
        yalign 0.5
        xsize 1300
        spacing 40
        text "{i}“No seas vencido de lo malo, sino vence con el bien el mal.”{/i}":
            size 50
            color "#ece6d6"
            xalign 0.5
            text_align 0.5
        text "Romanos 12:21":
            size 30
            color "#8c8c8c"
            xalign 0.5

# Al volver al menú: negro que se disipa
screen attract_curtain():
    zorder 500
    add Solid("#000000") at attract_curtain_out
    timer 1.3 action Hide("attract_curtain")

screen attract_debug():
    zorder 400
    add DynamicDisplayable(attract_debug_text)


## ── EL OPENING ───────────────────────────────────────────────

label attract_opening:

    python:
        attract_qm_prev = getattr(store, "quick_menu", None)
        if attract_qm_prev is not None:
            quick_menu = False
        attract_preload()

        # Bloque 4 · montaje (tipo, imagen, sonido, golpe). "cor" = animación corrupta
        attract_b_shots = [
            ("bg",  "death_mnts_1",     "slash",   "vpunch"),
            ("bg",  "cocina_infestada", "larvcry", None),
            ("cor", "rodrigo"),
            ("bg",  "death_mnts_2",     "slash",   "hpunch"),
            ("bg",  "avispa_guardia",   "thud",    None),
            ("cor", "galaxia"),
            ("bg",  "spdr1",            "thud",    "vpunch"),
            ("bg",  "death_glx_1",      "slash",   "hpunch"),
            ("cor", "rodrigo"),
            ("bg",  "death_wasp",       "slash",   "vpunch"),
            ("bg",  "cocina_infestada", "larvcry", None),
            ("cor", "galaxia"),
            ("bg",  "death_mnts_3",     "slash",   None),
            ("bg",  "avispa_dead",      "thud",    None),
            ("cor", "rodrigo"),
            ("bg",  "escalera_mano_2",  "slash",   None),
            ("bg",  "spdr1",            None,      None),
            ("cor", "galaxia"),
            ("bg",  "death_glx_1",      "slash",   None),
            ("bg",  "death_wasp",       None,      None),
            ("bg",  "death_mnts_2",     None,      None),
            ("cor", "rodrigo"),
            ("bg",  "avispa_dead",      None,      None),
            ("bg",  "cocina_infestada", None,      None),
            ("cor", "galaxia"),
            ("bg",  "death_mnts_1",     "slash",   None),
        ]

    show screen attract_guard
    show screen attract_overlay
    if ATTRACT_DEBUG:
        show screen attract_debug

    # ── 0 · el fondo del menú se corrompe y cae a negro ──
    stop music fadeout 0.8
    $ attract_bg("mainmenubg", extra=[attract_menu_corrupt])
    $ attract_pause(0.9)
    scene black
    show screen attract_letterbox
    $ attract_pause(0.5)

    ############################################################
    # BLOQUE 1 · BITÁCORA  (música: chase2_begin, ~14 s)
    ############################################################
    $ attract_music("chase2_begin")
    $ attract_clock_reset()

    # t 0.0 · Entrada 01
    $ attract_sfx("paper_flip", 0.6)
    $ attract_bg("sotano_inicial", cam=(1.0, 1.12, 3.2), sat=0.35, tint="#cfd8ff", dim=0.15)
    with Dissolve(0.5)
    $ attract_entry("ENTRADA 01 · DÍA 0", "Niños refugiados, sin lazos familiares. Sus historiales los hacen {color=#c23030}prescindibles{/color}.")
    $ attract_until(2.8)
    $ renpy.hide_screen("attract_entrada")

    # t 2.9 · Entrada 04
    $ attract_sfx("paper_flip", 0.6)
    $ attract_bg("pasillo_lab", cam=(1.1, 1.0, 3.0), sat=0.3, tint="#cfd8ff", dim=0.2)
    with attract_cut
    $ attract_entry("ENTRADA 04 · DÍA 11", "El sesenta por ciento ha fallecido. Los cuerpos se deforman, aún respirando por horas.")
    $ attract_ambient("heartbeat", 0.12)
    $ attract_until(5.7)
    $ renpy.hide_screen("attract_entrada")

    # t 5.8 · Entrada 09
    $ attract_sfx("paper_flip", 0.6)
    $ attract_bg("sala_proyector", cam=(1.0, 1.1, 3.0, 0, 30, 0, 0), sat=0.25, tint="#cfd8ff", dim=0.25)
    with attract_cut
    $ attract_entry("ENTRADA 09 · DÍA 28", "Cinco sujetos toleran el patógeno. Los llamamos Huéspedes Activos. Violentos. Territoriales.")
    $ renpy.music.set_volume(0.3, delay=2.5, channel="ambient")
    $ attract_until(8.6)
    $ renpy.hide_screen("attract_entrada")

    # t 8.7 · Entrada 17
    $ attract_sfx("paper_flip", 0.6)
    $ attract_bg("pasillo_abandonado", cam=(1.0, 1.12, 2.9), sat=0.2, tint="#cfd8ff", dim=0.35)
    with attract_cut
    $ attract_entry("ENTRADA 17 · DÍA 49", "{color=#c23030}[[REDACTADO]{/color} ya no responde. No somos los domadores aquí. Somos la presa.", cps=46)
    $ renpy.music.set_volume(0.55, delay=2.5, channel="ambient")
    $ attract_until(11.4)
    $ renpy.hide_screen("attract_entrada")

    # t 11.5 · Entrada 20 → los ojos aparecen al fondo
    $ attract_sfx("paper_flip", 0.6)
    $ attract_bg("pasillo_oscuro", cam=(1.0, 1.08, 2.6), sat=0.15, dim=0.5)
    with attract_cut
    $ attract_entry("ENTRADA 20 · DÍA 55", "Escucho sus pasos. {color=#c23030}[[REDACTADO]{/color} me busca, pero aún no me encuentra.", cps=52)
    $ renpy.music.set_volume(1.0, delay=2.0, channel="ambient")
    $ attract_until(12.7)
    $ renpy.hide_screen("attract_entrada")
    show galaxia shadow_eyes at center, attract_eyes_in
    with Dissolve(0.3)
    $ attract_until(ATTRACT_INTRO_LEN)

    ############################################################
    # BLOQUE 2 · CORTE SECO + TÍTULO (en silencio)
    ############################################################
    $ renpy.music.stop(channel="music", fadeout=0)
    $ renpy.music.stop(channel="ambient", fadeout=0)
    $ renpy.hide_screen("attract_entrada")
    $ renpy.show_layer_at([], layer="master", reset=True)
    scene black
    $ attract_sfx("thud", 1.0)
    show screen attract_title(True)
    $ attract_pause(ATTRACT_TITLE_LEN)
    hide screen attract_title

    ############################################################
    # BLOQUE 3 · FRAGMENTOS DE JUEGO  (música: chase2)
    ############################################################
    $ attract_music("chase2")
    $ attract_clock_reset()

    # t 0.0 · el primer reencuentro de Luz y Rodrigo
    $ attract_bg("puerta_oxidada", cam=(1.02, 1.14, 0.9))
    $ attract_sfx("door_slam", 0.9)
    with hpunch
    $ attract_until(0.45)
    $ attract_sfx("door_break", 0.9)
    with vpunch
    $ attract_until(0.95)
    $ attract_bg("foreboding_1", cam=(1.0, 1.10, 1.6), dim=0.1)
    show luz scared at left, attract_tremble
    show rodrigo alert at right, attract_slide_right
    with attract_flash
    $ attract_until(2.5)

    # t 2.5 · Cutipye corriendo
    $ attract_bg("pasillo_corriendo", cam=(1.06, 1.0, 1.7), extra=[attract_shake_cam])
    show cutipye scared at center, attract_run_toward(1.7)
    $ attract_sfx("run", 0.7)
    with attract_cut
    $ attract_until(4.2)

    # t 4.2 · Azura temblando; Luz y Rodrigo, siluetas al fondo
    $ attract_bg("vestibulo", cam=(1.0, 1.14, 2.4, 0, -30, 0, 0), dim=0.2)
    show luz neutral at attract_sil_far(0.74, 0.5, 1.3, 2.4)
    show rodrigo neutral at attract_sil_far(0.88, 0.5, 1.3, 2.4)
    show azura temblor at left, attract_tremble
    with attract_cut
    $ attract_until(6.6)

    # t 6.6 · Nagi siendo atacado
    $ attract_bg("pasillo_oscuro", cam=(1.0, 1.08, 1.9), dim=0.25)
    show galaxia walk_creepy at right, attract_lunge
    show nagi scared at centro_izquierda, attract_lifted
    with attract_cut
    $ attract_sfx("slash", 0.8)
    $ attract_until(8.5)

    # t 8.5 · tensión: cadáver → araña en el techo
    $ attract_bg("habitacion_cadaver", cam=(1.0, 1.12, 0.9))
    $ attract_sfx("flies", 0.7)
    with attract_flash
    $ attract_until(9.3)
    $ attract_bg("scene_spdr", cam=(1.0, 1.15, 0.9))
    with attract_cut
    $ attract_until(10.2)

    # t 10.2 · Galaxia en la ventana
    $ attract_bg("galaxia_ventana", cam=(1.0, 1.14, 1.7), dim=0.1)
    $ attract_sfx("glx_laugh", 0.35)
    with attract_cut
    $ attract_until(11.9)

    # t 11.9 · el sujeto herido
    $ attract_bg("sala_h127", cam=(1.0, 1.1, 1.6), dim=0.15)
    show sujeto_herido at center
    with attract_cut
    $ attract_until(13.5)

    # t 13.5 · Luz y Rodrigo huyen
    $ attract_bg("escape_1", cam=(1.05, 1.0, 1.5), extra=[attract_shake_cam])
    show luz scared at left, attract_run_toward(1.5)
    show rodrigo scared at right, attract_run_toward(1.5)
    $ attract_sfx("run", 0.7)
    with attract_cut
    $ attract_until(15.0)

    # t 15.0 · el piso cede
    $ attract_bg("derrumbe", cam=(1.0, 1.1, 1.3))
    $ attract_sfx("crack", 0.9)
    with vpunch
    $ attract_until(16.3)

    # t 16.3 · la escalera
    $ attract_bg("escalera_mano_1", cam=(1.0, 1.1, 1.1))
    with attract_cut
    $ attract_until(17.4)
    $ attract_bg("escalera_mano_2", cam=(1.0, 1.12, 1.0))
    $ attract_sfx("slash", 0.9)
    with vpunch
    $ attract_until(18.4)

    # t 18.4 · la Mantis
    $ attract_bg("habitacion_mantis", cam=(1.0, 1.16, 1.7), dim=0.1)
    $ attract_sfx("nailtap", 0.8)
    with attract_cut
    $ attract_until(ATTRACT_T_TEMPO)

    ############################################################
    # BLOQUE 4 · EL TEMPO SUBE (escenas cada vez más breves)
    ############################################################
    $ attract_c0 = ATTRACT_T_FINALE - 3.4
    $ attract_run_b(attract_b_shots, ATTRACT_T_TEMPO, attract_c0, 2.0)

    # · clímax: el disparo a Galaxia
    $ attract_bg("bg_almacen_medico", cam=(1.0, 1.16, 1.1), dim=0.2)
    show rodrigo aim_gun at left
    show galaxia walk_creepy at right, attract_lunge
    with attract_cut
    $ attract_until(attract_c0 + 1.0)

    $ attract_bg("gal_dead_floor", cam=(1.0, 1.1, 0.8))
    $ attract_sfx("gunshot", 1.0)
    with attract_flash
    $ attract_until(attract_c0 + 1.55)

    scene black
    $ attract_until(attract_c0 + 1.85)

    $ attract_bg("chase1_reprise", cam=(1.0, 1.12, 1.2))
    $ attract_sfx("glx_laugh", 0.6)
    with attract_cut
    $ attract_until(attract_c0 + 2.7)

    $ attract_bg("chase1_1", cam=(1.0, 1.2, 0.8))
    show galaxia healed at truecenter
    with attract_flash
    $ attract_until(ATTRACT_T_FINALE)

    ############################################################
    # BLOQUE 5 · EL INICIO DE LA HISTORIA
    ############################################################
    $ attract_bg("bosque_tarde", cam=(1.0, 1.10, 5.2), tint="#ffe2c0", dim=0.1)
    show nagi neutral    at attract_walk(-0.10, 1.30, 5.4, 0.55, 0.0)
    show cutipye neutral at attract_walk(-0.24, 1.16, 5.4, 0.55, 0.1)
    show azura neutral   at attract_walk(-0.38, 1.02, 5.4, 0.55, 0.2)
    show luz neutral     at attract_walk(-0.52, 0.88, 5.4, 0.55, 0.3)
    show rodrigo neutral at attract_walk(-0.66, 0.74, 5.4, 0.55, 0.4)
    with Dissolve(1.2)
    $ attract_until(ATTRACT_T_FINALE + 5.0)

    $ attract_bg("orfanato_exterior1", cam=(1.0, 1.22, 7.0), tint="#ffe2c0", dim=0.15)
    show nagi neutral    at attract_walk_away(0.30, 6.5, 0.5, 0.20, 0.0)
    show cutipye neutral at attract_walk_away(0.38, 6.5, 0.5, 0.20, 0.1)
    show azura neutral   at attract_walk_away(0.46, 6.5, 0.5, 0.20, 0.2)
    show luz neutral     at attract_walk_away(0.54, 6.5, 0.5, 0.20, 0.3)
    show rodrigo neutral at attract_walk_away(0.62, 7.0, 0.5, 0.20, 0.4)
    with Dissolve(0.9)
    $ attract_until(ATTRACT_T_END)

    ############################################################
    # BLOQUE 6 · TÍTULO + ROMANOS 12:21
    # La música hace fadeout lento mientras se muestran el título y el versículo.
    # Duración total del bloque: ~11 s → fadeout de 10 s para que termine con calma.
    ############################################################
    $ renpy.music.stop(channel="music", fadeout=10.0)
    scene black with Dissolve(1.4)
    $ attract_pause(0.4)
    show screen attract_title(False)
    $ attract_pause(2.6)
    hide screen attract_title
    $ attract_pause(0.7)
    show screen attract_verse
    $ attract_pause(ATTRACT_VERSE_LEN)
    hide screen attract_verse
    $ attract_pause(0.9)

    # (si termina normal, cae directo a la limpieza)

label attract_exit:
    python:
        for _s in ("attract_guard", "attract_overlay", "attract_letterbox", "attract_entrada",
                   "attract_title", "attract_verse", "attract_debug"):
            renpy.hide_screen(_s)
        renpy.music.stop(channel="sound")
        renpy.music.stop(channel="ambient", fadeout=0.3)
        renpy.music.set_volume(1.0, channel="ambient")
        renpy.show_layer_at([], layer="master", reset=True)
        if attract_qm_prev is not None:
            quick_menu = attract_qm_prev
    return