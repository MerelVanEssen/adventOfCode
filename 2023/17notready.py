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
		self.dir = [(0,1), (1,0), (0,-1), (-1,0)]
		self.grid = [[float('inf') for _ in range(self.lX)] for _ in range(self.lY)]
		self.start = (0,0)
		self.end = (self.lY - 1, self.lX - 1)

	def dijkstra(self):
		visited = set()
		deq = []
		heapq.heappush(deq, (0, 0, 0, False, 0, 1)) # cost, y, x, steps, dir left
		heapq.heappush(deq, (0, 0, 0, False, 1, 0)) # cost, y, x, steps, dir down
		self.grid[0][0] = 0

		while deq:
			cost, y, x, turn, dY, dX = heapq.heappop(deq)

			if (y, x) == self.end:
				return cost

			if (y, x, dY, dX) in visited:
				continue

			visited.add((y, x, dY, dX))

			# print(y, x, turn, dY, dX, "cost", cost)

			if turn == False:
				newCost = cost
				for i in range(3):
					y += dY
					x += dX
					
					if 0 <= y < self.lY and 0 <= x < self.lX:
						newCost += int(self.map[y][x])
						# print(y, x, newCost)
						heapq.heappush(deq, (newCost, y, x, True,  dY, dX))
			else:
				for dirY, dirX in {(-dX, dY), (dX, -dY)}:
					if (y, x, False, dirY, dirX) not in visited:
						heapq.heappush(deq, (cost, y, x, False, dirY, dirX))

		return 0
					

	def part1(self):
		total = self.dijkstra()
		return total

	def part2(self):
		total = 0

		return total

def main():
	# CHANGE INPUTFILE
	input = open("input/17.txt", "r").read()

	sol = Solution(input)
	print("Part 1:", sol.part1(), 936)
	print("Part 2:", sol.part2())

if __name__ == "__main__":
	main()