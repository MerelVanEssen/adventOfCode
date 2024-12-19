from functools import cache

class Solution:
	def __init__(self, input):
		self.lines = []
		lines = input.split('\n')
		for line in lines:
			seq, nrs = line.split()
			self.lines.append([seq, tuple(map(int, nrs.split(',')))])
	
	@cache
	def recursiveBlockPlacing(self, blocks, nrs):

		if len(blocks) == 0:
			if len(nrs) == 0:
				return 1
			else:
				return 0
		
		if len(nrs) == 0:
			if blocks.count("#") == 0:
				return 1
			else:
				return 0
		if len(blocks) < sum(nrs) + len(nrs) - 1:
			return 0
		
		total = 0
		if blocks[0] in "#?" and "." not in blocks[:nrs[0]] and len(blocks) >= nrs[0]:
			if len(blocks) == nrs[0]:
				total += self.recursiveBlockPlacing(blocks[nrs[0] + 1:], nrs[1:])
			elif blocks[nrs[0]] in ".?":
				total += self.recursiveBlockPlacing(blocks[nrs[0] + 1:], nrs[1:])
		if blocks[0] in ".?":
			total += self.recursiveBlockPlacing(blocks[1:], nrs)

		return total

	def part1(self):
		total = 0
		for seq, nrs in self.lines:
			check = self.recursiveBlockPlacing(seq, nrs)
			total += check
		return total

	def part2(self):
		total = 0
		for seq, nrs in self.lines:
			seq = seq + "?" + seq + "?" + seq + "?" + seq + "?" + seq
			nrs *= 5
			check = self.recursiveBlockPlacing(seq, nrs)
			total += check
		return total
		
def main():
	with open("input/12.txt", "r") as f:
		input = f.read()

	sol = Solution(input)
	print("Part 1:", sol.part1())
	print("Part 2:", sol.part2())

if __name__ == "__main__":
	main()
