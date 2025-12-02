# Advent of Code 2021 Day 1: Sonar Sweep

from collections import deque

def part1(lines):
	total = 0
	last = None
	for line in lines:
		n = int(line)
		if last and n > last:
			total += 1
		last = n
	return total

def part2(lines):
	total = 0
	deque_window1 = deque(maxlen=3)
	deque_window2 = deque(maxlen=3)
	for line in lines:
		n = int(line)
		deque_window1.append(n)
		if len(deque_window1) > 1:
			deque_window2.append(deque_window1[-2])
		if len(deque_window1) == 3 and len(deque_window2) == 3:
			if sum(deque_window1) > sum(deque_window2):
				total += 1
		if (len(deque_window1) > 3):
			deque_window1.popleft()
		if (len(deque_window2) > 3):
			deque_window2.popleft()
	return total

def main():
	filename = "input/01.txt"
	print("Using input file:", filename)
	f = open(filename, "r")
	input = f.read()
	lines  = input.split('\n')
	print("Part 1:", part1(lines))
	print("Part 2:", part2(lines))
	f.close() 

if __name__ == "__main__":
	main()