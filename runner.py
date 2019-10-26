from audio_input import recordMelody
from piano_roll import *

def main():
	melody = recordMelody(3)
	print(reduce(melody))

	odetojoy = ['E', 'E', 'F', 'G']
	print(reduce(odetojoy))

	print(similarity(reduce(melody), reduce(odetojoy)))

if __name__ =="__main__":
	main()