# Core gameplay loop functions and edge meter helpers

init python:
    def clamp_edge(value):
        return max(0, min(100, value))

    def update_edge(amount):
        global edge_meter
        edge_meter = clamp_edge(edge_meter + amount)
        renpy.restart_interaction()

    def add_item(item):
        inventory[item] = True

label tease_phase(location, description):
    scene expression f"backgrounds/{location}_bg" with fade
    "[description]"
    return

label tempt_phase(opponent, prompt):
    show expression f"monsters/{opponent}" at center with dissolve
    "[prompt]"
    menu:
        "How does Elara respond?":
            "Resist":
                $ update_edge(-10)
                "Lore ipsum resistance narrative."
            "Tease":
                $ update_edge(15)
                "Lore ipsum teasing narrative."
            "Submit":
                $ update_edge(25)
                "Lore ipsum submission narrative."
    hide expression f"monsters/{opponent}" with dissolve
    return

label torment_phase(intensity):
    if edge_meter >= 50:
        "Edge high variant: lore ipsum more intense torment."
    else:
        "Edge low variant: lore ipsum softer torment."
    $ update_edge(intensity)
    return

label release_phase(gif_name="werewolf_pin", duration=3.0):
    $ renpy.show(gif_name, at_list=[center])
    pause duration
    hide expression gif_name with dissolve
    "Lore ipsum release narrative."
    return

label relapse_phase():
    "Relapse aftermath lore ipsum." 
    return
