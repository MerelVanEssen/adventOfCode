from aoc import countSymbolInMap

class Solution:
	def __init__(self, input):
		self.antennas = {}
		self.map = input.split('\n')
		for i in range(len(self.map)):
			self.map[i] = [x for x in self.map[i]]
			
		# Get coordinates from the antennas
		for i in range(len(self.map)):
			for j in range(len(self.map[i])):
				if self.map[i][j] != '.':
					if self.map[i][j] in self.antennas:
						self.antennas[self.map[i][j]].append([i,j])
					else:
						self.antennas[self.map[i][j]] =[[i,j]]
		self.total1 = set()
		self.total2 = set()

	# Part 1: saves the coordinates from an antinode in a set
	def setAntinodes1(self, xFactor, yFactor, xNew, yNew):
		for i in range(2):
			if 0 <= xNew[i] < len(self.map) and 0 <= yNew[i] < len(self.map):
				self.total1.add((xNew[i], yNew[i]))

	# Part 2: looping through the line off antennas till you reach the wall
	def setAntinodes2(self, xFactor, yFactor, xNew, yNew):
		for i in range(2):
			while 0 <= xNew[i] < len(self.map) and 0 <= yNew[i] < len(self.map):
				self.total2.add((xNew[i], yNew[i]))
				xNew[i] += xFactor[i]
				yNew[i] += yFactor[i]

	# Compares all the matching antennas with each other
	def part(self):
		for antennas in self.antennas.values():
			for i in range(len(antennas)):
				for j in range(i + 1, len(antennas), 1):
					antennaA = antennas[i]
					antennaB = antennas[j]
					self.total2.add((antennaA[0], antennaA[1]))
					self.total2.add((antennaB[0], antennaB[1]))
					xFactor = [antennaA[0] - antennaB[0], antennaB[0] - antennaA[0]]
					yFactor = [antennaA[1] - antennaB[1], antennaB[1] - antennaA[1]]
					xNew = [antennaA[0] + xFactor[0], antennaB[0] + xFactor[1]]
					yNew = [antennaA[1] + yFactor[0], antennaB[1] + yFactor[1]]
					self.setAntinodes1(xFactor, yFactor, xNew, yNew)
					self.setAntinodes2(xFactor, yFactor, xNew, yNew)
		return len(self.total1), len(self.total2)

def main():
	input = open("input/08.txt", "r").read()
	
	sol = Solution(input)
	print("Part 1 & 2:", sol.part())

if __name__ == "__main__":
	main()