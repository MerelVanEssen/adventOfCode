import re
from collections import deque
from math import gcd
from functools import reduce
from collections import Counter
from aoc import turnMapBackwardsList
import heapq
from functools import cache

# self.hands = [[] for _ in range(7)]
# inte = [int(x) for x in line]
# self.field = [['.' for _ in row] for row in self.map]

class Solution:
	def __init__(self, input):
		patternRatings = r"\{x=(\d+),m=(\d+),a=(\d+),s=(\d+)\}"
		patternWorkflow = r"(\w+)\{([^}]*)\}"
		pattern = r"([\w])([< | >])(\d+):(\w+)"
		workflows, ratings = input.split('\n\n')
		
		self.ratings = re.findall(patternRatings, ratings)
		workflows = re.findall(patternWorkflow, workflows)
		self.workflows = {}

		self.groups = [[0],[0],[0],[0]]
		convert = {'x': 0, 'm': 1, 'a': 2, 's': 3}

		for i, flow in enumerate(workflows):
			splitsFlow = flow[1].split(',')
			for i in range(len(splitsFlow)):
				if ':' in splitsFlow[i]:
					splitsFlow[i] = re.findall(pattern, splitsFlow[i])
					nr = int(splitsFlow[i][0][2])
					self.groups[convert[splitsFlow[i][0][0]]].append(nr)
					self.groups[convert[splitsFlow[i][0][0]]].append(nr - 1)
					self.groups[convert[splitsFlow[i][0][0]]].append(nr + 1)
				else:
					splitsFlow[i] = (splitsFlow[i])
			self.workflows[flow[0]] = splitsFlow
		

	@cache
	def	checkStatement(self, group, operator, value, rating):
		convert = {"x": 0, "m": 1, "a": 2, "s": 3}

		nr = rating[convert[group]]
		if operator == '<':
			if int(nr) < int(value):
				return True
		else:
			if int(nr) > int(value):
				return True
		return False

	def rate(self, rating):
		label = "in"
		while True:
			if label == 'A':
				return (True)
			if label == 'R':
				return (False)
			
			flow = self.workflows[label]
			for statement in flow:	
				if isinstance(statement, str):
					label = statement
					break
				g, o, v, l = statement[0]
				if self.checkStatement(g, o, v, tuple(rating)):
					label = l
					break

	def part1(self):
		total = 0
		for rating in self.ratings:
			rating = list(map(int, rating))
			if self.rate(rating):
				total += sum(rating)
		return total

	def part2(self):
		total = 0
		for y in range(1, 4001):
			for x in range(1, 4001):
				for z in range(1, 4001):
					for a in range(1, 4001):
						rating = [y, x, z, a]
						if self.rate(rating):
							total += sum(rating)
		return total

def main():
	input = open("input/19.txt", "r").read()

	sol = Solution(input)
	print("Part 1:", sol.part1(), 397134)
	print("Part 2:", sol.part2(), 127517902575337)

if __name__ == "__main__":
	main()