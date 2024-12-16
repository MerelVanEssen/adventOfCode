import re
from collections import deque
from math import gcd
from functools import reduce
from collections import Counter
from aoc import turnMapBackwardsList
import heapq

# self.hands = [[] for _ in range(7)]
# inte = [int(x) for x in line]
# self.field = [['.' for _ in row] for row in self.map]

class Solution:
	def __init__(self, input):
		self.map = input.split('\n')
		self.lX = len(self.map)
		self.lY = len(self.map[0])
		self.dir = [[0,1], [1,0], [0,-1], [-1,0]]
		self.contraDir = [2,3,0,1]
		self.grid = [[float('inf') for _ in range(self.lY)] for _ in range(self.lX)]

	def dijkstra(self):
		visited = set()
		deq = []
		heapq.heappush(deq, (0, 0, 0, 1, 0)) # cost, y, x, steps, dir left
		heapq.heappush(deq, (0, 0, 0, 1, 1)) # cost, y, x, steps, dir down
		self.grid[0][0] = 0

		while deq:
			cost, y, x, straigth, direction = heapq.heappop(deq)

			if (y, x, direction) in visited:
				continue

			for i, d in enumerate(self.dir):

				newCost = cost
				newY = y + d[1]
				newX = x + d[0]

				if not (0 <= newY < len(self.map) and 0 <= newX < len(self.map[0])):
					continue

				if direction == i and straigth == 3:
					continue

				newCost = cost + int(self.map[newY][newX])

				if y == len(self.map) - 1 and x == len(self.map[0]) - 1:
					return (newCost)

				if straigth == 4:
					straigth = 1
				else:
					straigth += 1

				if newCost < self.grid[newY][newX]:
					self.grid[newY][newX] = newCost

				heapq.heappush(deq, (newCost, newY, newX, straigth, i))

			visited.add((y, x, direction))

		return self.grid[len(self.map) - 1][len(self.map[0]) - 1]
					

	def part1(self):
		total = self.dijkstra()

		for line in self.grid:
			print(line)
		return total

	def part2(self):
		total = 0

		return total

def main():
	# CHANGE INPUTFILE
	input = open("input/17.txt", "r").read()

	sol = Solution(input)
	print("Part 1:", sol.part1())
	print("Part 2:", sol.part2())

if __name__ == "__main__":
	main()