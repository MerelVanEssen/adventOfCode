import re
import copy
from collections import deque
import copy

with open("input/12.txt", "r") as f:
	input = f.read()

map = input.split('\n')

de = deque()
de2 = deque()

for y, line in enumerate(map):
	if 'S' in line:
		de.append([y, line.index('S'), 0, set()])
	for x, item in enumerate(line):
		if map[y][x] == 'a':
			de2.append([y, x, 0, set()])

dir = ((0,1), (1,0), (0,-1), (-1,0))

def searchWay(de):
	lowestCost = float('inf')

	while de:
		y, x, cost, seen = de.popleft()

		if map[y][x] == 'E':
			lowestCost = min(lowestCost, cost)
			continue

		if (y, x) in seen or cost > lowestCost:
			continue

		seen.add((y, x))

		for d in dir:
			newY, newX = y + d[0], x + d[1]
			if 0 <= newY < len(map) and 0 <= newX < len(map[0]):
				if map[newY][newX] == 'E' and map[y][x] != 'z':
					continue
				elif ord(map[newY][newX]) > ord(map[y][x]) + 1 and map[y][x] != 'S':
					continue
				de.append([newY, newX, cost + 1, seen])
	return (lowestCost)

print("Total part 1: ", searchWay(de))
print("Total part 2: ", searchWay(de2))


