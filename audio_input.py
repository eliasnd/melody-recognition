"""
Examples of Python audio manipulation.
Last revised: 10/25/2019 by Benned H
"""

# wavio lets us convert NumPy <--> .wav and back

import sounddevice as sd
from scipy.io.wavfile import write
from time import sleep

def countdown(n):
	# Prints a countdown to start recording.
	for i in range(n,0,-1):
		print(i)
		sleep(1)

def main():
	hz = 44100  # Sample rate
	seconds = 1  # Duration of recording

	#print("Recording in...")
	#countdown(seconds)
	record = sd.rec(int(seconds * hz), samplerate=hz, channels=1)
	print("Recording for",seconds,"seconds...")
	#countdown(seconds)
	
	sd.wait()  # Wait until recording is finished
	print("Type:",type(record),"Shape",record.shape,"Max",max(record))

	#write('output.wav', hz, record)  # Save as WAV file
	#print("output.wav saved.")

if __name__ =="__main__":
	main()