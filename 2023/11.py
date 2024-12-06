class Solution:
	def __init__(self, input):
		self.map = input.split('\n')

	def part(self, length):
		galx = []
		emptylines = 0
		emptyHorizon = [0] * len(self.map[0])
		length -= 1

		# Search for all the galaxies and already keeps track of the horizontal empty space
		for i, row in enumerate(self.map):
			galaxies = row.count('#')
			if galaxies == 0:
				emptylines += length
				continue
			index = -1
			while galaxies:
				if index == -1:
					index = row.find('#')
				else:
					index = row[index + 1:].find('#') + index + 1
				if index >= 0:
					galx.append([i + emptylines, index])
					emptyHorizon[index] = 1
				galaxies -= 1

		# Adding the empty spaces to the galaxy cordinates
		emptylines = 0
		for i in range(len(emptyHorizon)):
			if emptyHorizon[i] == 0:
				emptylines += length
			emptyHorizon[i] = emptylines
		
		for i in range(len(galx)):
			galx[i][1] += emptyHorizon[galx[i][1]]

		# Calculates the distance between all the galaxies
		minDistance = 0
		for i in range(len(galx)):
			j = i + 1
			while j < len(galx):
				if i != j:
					minDistance += abs(galx[i][0] - galx[j][0]) + abs(galx[i][1] - galx[j][1])
				j += 1
		return minDistance

def main():
	with open("input/11.txt", "r") as f:
		input = f.read()

	sol = Solution(input)
	expansion = 2
	print("Part 1:", sol.part(expansion), 9563821)
	expansion = 1000000
	print("Part 2:", sol.part(expansion), 827009909817)

if __name__ == "__main__":
	main()
