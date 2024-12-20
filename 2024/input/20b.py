import re
from collections import deque
import math
from functools import reduce
from collections import Counter
import heapq
import functools
from collections import defaultdict

# self.hands = [[] for _ in range(7)]
# inte = [int(x) for x in line]
# self.field = [['.' for _ in row] for row in self.map]

class Solution:
	def __init__(self, input):
		self.map = input.split('\n')
		self.start = self.end = 0
		self.cross = [[float('inf') for _ in line] for line in self.map]
		self.cross2 = [[float('inf') for _ in line] for line in self.map]
		self.shortest = float('inf')
		self.points = []
		for i, line in enumerate(self.map):
			if 'S' in line:
				j = line.index('S')
				self.start = (i, j)
			if 'E' in line:
				j = line.index('E')
				self.end = (i, j)

	def backtrack2(self): #start - > end
		deq = [(0, self.start[0], self.start[1], -1, -1)]
		while deq:
			cost, y, x, backY, backX = heapq.heappop(deq)
			self.cross2[y][x] = cost
			if self.map[y][x] == 'E':
				continue

			for dY, dX in [(0, 1), (1, 0), (0,-1), (-1,0)]:
				newY = dY + y
				newX = dX + x
				if (newY == backY and newX == backX) or self.map[newY][newX] == '#':
					continue
				heapq.heappush(deq, (cost + 1, newY, newX, y, x))

	def backtrack(self): # end - > start
		deq = [(0, self.end[0], self.end[1], -1, -1)]

		while deq:
			cost, y, x, backY, backX = heapq.heappop(deq)
			self.cross[y][x] = cost
			# if cost <= 84:
			self.points.append((y,x,cost))
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
		self.backtrack2()
		print(self.shortest)
		deq = self.points # cost, y, x, cheat used
		shortest = self.shortest
		savePaths = defaultdict(int)
		while deq:
			Y, X, Cost = heapq.heappop(deq)
			for dY, dX in [(0, 1), (1, 0), (0,-1), (-1,0)]:
				nY = dY + Y
				nX = dX + X
				if self.map[nY][nX] != '#':
					continue
				searchY = max(0, Y - 20)
				searchX = max(0, X - 20)
				searchYmax = min(len(self.map) - 1, Y + 20)
				searchXmax = min(len(self.map[0]) - 1, X + 20)
				found = set()
				while searchY < searchYmax + 1:
					sX = searchX
					while sX < searchXmax - 1:
						distance = abs(nY - searchY) + abs(nX - sX)
						if distance <= 20 and self.map[searchY][sX] != '#' and (searchY, sX) != (Y,X):
							# print(Y, X, Cost, distance, self.cross[searchY][sX], Cost+ distance + self.cross[searchY][sX])
							found.add((Y, X, searchY, sX, distance + self.cross[searchY][sX] + 1))
						sX += 1
					searchY += 1
		for y1, x1, y, x, cost in found:
			savePaths[cost + self.cross2[Y][X]] += 1
		total = 0
		for key, value in savePaths.items():
			if shortest - key + 1 >= 100:
				total += value

		return (total)


	def part2(self):
		total = 0
		
		return total

def main():
	# CHANGE INPUTFILE
	input = open("input.txt", "r").read()

	sol = Solution(input)
	print("Part 1:", sol.part1(), 988931)
	print("Part 2:", sol.part2())

if __name__ == "__main__":
	main()