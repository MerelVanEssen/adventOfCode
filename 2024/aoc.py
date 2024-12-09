# aoc.py



def countSymbolInMap(map, symbol):
	total = 0
	for line in map:
		total += line.count(symbol)
	return total

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
