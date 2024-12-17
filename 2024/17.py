import re

class Solution:
	def __init__(self, input):
		pattern = r"Register [A-C]: (\d+)"
		matches = re.findall(pattern, input)
		self.A = int(matches[0])
		self.B = int(matches[1])
		self.C = int(matches[2])

		index = input.index('m')
		input = input[index + 3:]
		nrs = input.split(',')
		self.P = [int(nr) for nr in nrs]
		self.goal = self.P[::-1]
	
	# Transfor the operand if it is 4, 5 or 6
	def getCombo(self, operand):
		if operand <= 3:
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

	# Recursive function to find the matching result
	def findIndex(self, index, depth):
		if depth == len(self.goal):
			return (index)

		for i in range(8):
			self.A = index * 8 + i
			self.B = 0
			self.C = 0
			outcome = self.part1()
			if outcome and outcome[0] == self.goal[depth]:
				if result:= self.findIndex((index * 8 + i), depth + 1):
					return result
		return 0

	def part2(self):
		result = self.findIndex(0, 0)
		return result

def main():
	input = open("input/17.txt", "r").read()

	sol = Solution(input)
	print("Part 1:", sol.part1())
	print("Part 2:", sol.part2())

if __name__ == "__main__":
	main()