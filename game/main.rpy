# Beastbound Desires - Main Entry
# Skeleton chapter loader and global variables

# Declare persistent or default variables
default persistent.chapter_unlocked = {
    "chapter1": True,
    "chapter2": False,
    "chapter3": False,
    "chapter4": False,
}
default edge_meter = 0
default intensity_setting = "mild"
default inventory = {}

define e = Character("Elara", color="#ff66cc", what_prefix="\"", what_suffix="\"")
define n = Character("Narrator")

label splashscreen:
    scene black
    n "This game contains adult themes, fantastical monsters, and heavy teasing. Proceed with awareness."
    return

label start:
    call screen main_menu_stub
    jump chapter_select

label chapter_select:
    scene black
    n "Choose where Elara's journey continues."
    menu:
        "Moonwood Forest (Chapter 1)":
            jump chapter1
        "Mount Infernus (Chapter 2)" if persistent.chapter_unlocked.get("chapter2", False):
            jump chapter2
        "Siren's Cove (Chapter 3)" if persistent.chapter_unlocked.get("chapter3", False):
            jump chapter3
        "Clockwork Bastion (Chapter 4)" if persistent.chapter_unlocked.get("chapter4", False):
            jump chapter4
        "Exit":
            return

label after_chapter1:
    $ persistent.chapter_unlocked["chapter2"] = True
    jump chapter_select

label after_chapter2:
    $ persistent.chapter_unlocked["chapter3"] = True
    jump chapter_select

label after_chapter3:
    $ persistent.chapter_unlocked["chapter4"] = True
    jump chapter_select

label after_chapter4:
    jump chapter_select

# Simple main menu placeholder until Ren'Py default menu is customized
screen main_menu_stub():
    tag menu
    vbox:
        align (0.5, 0.5)
        spacing 20
        text "Beastbound Desires" size 60
        textbutton "Start" action Return()
        textbutton "Quit" action Quit(confirm=False)
