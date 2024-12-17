import re
from collections import deque
from math import gcd
from functools import reduce
from collections import Counter
from aoc import turnMapBackwardsList
import heapq
from functools import cache

# self.hands = [[] for _ in range(7)]
# inte = [int(x) for x in line]
# self.field = [['.' for _ in row] for row in self.map]

class Solution:
	def __init__(self, A, B, C, P):
		self.A = A
		self.B = B
		self.C = C
		self.P = P
	
	def opcode0(self, regA, combo):
		regA = regA // (2 ** combo)
		return regA

	def opcode1(self, regB, lit): # bxl
		regB = regB ^ lit
		return regB

	def opcode2(self, combo): # bst
		regB = combo % 8
		if combo == 4:
			value = self.A
			regB = regB % value
		elif combo == 5:
			value = self.B
			regB = regB % value
		elif combo == 6:
			value = self.C
			regB = regB % value
		else:
			regB = combo % 8
		return regB
	
	def opcode3(self, regA, literacombo, instruction_pointer): # jnz niet +2
		if regA != 0:
			return literacombo
		return instruction_pointer + 2
	
	def opcode4(self, regB, regC): #bxc
		regB = regB ^ regC
		return regB
	
	def opcode5(self, combo): #out output
		return combo % 8

	def opcode6(self, regA, combo): # bdv
		regB = regA // (2 ** combo)
		return regB

	def opcode7(self, regA, combo):
		regC = regA // (2 ** combo)
		return regC

	def getCombo(self, operand):
		if operand >= 0 and operand <= 3:
			combo = operand
		elif operand == 4:
			combo = self.A
		elif operand == 5:
			combo = self.B
		elif operand == 6:
			combo = self.C
		else:
			combo = None
		return combo

	def part1(self):
		total = 0
		pointer = 0
		output = []

		while pointer < len(self.P):
			opcode = self.P[pointer]
			operand = self.P[pointer + 1]
			combo = self.getCombo(operand)
			
			if combo is not None:
				if opcode == 0:
					self.A = self.A // (2 ** combo)
				elif opcode == 1:
					self.B = self.B ^ operand
				elif opcode == 2:
					self.B = combo % 8
				elif opcode == 3:
					pointer = operand if self.A != 0 else pointer + 2
				if opcode == 4:
					self.B = self.B ^ self.C
				elif opcode == 5:
					output.append(combo % 8)
				elif opcode == 6:
					self.B = self.A // (2 ** combo)
				elif opcode == 7:
					self.C = self.A // (2 ** combo)
			if opcode != 3:
				pointer += 2
		return output

	def part2(self):
		total = 0
		A = B = C = 0
		program = self.P
		sindex = 105694709871369
		index = sindex
		while True:
			self.A = index
			self.B = 0
			self.C = 0
			output = self.part1()
			if index % sindex == 0:
				print (output, self.P, index, len(self.P), len(output))
			if output == self.P:
				break
			index += 1
			break
		return index
	
	# def part2(self):
	# 	a = 35282534841844
	# 	prev = 0
	# 	while True:
	# 		x = self.part1(a)
	# 		# if a % 1 == 0:
	# 		if x[:6] == [2, 4, 1, 2, 7, 5]:
	# 			print(a, len(x), a-prev, x)
	# 			prev = a
	# 		if x == self.P:
	# 			print(a)
	# 			break
	# 		# if len(x) < 16:
	# 		#     print(a)
	# 		#     a *= 2
	# 		a += 2097152

def main():
	# A = 729
	# B = 0

	# C = 0
	# P = 0, 1, 5, 4, 3, 0

	# A = 117440
	# B = 0
	# C = 0
	# P = [0,3,5,4,3,0]

	A = 61156655
	B = 0
	C = 0
	P = [2,4,1,5,7,5,4,3,1,6,0,3,5,5,3,0]

	sol = Solution(A,B,C,P)
	print("Part 1:", sol.part1())
	print("Part 2:", sol.part2(), 105694709871369)

if __name__ == "__main__":
	main()

# 735757430
# 747757470