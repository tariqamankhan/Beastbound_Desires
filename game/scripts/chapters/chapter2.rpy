# Mount Infernus - Chapter 2 skeleton
label chapter2:
    $ edge_meter = 0
    scene expression "backgrounds/mount_infernus_bg.png"
    n "Heat from Mount Infernus rolls over Elara like a living tide."

    $ tease_phase("mountain", "Lore ipsum tease along obsidian ridges.")
    $ tempt_phase("Lava Beast", "Lore ipsum temptation as embers dance.")

    menu:
        "Channel the flame":
            $ torment_phase("Lava Beast", "Lore ipsum forging focus.")
            $ add_item("infernus_coal")
            n "She captures cooled coal, pulsing faintly with magic."
        "Embrace the burn":
            $ release_phase("erotica/gifs/tentacle_probe.gif", 2.5)
            n "The mountain marks her with molten symbols."

    $ relapse_phase("Lore ipsum relapse amid smoke and ash.")

    menu:
        "Seek the summit":
            n "An ancient altar waits near the peak."
        "Descend to safety":
            n "A hidden cavern offers respite."

    call calculate_ending
    jump after_chapter2
