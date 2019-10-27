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

def parseBuckets(arr):
	# arr: a list of hop pitch estimates.

	bucketSize = 3
	buckets = []

	for i in range(0,len(arr),bucketSize):
		try:
			value = stat.mode(arr[i:i+bucketSize]) # Bucket's guess
			buckets.append(value)
		except stat.StatisticsError:
			buckets.append(arr[i])

	return buckets

def getMelody(src):
	samplerate, data = read(src)
	pitches = getPitches(src)
	print("Piches", pitches)
	hop_s = 1 << int((len(data) / len(pitches))).bit_length()
	melody = []

	# volume threshold -- sounds below this are considered background noise and ignored
	# Loud background - 0.1
	threshold = 0.00

	for i in range(len(pitches)):
		if rms(data[i:i+1]) < threshold:
			melody.append("R")
		if pitches[i] == "C-1":
			melody.append("R")
		else:
			melody.append(pitches[i][:-1])

	# Now, melody has thresholded pitches.
	buckets = parseBuckets(melody)
	print("Buckets", buckets)

	return buckets

def recordMelody(seconds):
	timesteps = int(seconds * samplerate)

	print("Recording in...")
	countdown(3)
	record = sd.rec(timesteps, samplerate=samplerate, channels=1)
	print("Recording for",seconds,"seconds...")
	countdown(seconds)
	
	sd.wait()  # Wait until recording is finished
	write('output.wav', samplerate, record)

	melody = getMelody('output.wav')
	os.remove('output.wav')
	return melody
