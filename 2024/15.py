class Solution:
	def __init__(self, input):
		input = input.split("\n\n")
		prep = input[0].split()
		self.movements = input[1].replace("\n", "")
		self.lenY = len(prep)
		self.lenX = len(prep[0])
		self.start1 = []
		self.start2 = []
		self.field = []
		self.field2 = []

		# Part 1
		for i in range(len(prep)):
			self.field.append([x for x in prep[i]])

		# Part 2 double the field	
		for i in range(len(self.field)):
			line = []
			for j in range(len(self.field[i])):
				if self.field[i][j] == '#':
					line.append('#')
					line.append('#')
				elif self.field[i][j] == '@':
					self.field[i][j] = '.'
					self.start1 = [i, len(line) / 2]
					self.start2 = [i, len(line)]
					line.append('.')
					line.append('.')
				elif self.field[i][j] == 'O':
					line.append('[')
					line.append(']')
				elif self.field[i][j] == '.':
					line.append('.')
					line.append('.')
			self.field2.append(line[:])

	def moveBalls(self, balls, dY):
		balls = list(sorted(balls))
		if dY == 1:
			balls.reverse()
		for y, x in balls:
			self.map[y][x] = '.'
			self.map[y][x + 1] = '.'
			newY = y + dY
			self.map[newY][x] = '['
			self.map[newY][x + 1] = ']'

	# dfs through the balls that are in the same direction
	def searchBalls(self, ball, dY):
		incl = []
		collection = set()
		incl = set()
		collection.add((ball[0], ball[1]))
		incl.add((ball[0], ball[1]))

		while collection:
			y, x = collection.pop()
			newY = y + dY
			char, char2 = self.map[newY][x], self.map[newY][x + 1]
			if char == '#' or char2 == '#':
				return False
			elif char == '[':
				incl.add((newY, x))
				collection.add((newY, x))
			elif char == ']':
				incl.add((newY, x - 1))
				collection.add((newY, x - 1))
			if char2 == '[':
				incl.add((newY, x + 1))
				collection.add((newY, x + 1))
		return incl

	# calculate how far every block is from the left corner
	def calculateSum(self):
		total = 0
		for i, line in enumerate(self.map):
			for j, char in enumerate(line):
				if char in '[O':
					total += 100 * i + j
		return total

	def part(self, part):
		dir = {'>': [0,1,'x'], '<': [0,-1,'x'], '^': [-1,0,'y'], 'v': [1,0,'y']}

		if part == 1:
			self.map = self.field
			y, x = self.start1
		else:
			self.map = self.field2
			y, x = self.start2
		for step in self.movements:
			dY, dX, direction = dir[step]
			newY = dY + y
			newX = dX + x
			char = self.map[newY][newX]
			
			if char == '.':
				y, x = newY, newX
				continue
			elif char == '#':
				continue
			elif char in "[]O":
				startX = newX
				startY = newY
				if direction == 'y' and char != 'O':
					if char == '[':
						assert self.map[newY][x + 1] == ']'
						ball = [newY, x]
					else:
						assert self.map[newY][x - 1] == '['
						ball = [newY, x - 1]
					inclBalls = self.searchBalls(ball, dY)
					if inclBalls == False:
						continue
					if len(inclBalls) > 0:
						self.moveBalls(inclBalls, dY)		
				elif direction == 'x' or char == 'O':
					while self.map[newY][newX] in '[]O':
						newX += dX
						newY += dY
					if self.map[newY][newX] == '#':
						continue
					elif self.map[newY][newX] == '.':
						self.map[newY][newX] = self.map[newY - dY][newX - dX]
						while newX != startX or newY != startY:
							newX -= dX
							newY -= dY
							self.map[newY][newX] = self.map[newY - dY][newX - dX]
				y = startY
				x = startX
		return self.calculateSum()

def main():
	input = open("input.txt", "r").read()

	sol = Solution(input)
	print("Part 1:", sol.part(1))
	print("Part 1:", sol.part(2))

if __name__ == "__main__":
	main()
