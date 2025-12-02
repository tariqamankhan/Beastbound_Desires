# Core gameplay loop utilities for Beastbound Desires
init python:
    def set_location_background(location_key):
        backgrounds = {
            "forest": "backgrounds/moonwood_forest_bg.png",
            "mountain": "backgrounds/mount_infernus_bg.png",
            "cove": "backgrounds/placeholder_bg.png",
            "bastion": "backgrounds/placeholder_bg.png",
        }
        bg = backgrounds.get(location_key, "backgrounds/placeholder_bg.png")
        renpy.show("scene_bg", what=Image(bg))

    def update_edge_meter(amount):
        global edge_meter
        edge_meter = max(0, min(100, edge_meter + amount))
        renpy.restart_interaction()

    def tease_phase(location, description):
        set_location_background(location)
        renpy.say(n, description)
        update_edge_meter(5)

    def tempt_phase(opponent, description):
        renpy.say(n, "Temptation rises as [opponent] closes in.")
        renpy.say(n, description)
        update_edge_meter(10)

    def torment_phase(opponent, description):
        renpy.say(n, "Torment tests resolve against [opponent].")
        renpy.say(n, description)
        update_edge_meter(15)

    def release_phase(gif_name="ui/placeholder_release.gif", duration=2.0):
        renpy.say(n, "Release washes over Elara in a whirlwind of sensations.")
        renpy.show(gif_name)
        renpy.pause(duration)
        renpy.hide(gif_name)
        update_edge_meter(-20)

    def relapse_phase(description):
        renpy.say(n, description)
        update_edge_meter(5)

    def trigger_gif(gif_name, duration=5.0):
        renpy.show(gif_name)
        renpy.pause(duration)
        renpy.hide(gif_name)
