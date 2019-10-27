from audio_input import recordMelody
from audio_output import playSequence
from piano_roll import identify

import pygame, pygame.sndarray
from time import sleep

# Happy Birthday -- Quarter note pulse
birthday = ['C', 'D', 'C', 'F', 'E', 'E', 'C', 'D', 'C', 'G', 'F', 'F', 'C', 'C', 'A', 'F', 'E', 'D', 'A#', 'A', 'F', 'G', 'F', 'F', 'F']

# Africa -- Toto -- Eighth note pulse
africa = [	'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'G', 'G', 'C', 'C', 'D',
			'C', 'A', 'C', 'A', 'D', 'D', 'C', 'A', 'C', 'D', 'C', 'A', 'G', 'A', 'D', 'C']

# US National Anthem -- Eighth note pulse
anthem = ['G', 'E', 'C', 'C', 'E', 'E', 'G', 'G', 'C', 'C', 'C', 'C', 'E', 'D', 'C', 'C', 'E', 'E', 'F#', 'F#', 
		  'G', 'G', 'G', 'G', 'G', 'G', 'E', 'E', 'E', 'D', 'C', 'C', 'B', 'B', 'B', 'B', 'A', 'B', 'C', 'C', 'C', 'C', 
		  'G', 'G', 'E', 'E', 'C', 'C', 'C', 'C']

def playRepertoire():
	print("Playing Happy Birthday...")
	playSequence(birthday)
	sleep(2)
	print("Playing Africa...")
	playSequence(africa)
	sleep(2)
	print("Playing Anthem...")
	playSequence(anthem)
	sleep(2)

def main():
	pygame.mixer.init(44100, -16,1,2048) # Allows us to play melodies.

	repertoire = [birthday, africa, anthem]
	#playRepertoire() # Play all three songs.

	test = 0
	if test:
		playSequence(
			['F', 'F', 'F', 'F', 'F', 'F', 'E', 'D#', 'D#', 'D#', 'D#', 'E', 'C#', 'E', 'E', 'F', 'F', 'E', 'C', 'C', 'C', 'C', 'D#', 'D#', 'D#', 'D#']
		, 3)
		return

	melody = recordMelody(3) # Decoded melody; pitches

	print("I heard " + str(melody))

	song, similarity = identify(melody, repertoire)

	print(repertoire.index(song))
	print("Similarity is " + str(similarity))


if __name__ =="__main__":
	main()