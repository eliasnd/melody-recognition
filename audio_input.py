"""
Examples of Python audio manipulation.
Last revised: 10/25/2019 by Benned H
"""

# wavio lets us convert NumPy <--> .wav and back

import sounddevice as sd
from scipy.io.wavfile import read, write
import aubio
import audioop
from time import sleep
from math import sqrt, floor

samplerate = 44100

def countdown(n,scale=1):
	# Prints a countdown to start recording.
	for i in range(n*scale,0,-1):
		print(i)
		sleep(1/scale)


def getPitches(src):
	samplerate = 44100 # unsure why global samplerate not working for this method. Benned please explain
	win_s = 4096 # fft size
	hop_s = 512 # hop size -- number of notes captured will be ( samplerate * seconds recorded ) / hop size

	s = aubio.source(src, samplerate, hop_s)
	samplerate = s.samplerate

	tolerance = 0.8

	pitch_o = aubio.pitch("yin", win_s, hop_s, samplerate)
	pitch_o.set_unit("midi") # we can do hz instead, doesn't really matter -- just convenient to use midi because of midi2note function
	pitch_o.set_tolerance(tolerance)

	f = aubio.digital_filter(7)
	f.set_a_weighting(samplerate)

	pitches = []
	confidences = []

	while True:
	    samples, read = s()
	    filtered_samples = f(samples)
	    pitches += [int(round(pitch_o(filtered_samples)[0]))]
	    if read < hop_s: break

	return list(map(aubio.midi2note, pitches))


def rms(arr):
	return sqrt(sum(arr**2) / len(arr))


def getMelody(src):
	samplerate, data = read(src)
	pitches = getPitches(src)
	hop_s = 1 << int((len(data) / len(pitches))).bit_length()
	melody = []

	threshold = 0.1 # volume threshold -- sounds below this are considered background noise and ignored

	for i in range(floor(len(pitches) / 10)):
		if rms(data[(i*hop_s*10):((i+1)*hop_s*10)]) < threshold:
			melody.append("R")
		else:
			notes = {}
			for j in range(10):
				if pitches[i+j] in notes:
					notes[pitches[i+j]] += 1
				else:
					notes[pitches[i+j]] = 1

			common = list(notes.keys())[0]

			for note in notes:
				if notes[note] > notes[common]:
					common = note

			if common == "C-1":
				common = "R"
			else:
				common = common[:-1]

			melody.append(common)

	return melody


def recordMelody(seconds):
	timesteps = int(seconds * samplerate)

	print("Recording in...")
	countdown(3)
	record = sd.rec(timesteps, samplerate=samplerate, channels=1)
	print("Recording for",seconds,"seconds...")
	countdown(seconds)
	
	sd.wait()  # Wait until recording is finished
	write('output.wav', samplerate, record)

	return getMelody('output.wav')

if __name__ =="__main__":
	main()