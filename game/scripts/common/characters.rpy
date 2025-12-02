# Character definitions and quick-reference traits
init:
    define elara = Character("Elara", color="#ff66cc", what_prefix="\"", what_suffix="\"")
    define aria = Character("Aria", color="#66ccff")
    define narrator = Character(None)

init python:
    character_traits = {
        "elara": {"role": "cursebearer", "tone": "playful"},
        "aria": {"role": "guide", "tone": "calm"},
    }
