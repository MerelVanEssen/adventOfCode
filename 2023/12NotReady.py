from collections import deque
from math import gcd
from functools import reduce
import re
from collections import Counter
import copy
from functools import cache

# self.hands = [[] for _ in range(7)]
# inte = [int(x) for x in line]
# self.field = [['.' for _ in row] for row in self.map]

class Solution:
	def __init__(self, input):
		self.lines = []
		lines = input.split('\n')
		for line in lines:
			seq, nrs = line.split()
			self.lines.append([seq, list(map(int, nrs.split(',')))])
		self.total = 0
		self.saveField = []

	def getRangeForEachBlock(self, seq, nrs):
		rangeBlock = []
		start = 0
		end = len(seq) - sum(nrs) - len(nrs) + 2
		for nr in nrs:
			rangeBlock.append([start, end])
			start += nr + 1
			end += nr + 1
		return rangeBlock

	def fillingNewSeq(self, field, nrs, seq):
		newSeq = ['.'] * len(seq)
		for j in range(len(field)):
			start = field[j][0]
			end = field[j][0] + nrs[j]
			while start < end and start < len(newSeq):
				newSeq[start] = '#'
				start += 1
		return newSeq

	def calculateCorrectFields(self, seq, nrs):
		total = 0
		for field in self.saveField:
			# Makes from the possibilities a list
			newSeq = self.fillingNewSeq(field, nrs, seq)

			# Create a string to check easy if it is already correct
			string = "".join(newSeq)
			amountQuestion = string.count('?')
			if amountQuestion == 0 and string == seq:
				total += 1
				continue
			
			# Compares the result with the given array
			found = True
			def wrongResults(newSeq, seq):
				for i in range(len(newSeq)):
					if seq[i] == '#' and newSeq[i] != '#':
						return True
					if seq[i] == '.' and newSeq[i] != '.':
						return True
				return False
			
			if wrongResults(newSeq, seq):
				continue

			# Splits the string to check if the group len is correct
			string = [part for part in string.split('.') if part]
			if len(string) != len(nrs):
				continue

			def checkGroupLen(nrs, string):
				for i in range(len(nrs)):
					if len(string[i]) != nrs[i]:
						return False
				return True

			if checkGroupLen(nrs, string):
				total += 1
		print(total)
		self.total += total

	# Check if the current block can be placed in the example
	def checkCurrentBlock(self, seq, nr, curr):
		start, end = curr
		for j in range(start, start + nr, 1):
			if seq[j] != '?' and seq[j] != '#':
				return False
		return True

	# Search recursive for the possibilities to place the blocks
	@cache
	def placeBlocks(self, length, rangeBlock, curr, i, seq, nrs):
		if i == len(rangeBlock):
			self.saveField.append((curr))
			return
		while curr[i][0] <= rangeBlock[i][1]:
			if self.checkCurrentBlock(seq, nrs[i], curr[i]):
				self.placeBlocks(length, rangeBlock, copy.deepcopy(curr), i + 1, seq, nrs)
			curr[i][0] += 1
			if curr[i][0] == curr[i][1]:
				break
			for j in range(i + 1, len(curr), 1):
				curr[j][0] += 1
		return

	def part1(self):
		for seq, nrs in self.lines:
			self.saveField.clear()
			rangeBlock = self.getRangeForEachBlock(seq, nrs)
			self.placeBlocks(len(seq), rangeBlock, copy.deepcopy(rangeBlock), 0, seq, nrs)
			self.calculateCorrectFields(seq, nrs)
		return self.total

	def part2(self):
		for seq, nrs in self.lines:

			seq = seq + '?' + seq + '?' + seq + '?' + seq + '?' + seq
			nrs = nrs + nrs + nrs + nrs + nrs
			self.saveField.clear()
			rangeBlock = self.getRangeForEachBlock(seq, nrs)
			self.placeBlocks(len(seq), rangeBlock, copy.deepcopy(rangeBlock), 0, seq, nrs)
			self.calculateCorrectFields(seq, nrs)
		return self.total
		
def main():
	with open("input/12.txt", "r") as f:
		input = f.read()

	sol = Solution(input)
	# print("Part 1:", sol.part1())
	print("Part 2:", sol.part2())

if __name__ == "__main__":
	main()
