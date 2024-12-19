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
		workflows, ratings = input.split('\n\n')
		
		self.ratings = re.findall(patternRatings, ratings)
		workflows = re.findall(patternWorkflow, workflows)
		self.workflows = {}
		for i, flow in enumerate(workflows):
			self.workflows[flow[0]] = flow[1].split(',')

	def	checkStatement(self, rating, group, operator, value):
		convert = {"x": 0, "m": 1, "a": 2, "s": 3}

		nr = rating[convert[group]]
		if operator == '<':
			if nr < value:
				return True
		else:
			if nr > match[0][2]:
				return True
		return False

				# if length == 1 and nextStatement == False:
				# 	if label == "A":
				# 		accept += sum(rating)
				# 		breakout = True
				# 	elif label == 'R':
				# 		breakout = True
				# 	else:
				# 		label = f[0]

	def process(self, rating):
		pattern3 = r"([\w])([< | >])(\d+):(\w+)"
		flow = self.workflows["in"]
		found = True
		label = "in"
		accept = 0
		for rating in self.ratings:
			
			flow = self.workflows[label]
			match = re.findall(pattern3, flow)
			if len(match) == 0:
				0
			for i, m in enumerate(match):
				group, operator, value, nextLabel = match[0]
					if self.checkStatement(rating, group, operator, value):
						label = nextLabel
						found = True
						break

					
		


	def part1(self):
		total = 0
		for rating in self.ratings:
			self.process(rating)
		return total

	def part2(self):
		total = 0

		return total

def main():
	input = open("input/19.txt", "r").read()

	sol = Solution(input)
	print("Part 1:", sol.part1())
	print("Part 2:", sol.part2())

if __name__ == "__main__":
	main()