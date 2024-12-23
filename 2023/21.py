import re
from collections import deque
from math import gcd
from functools import reduce
from collections import Counter
from aoc import turnMapBackwardsList
import heapq
from functools import cache

# hands = [[] for _ in range(7)]
# inte = [int(x) for x in line]
# field = [['.' for _ in row] for row in map]

STEPS = 26501365

input = open("input/21.txt", "r").read()
map = input.split('\n')
start = []
total = 0

# search start position
for i, line in enumerate(map):
	if 'S' in line:
		start = [i, line.index('S')]

seen = set()
deq1 = deque([start])
steps = 0
while deq1:
	deq2 = deq1.copy()
	deq1 = set()
	while deq2:
		co = deq2.popleft()
		y, x, = co

		for dy, dx in {(0,1), (1,0), (-1,0), (0,-1)}:
			ny = y + dy
			nx = x + dx

			if 0 <= ny < len(map) and 0 <= nx < len(map[0]) and map[ny][nx] != '#' and steps < STEPS:
				# if (ny, nx) in seen:
				# 	continue
				# seen.add((ny,nx))

				deq1.add((ny, nx))
	if steps == STEPS - 1:
		total = len(deq1)
	deq1 = deque(deq1)
	steps += 1

print("Part 1:", total)

