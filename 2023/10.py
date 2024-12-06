from collections import deque
import re
from collections import Counter
from icecream import ic # source myenv/bin/activate

UP = [-1,0]
DOWN = [1,0]
LEFT = [0,-1]
RIGHT = [0,1]

class Solution:
	def __init__(self, input):
		self.map = input.split('\n')
		self.field = []
		self.pipes = {	'J' : [LEFT,UP],
						'L' : [RIGHT,UP],
						'|' : [DOWN,UP],
						'-' : [LEFT,RIGHT],
						'7' : [LEFT,DOWN],
						'F' : [RIGHT,DOWN]}
		self.d = [DOWN,LEFT,UP,RIGHT]
		self.contra = [UP,RIGHT,DOWN,LEFT]

	def switchDir(self, pipe, lastDir):	
		if lastDir == DOWN and (pipe == 'J' or pipe == 'L'):
			return self.pipes[pipe][0]
		elif pipe == 'J' or pipe == 'L':
			return UP
		elif lastDir == UP and (pipe == '7' or pipe == 'F'):
			return self.pipes[pipe][0]
		elif pipe == '7' or pipe == 'F':
			return DOWN
		return lastDir

	def part1(self):
		start = [0,0]
		for i, row in enumerate(self.map):
			index = row.find('S')
			if index != -1:
				start = [i,index]
				break

		for d in self.d:
			self.field = [['.' for _ in row] for row in self.map]
			start[0] += d[0]
			start[1] += d[1]
			x,y = start
			steps = 0
			lastDir = d
			while True:
				steps += 1
				if not 0 <= x < len(self.map) and not 0 <= y < len(self.map[0]):
					continue
				pipe = self.map[x][y]
				if pipe == 'S':
					self.field[x][y] = pipe
					return steps // 2	
				if pipe not in self.pipes:
					continue
				self.field[x][y] = pipe
				curr = self.switchDir(pipe, lastDir)
				lastDir = curr
				x += curr[0]
				y += curr[1]
		return 0
	
	def pipeS(self):
		start = [0,0]
		for i, row in enumerate(self.map):
			index = row.find('S')
			if index != -1:
				start = [i,index]
				break
		if self.field[i][index - 1] == '.' and self.field[i - 1][index]:
			self.field[i][index] = 'J'
		elif self.field[i][index - 1] == '.' and self.field[i][index + 1]:
			self.field[i][index] = '-'
		elif self.field[i][index - 1] == '.' and self.field[i + 1][index]:
			self.field[i][index] = '7'
		elif self.field[i + 1][index] == '.' and self.field[i][index + 1]:
			self.field[i][index] = 'L'
		elif self.field[i][index + 1] == '.' and self.field[i - 1][index]:
			self.field[i][index] = 'F'
		elif self.field[i - 1][index] == '.' and self.field[i + 1][index]:
			self.field[i][index] = '|'

	def part2(self):
		blocks = 0
		self.pipeS()
		for i, line in enumerate(self.field):
			inside = False
			upordown = UP
			for j, char in enumerate(line):
				if inside == True and char == '.':
					self.field[i][j] = 'O'
					blocks += 1
				if char == 'L':
					upordown = UP
					inside = True
				elif char == 'F':
					upordown = DOWN
					inside = True
				elif inside == True and char == 'J':
					if upordown == UP:
						inside = False
				elif inside == True and char == '7':
					if upordown == UP:
						inside = False
				elif char == '|':
					if inside == False:
						inside = True
					else:
						inside = False
			print (line)
	    
		return blocks

def main():
	with open("input/10.txt", "r") as f:
		input = f.read()

	sol = Solution(input)
	print("Part 1:", sol.part1())
	print("Part 2:", sol.part2(), 349)
	f.close() 

if __name__ == "__main__":
	main()
