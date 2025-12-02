# Siren's Cove - Chapter 3 skeleton
label chapter3:
    $ edge_meter = 0
    $ set_location_background("cove")
    n "Mist curls over the tidal pools of the Siren's Cove, humming with forbidden hymns."

    $ tease_phase("cove", "Lore ipsum tease as waves lap against barnacled pillars.")
    $ tempt_phase("Siren Matron", "Lore ipsum temptation entwined with haunting melodies.")

    menu:
        "Anchor your mind":
            $ torment_phase("Siren Matron", "Lore ipsum focus while the chorus claws for control.")
            $ add_item("siren_shell")
            n "Elara tucks away a pearlescent shell thrumming with resonance."
        "Let the tide claim you":
            $ release_phase("erotica/gifs/placeholder.gif", 2.5)
            n "Salt spray and song crash over her in dizzying cadence."

    $ relapse_phase("Lore ipsum relapse as echoes refuse to leave her skull.")

    menu:
        "Dive toward the sunken gate":
            n "Bioluminescent runes flicker beneath the surface."
        "Surface for a breath":
            n "The storming sky offers little comfort, but some clarity."

    call calculate_ending
    jump after_chapter3
