"""
Examples of Python audio manipulation.
Last revised: 10/25/2019 by Benned H
"""

# wavio lets us convert NumPy <--> .wav and back

import sounddevice as sd
from scipy.io.wavfile import write
from scipy.fftpack import fft, fftfreq
from time import sleep
import matplotlib.pyplot as plt

def countdown(n,scale=1):
	# Prints a countdown to start recording.
	for i in range(n*scale,0,-1):
		print(i)
		sleep(1/scale)

def parsePitch(arr,steps):
	pass

def dominantFreq(wave, rate):
	fft_out = fft(wave)
	freqs = fftfreq(len(wave)) * rate
	return freqs[np.argmax(fft_out)]

def main():
	hz = 44100  # Sample rate
	seconds = 1 # Duration of recording
	timesteps = int(seconds * hz)

	#print("Recording in...")
	#countdown(1,10)
	record = sd.rec(timesteps, samplerate=hz, channels=1)
	print("Recording for",seconds,"seconds...")
	countdown(seconds)
	
	sd.wait()  # Wait until recording is finished
	print("Type:",type(record),"Shape",record.shape,"Max",max(record))

	x = np.linspace(0.0, seconds, timesteps)
	y = np.sin(10000*2*np.pi*x) + np.sin(5000*2*np.pi*x)

	print(dominantFreq(y, 1))

	plt.figure()
	plt.subplot(211)
	plt.plot(range(len(y)), y)
	plt.subplot(212)
	plt.plot(fftfreq(len(y)), fft(y))
	plt.show()

if __name__ =="__main__":
	main()