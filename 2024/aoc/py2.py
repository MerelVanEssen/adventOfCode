class Solution:
	def __init__(self, input, movements):
		self.map = input.split()
		for i in range(len(self.map)):
			line = []
			for j in range(len(self.map[i])):
				if self.map[i][j] == '#':
					line.append('#')
					line.append('#')
				elif self.map[i][j] == '@':
					line.append('@')
					line.append('.')
				elif self.map[i][j] == 'O':
					line.append('[')
					line.append(']')
				elif self.map[i][j] == '.':
					line.append('.')
					line.append('.')
			self.map[i] = line[:]
		self.incl = []

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
			return dir[0][0], dir[0][1], 'x-as'
		if c == "<":
			return dir[3][0], dir[3][1], 'x-as'
		if c == '^':
			return dir[2][0], dir[2][1], 'y-as'
		if c == 'v':
			return dir[1][0], dir[1][1], 'y-as'

	def moveBalls(self, balls, dY, dX):
		balls.reverse()
		for y, x in balls:
			self.map[y][x] = '.'
			self.map[y][x + 1] = '.'
			newY = y + dY
			self.map[newY][x] = '['
			self.map[newY][x + 1] = ']'

	def searchBalls(self, ball, dY, dX):
		incl = []
		collection = [[ball[0], ball[1]]]
		incl.append([ball[0], ball[1]])
		while collection:
			y, x = collection.pop()
			newY = y + dY
			char = self.map[newY][x]
			char2 = self.map[newY][x + 1]
			if char == '#' or char2 == '#':
				return []
			elif char == '[' and char2 == ']':
				incl.append([newY, x])
				collection.append([newY, x])
			elif char == '[':
				print("found bug? BUGGGGGG", char, char2, newY, x)
				return False
			elif char == ']':
				incl.append([newY, x - 1])
				collection.append([newY, x - 1])
			if char2 == '[':
				incl.append([newY, x + 1])
				collection.append([newY, x + 1])
		return incl

	def part1(self):
		y, x = self.getCoordinates()
		for step in self.movements:
			self.map[y][x] = '@'
			print(step)
			for line in self.map:
				print(line)
			self.map[y][x] = '.'
			dY, dX, direction = self.move(step)
			newY = dY + y
			newX = dX + x
			char = self.map[newY][newX]
			
			if char == '.':
				y = newY
				x = newX
				continue
			elif char == '#':
				continue
			elif char in "[]":
				startX = newX
				startY = newY
				if  direction == 'y-as':
					if char == '[':
						ball = [newY, newX]
					else:
						ball = [newY, newX - 1]
					inclBalls = self.searchBalls(ball, dY, dX)
					if inclBalls == False:
						print(step)
						continue
					if len(inclBalls) > 0:
						self.moveBalls(inclBalls, dY, dX)
					else:
						return
				else:
					while self.map[newY][newX] == '[' or self.map[newY][newX] == ']':
						newX += dX
					if self.map[newY][newX] == '#':
						continue
					elif self.map[newY][newX] == '.':
						self.map[newY][newX] = self.map[newY][newX - dX]
						while newX != startX:
							newX -= dX
							self.map[newY][newX] = self.map[newY][newX - dX]
				self.map[startY][startX] = '@'
				y = startY
				x = startX
			for line in self.map:
				for i, char in enumerate(line):
					if char == '[' and line[i + 1] == '.':
						for line in self.map:
							print(step, line)

		total = 0
		for i, line in enumerate(self.map):
			for j, char in enumerate(line):
				if char == '[':
					total += 100 * i + j
		return total

def main():
	input = open("input.txt", "r").read()
	movements = open("input1.txt", "r").read()

	sol = Solution(input, movements)
	print("Part 1:", sol.part1(), 1554058)

if __name__ == "__main__":
	main()

# 1569991 too high
# 1543425 too low