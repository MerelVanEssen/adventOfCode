class Solution:
	def __init__(self, input):
		self.map = input.split('\n')
		self.total1 = 0
		self.total2 = 0
	
	def recursive(self, i, j, collect, visited):
		if int(self.map[i][j]) != collect:
			return

		if self.map[i][j] == '9':
			self.total2 += 1
			if (i,j) not in visited:
				visited.add((i, j))
				self.total1 += 1
			return

		directions = ((0,1), (1, 0), (-1, 0), (0, -1))
		for d in directions:
			iNew = i + d[0]
			jNew = j + d[1]
			if 0 <= iNew < len(self.map) and 0 <= jNew < len(self.map[0]):
				self.recursive(iNew, jNew, collect + 1, visited)

	def part(self):
		for i, line in enumerate(self.map):
			for j, char in enumerate(line):
				if char == '0':
					self.recursive(i, j, 0, set())
		return self.total1, self.total2

def main():
	input = open("input/10.txt", "r").read()

	sol = Solution(input)
	print("Part 1 & 2:", sol.part())

if __name__ == "__main__":
	main()