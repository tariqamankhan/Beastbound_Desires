# Beastbound Desires

Skeleton Ren'Py project for a medieval fantasy adult visual novel.

## Structure
- `game/` core Ren'Py content
  - `options.rpy` basic configuration and content toggles
  - `scripts/` modular scripts
    - `main.rpy` entry point and chapter selection
    - `common/` shared logic (mechanics, endings, characters, assets, items)
    - `gui/` custom screens and styles
    - `chapters/` chapter-specific files plus a reusable template
- `images/`, `audio/` contain placeholder assets ready for replacement.

Chapters 1 and 2 are stubbed with lore ipsum placeholders and functional edge meter, choice, and item hooks to demonstrate the flow.
