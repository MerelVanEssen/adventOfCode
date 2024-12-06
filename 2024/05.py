from collections import deque
from math import gcd
from functools import reduce
import re
from icecream import ic # source myenv/bin/activate
import sys


# self.hands = [[] for _ in range(7)]
# inte = [int(x) for x in line]
# self.field = [['.' for _ in row] for row in self.map]

class Solution:
	def __init__(self, input):
		self.rulesList = {}
		self.books = []
		self.incorrectPages = []

		for line in input:
			if len(line) == 5:
				nr1, nr2 = line.split('|')
				if nr1 in self.rulesList:
					self.rulesList[nr1].append(nr2)
				else:
					self.rulesList[nr1] = [nr2]
			elif len(line) != 0:
				self.books.append(line.split(','))
		
	def checkPages(self, pages):
		savePages = []
		for nr in pages:
			if nr in savePages or (nr in self.rulesList and set(savePages) & set(self.rulesList[nr])):
				self.incorrectPages.append(pages)
				return False
			savePages.append(nr)
		return True

	# Calculates the page nr in the middle
	def	calculate_middle(self, pages):
		middle = len(pages) // 2
		nr = pages[middle]
		return (int(nr))

	def part1(self):
		total = 0

		for pages in self.books:
			if self.checkPages(pages):
				total += self.calculate_middle(pages)
		return total

	# Checks if there is any nr before that is not correct
	def checkPosition(self, page, i):
		pastNrs = page[:i]
		if page[i] in self.rulesList:
			rules = self.rulesList[page[i]]
			for nr in pastNrs[:i]:
				if nr in rules and i != 0:
					return True
		return False

	def part2(self):
		total = 0

		# Checks for every number if it is correct, if not, it lowers his position
		for page in self.incorrectPages:
			change = True
			while change == True:
				change = False
				for i in range(len(page)):
					if self.checkPosition(page, i):
						page[i - 1], page[i] = page[i], page[i - 1]
						change = True
						break
		
		for pages in self.incorrectPages:
			total += self.calculate_middle(pages)
		return total

def main():
	input = open("input/05.txt", "r").read().splitlines()

	sol = Solution(input)
	print("Part 1:", sol.part1())
	print("Part 2:", sol.part2())

if __name__ == "__main__":
	main()
