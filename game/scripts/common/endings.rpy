# Ending logic and scenes

label calculate_ending:
    if edge_meter >= 80:
        jump gooner_queen
    elif edge_meter >= 50:
        jump balanced_wanderer
    elif inventory.get("infernal_core"):
        jump infernal_heir
    else:
        jump purified

label gooner_queen:
    scene black with fade
    show characters/elara_aroused at center
    "You rule eternally in pleasure. Lore ipsum finale."
    return

label balanced_wanderer:
    scene black with fade
    show characters/elara_normal at center
    "You find balance between desire and duty. Lore ipsum finale."
    return

label infernal_heir:
    scene black with fade
    show monsters/lava_beast at center
    "You inherit infernal power. Lore ipsum finale."
    return

label purified:
    scene black with fade
    show characters/elara_defiant at center
    "You cleanse the curse and walk away. Lore ipsum finale."
    return
