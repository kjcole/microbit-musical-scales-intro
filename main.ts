input.onButtonPressed(Button.A, function on_button_pressed_a() {
    for (let note of chromatic) {
        music.playTone(note, music.beat(BeatFraction.Whole))
    }
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    for (let degree of major) {
        music.playTone(chromatic[degree], music.beat(BeatFraction.Whole))
    }
})
let major : number[] = []
let chromatic : number[] = []
chromatic = [Note.C4, Note.CSharp4, Note.D4, Note.Eb4, Note.E4, Note.F4, Note.FSharp4, Note.G4, Note.GSharp4, Note.A4, Note.Bb4, Note.B4, Note.C5]
major = [0, 2, 4, 5, 7, 9, 11, 12]
