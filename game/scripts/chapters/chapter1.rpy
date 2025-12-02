# Moonwood Forest - Chapter 1 skeleton
label chapter1:
    $ init_inventory()
    $ edge_meter = 0
    scene expression "backgrounds/moonwood_forest_bg.png"
    n "Moonwood Forest whispers with unseen desires."

    $ tease_phase("forest", "Lore ipsum tease under mist-laden boughs.")
    $ tempt_phase("Werewolf Alpha", "Lore ipsum temptation as fur brushes skin.")

    menu:
        "Resist the howl":
            $ torment_phase("Werewolf Alpha", "Lore ipsum resistance line.")
            $ add_item("werewolf_essence")
            n "Elara bottles a trace of essence for later rituals."
        "Submit to the pull":
            $ release_phase("erotica/gifs/werewolf_pin.gif", 2.5)
            n "The curse deepens, etched into her pulse."

    $ relapse_phase("Lore ipsum relapse as she catches breath.")

    menu:
        "Press deeper into the forest":
            n "Paths wind toward older magics."
        "Retreat to camp":
            n "Supplies and sanity are restored briefly."

    jump after_chapter1
