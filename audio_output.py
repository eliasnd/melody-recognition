import aubio

def playSequence(sequence):
    for note in sequence:
        if note == "C" or note == "D" or note == "E" or note == "F" or note == "G" or note == "A" or note == "B":
            note += "4"
        if note == "C#" or note == "D#" or note == "E#" or note == "F#" or note == "G#" or note == "A#" or note == "B#":
            note += "4"
        if note == "R":
            note = "C-1"