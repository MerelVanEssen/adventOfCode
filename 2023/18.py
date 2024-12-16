import re
from collections import deque
from math import gcd
from functools import reduce
from collections import Counter
from aoc import turnMapBackwardsList

# self.hands = [[] for _ in range(7)]
# inte = [int(x) for x in line]
# self.field = [['.' for _ in row] for row in self.map]

class Solution:
	def __init__(self, input):
		pattern = r"([A-Z]) ([\d+]) \((.*)\)"
		self.matches = re.findall(pattern, input)
		self.d = {"R": [0,1], 'L': [0,-1], "U": [-1,0], "D": [1,0]}
		self.map = []

	def searchLowest(self, way):
		lowestY = float('inf')
		lowestX = float('inf')
		highestY = float('-inf')
		highestX = float('-inf')

		for y, x in way:
			lowestY = min(lowestY, y)
			lowestX = min(lowestX, x)
			highestY = max(highestY, y)
			highestX = max(highestX, x)
		return abs(lowestY) + 3, abs(lowestX) + 3, highestY + abs(lowestY) + 6, highestX + abs(lowestX) + 6

	def drawMap(self, way, correctionY, correctionX, maxY, maxX):
		self.map = [['.' for _ in range(maxX + 1)] for _ in range(maxY + 1)]
		y = way[0][0]
		x = way[0][1]
		for y, x in way:
			self.map[y + correctionY][x + correctionX] = '#'
	
	def fillMap(self):
		outside = True
		deq = []

		for i, line in enumerate(self.map):
			if line.count('#') == 2:
				inside = True
				savePoints = set()
				index = line.index('#')
				deq.append([i, index + 1])
				savePoints.add((i, index + 1))
				while deq:
					y, x = deq.pop()
					for dY, dX in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
						yNew = y + dY
						xNew = x + dX
						if not (0 <= yNew < len(self.map) and 0 <= xNew < len(self.map[0])):
							inside = False
							break
						if self.map[yNew][xNew] == '.' and (yNew, xNew) not in savePoints:
							deq.append([yNew, xNew])
							savePoints.add((yNew, xNew))
				if inside == True:
					for y,x in savePoints:
						self.map[y][x] = '#'

		for line in self.map:
			print(line)

	def part1(self):
		d = {"R": [0,1], 'L': [0,-1], "U": [-1,0], "D": [1,0]}
		y = x = 0
		way = set()
		for match in self.matches:
			step = 0
			while step < int(match[1]):
				y += self.d[match[0]][0]
				x += self.d[match[0]][1]
				step += 1
				way.add((y, x))
		correctionY, correctionX, maxY, maxX = self.searchLowest(list(way))
		print(way)
		print(correctionY, correctionX, maxY, maxX)
		self.drawMap(list(way), correctionY, correctionX, maxY, maxX)
		self.fillMap()

		total = 0
		for line in self.map:
			total += line.count('#')
		return total

	def part2(self):
		total = 0

		return total

def main():
	# CHANGE INPUTFILE
	input = open("input/18.txt", "r").read()

	sol = Solution(input)
	print("Part 1:", sol.part1())
	print("Part 2:", sol.part2())

if __name__ == "__main__":
	main()