from collections import Counter

with open("input/06.txt", "r") as f:
	rawInput = f.read()

streams = rawInput.split('\n')

def findMarker(stream, amount):
	for i in range(len(stream) - amount):
		substream = stream[i:i + amount]
		counter = Counter(substream)
		if all(x == 1 for x in counter.values()):
			return i + amount

total = 0
total2 = 0
for stream in streams:
	total += findMarker(stream, 4)
	total2 += findMarker(stream, 14)

print("Part 1:", total)
print("Part 2:", total2)