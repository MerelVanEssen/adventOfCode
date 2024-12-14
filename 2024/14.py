import re
from collections import deque, Counter, defaultdict
from functools import reduce

class Solution:
	def __init__(self, input, x, y):
		self.found = 0
		self.saveField = []
		self.map = input.split('\n')
		self.lenY = y
		self.lenX = x
		field = ['.' for _ in range(x)]
		self.field = [field[:] for _ in range(y)]
		for i in range(len(self.map)):
			parts = self.map[i].split()
			part1 = parts[0].split(',')
			part2 = parts[1].split(',')
			part1 = [int(x) for x in part1]
			part2 = [int(x) for x in part2]
			if part2[0] < 0:
				part2[0] = -part2[0]
				part2[0] %= self.lenX
				part2[0] = -part2[0]
			else:
				part2[0] %= self.lenX
			if part2[1] < 0:
				part2[1] = -part2[1]
				part2[1] %= self.lenY
				part2[1] = -part2[1]
			else:
				part2[1] %= self.lenY
			self.map[i] = [part1,part2]

	def corrector(self, newPos, length):
		if newPos >= length:
			newPos = newPos % length
		elif newPos < 0:
			newPos = length - abs(newPos)
		return newPos

	
	def searchTree(self, field, y, x):
		lineLen = 0
		while y + lineLen < self.lenY and field[y + lineLen][x] == '#':
			lineLen += 1		
		return lineLen

	def part1(self):
		total = 0
		field = ['.' for _ in range(self.lenX)]
		field = [field[:] for _ in range(self.lenY)]
		saveMap = []
		maxLinefield = 0
		saveTimes = 0
		for times in range(50000):
			field = ['.' for _ in range(self.lenX)]
			field = [field[:] for _ in range(self.lenY)]
			for i in range(len(self.map)):
				pos, move = self.map[i]
				pos[0] = self.corrector(pos[0] + move[0], self.lenX)
				pos[1] = self.corrector(pos[1] + move[1], self.lenY)
				self.map[i] = [pos, move]
				field[pos[1]][pos[0]] = '#'
			for i in range(len(self.map)):
				lineleng = self.searchTree(field, self.map[i][0][1],self.map[i][0][0])
				if maxLinefield < lineleng:
					saveTimes = times + 1
					maxLinefield = lineleng
					# saveField = field[:]
					# saveMap = self.map[:]
		middleX = self.lenX // 2
		middleY = self.lenY // 2
		middle = 0
		totalQ = [0,0,0,0]
		for pos, move in self.map:
			if pos[0] == middleX or pos[1] == middleY:
				middle += 1
				continue
			if pos[0] < middleX and pos[1] < middleY:
				totalQ[0] += 1
			elif pos[0] > middleX and pos[1] < middleY:
				totalQ[1] += 1
			elif pos[0] < middleX and pos[1] > middleY:
				totalQ[2] += 1
			elif pos[0] > middleX and pos[1] > middleY:
				totalQ[3] += 1
		return totalQ[0] * totalQ[1] * totalQ[2] * totalQ[3], saveTimes

def main():
	# CHANGE INPUTFILE
	input = open("input.txt", "r").read()

	# sol = Solution(input, 11, 7)
	sol = Solution(input, 101, 103)
	print("Part 1 TEST:", sol.part1())

if __name__ == "__main__":
	main()

	# 50331600 too low
	# 224446464 too low
	# 227002500 too low
