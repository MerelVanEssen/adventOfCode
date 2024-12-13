import re
from collections import deque
from math import gcd
from functools import reduce
from collections import Counter
from aoc import turnMapBackwardsList
from functools import cache

# self.hands = [[] for _ in range(7)]
# inte = [int(x) for x in line]
# self.field = [['.' for _ in row] for row in self.map]

class Solution:
	def __init__(self, input):
		self.map = input.split('\n')
		self.energized = set()
		self.visit = set()
		self.dir = [[0,1], [-1,0], [0,-1], [1, 0]]
		self.copy = self.map[:]
		for i in range(len(self.copy)):
			self.copy[i] = [x for x in self.copy[i]]
		self.maxEnergized = 0

	@cache
	def correctDir(self, dir):
		if dir == -1:
			return [3]
		elif dir == 4:
			return [0]
		return [dir]

	@cache
	def mirror(self, mirror, dir):
		if mirror == '.':
			return [dir]
		elif mirror == '\\':
			if dir == 0 or dir == 2:
				dir -= 1
			else:
				dir += 1
		elif mirror == '/':
			if dir == 0 or dir == 2:
				dir += 1
			else:
				dir -= 1
		elif mirror == '|' and (dir == 0 or dir == 2):
			return [1, 3]
		elif mirror == '-' and dir != 0 and dir != 2:
			return [0, 2]
		return self.correctDir(dir)
	
	def checkMirror(self, mirror, dir):
		
		return(self.mirror(mirror, dir))

	def followBeam(self, x, y, dir, depth):
		if (x, y, dir) in self.visit or depth == 990:
			return
		
		if 0 <= x < len(self.map) and 0 <= y < len(self.map[0]):
			self.visit.add((x, y, dir))
			self.copy[x][y] = '#'
			self.energized.add((x, y))
			mirror = self.map[x][y]
			dir = self.checkMirror(mirror, dir)
			for d in dir:
				self.followBeam(x + self.dir[d][0], y + self.dir[d][1], d, depth + 1)
		return
	
	def followBeam2(self, items):
		while items:
			x, y, dir, setList = items.pop(0)
			




	def part1(self):
		self.followBeam(0, 0, 0, 0)
		for line in self.copy:
			print(line)
		return len(self.energized)

	def part2(self):
		total = 0
		for i in range(len(self.map[0])):
			self.visit.clear()
			self.energized.clear()
			self.followBeam(0, i, 3, 0)
			self.followBeam2([0, i, 3, set()])
			self.maxEnergized = max(self.maxEnergized, len(self.energized))
			# print(0, i, self.maxEnergized)

		for i in range(len(self.map[0])):
			self.visit.clear()
			self.energized.clear()
			self.followBeam(len(self.map[0]) - 1, i, 1, 0)
			self.maxEnergized = max(self.maxEnergized, len(self.energized))
			# print(len(self.map[0]) - 1, i, self.maxEnergized)

		for i in range(len(self.map)):
			self.visit.clear()
			self.energized.clear()
			self.followBeam(i, 0, 0, 0)
			self.maxEnergized = max(self.maxEnergized, len(self.energized))
			# print(i, 0, self.maxEnergized)

		for i in range(len(self.map)):
			self.visit.clear()
			self.energized.clear()
			self.followBeam(len(self.map) - 1, i, 2, 0)
			self.maxEnergized = max(self.maxEnergized, len(self.energized))
			# print(len(self.map) - 1, i, self.maxEnergized)
		return self.maxEnergized

def main():
	# CHANGE INPUTFILE
	input = open("input/16.txt", "r").read()

	sol = Solution(input)
	# print("Part 1:", sol.part1())
	print("Part 2:", sol.part2())

if __name__ == "__main__":
	main()