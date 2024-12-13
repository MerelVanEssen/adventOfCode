import re
from collections import deque, Counter, defaultdict
from math import gcd
from functools import reduce
from aoc import turnMapBackwardsList

# self.hands = [[] for _ in range(7)]
# inte = [int(x) for x in line]
# self.field = [['.' for _ in row] for row in self.map]

class Solution:
	def __init__(self, input):
		self.map = input.split('\n')
		self.grid = [[False for _ in range(len(self.map[0]))] for _ in range(len(self.map))]
		self.dir = [[0,1], [1,0], [0,-1], [-1,0]]
		self.visit = set()
		self.amount = 0
		self.border = 0
		self.corners = 0

	def floating(self, index, char, y, x):
		deq = [(y, x)]
		self.grid[y][x] = index
		self.visit.add((y, x))
		amount = 1
		border = 0
		corner = 0

		while deq:
			curr = deq.pop(0)
			wrongCornerInside = []
			visitedCorners = set()
			for i, d in enumerate(self.dir):
				newY = d[0] + curr[0] 
				newX = d[1] + curr[1]
				insideMap = False
				if 0 <= newY < len(self.map) and 0 <= newX < len(self.map):
					insideMap = True
				setNew = (newY, newX)
				if insideMap and self.map[newY][newX] == char and setNew not in self.visit:
					amount += 1
					self.grid[newY][newX] = index
					deq.append(setNew)
					self.visit.add(setNew)
				else:
					if not (insideMap and self.map[newY][newX] == char):
						border += 1
						wrongCornerInside.append(i) # inside corners
						if i == 0 or i == 2:
							if newY - 1 < 0 or (insideMap and self.map[newY - 1][newX] != char):
								visitedCorners.add((newY - 1, newX))
								print("1 add", newY - 1, newX)
							if newY + 1 >= len(self.map) or (insideMap and self.map[newY + 1][newX] != char):
								print("2 add", newY + 1, newX)
								visitedCorners.add((newY + 1, newX))
						elif i == 1 or i == 3:
							if newX + 1 < len(self.map[0]) or (insideMap and self.map[newY][newX + 1] != char):
								visitedCorners.add((newY, newX + 1))
								print("3 add", newY, newX + 1)
							if newX - 1 >= 0 or (insideMap and self.map[newY][newX - 1] != char):
								visitedCorners.add((newY, newX - 1))
								print("4 add", newY, newX - 1)			
			if 0 in wrongCornerInside and 1 in wrongCornerInside:
				corner += 1
			if 1 in wrongCornerInside and 2 in wrongCornerInside:
				corner += 1
			if 2 in wrongCornerInside and 3 in wrongCornerInside:
				corner += 1
			if 3 in wrongCornerInside and 0 in wrongCornerInside:
				corner += 1

		print("corners", len(visitedCorners))			
		for line in self.grid:
			print(line)
		
		return amount, border, corner + len(visitedCorners)

	def part(self):
		index = 0
		corners = 0
		borders = 0
		for y in range(len(self.map)):
			for x in range(len(self.map[0])):
				char = self.map[y][x]
				print(char)
				if (y,x) not in self.visit:
					amount, border, corner = self.floating(index, char, y, x)
					print(amount, border, corner)
					corners += amount * corner
					borders += amount * border
					index += 1
		return borders, corners

def main():
	# CHANGE INPUTFILE
	input = open("input/12.txt", "r").read()

	sol = Solution(input)
	print("Part 1:", sol.part(), 1546338, 978590)

if __name__ == "__main__":
	main()