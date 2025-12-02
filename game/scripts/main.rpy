# Beastbound Desires - main entry script

# Declare some global defaults
default edge_meter = 0
default inventory = {}
default persistent.chapter_unlocked = {"chapter1": True, "chapter2": False}

label splashscreen:
    scene black
    "This game contains adult themes: rough monster encounters, etc. Proceed?"
    menu:
        "Content warning acknowledged?":
            "Yes":
                return
            "No":
                $ renpy.quit()

label start:
    call screen edge_meter_overlay
    $ inventory = {"werewolf_essence": False, "infernal_core": False}
    $ edge_meter = 0
    scene black with fade
    "Lore ipsum opening sets the mood of Elara's cursed journey."
    menu:
        "Choose where to begin":
            "Chapter 1: Moonwood Forest" if persistent.chapter_unlocked.get("chapter1", False):
                jump chapter1
            "Chapter 2: Mount Infernus" if persistent.chapter_unlocked.get("chapter2", False):
                jump chapter2
    return
