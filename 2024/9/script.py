from collections import deque

class Solution:
	def __init__(self, input):
		self.lines = input.split('\n')
		for i in range(len(self.lines)):
			self.lines[i] = list(map(int, self.lines[i].split()))

	def part(self):
		totalPart1 = 0
		totalPart2 = 0

		for numbers in self.lines:
			piramid = [numbers]
			totalPart1 += numbers[-1]
			found = False
			i = 0
			while found == False:
				newLayer = []
				for j in range(len(piramid[i]) - 1):
					newLayer.append(piramid[i][j + 1] - piramid[i][j])
				if all(nr == 0 for nr in newLayer):
					break
				piramid.append(newLayer[:])
				totalPart1 += newLayer[-1]
				i += 1
			
			# Part 2 calculate every first nr of the row
			i = len(piramid) - 1
			total = 0
			while i >= 0:
				total = piramid[i][0] - total
				i -= 1
			totalPart2 += total
		return (totalPart1, totalPart2)

def main():
	with open("input.txt", "r") as f:
		input = f.read()

	sol = Solution(input)
	print("Part 1:", sol.part())
	f.close() 

if __name__ == "__main__":
	main()
