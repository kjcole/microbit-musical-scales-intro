def on_button_pressed_a():
    for note in chromatic:
        music.play_tone(note, music.beat(BeatFraction.WHOLE))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    for degree in major:
        music.play_tone(chromatic[degree], music.beat(BeatFraction.WHOLE))
input.on_button_pressed(Button.B, on_button_pressed_b)

major: List[number] = []
chromatic: List[number] = []
chromatic = [Note.C4,
    Note.CSHARP4,
    Note.D4,
    Note.EB4,
    Note.E4,
    Note.F4,
    Note.FSHARP4,
    Note.G4,
    Note.GSHARP4,
    Note.A4,
    Note.BB4,
    Note.B4,
    Note.C5]
major = [0, 2, 4, 5, 7, 9, 11, 12]