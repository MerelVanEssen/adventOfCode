import re
from collections import deque
import math
from functools import reduce
from collections import Counter
import heapq
import functools

# self.hands = [[] for _ in range(7)]
# inte = [int(x) for x in line]
# self.field = [['.' for _ in row] for row in self.map]

class Solution:
	def __init__(self, input):
		self.map = input.split('\n')
		self.start = self.end = 0
		self.cross = [[float('inf') for _ in line] for line in self.map]
		self.shortest = float('inf')
		for i, line in enumerate(self.map):
			if 'S' in line:
				j = line.index('S')
				self.start = (i, j)
			if 'E' in line:
				j = line.index('E')
				self.end = (i, j)

	def backtrack(self):
		deq = [(0, self.end[0], self.end[1], -1, -1)]

		while deq:
			cost, y, x, backY, backX = heapq.heappop(deq)
			self.cross[y][x] = cost

			if self.map[y][x] == 'S':
				if cost < self.shortest:
					self.shortest = cost
				continue

			for dY, dX in [(0, 1), (1, 0), (0,-1), (-1,0)]:
				newY = dY + y
				newX = dX + x
				if (newY == backY and newX == backX) or self.map[newY][newX] == '#':
					continue
				heapq.heappush(deq, (cost + 1, newY, newX, y, x))

	def part1(self):
		self.backtrack()
		deq = [(0, self.start[0], self.start[1], False, set())] # cost, y, x, cheat used
		p1 = None
		shortest = self.shortest
		savePaths = []

		while deq:
			cost, y, x, usedCheat, path = heapq.heappop(deq)

			path.add((y, x, usedCheat))
			# pathcost = abs(y - self.end[0]) + abs(x - self.end[1])
			# if cost + pathcost > shortest - 100:
			# 	continue

			if self.map[y][x] == 'E':
				if usedCheat == True:
					savePaths.append(len(path))
				continue

			for dY, dX in [(0, 1), (1, 0), (0,-1), (-1,0)]:
				newY = dY + y
				newX = dX + x

				if 0 <= newY < len(self.map) and 0 <= newX < len(self.map[0]):
					if self.map[newY][newX] == '#' and usedCheat == False and (newY, newX, True) not in path:
						if 0 <= newY + dY < len(self.map) and 0 <= newX + dX < len(self.map[0]):
							if (newY, newX, True) not in path and self.map[newY + dY][newX + dX] == '.' or self.map[newY + dY][newX + dX] == 'E':
								savePaths.append(len(path) + 2 + self.cross[newY + dY][newX + dX])
					if self.map[newY][newX] != '#' and (newY, newX, usedCheat) not in path:
						heapq.heappush(deq, (cost + 1, newY, newX, usedCheat, path.copy()))

		total = 0
		for item in savePaths:
			if shortest - item + 1 >= 100:
				total += 1
		# print(saveTime)
		return (total)


	def part2(self):
		total = 0
		
		return total

def main():
	# CHANGE INPUTFILE
	input = open("input.txt", "r").read()

	sol = Solution(input)
	print("Part 1:", sol.part1())
	print("Part 2:", sol.part2())

if __name__ == "__main__":
	main()
