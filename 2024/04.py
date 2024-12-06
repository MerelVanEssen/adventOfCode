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
		self.n = len(self.horizontal)
		self.vertical = ['' for _ in range(self.n)]
		self.xmas = "XMAS"
		self.samx = "SAMX"

		# turn field for search vertical
		for i in range(self.n):
			for j in range(self.n):
				self.vertical[j] += self.horizontal[i][j]
		
	def get_diagonal(self, x, y, direction):
		diagonal = []
		while 0 <= x < self.n and 0 <= y < self.n:
			diagonal.append(self.horizontal[x][y])
			x += direction[0]
			y += direction[1]
		return ''.join(diagonal)

	def part1(self):
		count = 0
		
		# search horizontal & vertical
		for line in self.horizontal + self.vertical:
			count += line.count(self.xmas) + line.count(self.samx)

		# search diagonal (first two parts)
		for r in range(self.n):
			diag1 = self.get_diagonal(r, 0, (1, 1))
			count += diag1.count(self.xmas) + diag1.count(self.samx)

			diag2 = self.get_diagonal(r, self.n - 1, (1, -1))
			count += diag2.count(self.xmas) + diag2.count(self.samx)

		# search diagonal (last two parts, skip the middle line)
		r = 1
		while r < self.n:
			diag1 = self.get_diagonal(0, r, (1, 1))
			count += diag1.count(self.xmas) + diag1.count(self.samx)
			r += 1

		for r in range(self.n - 1):
			diag2 = self.get_diagonal(0, r, (1, -1))
			count += diag2.count(self.xmas) + diag2.count(self.samx)
		return (count)

	def part2(self):
		count = 0
		for i in range(self.n):
			for j in range(self.n):
				if self.horizontal[i][j] == 'A' and 0 < i < self.n - 1 and 0 < j < self.n - 1:
					# check around 'A' and save the letters
					leftdown = self.horizontal[i-1][j-1] + self.horizontal[i+1][j+1]
					rightup = self.horizontal[i+1][j-1] + self.horizontal[i-1][j+1]
					if leftdown == "MS" and (rightup == 'MS' or rightup == 'SM'):
						count += 1
					elif leftdown == 'SM' and (rightup == 'MS' or rightup == 'SM'):
						count += 1
		return (count)	

def main():
	with open("input/04.txt", "r") as f:
		input = f.read()

	sol = Solution(input)
	print("Part 1:", sol.part1())
	print("Part 2:", sol.part2())

if __name__ == "__main__":
	main()
