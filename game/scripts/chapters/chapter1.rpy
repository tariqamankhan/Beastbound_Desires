# Chapter 1: Moonwood Forest

label chapter1:
    scene backgrounds/moonwood_forest_bg with fade
    e "Lore ipsum: Moonwood Forest introduction."
    call tease_phase("moonwood_forest", "Misty woods tease phase placeholder.")
    call tempt_phase("werewolf_alpha", "A towering werewolf looms. Lore ipsum prompt.")
    call torment_phase(20)

    menu:
        "Do you collect the werewolf essence?":
            "Collect it":
                $ add_item("werewolf_essence")
                e "Lore ipsum: Essence claimed."
            "Leave it":
                e "Lore ipsum: Essence left behind."
    call release_phase("werewolf_pin", 3.0)
    call relapse_phase()
    $ persistent.chapter_unlocked["chapter2"] = True
    jump calculate_ending
