import re
from collections import deque
from math import gcd
from functools import reduce
from collections import Counter

class Solution:
	def __init__(self, input):
		self.map = input.split('\n')
		for i, line in enumerate(self.map):
			self.map[i] = line.split(':')
			self.map[i][1] = self.map[i][1].split()
			self.map[i][0] = int(self.map[i][0])
			self.map[i][1] = [int(x) for x in self.map[i][1]]

	def calculateSum(self, nrs, opChoice):
		total = nrs[0]
		for i in range(len(opChoice)):
			if opChoice[i] == '*':
				total *= nrs[i + 1]
			elif opChoice[i] == '+':
				total += nrs[i + 1]
			else:
				total = int(str(total) + str(nrs[i + 1]))
		return total
	
	def recursiveFilling(self, total, nrs, opChoice, i, operators):
		if i == len(nrs) - 1:
			sumNrs = self.calculateSum(nrs, opChoice)
			if sumNrs == total:
				return True
			return False
		for operator in operators:
			opChoiceNew = opChoice + [operator]
			if self.recursiveFilling(total, nrs, opChoiceNew, i + 1, operators):
				return True
		return False

	def part(self, operators):
		totalNrs = 0
		for total, nrs in self.map:
			opChoice = []
			if self.recursiveFilling(total, nrs, opChoice, 0, operators):
				totalNrs += total
		return totalNrs

def main():
	input = open("input/07.txt", "r").read()

	sol = Solution(input)
	print("Part 1:", sol.part(['*', '+']))
	print("Part 2:", sol.part(['*', '+', '||']))

if __name__ == "__main__":
	main()