from math import gcd
import re

# Problem:
# a1x + b1y = c1
# a2x + b2y = c2

class Solution:
	def __init__(self, input):
		self.input = input
		self.results = []
		pattern = r"(Button [AB]|Prize): X[+=]?(\d+), Y[+=]?(\d+)"
		matches = re.findall(pattern, self.input)
		saveList = []
		for match in matches:
			if match:
				x_value = int(match[1])
				y_value = int(match[2])
				saveList.append(x_value)
				saveList.append(y_value)
				if len(saveList) == 6:
					self.results.append(saveList)
					saveList = []

 	# 		​c2​ ⋅ a1 - ​c1 ​⋅ a2​​
	# y =	-----------------	
	# 		a1 ​⋅ b2 ​- a2 ​⋅ b1

	# 		c1 - b1 * y 
	# x = 	-----------
	# 		     a1
	
	# method of elimination using determinants
	def solve(self, a1, b1, c1, a2, b2, c2):
		y = (c2 * a1 - c1 * a2) / (a1 * b2 - a2 * b1)
		x = (c1 - b1 * y) / a1
		return x, y

	def part(self, part):
			total = 0
			extra = 0

			if part == 2:
				extra = 10000000000000

			for a1, a2, b1, b2, c1, c2 in self.results:
				x, y = self.solve(a1, b1, c1 + extra, a2, b2, c2 + extra)
				if int(x) == x and int(y) == y:
					total += 3 * x + y
			return int(total)

def main():
	input = open("input/13.txt", "r").read()

	sol = Solution(input)
	print("Part 1:", sol.part(1))
	print("Part 2:", sol.part(2))

if __name__ == "__main__":
	main()