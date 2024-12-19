import re
from collections import deque
from math import gcd
from functools import reduce
from collections import Counter
from aoc import turnMapBackwardsList
import heapq

class Solution:
	def __init__(self, input):
		pattern = r"([A-Z]) (\d+) \(#(.*)\)"
		self.matches = re.findall(pattern, input)
		d = {"R": [0,1], 'L': [0,-1], "U": [-1,0], "D": [1,0]}
		self.points = [[0,0]]
		self.b = 0

		y = x = 0
		for direction, steps, color in self.matches:
			dy, dx = d[direction]
			steps = int(steps)
			self.b += steps
			y += (dy * steps)
			x += (dx * steps)
			self.points.append([y, x])
	
	def hexaConverter(self, color):
		hexadecimal = "0123456789abcdef"

		nr = 0
		for i, hexa in enumerate(reversed(color)):
			value = hexadecimal.index(hexa)
			nr += value * (16 ** i)  
		return nr

	def part1(self):
		boundary = self.b
		area = 0
		# Shoelace formula
		for i, point in enumerate(self.points):
			y, x = point[0], point[1]
			if i + 1 == len(self.points):
				area += y * (self.points[i - 1][1] - self.points[-1][1])
			else:
				area += y * (self.points[i - 1][1] - self.points[i + 1][1])
		area = abs(area) / 2

		# Pick's theorem
		insideArea = area - (boundary / 2) + 1
		return int(insideArea + boundary)

	def part2(self):
		directions = [[0,1],[1,0],[0,-1],[-1,0]]
		self.points.clear()
		self.points = [[0,0]]

		y = x = 0
		self.b = 0
		for d, s, color in self.matches:
			distance = self.hexaConverter(color[:5])
			direction = self.hexaConverter(color[5])

			dy, dx = directions[direction]
			self.b += distance
			y += dy * distance
			x += dx * distance
			self.points.append([y, x])
		return self.part1()

def main():
	input = open("input/18.txt", "r").read()

	sol = Solution(input)
	print("Part 1:", sol.part1())
	print("Part 2:", sol.part2())

if __name__ == "__main__":
	main()