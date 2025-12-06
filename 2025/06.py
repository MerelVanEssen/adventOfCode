# DAY 3: Trash Compactor

def multiplyList(lst):
	result = 1
	for x in lst:
		result = result * x
	return result

def calculate(nrs, key):
	if key == '+':
		return sum(nrs)
	elif key == '*':
		return multiplyList(nrs)
	return 0

def part1(lines):
	total = 0
	l = len(lines) - 1
	for j in range(len(lines[0])):
		nrs = []
		for i in range(l + 1):
			nr = lines[i][j]
			if lines[i][j].isdigit():
				nr = int(lines[i][j])
				nrs.append(nr)
		total += calculate(nrs, lines[l][j])
	return total

def part2(lines):
	total = 0
	l = len(lines) - 1
	nrs = []
	k = ''
	for j in range(max(len(line) for line in lines)):
		nr = ''
		ready = True
		for i in range(l + 1):
			if j < len(lines[i]):
				if lines[i][j].isdigit():
					nr += lines[i][j]
					ready = False
				elif lines[i][j] == '*' or lines[i][j] == '+':
					k = lines[i][j]
		if nr != '':
			nrs.append(nr)
		if ready:
			total += calculate([int(x) for x in nrs], k)
			nrs = []
			k = ''
	if nrs:
		total += calculate([int(x) for x in nrs], k)
	return total

filename = "input/06.txt"
print("Using input file:", filename)
f = open(filename, "r")
input = f.read()
lines  = input.split('\n')
lines2 = lines[:]
for i in range(len(lines)):
	lines[i] = lines[i].split()
print("Part 1:", part1(lines))
print("Part 2:", part2(lines2))
f.close() 
