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
			decoding.append(notes[melody[i]])

	return decoding

def transpose(melody, s): # Transposes a melody by s half-steps
	transposed = []

	for i in range(len(melody)):
		if melody[i] == -1:
			transposed.append(-1)
		else:
			transposed.append((melody[i] + s) % 12)

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

def match(melody1, melody2): # Returns the similarity of two melodies of equal length
	similarity = 0

	for n in range(len(melody1)): # Compares each note in the melodies
		if melody1[n] == melody2[n]:
			similarity += 1
		elif melody1[n] != -1:
			diff = min(abs(melody1[n] - melody2[n]), min(melody1[n], melody2[n]) + 12 - max(melody1[n], melody2[n])) # Computes smallest distance between notes, returns 0 if > 3 half-steps
			sqrDiff = 1 / (1+diff**2)
			similarity += sqrDiff;

	similarity /= len(melody1) # Normalizes by dividing by length of melody
	return similarity


def compare(melody1, melody2): # Returns the similarity of two melodies of variable length -- second melody must be longer
	mostSimilar = melody1
	bestMatch = melody2
	maxSimilarity = 0

	for t in range(11): # Right now, just try every possible transposition
		t1 = transpose(melody1, t)
		for s in range(1, 4): # Try scaling up to 4x
			s1 = scale(t1, s)
			for p in range(len(melody2) - len(s1)): # p is left side of s1, so at last iteration right sides of melodies will align
				similarity = match(s1, melody2[p:p+len(s1)]) # Match first melody with excerpt of second melody
				if similarity > maxSimilarity:
					maxSimilarity = similarity
					mostSimilar = s1
					bestMatch = melody2[p:p+len(s1)]

	print("Most similar is")
	print(decode(mostSimilar))
	print("Best match is")
	print(decode(bestMatch))
	return maxSimilarity

def identify(melody, repertoire):
	similarities = []
	encoding = encode(melody)

	for r in repertoire:
		similarities.append(compare(encoding, encode(r)))

	mostSimilar = repertoire[similarities.index(max(similarities))]
	return mostSimilar, similarities
