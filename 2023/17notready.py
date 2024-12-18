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
		self.lY = len(self.map)
		self.lX = len(self.map[0])
		self.dir = [[0,1], [1,0], [0,-1], [-1,0]]
		self.grid = [[float('inf') for _ in range(self.lX)] for _ in range(self.lY)]

	def dijkstra(self):
		visited = set()
		deq = []
		heapq.heappush(deq, (0, 0, 0, 1, 0, 0)) # cost, y, x, steps, dirY, dirX

		while deq:
			cost, y, x, s, dy, dx = heapq.heappop(deq)

			if s == 4:
				continue

			if (y, x, dy, dx, s) in visited:
				continue
			visited.add((y, x, dy, dx, s))
			
			if y == self.lY - 1  and x == self.lX - 1:
				return cost
			
			for ndy, ndx in self.dir:
				if ndy == -dy and ndx == -dx:
					continue

				newY = y + ndy
				newX = x + ndx

				if 0 <= newY < self.lY and 0 <= newX < self.lX:
					newCost = cost + int(self.map[newY][newX])

					if [dy,dx] == [ndy,ndx]:
						heapq.heappush(deq, (newCost, newY, newX, s + 1, ndy, ndx))
					else:
						heapq.heappush(deq, (newCost, newY, newX, 1, ndy, ndx))
		return 0

	def dijkstra2(self):
		visited = set()
		deq = []
		heapq.heappush(deq, (0, 0, 0, 1, 0, 1)) # cost, y, x, steps, dirY, dirX
		heapq.heappush(deq, (0, 0, 0, 1, 1, 0))

		while deq:
			cost, y, x, s, dy, dx = heapq.heappop(deq)

			if s == 9:
				continue

			if (y, x, dy, dx, s) in visited:
				continue
			visited.add((y, x, dy, dx, s))
			if cost < self.grid[y][x]:
				self.grid[y][x] = cost

			if y == self.lY - 1  and x == self.lX - 1:
				return cost
			
			for ndy, ndx in self.dir:
				
				if ndy == -dy and ndx == -dx:
					continue

				newY = y + ndy
				newX = x + ndx

				if 0 <= newY < self.lY and 0 <= newX < self.lX:
					newCost = cost + int(self.map[newY][newX])

					if [dy,dx] == [ndy,ndx]:
						heapq.heappush(deq, (newCost, newY, newX, s + 1, ndy, ndx))
					elif s > 3:
						heapq.heappush(deq, (newCost, newY, newX, 1, ndy, ndx))
		return 0
					

	def part1(self):
		return self.dijkstra()

	def part2(self):
		total = self.dijkstra2()
		for line in self.grid:
			print(line)
		return total

def main():
	# CHANGE INPUTFILE
	input = open("input/17.txt", "r").read()

	sol = Solution(input)
	print("Part 1:", sol.part1())
	print("Part 2:", sol.part2())

if __name__ == "__main__":
	main()

# 1181 too high