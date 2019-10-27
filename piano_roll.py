notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

def encode(melody): # Encodes a melody formatted as ['C', 'D', 'E', ...] into an array [0, 1, 2, ...]
	encoding = []

	for i in range(len(melody)):
		if melody[i] == "R": # Rests aren't in the scale, so have to check for them instead. Since this is only called once, shouldn't be an issue.
			encoding.append(-1)
		else:
			encoding.append(notes.index(melody[i]))

	return encoding

def decode(melody): # Decodes an array formatted as [0, 1, 2, ...] into a melody ['C', 'D', 'E', ...]
	decoding = []

	for i in range(len(melody)):
		if melody[i] == -1:
			decoding.append("R")
		else:
			decoding.append(notes[i])

	return decoding

def transpose(melody, s): # Transposes a melody by s half-steps
	transposed = []

	for i in range(len(melody)):
		if melody[i] == -1:
			transposed.append(-1)
		else:
			transposed.append(melody[i] + s % 12)

	return transposed

def pickScale(melody1, melody2):
	# Code here
	return

def scale(melody, f): # Scales a melody by factor f
	scaled = []

	if f % 1 == 0:
		for i in range(len(melody)):
			scaled.extend([melody[i]] * f)

	return scaled

def match(melody1, melody2): # Returns the similarity between two melodies
	# maxSimilarity = 0
	# transpose()
	# for (possible scales):
	# 	scale(possible scale)
	#	for (possible positions):
	#		move(possible position)
	#		if similarity > maxSimilarity:
	#			maxSimilarity = similarity
	return 0

