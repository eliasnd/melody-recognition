"""
-- function: playSequence(sequenceArr) -- plays sounds from note arrays (etc. ["C", "D", "R", "F#"] will play C, D, rest, F#, each for 0.5 second)

"""

import scipy.signal
import pygame, pygame.sndarray
import numpy as np
from time import sleep

sample_rate = 44100
def play_for(sample_wave, ms):
    #Play the given NumPy array, as a sound, for ms milliseconds.
    sound = pygame.sndarray.make_sound(sample_wave)
    sound.play(-1)
    pygame.time.delay(ms)
    sound.stop()

def sine_wave(hz, peak, n_samples=sample_rate):
    length = sample_rate / float(hz)
    omega = np.pi * 2 / length
    xvalues = np.arange(int(length)) * omega
    onecycle = peak * np.sin(xvalues)
    return np.resize(onecycle, (n_samples,)).astype(np.int16)

def playSequence(sequence, duration):
    # duration is in seconds

    # Calculate length of each note given duration
    total_ms = duration * 1000
    ms = int(total_ms / len(sequence))

    freqDict = {
    "C": 523.25,
    "C#": 554.37,
    "D": 587.33,
    "D#": 622.25,
    "E": 659.25,
    "F": 698.46,
    "F#": 739.99,
    "G": 783.99,
    "G#": 830.61,
    "A": 880.00,
    "A#": 932.33,
    "B": 987.77,
    }
    notes = []
    for i in range(len(sequence)): 
        if sequence[i] == "R":
            notes.append(0)
        else:
            notes.append(freqDict.get(sequence[i]))
    for note in notes:
        if note != 0:
            play_for(sine_wave(note, 4096), ms)
        else:
            sleep(ms/1000)