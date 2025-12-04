# Advent of Code 2021 Day 6: Lightfishes

def result(amount: int, fishes: list):
	for _ in range(amount):
		if fishes[0] > 0:
			fishes[7] += fishes[0]
			fishes[9] += fishes[0]
			fishes[0] = 0
		for i in range(len(fishes)):
			if i < 9:
				fishes[i] = fishes[i + 1]
		fishes[9] = 0
	return sum(fishes)

filename = "input/06.txt"
print("Using input file:", filename)
f = open(filename, "r")
input = f.read()
lines  = input.split(',')
lines = [int(nr) for nr in lines]
fishes = [0] * 10
for nr in lines:
	fishes[nr] += 1
print("Part 1:", result(80, fishes[:]))
print("Part 2:", result(256, fishes))
f.close() 