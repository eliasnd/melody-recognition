"""
Generate random sound using NumPy.
Benned Hedegaard
"""

import numpy as np
import simpleaudio as sa

# get timesteps for each sample, T is note duration in seconds
hz = 44100
duration = 3 # Of each note
timesteps = int(duration * hz)

r = np.random.uniform(-5,5,(timesteps,1))

# normalize to 16-bit range
audio = r * 32767 / np.max(np.abs(r))
# convert to 16-bit data
audio = audio.astype(np.int16)

print(audio.shape)

# start playback
play_obj = sa.play_buffer(audio, 1, 2, hz)

# wait for playback to finish before exiting
play_obj.wait_done()