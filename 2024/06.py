from collections import deque
from math import gcd
from functools import reduce
import re
from collections import Counter
from icecream import ic # source myenv/bin/activate

# self.hands = [[] for _ in range(7)]
# inte = [int(x) for x in line]
# self.field = [['.' for _ in row] for row in self.map]

class Solution:
	def __init__(self, input):
		self.map = input.split('\n')
		self.pos = []

		# search start position
		for i, line in enumerate(self.map):
			if '^' in line:
				self.pos = [i, line.index('^')]
				break
		# making an empty map for keeping track of the route
		self.copy = ['.'] * len(self.map)
		self.map = [[x for x in line] for line in self.map]
		for i in range(len(self.copy)):
			self.copy[i] = [0] * len(self.map[0])
		self.empty = self.copy[0][:]
		self.saveRoute = set()

	def part1(self):
		total = 1
		dir = [[-1,0], [0,1], [1,0],[0,-1]]
		turn = 0
		pos = self.pos[:]
		self.copy[pos[0]][pos[1]] = 1
		x, y = pos[0] + dir[turn][0], pos[1] + dir[turn][1]

		while 0 <= x < len(self.map) and 0 <= y < len(self.map[0]):
			if self.map[x][y] == '#':
				if turn == 3:
					turn = 0
				else:
					turn += 1
			else:
				self.copy[x][y] = turn + 1
				pos[0], pos[1] = x, y
				if self.map[x][y] != '^' and (x,y) not in self.saveRoute:
					total += 1
					self.saveRoute.add((x, y))
			x, y = pos[0] + dir[turn][0], pos[1] + dir[turn][1]
		return total

	def loopchecker(self, pos):
		dir = [[-1,0], [0,1], [1,0],[0,-1]]
		turn = 0
		self.copy[pos[0]][pos[1]] = 1
		x, y = pos[0] + dir[turn][0], pos[1] + dir[turn][1]

		while 0 <= x < len(self.map) and 0 <= y < len(self.map[0]):
			if self.map[x][y] == '#':
				if turn == 3:
					turn = 0
				else:
					turn += 1
			else:
				if self.copy[x][y] == turn + 1:
					return True
				self.copy[x][y] = turn + 1
				pos[0], pos[1] = x, y
			x, y = pos[0] + dir[turn][0], pos[1] + dir[turn][1]
		return False

	def part2(self):
		total = 0

		for i, j in list(self.saveRoute):
			if i == self.pos[0] and j == self.pos[1]:
				continue
			for p in range(len(self.copy)):
				self.copy[p] = self.empty.copy()
			self.map[i][j] = '#'
			if self.loopchecker(self.pos[:]):
				total += 1
			self.map[i][j] = '.'
		return total

def main():
	input = open("input/06.txt", "r").read()

	sol = Solution(input)
	print("Part 1:", sol.part1())
	print("Part 2:", sol.part2())

if __name__ == "__main__":
	main()