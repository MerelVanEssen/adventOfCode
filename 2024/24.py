import re
from collections import deque, Counter
from math import gcd
from functools import reduce, cache
from aoc import turnMapBackwardsList
import heapq
from z3 import *

# self.hands = [[] for _ in range(7)]
# inte = [int(x) for x in line]
# self.field = [['.' for _ in row] for row in self.map]

class Solution:
	def __init__(self, input):

		pattern = r"(\w+): ([01])"
		gates = re.findall(pattern, input)
		self.gates = deque()
		for gatenr, pulse in gates:
			self.gates.append([gatenr, pulse, []])
		
		pattern = r"(\w+) (\w+) (\w+) -> (\w+)"
		wires = re.findall(pattern, input)

		self.wires = []
		for income1, gate, income2, receiver in wires:
			self.wires.append([gate, income1, income2, receiver, 0, 0, 0])
		self.saveFound = []
		self.solver = Solver()

	def part1(self, toSwap, solver):
		collectZ = []

		while self.gates:
			gatenr, pulse, nrs = self.gates.popleft()

			pulse = int(pulse)
			
			if gatenr[0] == 'z':
				searchFor = nrs[0]
				matchNr = 'z' + nrs[1:]
				self.solver.add(searchFor = matchNr)
				collectZ.append([gatenr, pulse, nrs])
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
			
			def checkxy(part1, part2, nrs):
				if part1[0] in 'yx' and part2[0] in 'yx':
					nrs.append(part1[1:])
				return nrs

			def changeReciever(receiver, swapValues):
				for i, value in enumerate(swapValues):
					if receiver == value:
						if i % 2 == 0:
							receiver = swapValues[i+1]
							swapValues.remove(i + 1)
							swapValues.remove(i)
						else:
							receiver = swapValues[i-1]
							swapValues.remove(i)
							swapValues.remove(i-1)			
				return receiver, swapValues

			for i, wire in enumerate(self.wires):
				gate, income1, income2, receiver, get, p1, p2 = wire

				receiver, toSwap = changeReciever(receiver, toSwap)
				if self.wires[i][4] != 3:
					continue
				self.wires[i][4] = 0

				if gate == "OR":
					if self.wires[i][5] == 1 or self.wires[i][6] == 1:
						self.gates.append([receiver, 1, checkxy(income1, income2, nrs)])
					else:
						self.gates.append([receiver, 0, checkxy(income1, income2, nrs)])
				elif gate == 'AND':
					if self.wires[i][5] == 1 and self.wires[i][6] == 1:
						self.gates.append([receiver, 1, checkxy(income1, income2, nrs)])
					else:
						self.gates.append([receiver, 0, checkxy(income1, income2, nrs)])
				elif gate == 'XOR':
					if int(self.wires[i][5]) ^ int(self.wires[i][6]):
						self.gates.append([receiver, 1, checkxy(income1, income2, nrs)])
						self.wires[i][5] = 0
						self.wires[i][6] = 0
					else:
						self.gates.append([receiver, 0, checkxy(income1, income2, nrs)])
						self.wires[i][5] = 0
						self.wires[i][6] = 0
		
		swap = []
		for nr, bit, nrs in collectZ:
			if nr[1:] != nrs[0]:
				swap.append(nr)
		if len(toSwap) == 0 and len(nrs) == 0:
			return True
		return False
	
	def part2(self):
		total = 0

		
		def search(wires):
			save = {}
			for i , wire in enumerate(wires):
				gate, income1, income2, receiver, get, p1, p2 = wire
				if receiver[0] == "z":
					nr = int(receiver[1:])
					save[nr] = [[income1, income2]]

			for _ in range(10):
				for i , wire in enumerate(wires):
					gate, income1, income2, receiver, get, p1, p2 = wire
					for key, values in save.items():
						value = values[-1]
						if value[0][0] in "xy":
							continue
						if receiver in value:
							values.append([income1, income2])
							save[nr] = values

			wrong = 0
			for line, values in save.items():
				value = values[-1][0]
				value = int(value[1:])
				if value != line:
					wrong += 1
			if wrong < 28:
				print("WRONG:", wrong)
		

		labels = ['pmf','fcn','rws','gwq','rrq','gjw','wjm','cgm','qbr','qsr','vqp','frr','fhs','fjs','knw','hwq','cdf','cmn','qwd','ntb','djg','kpw','qvq','cdn','qvh','fpc','vkv','bbc','qgg','pbq','ncj','dvw','jdt','rsm','dhh','jdj','stq','dgj']
		for i, label1 in enumerate(labels):
			for j, label2 in enumerate(labels):
				if i != j:
					copywires = self.wires[:]
					saveIndex = [-1,-1]
					for i, item in enumerate(self.wires):
						if item[3] == label1 and saveIndex[0] == -1:
							saveIndex[0] = i
						elif item[3] == label2 and saveIndex[1] == -1:
							saveIndex[1] = i
						if -1 not in saveIndex:
							break
					print(i, j, copywires[i][3], copywires[j][3])
					copywires[i][3], copywires[j][3] = copywires[j][3], copywires[i][3]
					search(copywires)
							
		# labels = []
		# for line, values in save.items():
		# 	for pair in values:  # Itereer door elk paar in de lijst
		# 		labels.extend(pair)

		# # Tel de frequentie van elk label
		# label_counts = Counter(labels)

		# # Print de frequenties
		# for label, count in label_counts.items():
		# 	if count >= 2 and label[0] not in "yx":
		# 		print(f"{label}: {count}")

		return total

def main():
	try:
		input = open("input/24.txt", "r").read()
	except OSError as err:
		print("Error", err)
		return

	sol = Solution(input)
	# print("Part 1:", sol.part1([]))
	print("Part 2:", sol.part2())

if __name__ == "__main__":
	main()