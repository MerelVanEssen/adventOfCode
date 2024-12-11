#!/usr/bin/python3

class Solution:
	def __init__(self, input):
		self.map = input.split('\n')
		self.l = []
		index = 0
		for i, nr in enumerate(input):
			if i % 2 == 0: # file
				self.l += [index] * int(nr)
				index += 1
			else: # space
				self.l += ['.'] * int(nr)
		print("self", self.l)

	def calculateLen(self, i):
		j = 0
		save = self.l[i]
		while i + j < len(self.l) and self.l[i + j] == save:
			j += 1
		return j

	def calculateLenBack(self, i, j):
		save = self.l[j]
		length = 0
		while self.l[j - length] == save:
			if j - length == i:
				return length, True
			length += 1
		return length, False

	def removeBlock(self, j, length):
		print(j, length, j - length)
		start = j - length + 1
		while start <= j and start < len(self.l):
			self.l[start] = '.'
			start += 1

	def movingPart(self, i, j, length):
		z = 0
		while z < length and i + z < len(self.l) and j - z >= 0:
			self.l[i + z] = self.l[j - z]						
			z += 1
		self.removeBlock(j, length)

	def rotate(self):
		i = 0
		while i < len(self.l):
			length = self.calculateLen(i)
			print("round", length)
			if self.l[i] == '.':
				j = len(self.l) - 1
				while j > i:
					length2, ready = self.calculateLenBack(i, j)
					if ready == True:
						break
					print("len", length2)
					if self.l[j] != '.' and length2 <= length:
						self.movingPart(i, j, length2)
						i -= length - length2
						break
					j -= length2
			i += length
		print("end line", self.l)

	def part2(self):
		self.rotate()

def main():
	input = open("input/09.txt", "r").read()
	print(input)
	sol = Solution(input)
	# print("Part 1:", sol.part1())
	print("Part 2:", sol.part2(), 6382582136592)

if __name__ == "__main__":
	main()