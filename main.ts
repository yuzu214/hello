basic.forever(function () {
    basic.showIcon(IconNames.Pitchfork)
    basic.pause(100)
    basic.showIcon(IconNames.Umbrella)
    basic.pause(100)
    basic.showLeds(`
        . . . . .
        . . # # .
        . . # . #
        . . . . .
        # . # . .
        `)
})
