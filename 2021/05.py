# Advent of Code 2021 Day 5: Coordinates

from collections import defaultdict
import re

def getStartAndEnd(nr1, nr2):
	if nr1 < nr2:
		return nr1, nr2
	return nr2, nr1

def result(lines):
	d = defaultdict(int)
	d2 = defaultdict(int)

	for x1, y1, x2, y2 in lines:
		if x1 == x2:
			y, y_end = getStartAndEnd(int(y1), int(y2)) 
			while y <= y_end:
				d[x1 + ',' + str(y)] += 1
				d2[x1 + ',' + str(y)] += 1
				y += 1
		elif y1 == y2:
			x, x_end = getStartAndEnd(int(x1), int(x2))
			while x <= x_end:
				d[str(x) + ',' + y1] += 1
				d2[str(x) + ',' + y1] += 1
				x += 1
		elif abs(int(x1) - int(x2)) == abs(int(y1) - int(y2)):
			x, x_end = getStartAndEnd(int(x1), int(x2))
			y = int(y1) if x == int(x1) else int(y2)
			y_end = int(y2) if x == int(x1) else int(y1)
			while x <= x_end:
				d2[str(x) + ',' + str(y)] += 1
				x += 1
				if y <= y_end:
					y += 1
				else:
					y -= 1
	# part 1
	total = 0
	for key in d:
		if d[key] >= 2: total += 1
	# part 2
	total2 = 0
	for key in d2:
		if d2[key] >= 2: total2 += 1
	return total, total2

filename = "input/05.txt"
print("Using input file:", filename)
f = open(filename, "r")
input = f.read()
lines = [re.findall(r"\d+"	, line) for line in input.split('\n')]
print("Part 1:", result(lines))
f.close() 
