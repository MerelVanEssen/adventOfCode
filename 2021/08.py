# Advent of Code 2021 Day 8: Seven Segment Search

from collections import Counter

def part1(lines):
	total = 0
	wires = [2, 3, 4, 7]
	for line in lines:
		_ , nrs = line.split('|')
		nrs = nrs.split(' ')
		for nr in nrs:
			if len(nr) in wires:
				total += 1
	return total

def searchLetters(digit, s):
	found = 0
	for letter in digit:
		if letter in s:
			found += 1
	return found

def part2(lines):
	total = 0
	for line in lines:
		example, nrs = line.split('|')
		example = example.split(' ')
		digits = [''] * 10
		six = []
		five = []
		for nr in example:
			l = len(nr)
			if l == 2:
				digits[1] = nr
			elif l == 3:
				digits[7] = nr
			elif l == 4:
				digits[4] = nr
			elif l == 7:
				digits[8] = nr
			elif len(nr) == 6:
				six.append(nr)
			elif len(nr) == 5:
				five.append(nr)
				
		# search 9
		for i, s in enumerate(six):
			found = searchLetters(digits[4], s)
			if found == 4:
				digits[9] = s
				six.remove(s)
				break
		# search 0
		for i, s in enumerate(six):
			found = searchLetters(digits[1], s)
			if found == 2:
				digits[0] = s
				six.remove(s)
				break
		digits[6] = six[0]
		# search 3
		for i, s in enumerate(five):
			found = searchLetters(digits[1], s)
			if found == 2:
				digits[3] = s
				five.remove(s)
				break
		# search 5
		for i, s in enumerate(five):
			found = searchLetters(digits[4], s)
			if found == 3:
				digits[5] = s
				five.remove(s)
				break
		digits[2] = five[0]
		count = ''
		for nr in nrs.split():
			for i, digit in enumerate(digits):
				if Counter(nr) == Counter(digit):
					count += str(i)
		total += int(count)
	return total

filename = "input/08.txt"
print("Using input file:", filename)
f = open(filename, "r")
input = f.read()
lines  = input.split('\n')
print("Part 1:", part1(lines))
print("Part 2:", part2(lines))
f.close() 

# 701528 too low