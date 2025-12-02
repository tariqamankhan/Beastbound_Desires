# Core gameplay loop utilities for Beastbound Desires
init python:
    def set_location_background(location_key):
        backgrounds = {
            "forest": "backgrounds/moonwood_forest_bg.png",
            "mountain": "backgrounds/mount_infernus_bg.png",
        }
        bg = backgrounds.get(location_key, "backgrounds/placeholder_bg.png")
        renpy.show("scene_bg", what=Image(bg))

    def update_edge_meter(amount):
        global edge_meter
        edge_meter = max(0, min(100, edge_meter + amount))
        renpy.restart_interaction()

    def tease_phase(location, description):
        set_location_background(location)
        n description
        $ update_edge_meter(5)

    def tempt_phase(opponent, description):
        n "Temptation rises as [opponent] closes in."
        n description
        $ update_edge_meter(10)

    def torment_phase(opponent, description):
        n "Torment tests resolve against [opponent]."
        n description
        $ update_edge_meter(15)

    def release_phase(gif_name="ui/placeholder_release.gif", duration=2.0):
        $ n("Release washes over Elara in a whirlwind of sensations.")
        show expression gif_name at center
        pause duration
        hide expression gif_name
        $ update_edge_meter(-20)

    def relapse_phase(description):
        n description
        $ update_edge_meter(5)

    def trigger_gif(gif_name, duration=5.0):
        show expression gif_name at center
        pause duration
        hide expression gif_name
