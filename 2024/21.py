import re
import heapq
from functools import lru_cache
from itertools import permutations
from collections import deque

class Solution:
	def __init__(self, input):
		self.seqs = input.split('\n')
		self.num = {'A': (3,2), '0': (3, 1), '1': (2,0), '2': (2, 1), '3': (2, 2), '4': (1, 0), '5': (1,1), '6': (1, 2), '7': (0, 0), '8': (0, 1), '9': (0, 2)}
		self.dir = {'^': (0,1), 'A': (0,2), '<': (1,0), 'v': (1,1), '>': (1,2)}

		self.nums = {(3,2): 'A', (3, 1): '0', (2,0): '1', (2, 1): '2' , (2, 2): '3', (1, 0): '4', (1,1): '5', (1, 2): '6', (0, 0): '7', (0, 1): '8', (0, 2): '9'}
		self.direct = {(0,1): '^', (0,2): 'A', (1,0): '<', (1,1): 'v', (1,2): '>'}
		self.numbers = []
		self.directions = []
		self.savePaths = []
		self.savePaths2 = []

	def getComb(self, dir):
		direction = {(-1,0): '^', (0,-1): '<', (1,0): 'v', (0,1): '>'}
		allDir = {}
		for y1, x1 in dir:
			for y2, x2 in dir:
				if (y1,x1) == (y2,x2):
					allDir[(y1,x1,y2,x2)] = ['A']
				else:
					savePaths = []
					deq = deque()
					deq.append([y1,x1,""])
					totalDis = abs(y1 - y2) + abs(x1 - x2)
					while deq:
						y, x, path = deq.popleft()

						if len(path) > totalDis:
							continue

						if (y,x) == (y2,x2):
							savePaths.append(path + 'A')

						for yd, xd in {(0,1), (1,0), (-1,0), (0,-1)}:
							yNew = y + yd
							xNew = x + xd
							if (yNew,xNew) in dir:	
								deq.append((yNew, xNew, path + direction[(yd,xd)]))

					allDir[(y1,x1,y2,x2)] = savePaths
		return allDir
							
	def generateCombinations(self):
		self.numbers = self.getComb(self.nums)
		self.directions = self.getComb(self.direct)
	

	def recursiveNums(self, seq, y, x, path):
		if not seq:
			self.savePaths.append(path)
			return
		ny, nx  = self.num[seq[0]]
		for part in self.numbers[(y, x, ny, nx)]:
			self.recursiveNums(seq[1:], ny, nx, path + part)
	
	@lru_cache
	def recursive(self, seq, y, x, path):
		if not seq:
			self.savePaths.append(path)
			return
		ny, nx = self.dir[seq[0]]
		for part in self.directions[(y, x, ny, nx)]:
			self.recursive(seq[1:], ny, nx, path + part)

	def part2(self):
		total = 0
		self.generateCombinations()
		for seq in self.seqs:
			minPath = float('inf')
			self.savePaths = []
			self.recursiveNums(seq, 3, 2, "")
			nextPath = self.savePaths[:]
			for i in range(25):
				saveP = nextPath
				nextPath = []
				for path in saveP:
					self.savePaths = []
					self.recursive(path, 0, 2, "")
					nextPath.extend(self.savePaths)
					if i == 24:
						for p in self.savePaths:
							minPath = min(minPath, len(p))
			print(seq, seq[:3], "*", minPath)
			total += int(seq[:3]) * minPath
		return total

def main():
	input = open("input/21.txt", "r").read()

	sol = Solution(input)
	# print("Part 1:", sol.part1(), 126384, 137870)
	print("Part 2:", sol.part2(), 170279148659464)

if __name__ == "__main__":
	main()