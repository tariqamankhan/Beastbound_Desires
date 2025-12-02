# Chapter 2: Mount Infernus

label chapter2:
    scene backgrounds/mount_infernus_bg with fade
    e "Lore ipsum: Mount Infernus ascent."
    call tease_phase("mount_infernus", "Sulfurous winds tease phase placeholder.")
    call tempt_phase("lava_beast", "Infernal beast emerges. Lore ipsum prompt.")
    call torment_phase(25)

    menu:
        "Do you seize the infernal core?":
            "Seize it":
                $ add_item("infernal_core")
                e "Lore ipsum: Core secured."
            "Refuse":
                e "Lore ipsum: Core rejected."
    call release_phase("tentacle_probe", 3.0)
    call relapse_phase()
    jump calculate_ending
