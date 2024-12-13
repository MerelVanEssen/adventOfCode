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
		self.amount = 0
		self.border = 0
		self.corner = 0
		self.bordersX = set()
		self.bordersY = set()
		self.visited = set()

	def searchArea(self, char, x, y):
		if not (0 <= x < len(self.map) and 0 <= y < len(self.map[0])):
			self.border += 1
			return
		if self.map[x][y] != char:
			self.border += 1
			return
		if self.grid[x][y] == True:
			return
		self.grid[x][y] = True
		self.amount += 1
		for d in self.dir:
			newX = x + d[0]
			newY = y + d[1]
			self.searchArea(char, newX, newY)
	
	def checkCorner(self, char, x, y, i):
		if (x < 0 or  i == 1) and (y < 0 or i == 3): #corner leftup
			self.corner += 1
		if (x < 0 or  i == 1) and (y >= len(self.map[0]) or i == 0): # corner right up
			self.corner += 1
		if (y < 0 or i == 2) and (x >= len(self.map) or i == 1): # corner left down
			self.corner += 1
		if ((x >= len(self.map) or i == 1) and ( y >= len(self.map[0]) or i == 0)) # corner right down
			self.corner += 1


	def searchArea2(self, char, x, y, i):
		returnNow = False
		if x < 0 or x >= len(self.map):
			# print("add x", x, y)
			if i == 3:
				self.bordersX.add((x + 1, y))
			else:
				self.bordersX.add((x, y))
			returnNow = True
		if y < 0 or y >= len(self.map[0]):
			if i == 2:
				self.bordersY.add((y + 1, x))
			else:
				self.bordersY.add((y, x))
			# print("add y", y, x)
			returnNow = True
		if returnNow == True:
			self.border += 1
			return False
		if self.map[x][y] != char:
			if i == 3:
				self.bordersX.add((x + 1, y))
			elif i == 1:
				self.bordersX.add((x, y))
			elif i == 2:
				self.bordersY.add((y + 1, x))
			else:
				self.bordersY.add((y, x))
			self.border += 1
			return True
		if self.grid[x][y] == True:
			return False
		self.grid[x][y] = True
		self.amount += 1
		for i, d in enumerate(self.dir):
			newX = x + d[0]
			newY = y + d[1]
			self.searchArea2(char, newX, newY, i)
		return False

	def countSides(self, nrs, lines):
		total = 0
		uniqueNrs = {}
		nrs = list(nrs)
		print(nrs)
		for x, y in nrs:
			if x not in uniqueNrs:
				uniqueNrs[x] = [y]
			else:
				value = uniqueNrs[x]
				value.append(y)
				uniqueNrs[x] = value
		print("u", uniqueNrs)
		for nrs in uniqueNrs:
			saveNrs = nrs
			nrs = uniqueNrs[nrs]
			nrs.sort()
			prev = nrs[0]
			firstNr = nrs[0]
			for nr in nrs:
				if nr != prev + 1:
					lines.append([saveNrs, firstNr, prev])
					firstNr = nr
					total += 1
				prev = nr
		print("lines", lines)
		return(total)

	def part1(self):
		total = 0
		total2 = 0
		saveChar = self.map[0][0]
		for x, line in enumerate(self.map):
			for y, char in enumerate(line):
				if self.grid[x][y] == False:
					self.searchArea2(char, x, y, 0)
					# print("Letter", char)
					total += self.amount * self.border

					part2 = (self.amount * self.countSides(self.bordersX, []))
					print("part2 A" , part2, part2 // self.amount)
					total2 += part2
					part2 = (self.amount * self.countSides(self.bordersY, []))
					print("part2 B" , part2, part2 // self.amount)
					total2 += part2

					self.bordersX.clear()
					self.bordersY.clear()
					self.amount = 0
					self.border = 0
		return total, total2

	def part2(self):
		total = 0

		return total

def main():
	# CHANGE INPUTFILE
	input = open("input/12.txt", "r").read()

	sol = Solution(input)
	print("Part 1:", sol.part1(), 1546338, 978590)
	print("Part 2:", sol.part2())

if __name__ == "__main__":
	main()