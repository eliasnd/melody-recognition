"""
Given pitch estimates for each hop, predict bucket pitches.
Benned Hedegaard, 10/26/2019
"""

import statistics as stat
import piano_roll as pr

C_key = pr.encode(['C','D','E','F','G','A','B'])
Cs_key = pr.encode(['C#','D#','F','F#','G#','A#','C'])
D_key = pr.encode(['D','E','F#','G','A','B','C#'])
Ds_key = pr.encode(['D#','F','G','G#','A#','C','D'])
E_key = pr.encode(['E','F#','G#','A','B','C#','D#'])
F_key = pr.encode(['F','G','A','A#','C','D','E'])
Fs_key = pr.encode(['F#','G#','A#','B','C#','D#','F'])
G_key = pr.encode(['G','A','B','C','D','E','F#'])
Gs_key = pr.encode(['G#','A#','C','C#','D#','F','G'])
A_key = pr.encode(['A','B','C#','D','E','F#','G#'])
As_key = pr.encode(['A#','C','D','D#','F','G','A'])
B_key = pr.encode(['B','C#','D#','E','F#','G#','A#'])

keys = [C_key,Cs_key,D_key,Ds_key,E_key,F_key,Fs_key,G_key,Gs_key,A_key,As_key,B_key]

def parseBuckets(arr):
	# arr: a list of hop pitch estimates.

	bucketSize = 3
	buckets = []

	for i in range(0,len(arr),bucketSize):
		try:
			value = stat.mode(arr[i:i+bucketSize]) # Bucket's guess
			buckets.append(value)
		except stat.StatisticsError:
			buckets.append(arr[i])

	return buckets

def quantize(buckets):
	# buckets: Get this from parseBuckets.
	if len(buckets) == 0:
		print("Error: empty list given!")
		return None

	lengths = []
	currNote = buckets[0]
	currLen = 1

	for i in range(1,len(buckets)):
		if buckets[i] == currNote:
			currLen += 1
		else:
			lengths.append(currLen)
			currNote = buckets[i]
			currLen = 1

	lengths.append(currLen)
	print(lengths)

	return lengths

def pickScale(melody1):
	# Returns possible transpositions (0, -1 , 4, etc.)
	# which make 0 the tonic of the given int-encoded melody.
	noteCounter = [0]*12 # [0,0, ...]

	for b in melody1:
		if b == -1:
			continue
		noteCounter[b] += 1

	print(noteCounter)
	
	scores = []

	for key in keys:
		key_score = 0
		for n in key: # The integer notes values to consider.
			key_score += noteCounter[n]
		scores.append(key_score)

	print(scores)

	# Now pick keys to consider, in-order
	winners = []
	top_score = max(scores)
	for i in range(top_score,0,-1):
		for k in range(len(scores)):
			if scores[k] == i:
				winners.append(k)

	return winners

def main():
	testSamples = [	'C','C','C',
					'C','C','R',
					'R','R','R',
					'F','R','R',
					'F','C','R',
					'F','R','R',
					'D','E','F']

	buckets = parseBuckets(testSamples)

	print("Buckets:",buckets)
	print("Encoded:",pr.encode(buckets))

	winners = pickScale(pr.encode(buckets))
	print(winners)
	print("Winners:",pr.decode(winners))
	#quantize(buckets)

if __name__ == "__main__":
	main()