# Ending calculations and placeholder scenes
label calculate_ending:
    if edge_meter >= 80:
        jump gooner_queen
    elif edge_meter >= 50:
        jump haunted_wanderer
    elif edge_meter >= 20:
        jump tempered_scout
    else:
        jump purified_scholar

label gooner_queen:
    scene black
    n "Elara claims a throne forged from desire itself."
    return

label haunted_wanderer:
    scene black
    n "Shadows cling to Elara as she roams for more answers."
    return

label tempered_scout:
    scene black
    n "Balance restored, she scouts the next frontier."
    return

label purified_scholar:
    scene black
    n "Knowledge tempers the curse, guiding her path forward."
    return
