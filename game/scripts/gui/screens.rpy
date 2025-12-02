screen edge_meter_overlay():
    frame:
        align (0.95, 0.1)
        has vbox
        text "Edge Meter" size 18
        bar value edge_meter range 100 xmaximum 200

screen gallery_stub():
    tag menu
    frame:
        align (0.5, 0.5)
        vbox:
            spacing 10
            text "Gallery (placeholder)" size 32
            text "Unlock erotic scenes by progressing through endings."
            textbutton "Return" action Return()

# Include a simple quick menu
screen quick_menu():
    hbox:
        style_prefix "quick"
        xalign 0.5
        yalign 1.0
        spacing 12
        textbutton "Save" action ShowMenu("save")
        textbutton "Load" action ShowMenu("load")
        textbutton "Prefs" action ShowMenu("preferences")
        textbutton "Skip" action Skip()

init python:
    config.overlay_screens.append("edge_meter_overlay")
    config.overlay_screens.append("quick_menu")
