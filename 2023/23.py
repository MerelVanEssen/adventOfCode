import re
from copy import deepcopy
from collections import defaultdict

input = open("input/23.txt", "r").read()

map = input.split('\n')

dir = ((0,1),(1,0),(-1,0),(0,-1))
arrows = ">v^<"

# Part 1
deq = []
deq.append([0,1,0, set(), (-1,-1), False])
longestPath = 0

while deq:
	y, x, cost, seen, lastDir, newSet = deq.pop()
	if (y,x) == (len(map) - 1, len(map[0]) - 2):
		longestPath = max(longestPath, cost)
		continue

	if newSet:
		seen = seen | {(y, x)}

	newWays = []
	for i, d in enumerate(dir):
		if d == (-lastDir[0], -lastDir[1]):
			continue
		newY = y + d[0]
		newX = x + d[1]
		if (newY, newX) in seen:
			continue
		if map[newY][newX] == '.':
			newWays.append([newY, newX, cost + 1, seen, d, False])
		elif map[newY][newX] != '#':
			if map[newY][newX] == arrows[i]:
				newWays.append([newY + d[0], newX + d[1], cost + 2, seen, d, False])
	for way in newWays:
		if len(newWays) > 1:
			way[5] = True
		deq.append(way)

# Part 2
deq = []
deq.append([0,1,0, set(), (-1,-1), False])
nodes = []
nodes.append((0,1))
nodes.append((len(map) - 1, len(map[0]) - 2))

for y, line in enumerate(map):
	if y == 0 or y == len(map) - 1:
		continue
	for x, place in enumerate(line):
		if x == 0 or x == len(map[0]) - 1 or map[y][x] == '#':
			continue
		amount = 0
		for d in dir:
			if map[y + d[0]][x + d[1]] != "#":
				amount += 1
		if amount > 2:
			nodes.append((y, x))

dic = defaultdict(set)

def	findWay(y, x, nodes, lastStep):
	steps = 1
	while (y,x) not in nodes:
		for d in dir:
			if (map[y + d[0]][x + d[1]] != '#' and (y + d[0], x + d[1]) != lastStep):
				lastStep = (y, x)
				y += d[0]
				x += d[1]
				steps += 1
				break
	return y, x, steps

for y, x in nodes:
	for d in dir:
		newY = y + d[0]
		newX = x + d[1]
		if not (0 <= newY < len(map) and 0 <= newX < len(map[0])) or map[newY][newX] == '#':
			continue
		endY, endX, steps = findWay(newY, newX, nodes, (y,x))
		dic[(y,x)].add((endY,endX,steps))

longestPath2 = 0

def	calculateLongestWay(node, lastNode, seen, total):
	global longestPath2

	if node == (len(map) - 1, len(map[0]) - 2):
		longestPath2 = max(longestPath2, total)
		return

	nodes = dic[node]
	for y, x, cost in nodes:
		if [y,x] not in seen:
			newSeen = seen + [[y,x]]
			calculateLongestWay((y,x), node, newSeen, total + cost)

node = (0,1)
start = list()
start.append([0,1])
calculateLongestWay((0,1), (-1,-1), start, 0)

print("Part 1:", longestPath)
print("Part 2:", longestPath2)
