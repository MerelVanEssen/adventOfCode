import re
from collections import deque
from math import gcd
from functools import reduce
from collections import Counter
from aoc import turnMapBackwardsList
from functools import cache
import heapq

# self.hands = [[] for _ in range(7)]
# inte = [int(x) for x in line]
# self.field = [['.' for _ in row] for row in self.map]

class Solution:
	def __init__(self, input):
		self.map = input.split('\n')
		self.dir = [[0,1], [1,0], [0,-1], [-1,0]]
		self.way = [[ x for x in line] for line in self.map]
		self.grid = [[float('inf') for _ in range(len(self.map[0]))] for _ in range(len(self.map))]
		self.gridPath = [[set() for _ in range(len(self.map[0]))] for _ in range(len(self.map))]
		self.steps = 0
		self.turn = 0
		for i, line in enumerate(self.map):
			if 'S' in line:
				index = line.index("S")
				self.start = [i, index]
			if 'E' in line:
				index = line.index("E")
				self.end = [i, index]
		self.path = set()
		self.visited = set()

	def part1(self):
		deq = []
		visited = set()
		heapq.heappush(deq, (1, self.start[0], self.start[1], 0, set())) # cost, y, x, dir down
		visited.add((self.start[0], self.start[1]))
		self.grid[0][0] = 0

		while deq:
			cost, y, x, direction, path = heapq.heappop(deq)

			path.add((y, x))

			if [y,x] == self.end:
				self.visited.update(path)
				return cost - 1
			
			for i, d in enumerate(self.dir):
				newY = y + d[0]
				newX = x + d[1]

				if not (0 <= newY < len(self.map) and 0 <= newX < len(self.map[0])) or self.map[newY][newX] == '#':
					continue

				if (newY, newX) in visited:
					continue

				visited.add((newY, newX))
				
				if i == direction:
					Newcost = cost + 1
				elif abs(direction - i)  == 1 or (direction == 0 and i == 3) or (direction == 3 and i == 0) :
					Newcost = cost + 1001
				else:
					Newcost = cost + 2001
				self.grid[newY][newX] = Newcost
				copyPath = path.copy()
				heapq.heappush(deq, (Newcost, newY, newX, i, copyPath))
		return (0)

	def part2(self):
		deq = []
		heapq.heappush(deq, (0, self.start[0], self.start[1], 0)) # cost, y, x, dir down
		fastestWay = float('inf')
		print(len(self.visited))
		while deq:
			cost, y, x, direction = heapq.heappop(deq)
		
			if (y, x) in self.visited and cost == self.grid[y][x]:
				self.visited.update(self.gridPath[y][x])

			# self.grid[y][x] = cost

			if [y,x] == self.end:
				# if cost = fastestWay:
				# 	fastestWay = cost
				# 	self.visited.update(self.gridPath[y][x])
				continue
			
			for i, d in enumerate(self.dir):
				newY = y + d[0]
				newX = x + d[1]
				if not (0 <= newY < len(self.map) and 0 <= newX < len(self.map[0])) or self.map[newY][newX] == '#':
					continue

				if i == direction:
					Newcost = cost + 1
				elif abs(direction - i)  == 1 or (direction == 0 and i == 3) or (direction == 3 and i == 0) :
					Newcost = cost + 1001
				else:
					Newcost = cost + 2001

				if (newY, newX) in self.gridPath[newY][newX]:
					continue

				self.gridPath[newY][newX].add((newY, newX))
				
				heapq.heappush(deq, (Newcost, newY, newX, i))
		
		total = 0
		for y, x in self.visited:
			self.way[y][x] = '$'
		for line in self.way:
			total += line.count('$')
		return (total)

def main():
	# CHANGE INPUTFILE
	input = open("input/16.txt", "r").read()

	sol = Solution(input)
	print("Part 1:", sol.part1())
	print("Part 2:", sol.part2())

if __name__ == "__main__":
	main()