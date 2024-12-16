import re
from functools import cache

class Solution:
	def __init__(self, input, x, y):
		pattren = r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)"
		match = re.findall(pattren, input)
		self.lenY = y
		self.lenX = x
		self.robots = []
		self.robots2 = []
		self.saveRobotsFromLine = set()

		# Saves the nrs and calculates the modus of each move coordinate
		for m in match:
			moveX = int(m[2])
			if moveX < 0:
				moveX = -moveX % self.lenX
				moveX = -moveX
			else:
				moveX %= self.lenX
			moveY = int(m[3])
			if moveY < 0:
				moveY = -moveY % self.lenY
				moveY = -moveY
			else:
				moveY %= self.lenY
			self.robots.append([int(m[0]), int(m[1]), moveX, moveY])
			self.robots2.append([int(m[0]), int(m[1]), moveX, moveY])

	# if the new place is outsides the field it replaces it back in the field
	@cache
	def corrector(self, newPos, length):
		if newPos >= length:
			return newPos % length
		elif newPos < 0:
			return length - abs(newPos)
		return newPos
	
	# Search after the longest line that resembles the trunk of the christmas tree
	def searchTrunkLength(self, field, y, x):
		self.saveRobotsFromLine.add((y, x))
		trunkLength = 0
		while y + trunkLength < self.lenY and field[y + trunkLength][x] == '#':
			trunkLength += 1		
		return trunkLength

	def part1(self):
		for times in range(100):
			for i in range(len(self.robots)):
				posX, posY, moveX, moveY = self.robots[i]
				posX = self.corrector(posX + moveX, self.lenX)
				posY = self.corrector(posY + moveY, self.lenY)
				self.robots[i] = [posX, posY, moveX, moveY]
		
		# Checks where the robot is and devide them in the 4 parts
		middleX = self.lenX // 2
		middleY = self.lenY // 2
		totalQ = [0,0,0,0]
		for posX, posY, moveX, moveY in self.robots:
			if posX < middleX and posY < middleY:
				totalQ[0] += 1
			elif posX > middleX and posY < middleY:
				totalQ[1] += 1
			elif posX < middleX and posY > middleY:
				totalQ[2] += 1
			elif posX > middleX and posY > middleY:
				totalQ[3] += 1
		return totalQ[0] * totalQ[1] * totalQ[2] * totalQ[3]

	def part2(self):
		fieldline = ['.' for _ in range(self.lenX)]
		currField = [fieldline[:] for _ in range(self.lenY)]
		maxTrunkLength = 0
		saveTimes = 0
		for times in range(10000):	
			currField = [fieldline[:] for _ in range(self.lenY)]
			for i in range(len(self.robots2)):
				posX, posY, moveX, moveY = self.robots2[i]
				posX = self.corrector(posX + moveX, self.lenX)
				posY = self.corrector(posY + moveY, self.lenY)
				self.robots2[i] = [posX, posY, moveX, moveY]
				currField[posY][posX] = '#'

			# Checks for each robot if there is a line from that point
			for i in range(len(self.robots2)):
				if (self.robots2[i][1],self.robots2[i][0]) in self.saveRobotsFromLine and self.lenY - self.robots2[i][1] < trunkLength:
					continue
				trunkLength = self.searchTrunkLength(currField, self.robots2[i][1],self.robots2[i][0])
				if maxTrunkLength < trunkLength:
					saveTimes = times + 1
					maxTrunkLength = trunkLength
			self.saveRobotsFromLine.clear()
		return saveTimes

def main():
	input = open("input/14.txt", "r").read()

	sol = Solution(input, 101, 103)
	print("Part 1:", sol.part1())
	print("Part 2:", sol.part2())

if __name__ == "__main__":
	main()
