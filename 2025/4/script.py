from collections import deque
from math import gcd
from functools import reduce
import re
from icecream import ic # source myenv/bin/activate

# self.hands = [[] for _ in range(7)]
# inte = [int(x) for x in line]
# self.field = [['.' for _ in row] for row in self.map]

class Solution:
	def __init__(self, input):
		self.horizontal = input.split('\n')
		self.vertical = ["" for _ in range(len(self.horizontal[0]))]
		self.word = "XMAS"
		self.wordb = "SAMX"
		for i in range(len(self.horizontal)):
			for j in range(len(self.horizontal[i])):
				self.vertical[j] = self.vertical[j] + self.horizontal[i][j]
		
	def get_diagonal(self, x, y, direction):
		diagonal = []
		while 0 <= x < len(self.horizontal) and 0 <= y < len(self.horizontal[0]):
			diagonal.append(self.horizontal[x][y])
			x += direction[0]
			y += direction[1]
		return ''.join(diagonal)
	
	def part1(self):
		total = 0

		for line in self.horizontal:
			total += line.count(self.word)
			total += line.count(self.wordb)

		for line in self.vertical:
			total += line.count(self.word)
			total += line.count(self.wordb)

		for r in range(len(self.horizontal)):
			diag1 = self.get_diagonal(r, 0, (1, 1))
			total += diag1.count(self.word)
			total += diag1.count(self.wordb)
			diag2 = self.get_diagonal(r, len(self.horizontal) - 1, (1, -1))
			total += diag2.count(self.word)
			total += diag2.count(self.wordb)

		r = 1
		while r < len(self.horizontal[0]):
			diag1 = self.get_diagonal(0, r, (1, 1))
			total += diag1.count(self.word)
			total += diag1.count(self.wordb)
			r += 1

		for r in range(len(self.horizontal[0]) - 1):
			diag2 = self.get_diagonal(0, r, (1, -1))
			total += diag2.count(self.word)
			total += diag2.count(self.wordb)
		return (total)

	def part2(self):
		total = 0
		possibilities= ["MS", "SM"]
		for i in range(len(self.horizontal)):
			for j in range(len(self.horizontal[0])):
				if self.horizontal[i][j] == 'A' and 0 < i < len(self.horizontal) - 1 and 0 < j < len(self.horizontal[1]) - 1:
					if self.horizontal[i-1][j-1] + self.horizontal[i+1][j+1] == "MS":
						if self.horizontal[i+1][j-1] + self.horizontal[i-1][j+1] == 'MS':
							total += 1
						elif self.horizontal[i+1][j-1] + self.horizontal[i-1][j+1] == 'SM':
							total += 1
					elif self.horizontal[i-1][j-1] + self.horizontal[i+1][j+1] == 'SM':
						if self.horizontal[i+1][j-1] + self.horizontal[i-1][j+1] == 'MS':
							total += 1
						elif self.horizontal[i+1][j-1] + self.horizontal[i-1][j+1] == 'SM':
							total += 1
		return (total)	

def main():
	with open("input.txt", "r") as f:
		input = f.read()

	sol = Solution(input)
	print("Part 1:", sol.part1(), 2591)
	print("Part 2:", sol.part2(), 1880)
	f.close() 
# 2165 to low
if __name__ == "__main__":
	main()
