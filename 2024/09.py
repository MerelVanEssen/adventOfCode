class Solution:
	def	__init__(self, input):
		self.l = []
		index = 0
		for i, nr in enumerate(input):
			nr = int(nr)
			if i % 2 == 0:
				self.l += [index] * nr
				index += 1
			else:
				self.l += ['.'] * nr
		self.saveL = self.l[:]
		self.firstDots = 0
	
	def calculateScore(self):
		total = 0
		for i, nr in enumerate(self.l):
			if nr != '.':
				total += nr * i
		return total

	def	part1(self):
		j = len(self.l) - 1
		i = 0
		saveLastDot = len(self.l)
		while i < j:
			if self.l[i] == '.':
				# found lenght of the block that you want to move
				while j >= i:
					if self.l[j] != '.':
						saveLastDot = j
						self.l[i] = self.l[j]
						self.l[j] = '.'
						break
					j -= 1
			i += 1
		self.l = self.l[:saveLastDot]
		return self.calculateScore()

	def	part2(self):
		self.l = self.saveL
		j = len(self.l) - 1
		while j >= 0:
			if self.l[j] != '.':
				saveJ = j 
				saveIndex = self.l[j]
				lengthBlock = 0
				# find lenght of the block that you want to move
				while j >= 0 and self.l[j] == saveIndex:
					j -= 1
					lengthBlock += 1
				
				# Remembers where the first dot is
				i = self.firstDots
				fDot = False
				while i < j:
					if self.l[i] == '.':
						if fDot == False:
							self.firstDots = i 
							fDot = True
						saveI = i
						lenghtFront = 0

						# searching for a place where the block fits
						while i < len(self.l) and self.l[i] == '.':
							i += 1
							lenghtFront += 1
						if lengthBlock <= lenghtFront:
							z = 0
							while z < lengthBlock:
								self.l[saveI + z] = saveIndex
								self.l[saveJ - z] = '.'
								z += 1
							break
					
					i += 1
			else:
				j -= 1
		return self.calculateScore()

def main():
	f = open("input/09.txt", "r")
	input = f.read()
	sol = Solution(input)
	print("Part 1:", sol.part1())
	print("Part 2:", sol.part2())

if __name__ == "__main__":
	main()
