notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"] # Lots of time saved if we can hash from notes to numbers

def noteDist(i1, i2): # Pass indices to avoid searching multiple times
	innerDist = abs(i1 - i2)
	outerDist = min(i1, i2) + len(notes) - max(i1, i2) # Distance wrapping around
	return min(innerDist, outerDist)

def reduce(melody):
	reduced = []

	started = False

	for i in range(len(melody)):
		if not started:
			if melody[i] != 'R':
				started = True
				reduced.append(melody[i])
		else:
			if melody[i] != reduced[len(reduced)-1]:
				reduced.append(melody[i])

	if reduced[len(reduced)-1] == "R":
		reduced = reduced[:-1]

	return reduced

def transpose(melody, steps):
	transposed = melody.copy()

	for i in range(len(melody)):
		if melody[i] != "R":
			note = melody[i]
			transposed[i] = notes[(notes.index(note) + steps) % len(notes)]

	return transposed

def commonNotes(m1, m2):
	maxSimilarity = 0

	for i in range(len(notes)):
		similarity = 0
		t1 = transpose(m1, i)

		for n in range(min(len(m1), len(m2))):
			if t1[n] == m2[n]:
				similarity += 1

			# if (len(m1) - n + similarity) / len(m1) < maxSimilarity: # Allows short-circuit evaluation on long melodies
				# break

		similarity /= len(m1)
		if similarity > maxSimilarity:
			maxSimilarity = similarity

	return maxSimilarity

def closeNotes(m1, m2):
	# To start, I'm assuming the melodies are same length and time signature

	maxSimilarity = 0

	for i in range(len(notes)):
		similarity = 0
		t1 = transpose(m1, i)

		for n in range(len(m1)):
			if t1[n] == m2[n]:
				similarity += 1
			else:
				similarity += 1 - (noteDist(notes.index(t1[n]), notes.index(m2[n])) & 3) / 3 # Distances of >3 half-steps aren't considered similar

			# if (len(m1) - n + similarity) / len(m1) < maxSimilarity: # Allows short-circuit evaluation on long melodies
				# break

		similarity /= len(m1)
		if similarity > maxSimilarity:
			maxSimilarity = similarity

	return maxSimilarity

def similarity(m1, m2):
	# To start, I'm assuming the melodies are same length and time signature

	maxSimilarity = 0

	for i in range(len(notes)):
		similarity = 0
		t1 = transpose(m1, i)

		for n in range(len(m1)):
			if t1[n] == m2[n]:
				similarity += 1
			else:
				similarity += 1 - (noteDist(notes.index(t1[n]), notes.index(m2[n])) & 3) / 3 # Distances of >3 half-steps aren't considered similar

			# if (len(m1) - n + similarity) / len(m1) < maxSimilarity: # Allows short-circuit evaluation on long melodies
				# break

		similarity /= len(m1)
		if similarity > maxSimilarity:
			maxSimilarity = similarity

	return maxSimilarity