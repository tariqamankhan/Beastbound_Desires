# Template for new chapters

label chapter_template:
    scene backgrounds/<location> with fade
    e "Lore ipsum: Chapter intro."
    call tease_phase("<location>", "Tease description placeholder.")
    call tempt_phase("<opponent>", "Prompt placeholder.")
    call torment_phase(20)

    menu:
        "Branching choice placeholder":
            "Option A":
                e "Lore ipsum branch A."
            "Option B":
                e "Lore ipsum branch B."
    call release_phase("werewolf_pin", 3.0)
    call relapse_phase()
    jump calculate_ending
