"""
Examples of Python audio manipulation.
Last revised: 10/25/2019 by Benned H
"""

# wavio lets us convert NumPy <--> .wav and back

import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
from time import sleep
import matplotlib.pyplot as plt

def countdown(n,scale=1):
	# Prints a countdown to start recording.
	for i in range(n*scale,0,-1):
		print(i)
		sleep(1/scale)

def parsePitch(arr,steps):
	pass

def main():
	hz = 44100  # Sample rate
	seconds = 1 # Duration of recording
	timesteps = int(seconds * hz)

	print("Recording in...")
	countdown(1,10)
	record = sd.rec(timesteps, samplerate=hz, channels=1)
	print("Recording for",seconds,"seconds...")
	countdown(seconds)
	
	sd.wait()  # Wait until recording is finished
	print("Type:",type(record),"Shape",record.shape,"Max",max(record))

	plt.plot(np.fft.fft(record))
	plt.show()

	#np.savetxt("recording.txt", record)
	#write('output.wav', hz, record)  # Save as WAV file
	#print("output.wav saved.")

if __name__ =="__main__":
	main()