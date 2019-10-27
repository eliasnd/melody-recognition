from audio_input import recordMelody
from audio_output import playSequence
from comparison import identify

import pygame, pygame.sndarray
from time import sleep

# Happy Birthday -- Quarter note pulse
birthday = ['C', 'D', 'C', 'F', 'E', 'E', 'C', 'D', 'C', 'G', 'F', 'F', 'C', 'C', 'A', 'F', 'E', 'D', 'A#', 'A', 'F', 'G', 'F', 'F', 'F']

# Africa -- Toto -- Eighth note pulse
aha = ['F#', 'F#', 'D', 'B', 'R', 'B', 'R', 'E', 'R', 'E', 'R', 'E', 'G#', 'G#', 'A', 'B', 'A', 'A', 'A', 'E', 'R', 'D', 'R', 'F#', 'R', 'F#',
	   'R', 'F#', 'E', 'E', 'F#', 'E']

# US National Anthem -- Eighth note pulse
anthem = ['G', 'E', 'C', 'C', 'E', 'E', 'G', 'G', 'C', 'C', 'C', 'C', 'E', 'D', 'C', 'C', 'E', 'E', 'F#', 'F#', 
		  'G', 'G', 'G', 'G', 'G', 'G', 'E', 'E', 'E', 'D', 'C', 'C', 'B', 'B', 'B', 'B', 'A', 'B', 'C', 'C', 'C', 'C', 
		  'G', 'G', 'E', 'E', 'C', 'C', 'C', 'C']

def playRepertoire():
	print("Playing Happy Birthday...")
	playSequence(birthday)
	sleep(2)
	print("Playing Africa...")
	playSequence(aha)
	sleep(2)
	print("Playing Anthem...")
	playSequence(anthem)
	sleep(2)

def main():
	pygame.mixer.init(44100, -16,1,2048) # Allows us to play melodies.

	repertoire = [birthday, aha, anthem]
	#playRepertoire() # Play all three songs.

	test = 0
	if test:
		playSequence(
		['C', 'A#', 'F#', 'D#', 'G#', 'G#', 'C', 'C#', 'D#', 'C#', 'C#']
		, 3)
		return

	melody, confidences = recordMelody(5) # Decoded melody; pitches

	playSequence(melody, 3)

	print("I heard " + str(melody))

	song, similarities = identify(melody, confidences, repertoire)

	print(repertoire.index(song))
	print("Similarities are", similarities)


if __name__ =="__main__":
	main()