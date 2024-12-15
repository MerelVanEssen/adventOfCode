import re
import functools

class Solution:
	def __init__(self, input, movements):
		self.map = input.split()
		for i in range(len(self.map)):
			self.map[i] = [x for x in self.map[i]]
		# self.map = [[x for x in row] for row in self.map]
		self.movements = movements.replace("\n", "")
		self.lenY = len(self.map)
		self.lenX = len(self.map[0])

	def getCoordinates(self):
		for i, line in enumerate(self.map):
			for j, char in enumerate(line):
				if '@' == char:
					fish = [i,j]
					self.map[i][j] = '.'
					return fish

	def move(self, c):
		dir = [[0,1],[1,0],[-1,0],[0,-1]]
		if c == '>':
			return dir[0]
		if c == "<":
			return dir[3]
		if c == '^':
			return dir[2]
		if c == 'v':
			return dir[1]

	def part1(self):
		y, x = self.getCoordinates()
		for step in self.movements:
			self.map[y][x] = '.'
			dY, dX = self.move(step)
			newY = dY + y
			newX = dX + x
			if self.map[newY][newX] == '.':
				y = newY
				x = newX
			elif self.map[newY][newX] == '#':
				continue
			elif self.map[newY][newX] == 'O':
				# print("found stone", newY, newX)
				startY = newY
				startX = newX
				while self.map[newY][newX] == 'O':
					newY += dY
					newX += dX
				# print("end stone", newY, newX, self.map[newY][newX])
				if self.map[newY][newX] == '#':
					continue
				elif self.map[newY][newX] == '.':
					self.map[newY][newX] = 'O'
					while newY != startY and newX != startX:
						newY -= dY
						newX -= dX
						self.map[newY][newX] = 'O'
					# print("back", newY, newX, self.map[newY][newX])
					y = startY
					x = startX
			self.map[y][x] = '@'
		total = 0
		for i in range(len(self.map)):
			for j in range(len(self.map[0])):
				if self.map[i][j] == 'O':
					total += 100 * i + j
		return total
	
	def part2(self):
		return 0

def main():
	input = open("input.txt", "r").read()
	movements = open("input2.txt", "r").read()

	sol = Solution(input, movements)
	print("Part 1:", sol.part1())
	print("Part 2:", sol.part2())

if __name__ == "__main__":
	main()