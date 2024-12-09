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

	def herschik2(self, result, change):
		newFileBlock = []
		newResult = []
		rest = False
		while self.fileBlock:
			# print(newResult)
			if rest == False:
				curr = self.fileBlock.pop(0)
			rest = False
			# print("curr", curr)
			if curr == 0:
				break
			if curr[0] == 0: # file
				newResult += curr[2]
				# print("found file")
				newFileBlock.append(curr[:])
				# print("1ADD curr[:]", curr)
			else: # space
				space = curr[1]
				found = False
				for i in range(len(self.fileBlock) - 1, 0, -1):
					if self.fileBlock[i][0] == 0 and self.fileBlock[i][1] <= space:
						# print("found move", self.fileBlock[i][0], space)
						change = True
						found = True
						move = self.fileBlock[i][:]
						self.fileBlock[i][0] = 1
						self.fileBlock[i][2] = ["."] * self.fileBlock[i][1]
						# print("2ADD move[:]", move)
						newFileBlock.append(move[:])
						if move[1] != space:
							
							curr[1] = space - move[1]
							curr[2] = ["."] * curr[1]
							curr[0] = 1
							# self.fileBlock.insert(0, curr[:])
							rest = True
							# print("found with rest", rest)
							nrs = move[2]
							move[2] = nrs[:move[1]]
							move[0] = 0
						newResult += move[2]				
						break
				if found == False:
					newResult += curr[2]
					newFileBlock.append(curr[:])
					# print("3ADD curr", curr)
		self.fileBlock = newFileBlock[:]
		print(newResult)
		return (change, newResult)
			
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
			change = True
			i = 0
			while change and i < 5:
				change = False
				change, result = self.herschik2(result, change)
				change = True
				i += 1
			total = self.sumCounting2(result)
		return total

def main():
	input = open("input/09.txt", "r").read()

	sol = Solution(input)
	# print("Part 1:", sol.part1())
	print("Part 2:", sol.part2())

if __name__ == "__main__":
	main()

	# 6353393526605
	# 6353658456323

	# 6382582218784 6393172435435
	# 6409919630033