from collections import deque
import re
from icecream import ic # source myenv/bin/activate

# self.hands = [[] for _ in range(7)]
# inte = [int(x) for x in line]

class Solution:
	def __init__(self, input):
		lines = input.split()

	def part1(self, input):
		awnser = 0
		return (awnser)

	def part2(self, input):
		awnser = 0
		return (awnser)	

def main():
	sol = Solution()
	with open("input.txt", "r") as f:
		input = f.read()

	print("Part 1:" sol.part1(input))
	print("Part 2:" sol.part2(input))
	f.close() 

if __name__ == "__main__":
	main()
