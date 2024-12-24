import re
from collections import deque, Counter
from math import gcd
from functools import reduce, cache
from aoc import turnMapBackwardsList
import heapq

# self.hands = [[] for _ in range(7)]
# inte = [int(x) for x in line]
# self.field = [['.' for _ in row] for row in self.map]

class Solution:
	def __init__(self, input):

		pattern = r"(\w+): ([01])"
		gates = re.findall(pattern, input)
		self.gates = deque()
		for gatenr, pulse in gates:
			self.gates.append([gatenr, pulse])
		
		pattern = r"(\w+) (\w+) (\w+) -> (\w+)"
		wires = re.findall(pattern, input)

		self.wires = []
		for income1, gate, income2, receiver in wires:
			self.wires.append([gate, income1, income2, receiver, 0, 0, 0])




	def part1(self):
		collectZ = []

		while self.gates:
			gatenr, pulse = self.gates.popleft()

			pulse = int(pulse)
			
			if gatenr[0] == 'z':
				collectZ.append([gatenr, pulse])
				continue
		
			# update the signals
			for i, wire in enumerate(self.wires):
				gate, income1, income2, receiver, get, p1, p2 = wire

				# first update the amount
				if income1 == gatenr:
					self.wires[i][5] = pulse
					if self.wires[i][4] == 1:
						continue
					self.wires[i][4] += 1
				elif income2 == gatenr:
					self.wires[i][6] = pulse
					if self.wires[i][4] == 2:
						continue
					self.wires[i][4] += 2
			

			for i, wire in enumerate(self.wires):
				gate, income1, income2, receiver, get, p1, p2 = wire

				if self.wires[i][4] != 3:
					continue
				self.wires[i][4] = 0

				if gate == "OR":
					if self.wires[i][5] == 1 or self.wires[i][6] == 1:

						self.gates.append([receiver, 1])
					else:
						self.gates.append([receiver, 0])
				elif gate == 'AND':
					if self.wires[i][5] == 1 and self.wires[i][6] == 1:
						self.gates.append([receiver, 1])
					else:
						self.gates.append([receiver, 0])
				elif gate == 'XOR':
					if int(self.wires[i][5]) ^ int(self.wires[i][6]):
						self.gates.append([receiver, 1])
						self.wires[i][5] = 0
						self.wires[i][6] = 0
					else:
						self.gates.append([receiver, 0])
						self.wires[i][5] = 0
						self.wires[i][6] = 0
		collectZ.sort()

		bits = ""
		for nr, bit in collectZ:
			bits += "".join(str(bit))
		
		return int(bits[::-1], 2)

	def part2(self):
		total = 0

		return total

def main():
	try:
		input = open("input/24.txt", "r").read()
	except OSError as err:
		print("Error", err)
		return

	sol = Solution(input)
	print("Part 1:", sol.part1())
	print("Part 2:", sol.part2())

if __name__ == "__main__":
	main()