# Project Structure

## Root Files
- `script.rpy`: Main story script (Act 1 start)
- `script_2.rpy`, `script_3.rpy`: Additional story acts/chapters
- `definitions.rpy`: Character definitions, variables, images, audio, transforms
- `options.rpy`: Game configuration, build settings, transitions
- `gui.rpy`: GUI styling, colors, fonts, sizes
- `screens.rpy`: UI screen definitions (menus, HUD, dialogs)

## Asset Directories

### `/audio`
- `music/`: Background tracks (`.ogg`, `.mp3`) with loop points defined
- `sfx/`: Sound effects for actions, ambience, interactions

### `/images`
- `bg/`: Background scenes and locations
- `sprites/`: Character sprites with multiple expressions/states
- `objects/`: Props and interactive items
- `game_over/`: Death/failure screens

### `/gui`
- `button/`: Button states (idle, hover, selected)
- `bar/`: UI bar components (top, bottom, left, right)
- Root: Frames, notification boxes, namebox, main menu background

### `/fonts`
Custom typefaces (HelpMe.ttf for Galaxia character dialogue)

### `/.kiro`
AI assistant configuration and steering documents

### `/cache`
Auto-generated Ren'Py caches (bytecode, shader cache, analysis data)

### `/saves`
Player save files

### `/tl`
Translation files (if localization is added)

## Code Organization Conventions

### Character Definitions
All characters defined in `definitions.rpy` with:
- Short variable name (e.g., `r` for Rodrigo)
- Display name and color
- Special fonts if needed (e.g., Galaxia uses HelpMe.ttf)

### Images
Named with pattern: `[character/scene] [variant]`
```python
image rodrigo neutral = "images/sprites/Rodri.png"
image bg_pasillo_scroll = "bg/pasillo.png"
```

### Audio
Defined with named constants:
```python
define audio.main_menu = "<loop 28.25>music/menu.ogg"
define gunshot = "sfx/gunshot.mp3"
```

### Game State Variables
Tracked in `definitions.rpy`:
- Affinity variables: `afinidad_[character]`
- Mental state: `estado_mental`
- Timing: `tiempo_escape`
- Death flags: `[character]_dead`
- Ending type: `ending_type`

### Transforms
Visual effects and animations defined in `definitions.rpy`:
- Position transforms: `centro_izquierda`, `centro_derecha`
- Effect transforms: `distortion_light`, `distortion_heavy`, `heartbeat`
- Filter transforms: `sepia_filter`, `blanco_y_negro`, `oscuro`
- Animation transforms: `shaking`, `vjump`, `slow_scroll`

### Labels
Story structure:
- `label start`: Game entry point
- `label intro`: Opening sequence
- `label chapter_complete(nombre)`: Chapter transition handler
- Act/chapter labels as needed in story flow

## Naming Conventions
- Files: lowercase with underscores (e.g., `script_2.rpy`)
- Variables: lowercase with underscores (e.g., `afinidad_luz`)
- Characters: lowercase single letter (e.g., `r`, `l`, `c`)
- Images: lowercase with spaces or underscores (e.g., `rodrigo neutral`)
- Audio: lowercase with underscores (e.g., `door_slam`)
- Labels: lowercase with underscores (e.g., `chapter_complete`)

## Style Guidelines
- Spanish language for narrative and dialogue
- Comments in Spanish
- Indent with 4 spaces (Ren'Py standard)
- Menu choices affect affinity and mental state
- Use `show`/`hide` for sprite management
- Use `scene` for background transitions
- Always include audio fade transitions (e.g., `fadein 2`, `fadeout 1.5`)
