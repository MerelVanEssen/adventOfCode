from collections import deque

class Solution:
	def __init__(self):
		self.COLORNAMES = ["blue", "red", "green"]
		self.AMOUNT = [14, 12, 13]

	def part1and2(self, input):
		awnser = 0
		awnser2 = 0
		lines = input.split('\n')

		for line in lines:
			game, data = line.split(': ')
			groups = data.split(";")
			isValid = True
			max_colors = [0] * 3

			for group in groups:
				colors = group.split(",")
				saveNrs = [0] * 3

				for color in colors:
					nr, color = color.split()
					index = self.COLORNAMES .index(color)
					saveNrs[index] += int(nr)
					if saveNrs[index] > self.AMOUNT[index]:
						isValid = False

					max_colors = [max(max_colors[i], saveNrs[i]) for i in range(3)]

			awnser2 += max_colors[0] * max_colors[1] * max_colors[2]
			if isValid:
				gameWord, gamenr = game.split()
				awnser += int(gamenr)

		return (awnser, awnser2)

def main():
	sol = Solution()
	with open("input/02.txt", "r") as f:
	input = f.read()
	print(sol.part1and2(input))

if __name__ == "__main__":
	main()
