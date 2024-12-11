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
		self.spaceBlock = []
		self.fileBlock = []

	def getSpace(self, line):
		
		index = 0
		result = []
		for i in range(len(line)):
			if i % 2 == 0:
				files = [index] * int(line[i])
				index += 1
				result += files
				self.fileBlock.append([0, int(line[i]), files])
			else:
				space = ["."] * int(line[i])
				result += space
				self.fileBlock.append([1, int(line[i]), space])
		return result

	def sumCounting(self, result):
		total = 0
		index = 0
		for i, nr in enumerate(result):
			if nr != '.':
				total += int(nr) * index
				index += 1	
		return (total)

	def herschik(self, result):
		j = len(result) - 1
		total = 0
		i = 0
		while i < len(result):
			while i < len(result) and result[i] != '.':
				i += 1
			if i >= j:
				break
			while j > 0 and result[j] == '.':
				j -= 1
			result[i] = result[j]
			result[j] = '.'
			i += 1
			j -= 1
		return self.sumCounting(result)


	def part1(self):
		total = 0
		for line in self.map:
			result = self.getSpace(line)
			t = self.herschik(result)
			total += t
		return total

	def combinesSpaces(self):
		i = 0
		newBlock = []
		while i < len(self.fileBlock) :
			if i < len(self.fileBlock) - 1 and self.fileBlock[i][0] == 1 and self.fileBlock[i + 1][0] == 1:
				self.fileBlock[i + 1][1] += self.fileBlock[i][1]
			else:
				if self.fileBlock[i][0] == 1:
					self.fileBlock[i][2] = ['.'] * self.fileBlock[i][1]
				newBlock.append(self.fileBlock[i])
			i += 1
		self.fileBlock = newBlock

	def herschik2(self, result):
		# print(self.fileBlock)
		newResult = []
		j = 0
		while j < len(self.fileBlock):
			if self.fileBlock[j][0] == 0: # file
				newResult += self.fileBlock[j][2]
				j += 1
			else: # space
				print("search for", self.fileBlock[j])
				space = self.fileBlock[j][1]
				i = len(self.fileBlock) - 1
				found = False
				while i > j:
					if self.fileBlock[i][0] == 0 and self.fileBlock[i][1] <= space:
						print("block fits:", self.fileBlock[i])
						newResult += self.fileBlock[i][2]
						saveBlock = self.fileBlock[i][:]
						self.fileBlock[i][0] = 1
						self.fileBlock[i][2] = ['.'] * self.fileBlock[i][1]
						found = True
						if self.fileBlock[i][1] == space: # fits exactly
							j += 1
						elif self.fileBlock[i][1] < space: #space left
							self.fileBlock[j][1] = space - self.fileBlock[i][1]
							self.fileBlock[j][2] = ['.'] * self.fileBlock[j][1]
						break
					i -= 1
				if not found:
					newResult += self.fileBlock[0][2]
					self.fileBlock.pop(0)
			# print(self.fileBlock)
		print("result", newResult)
		return (newResult)
			
	def sumCounting2(self, result):
		total = 0
		index = 0
		for i, nr in enumerate(result):
			if nr != '.':
				total += int(nr) * i
		return (total)


	def part2(self):
		total = 0
		for line in self.map:
			result = self.getSpace(line)
			result = self.herschik2(result)
			total = self.sumCounting2(result)
		return total

def main():
	input = open("input/09.txt", "r").read()

	sol = Solution(input)
	# print("Part 1:", sol.part1())
	print("Part 2:", sol.part2(), 6382582136592)

if __name__ == "__main__":
	main()