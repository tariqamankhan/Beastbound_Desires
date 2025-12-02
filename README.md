# Beastbound Desires

Skeleton Ren'Py project for a medieval fantasy adult visual novel.

## Structure
- `game/main.rpy`: Entry point, chapter selection, and splash handling.
- `game/options.rpy`: Basic configuration, warning splash, and window sizing.
- `game/scripts/common/`: Shared logic including mechanics, endings, characters, and inventory helpers.
- `game/scripts/chapters/`: Modular chapters (`chapter1` and `chapter2` included) plus a template for future additions.
- `game/scripts/gui/`: Placeholder screens and styles, including edge meter overlay and quick menu.
- `game/images/`: Placeholder assets for backgrounds, characters, monsters, UI, and erotica GIFs.
- `game/audio/`: Empty folders for music, sfx, and voice placeholders.
- `game/fonts/`: Placeholder medieval-styled font file reference.

## Running
Open the project in Ren'Py and launch from `game/main.rpy`. Chapters load through `chapter_select`, unlocking Chapter 2 after completing Chapter 1.
