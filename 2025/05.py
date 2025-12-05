# DAY 3: Cafeteria ingredient freshness

def part1(pairs, ingredients):
	total = 0
	for ingredient in ingredients:
		fresh = False
		for low, high in pairs:
			if low <= int(ingredient) <= high:
				fresh = True
				break
		if fresh:
			total += 1
	return total

def createNewPairs(pairs):
	newpairs = set()
	pairs = list(pairs)

	for i in range(len(pairs)):
		low1, high1 = pairs[i]
		merge = False
		for j in range(len(pairs)):
			low2, high2 = pairs[j]
			if i == j or high1 < low2 or high2 < low1:
				continue
			merge = True
			newpairs.add((min(low1, low2), max(high1, high2)))
		if not merge:
			newpairs.add((low1, high1))
	return newpairs

def part2(pairs):
	while True:
		newPairs = createNewPairs(pairs)
		if newPairs == pairs:
			break
		pairs = newPairs
	total = 0
	for low, high in pairs:
		total += high - low + 1
	return total

filename = "input/05.txt"
print("Using input file:", filename)
f = open(filename, "r")
input = f.read()
ranges, ingredients  = input.split('\n\n')
ranges = ranges.split('\n')
pairs = [(int(a), int(b)) for a, b in (line.split('-') for line in ranges)]
print("Part 1:", part1(pairs[:], ingredients.split('\n')))
print("Part 2:", part2(set(pairs)))
f.close() 