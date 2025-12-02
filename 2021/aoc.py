# aoc.py

def countSymbolInMap(map, symbol):
	total = 0
	for line in map:
		total += line.count(symbol)
	return total

def createMap(lines: map):
	map = []
	for line in lines:
		map.append(line)
	return map

### TURNING MAPS ###

# Turn map 90 degrees forwards
def turnMap(map):
	newMap = ["" for _ in range(len(map[0]))]
	for line in map:
		for i, char in enumerate(line):
			newMap[i] = newMap[i] + char
	return newMap 

# Turn map 90 degrees forwards to a n*n List
def turnMapList(map):
	newMap = [[] for _ in range(len(map[0]))]
	for line in map:
		for i, char in enumerate(line):
			newMap[i] = newMap[i] + char
	return newMap 

# Turn map 90 degrees backwards
def turnMapBackwards(map):
	newMap = ["" for _ in range(len(map[0]))]
	for line in map:
		for i, char in enumerate(line):
			newMap[i].insert(0, char)
	return newMap

# Turn map 90 degrees backwards to a n*n List
def turnMapBackwardsList(map):
	newMap = [[] for _ in range(len(map[0]))]
	for line in map:
		for i, char in enumerate(line):
			newMap[i].insert(0, char)
	return newMap

def bitsToDecimal(bits):
	total = 0
	for i, bit in enumerate(reversed(bits)):
		if bit == '1':
			total += 2**i
	return total

def decimalToBits(decimal, length):
	bits = ''
	while decimal > 0:
		bits = str(decimal % 2) + bits
		decimal = decimal // 2
	while len(bits) < length:
		bits = '0' + bits
	return bits