from collections import deque
from icecream import ic # source myenv/bin/activate
import re

class Solution:
	PATTERN = r"mul\(\d+,\d+\)"

	def __init__(self, input):
		self.lines = input

	# search for pattern (nr,nr) and multiply the nrs, returns total sum
	def calculateMatches(self, line):
		match = re.findall(self.PATTERN, line)
		total = 0
		for m in match:
			nrs = m[4:].replace(")", "")
			nr = nrs.split(',')
			total += (int(nr[0]) * int(nr[1]))
		return total

	# Part 1
	def part1(self):
		return (self.calculateMatches(self.lines))

	# Part 2 Splits on "do()" and than takes the relevant part till "don't" for calculate the matches
	def part2(self):
		totalsum = 0
		lines = self.lines.split("do()")
		for line in lines:
			if len(line) > 0:
				dontIndex = line.find("don't()")
				if dontIndex != -1:
					totalsum += self.calculateMatches(line[:dontIndex])
				else:
					totalsum += self.calculateMatches(line)
		return (totalsum)

def main():
	
	with open("input/03.txt", "r") as f:
		input = f.read()

	sol = Solution(input)
	print("Part 1", sol.function1())
	print("Part 2", sol.function2())

if __name__ == "__main__":
	main()
