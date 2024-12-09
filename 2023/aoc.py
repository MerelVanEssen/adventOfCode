# aoc.py

# ----- COMPARE ----- #

# Compare 2 lists and give back how many items are different
def checkOneDifference(list1, list2):
	differences = [
		(i, a, b)
		for i, (a, b) in enumerate(zip(list1, list2))
		if a != b
	]
	return len(differences)


# ----- TURN MAPS ----- #
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
