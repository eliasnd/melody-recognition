"""
Examples of Python audio manipulation.
Last revised: 10/25/2019 by Benned H
"""

# pyaudio may work for everything, but it's a lot of code.
# wavio lets us convert NumPy <--> .wav and back

import sounddevice as sd
from scipy.io.wavfile import write
from time import sleep

def countdown(n):
	# Prints a countdown to start recording.
	print("Countdown...")
	for i in range(n,0,-1):
		print(i)
		sleep(1)

def main():
	fs = 44100  # Sample rate
	seconds = 3  # Duration of recording

	countdown(seconds)
	myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
	print("Recording for",seconds,"seconds...")
	sd.wait()  # Wait until recording is finished
	print("here")

	write('output.wav', fs, myrecording)  # Save as WAV file
	print("output.wav saved.")

if __name__ =="__main__":
	main()