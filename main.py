def on_button_pressed_a():
    for value in pitches:
        music.play_tone(value, music.beat(BeatFraction.WHOLE))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    for value2 in scale:
        music.play_tone(pitches[value2], music.beat(BeatFraction.WHOLE))
input.on_button_pressed(Button.B, on_button_pressed_b)

scale: List[number] = []
pitches: List[number] = []
pitches = [262,
    277,
    294,
    311,
    330,
    349,
    370,
    392,
    415,
    440,
    466,
    494,
    523]
scale = [0, 2, 4, 5, 7, 9, 11, 12]