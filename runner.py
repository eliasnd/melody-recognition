from audio_input import recordMelody
from piano_roll import *

def identify(melody, repertoire):
	similarities = []
	encoding = encode(melody)

	for r in repertoire:
		similarities.append(compare(encoding, encode(r)))

	mostSimilar = repertoire[similarities.index(max(similarities))]
	return mostSimilar, max(similarities)

def main():

	# Happy Birthday -- Quarter note pulse
	birthday = ['C', 'D', 'C', 'F', 'E', 'E', 'C', 'D', 'C', 'G', 'F', 'F', 'C', 'C', 'A', 'F', 'E', 'D', 'A#', 'A', 'F', 'G', 'F', 'F', 'F']

	# Africa -- Toto -- Eighth note pulse
	africa = [	'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'G', 'G', 'C', 'C', 'D',
				'C', 'A', 'C', 'A', 'D', 'D', 'C', 'A', 'C', 'D', 'C', 'A', 'G', 'A', 'D', 'C']

	# US National Anthem -- Eighth note pulse
	anthem = ['G', 'E', 'C', 'C', 'E', 'E', 'G', 'G', 'C', 'C', 'C', 'C', 'E', 'D', 'C', 'C', 'E', 'E', 'F#', 'F#', 
			  'G', 'G', 'G', 'G', 'G', 'G', 'E', 'E', 'E', 'D', 'C', 'C', 'B', 'B', 'B', 'B', 'A', 'B', 'C', 'C', 'C', 'C', 
			  'G', 'G', 'E', 'E', 'C', 'C', 'C', 'C']

	#Repertoire
	repertoire = [birthday, africa, anthem]

	test = recordMelody(3)

	print("I heard " + str(test))

	song, similarity = identify(test, repertoire)

	print(repertoire.index(song))
	print("Similarity is " + str(similarity))


if __name__ =="__main__":
	main()