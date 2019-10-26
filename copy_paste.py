import numpy as np
import simpleaudio as sa

# calculate note frequencies
A_freq = 440
Csh_freq = A_freq * 2 ** (4 / 12)
E_freq = A_freq * 2 ** (7 / 12)
Gsh_freq = A_freq * 2 ** (11 / 12)

# get timesteps for each sample, T is note duration in seconds
hz = 44100
duration = 0.04 # Of each note in seconds
timesteps = duration * hz
t = 2 * np.pi * np.linspace(0, duration, timesteps, False)

# generate sine wave notes
A_note = np.sin(A_freq * t)
Csh_note = np.sin(Csh_freq * t)
E_note = np.sin(E_freq * t)
Gsh_note = np.sin(Gsh_freq * t)

# concatenate notes
audio = np.hstack((A_note, Csh_note, E_note, Gsh_note))

audio = np.hstack((audio,audio,audio,audio))

# normalize to 16-bit range
audio *= 32767 / np.max(np.abs(audio))
# convert to 16-bit data
audio = audio.astype(np.int16)

print(audio.shape)

# start playback
play_obj = sa.play_buffer(audio, 1, 2, hz)

# wait for playback to finish before exiting
play_obj.wait_done()