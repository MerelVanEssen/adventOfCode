import re
from collections import deque
from math import gcd
from functools import reduce
from collections import Counter
from aoc import turnMapBackwardsList

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
		self.grid = [[[float('inf'), 1, -1] for _ in range(self.lY)] for _ in range(self.lX)]
		self.grid2 = [[[float('inf'), 1, -1] for _ in range(self.lY)] for _ in range(self.lX)]
		self.minHeatLoss = float('inf')

	def recursive(self, x, y, heatLoss, straight, lastDir):
		if straight >= 4:
			return
		if heatLoss < self.grid[x][y]:
			self.grid[x][y] = heatLoss
		else:
			return
		if heatLoss >= self.minHeatLoss:
			return
		if (x == self.lX - 1 and y == self.lY - 1):
			print(f"Visiting ({x}, {y}) with heatLoss {heatLoss}, straight {straight}, lastDir {lastDir}")
			print(f"Grid[{x}][{y}] = {self.grid[x][y]}")
			self.minHeatLoss = min(self.minHeatLoss, heatLoss)
			return

		for i, d in enumerate(self.dir):
			if self.contraDir[i] != lastDir:
				newX = x + d[0]
				newY = y + d[1]	
				if not (0 <= newX < self.lX and 0 <= newY < self.lY):
					continue
				newHeatLoss = heatLoss + int(self.map[newX][newY])
				if i == lastDir:
					self.recursive(newX, newY, newHeatLoss, straight + 1, i)
				else:
					self.recursive(newX, newY, newHeatLoss, 1, i)

	def dfs(self):
		deq = []
		deq.append((0,0,0,1,-1))
		while deq:
			y, x, cost, straight, lastDir = deq.pop(0)
			for i, d in enumerate(self.dir):
				newY = d[0] + y
				newX = d[1] + x
				if 0 <= newY < len(self.map) and 0 <= newX < len(self.map[0]):
					newCost = cost + int(self.map[newY][newX])
					newStraight = 1
					if i == lastDir:
						newStraight = straight + 1
					if newStraight > 4:
						continue
					if newCost < self.grid2[newY][newX][0]:
						newI = i
						if self.grid2[newY][newX][2] != -1:
							newStraight = self.grid2[newY][newX][1]
							newI = self.grid2[newY][newX][2]
						deq.append((newY, newX, newCost, newStraight, newI))
						self.grid2[newY][newX][0] = newCost
						self.grid2[newY][newX][1] = newStraight
						self.grid2[newY][newX][2] = i
		for line in self.grid2:
			print(line)
		return(self.grid2[len(self.map) - 1][len(self.map[0]) - 1])



	def part1(self):
		total = 0
		# self.recursive(0,0,0,0,-1)
		return self.dfs()
		
		# return self.minHeatLoss

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