# Custom screens including edge meter and gallery placeholder

screen edge_meter_overlay():
    frame align (0.02, 0.05):
        has vbox
        text "Edge Meter" size 18
        bar value edge_meter range 100 xmaximum 200 style "edge_meter_bar"

screen gallery_placeholder():
    tag menu
    add Solid("#000000")
    vbox:
        align (0.5, 0.5)
        spacing 10
        text "Gallery coming soon" size 32
        textbutton "Return" action Return(True)

# Standard quick menu
screen quick_menu():
    hbox:
        style_prefix "quick"
        xalign 0.5
        yalign 1.0
        textbutton _( "Save" ) action ShowMenu('save')
        textbutton _( "Load" ) action ShowMenu('load')
        textbutton _( "Prefs" ) action ShowMenu('preferences')
        textbutton _( "Gallery" ) action ShowMenu('gallery_placeholder')
