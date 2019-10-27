"""
Examples of Python audio manipulation.
Last revised: 10/25/2019 by Benned H
"""

# wavio lets us convert NumPy <--> .wav and back

import sounddevice as sd
from scipy.io.wavfile import read, write
import os
import aubio
from time import sleep
from math import sqrt, floor
import statistics as stat
import numpy as np

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
	    #filtered_samples = f(samples)
	    #pitches += [int(round(pitch_o(filtered_samples)[0]))]
	    pitches.append(int(round(pitch_o(samples)[0])))
	    confidences.append(pitch_o.get_confidence())
	    if read < hop_s: break

	for i in range(len(pitches)):
		if pitches[i] > 126:
			pitches[i] = 0
	return list(map(aubio.midi2note, pitches)), confidences


def rms(arr):
	return sqrt(sum(arr**2) / len(arr))

def getMelody(src):
	samplerate, data = read(src)
	pitches, confidences = getPitches(src)
	hop_s = 1 << int((len(data) / len(pitches))).bit_length()
	melody = []

	# volume threshold -- sounds below this are considered background noise and ignored
	# Loud background - 0.1
	threshold = 0.00

	# Now parse into buckets
	bucketSize = 40
	buckets = []

	# First clean octaves and detected rests.
	for i in range(len(pitches)):
		if pitches[i] == "C-1":
			pitches[i] = "R"
		else:
			pitches[i] = pitches[i][:-1]
	
	# Then threshold quiet rests, bucket results.
	for i in range(0,len(pitches),bucketSize):
		if rms(data[i:i+bucketSize]) < threshold:
			buckets.append("R")
		else:
			try:
				value = stat.mode(pitches[i:i+bucketSize]) # Bucket's guess
				buckets.append(value)
			except stat.StatisticsError:
				buckets.append(pitches[i])

	# Now, melody has thresholded buckets.

	return buckets, confidences

def recordMelody(seconds):
	timesteps = int(seconds * samplerate)

	print("Recording in...")
	countdown(3)
	record = sd.rec(timesteps, samplerate=samplerate, channels=1)
	print("Recording for",seconds,"seconds...")
	countdown(seconds)
	
	sd.wait()  # Wait until recording is finished
	write('output.wav', samplerate, record)

	melody, confidences = getMelody('output.wav')
	os.remove('output.wav')
	return melody, confidences
