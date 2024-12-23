from collections import defaultdict
import itertools
import networkx as nx

class Solution:
	def __init__(self, input):
		input = input.split('\n')
		connections = [c.split('-') for c in input]
		self.dict = defaultdict(list)
		self.graph = nx.Graph()
		for c1, c2 in connections:
			self.graph.add_edge(c1, c2)
			self.dict[c1] += [c2]
			self.dict[c2] += [c1]

	def part1(self):
		groups = set()
		total = 0
		for c1, cons in self.dict.items():
			for c2 in cons:
				con = self.dict[c2]
				for c3 in con:
					co = self.dict[c3]
					if c1 in co:
						groups.add((c1,c2,c3))

		# sort the groups to exclude dubble ones		
		groups = set(tuple(sorted(group)) for group in groups)
		
		for c1, c2, c3 in list(groups):
			if 't' == c1[0] or 't' == c2[0] or 't' == c3[0]:
				total += 1
		return total

	def part2(self):
		# find biggest group
		groups = list(nx.find_cliques(self.graph))
		smallestGroup = []
		for item in groups:
			if len(item) > len(smallestGroup):
				smallestGroup = item
		smallestGroup.sort()
		return ",".join(smallestGroup)

def main():
	input = open("input/23.txt", "r").read()

	sol = Solution(input)
	print("Part 1:", sol.part1())
	print("Part 2:", sol.part2())

if __name__ == "__main__":
	main()