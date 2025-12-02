# Clockwork Bastion - Chapter 4 skeleton
label chapter4:
    $ edge_meter = 0
    $ set_location_background("bastion")
    n "Gears the size of houses grind inside the Clockwork Bastion, measuring out desire in precise ticks."

    $ tease_phase("bastion", "Lore ipsum tease among brass arches and steam vents.")
    $ tempt_phase("Automaton Warden", "Lore ipsum temptation as metal fingers trace curious circuits.")

    menu:
        "Seize command protocols":
            $ torment_phase("Automaton Warden", "Lore ipsum overriding the machine's cadence.")
            $ add_item("clockwork_core")
            n "She pockets a humming core, still warm from the Warden's chest."    
        "Sync with its rhythm":
            $ release_phase("erotica/gifs/tentacle_probe.gif", 2.5)
            n "Pistons and pistils move in unison, drafting pleasure blueprints."    

    $ relapse_phase("Lore ipsum relapse as gears spin behind her eyes.")

    menu:
        "Ascend to the observatory":
            n "Glass lenses reveal constellations etched like circuits."
        "Descend to the engine heart":
            n "A pulsing drive shaft promises further mysteries."

    call calculate_ending
    jump after_chapter4
