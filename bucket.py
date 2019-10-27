"""
Given pitch estimates for each hop, predict bucket pitches.
Benned Hedegaard, 10/26/2019
"""

import statistics as stat

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

	print(buckets)
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

def main():
	testSamples = [	'C','C','C',
					'C','C','R',
					'R','R','R',
					'F','R','R',
					'F','C','R',
					'F','R','R',
					'D','E','F']

	buckets = parseBuckets(testSamples)
	quantize(buckets)

if __name__ == "__main__":
	main()