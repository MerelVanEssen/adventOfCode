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
		self.lines = []
		lines = input.split('\n')
		for line in lines:
			seq, nrs = line.split()
			self.lines.append([seq, list(map(int, nrs.split(',')))])
		self.total = 0
		
	def calculateStartEndPos(self, seq, nrs):
		rightLines = set()
		posNrs = []
		pos = 0
		for nr in nrs:
			posNrs.append([pos, 0])
			pos += nr + 1
		i = len(posNrs) - 1
		spaceLeft = len(seq) - 1
		while i >= 0:
			posNrs[i][1] = spaceLeft
			spaceLeft -= (nrs[i] + 1)
			i -= 1
		return nrs

	def countPossibilities(self, seq, nrs, posNrs):

		for i in range(len(posNrs)):
			j = i + 1
			while posNrs[i][0] <= posNrs[i][1]:
				for j in range(i + 1, len(posNrs), 1):
					savePos = posNrs[j][:]
					while posNrs[j][0] <= posNrs[j][1]:
						self.checkLine()
						posNrs[j][0] += 1
					posNrs[j] = savePos[:]
				posNrs[i][0] += 1

	
	def part1(self):
		total = 0
		

		for seq, nrs in self.lines:
			ic (seq, nrs)
			posNrs = self.calculateStartEndPos(seq,nrs)
			self.countPossibilities(seq, nrs, posNrs)

def main():
	with open("input.txt", "r") as f:
		input = f.read()

	sol = Solution(input)
	print("Part 1:", sol.part1())
	# print("Part 2:", sol.part2())

if __name__ == "__main__":
	main()
