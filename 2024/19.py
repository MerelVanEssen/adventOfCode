from functools import cache

class Solution:
	def __init__(self, input):
		input = input.split('\n')
		self.towels = input[0].replace(" ", "").split(',')
		self.design = input[2:]

	def recursiveSearch(self, design):
		if len(design) == 0:
			return True
	
		for towel in self.towels:
			if design.startswith(towel):
				if self.recursiveSearch(design[len(towel):]):
					return True
		return False

	@cache
	def recursiveSearch2(self, design):
		if len(design) == 0:
			return 1
		total = 0
		for towel in self.towels:	
			if design.startswith(towel):
				total += self.recursiveSearch2(design[len(towel):])
		return total
		
	def part(self):
		total1 = 0
		total2 = 0
		for design in self.design:
			if self.recursiveSearch(design) == True:
				total1 += 1
			total2 += self.recursiveSearch2(design)
		return total1, total2

def main():
	input = open("input/19.txt", "r").read()

	sol = Solution(input)
	print("Part 1 & Part 2:", sol.part())

if __name__ == "__main__":
	main()