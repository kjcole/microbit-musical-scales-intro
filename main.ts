input.onButtonPressed(Button.A, function on_button_pressed_a() {
    for (let value of pitches) {
        music.playTone(value, music.beat(BeatFraction.Whole))
    }
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    for (let value2 of scale) {
        music.playTone(pitches[value2], music.beat(BeatFraction.Whole))
    }
})
let scale : number[] = []
let pitches : number[] = []
pitches = [262, 277, 294, 311, 330, 349, 370, 392, 415, 440, 466, 494, 523]
scale = [0, 2, 4, 5, 7, 9, 11, 12]
