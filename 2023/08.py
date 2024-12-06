from collections import deque
from math import gcd
from functools import reduce
import re
from icecream import ic # source myenv/bin/activate

class Solution:
	def __init__(self, input):
		lines = input.split('\n')
		self.instructions = lines[0]
		route = lines[2:]
		self.dic = {}
		for i in range(len(route)):
			self.dic[route[i][:3]] = [route[i][7:10],route[i][12:15]]

	def part1(self):
		curr = "AAA"
		steps = 0
		while curr != "ZZZ":
			for direction in self.instructions:
				steps += 1
				left, right = self.dic[curr]
				if direction == "L":
					curr = left
				else:
					curr = right
				if curr == "ZZZ":
					break		
		return (steps)

	# get all the start positions, ending with an A
	def getStartNumbers(self):
		startNrs = []
		for item in self.dic:
			if item[2] == 'A':
				startNrs.append(item)
		return (startNrs)

	# Caluculates for every start position how many steps before repeating
	def amountStepsCircuit(self, curr):
		steps = 0
		while True:
			for direction in self.instructions:
				left, right = self.dic[curr]
				steps += 1
				if direction == "L":
					curr = left
				else:
					curr = right
				if curr[2] == "Z":
					return steps

	# the least common multiple (LCM)
	def lcm(self, a, b):
		return (a * b) // gcd(a, b)

	def part2(self):
		startNrs = self.getStartNumbers()
		stepsForStartnr = []
		for curr in startNrs:
			stepsForStartnr.append(self.amountStepsCircuit(curr))
		# calculates over all the stepsForStartNr the least common multiple (LCM)
		return (reduce(self.lcm, stepsForStartnr))

def main():
	with open("input/08.txt", "r") as f:
		input = f.read()

	sol = Solution(input)
	print("Part 1:", sol.part1())
	print("Part 2:", sol.part2())
	f.close() 

if __name__ == "__main__":
	main()
