## Basic Ren'Py configuration for Beastbound Desires
init -1 python:
    config.developer = True
    config.window_title = "Beastbound Desires"
    config.version = "0.1.0-skeleton"
    config.name = "Beastbound Desires"

# Toggle for adult intensity descriptions
init python:
    define_adult_modes = ["mild", "rough", "extreme"]

# Default screen size
define config.screen_width = 1280
define config.screen_height = 720

# Placeholder for content warnings
label before_main_menu:
    scene black
    "Content Warning: This story explores adult monster encounters, curses, and consented fantasy themes."
    return
