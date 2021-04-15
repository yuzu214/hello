def on_forever():
    basic.show_icon(IconNames.PITCHFORK)
    basic.pause(100)
    basic.show_icon(IconNames.UMBRELLA)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
        . . # # .
        . . # . #
        . . . . .
        # . # . .
        """)
basic.forever(on_forever)
