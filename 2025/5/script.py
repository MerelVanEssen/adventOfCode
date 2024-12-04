from collections import deque
from math import gcd
from functools import reduce
import re
from icecream import ic # source myenv/bin/activate

# self.hands = [[] for _ in range(7)]
# inte = [int(x) for x in line]

class Solution:
	def __init__(self, input):
		self.lines = input.split('\n')

	def part1(self):
		awnser = 0
		return (awnser)
	
	def part1(self):
		awnser = 0
		return (awnser)

def main():
	with open("input.txt", "r") as f:
		input = f.read()

	sol = Solution(input)
	print("Part 1", sol.part1())
	print("Part 2", sol.part2())

if __name__ == "__main__":
	main()
