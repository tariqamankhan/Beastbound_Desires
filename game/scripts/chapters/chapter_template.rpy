# Template for future chapters
label chapter_template:
    $ init_inventory()
    call tease_phase("placeholder", "Lore ipsum opening for new chapter.")
    call tempt_phase("foe", "Lore ipsum temptation phase.")
    menu:
        "Resist":
            call torment_phase("foe", "Resist path placeholder.")
        "Submit":
            call release_phase("erotica/gifs/placeholder.gif", 1.0)
    call relapse_phase("Relapse placeholder text.")
    call calculate_ending
    return
