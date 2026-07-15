# Technical Stack

## Framework
- **Ren'Py**: Python-based visual novel engine
- **Python**: 3.12 (bytecode cache indicates Python 3.12)
- **Resolution**: 1920x1080 native

## Project Structure
- `.rpy` files: Ren'Py script files (human-readable source)
- `.rpyc` files: Compiled bytecode (auto-generated, don't edit)
- `cache/`: Runtime caches (bytecode, analysis)
- `saves/`: Player save data

## Audio System
Custom audio channel configuration:
- Music mixer
- Sound effects mixer
- Voice mixer
- **Ambient mixer**: Custom channel for ambient loops (registered in `options.rpy`)

## Asset Organization
- `audio/music/`: Background music (`.ogg`, `.mp3`)
- `audio/sfx/`: Sound effects
- `images/bg/`: Background images
- `images/sprites/`: Character sprites
- `images/objects/`: Interactive objects
- `images/game_over/`: Death/game over screens
- `fonts/`: Custom fonts (HelpMe.ttf for special character)
- `gui/`: UI elements (buttons, frames, bars)

## Build System
Uses Ren'Py's built-in build system configured in `options.rpy`:
- Build name: "Possessed"
- Save directory: "Possessed-1753492026"
- Window icon: `gui/window_icon.png`

## Common Commands
```bash
# Launch game (from Ren'Py launcher)
# No direct CLI - use Ren'Py launcher application

# File operations
# Edit .rpy files directly
# .rpyc files regenerate automatically on launch

# Testing
# Use Ren'Py's built-in console: Shift+O (debug mode)
# Reload game: Shift+R
# Force recompile: Delete .rpyc files
```

## Development Patterns
- Main menu background: `mainmenubg` image
- Splash screen warning label: `splashscreen`
- Entry point: `label start`
- Chapter completion: `label chapter_complete(nombre)`
- HUD toggle: `mostrar_hud` variable
- Persistent data: `persistent.` prefix (e.g., `persistent.credits_seen`)

## Libraries
Standard Ren'Py distribution. Third-party libs go in `libs/` folder if needed.
