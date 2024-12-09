from collections import deque
from math import gcd
from functools import reduce
import re
from collections import Counter
from aoc import turnMap

def checkOneDifference(list1, list2):
	differences = [
		(i, a, b)
		for i, (a, b) in enumerate(zip(list1, list2))
		if a != b
	]
	return len(differences)

def searchMirrorPart2(lines):
	# search from each position if the lines are the same
	for i in range(len(lines)):
		z = 0
		usedFix = False
		while i + z + 1 < len(lines) and i - z >= 0:
			if lines[i - z] != lines[i + z + 1]:
				if usedFix == True:
					usedFix = False
					break
				diff = checkOneDifference(lines[i-z],lines[i+z+1])
				if diff == 1:
					usedFix = True
				else:
					break
			z += 1
		if usedFix == True and (i - z <= 0 or i + z + 1 >= len(lines) - 1):
			return i + 1
	return 0

def searchMirror(lines):
	# search from each position if the lines are the same
	for i in range(len(lines)):
		z = 0
		while i+z+1 < len(lines) and i-z >= 0 and lines[i-z] == lines[i+z+1]:
			if i-z == 0 or i+z+1 == len(lines) - 1:
				return i + 1
			z += 1
	return 0

# Splits input in maps and creates a normal map and one that is turned 90°
def loopMaps(maps):
	rows = 0
	columns = 0
	rows2 = 0
	colums2 = 0
	map = []
	for line in maps:
		if len(line) > 0:
			map.append(line)
		elif len(map) > 0:
			value1 = searchMirror(map)
			value2 = searchMirrorPart2(map)
			rows += value1
			rows2 += value2
			if value1 == 0:
				columns += searchMirror(turnMap(map))
			if value2 == 0:
				colums2 += searchMirrorPart2(turnMap(map))
			map = []
	return (100 * rows + columns), (100 * rows2 + colums2)
	  
def main():
	with open("input/13.txt", "r") as f:
		input = f.read()

	maps = input.split('\n')
  
	print("Part 1 & 2", loopMaps(maps))
 
if __name__=="__main__":
	main()