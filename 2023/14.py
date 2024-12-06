from collections import deque
from math import gcd
from functools import reduce
import re
from aoc import turnMapBackwardsList
# self.hands = [[] for _ in range(7)]
# inte = [int(x) for x in line]
# newMap = [[] for _ in range(len(map[0]))]

class Solution:
	def __init__(self, input):
		self.map = input.split('\n')
		for i in range(len(self.map)):
			self.map[i] = [x for x in self.map[i]]
	
	# turn map 90 degrees backwards
	# def turnMap(self, map):
	# 	newMap = [[] for _ in range(len(map[0]))]
	# 	for line in map:
	# 		for i, char in enumerate(line):
	# 			newMap[i].insert(0, char)
	# 	return newMap

	def moveField(self):
		saveShapeRocks = [0 for x in self.map[0]]
		for i, row in enumerate(self.map):
			for j, step in enumerate(row):
				if step == '#':
					saveShapeRocks[j] = i + 1
				elif step == 'O':
					self.map[i][j] = '.'
					self.map[saveShapeRocks[j]][j] = 'O'
					saveShapeRocks[j] += 1

	def calculateWeight(self):
		weight = 0
		lineWeight = len(self.map)
		for line in self.map:
			weight += lineWeight * line.count('O')
			lineWeight -= 1
		return(weight)
	
	def part1(self):
		self.moveField()
		return (self.calculateWeight())
	
	def makeSet(self):
		stringSet = ""
		for line in self.map:
			stringSet += ''.join(line)
		return stringSet

	# searching when the field repeats itself and calculate the steps between
	def part2(self):
		saveFields = set()
		saveFirstField = set()
		saveIndex = []
		i = 0
		while i < 1000000000:
			for j in range(4):
				self.moveField() #North / East / South / West
				self.map = turnMapBackwardsList(self.map)
			saveSet = (self.makeSet())
			if saveSet in saveFields:
				saveIndex.append(i)
				if len(saveIndex) == 1:
					saveFirstField.add(saveSet)
				elif saveSet in saveFirstField:
					rounds = i - saveIndex[0]
					i = 1000000000 - ((1000000000 - saveIndex[0]) % rounds)
			saveFields.add(saveSet)
			i += 1
		return (self.calculateWeight())

def main():
	with open("input/14.txt", "r") as f:
		input = f.read()

	sol = Solution(input)
	print("Part 1", sol.part1(), 108826)
	print("Part 2", sol.part2(), 99291)

if __name__ == "__main__":
	main()
