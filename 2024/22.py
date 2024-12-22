from functools import cache
from collections import defaultdict

class Solution:
	def __init__(self, input):
		self.numbers = input.split('\n')

	def mixNr(self, secretNr, nr):
		return nr ^ secretNr

	def pruneNr(self, nr):
		return nr % 16777216

	@cache
	def secretNr(self, secretNr):
		secretNr = self.mixNr(secretNr, secretNr * 64)
		secretNr = self.pruneNr(secretNr)
		secretNr = self.mixNr(secretNr, secretNr // 32)
		secretNr = self.pruneNr(secretNr)
		secretNr = self.mixNr(secretNr, secretNr * 2048)
		secretNr = self.pruneNr(secretNr)
		return (secretNr)

	# Calculates the difference between the last nrs
	@cache
	def giveSeq(self, fourdigits):
		return tuple([fourdigits[i] - fourdigits[i - 1] for i in range(1, len(fourdigits))])

	def part(self):
		total = 0
		dAmount = defaultdict(int)
		dTotal = defaultdict(int)

		for nr in self.numbers:
			secretNr = int(nr)
			lastDigits = [secretNr % 10]
			
			# Looping through all the seconds and saves the 2000th nr (part 1) and a list with the last nr (price)
			for i in range(2000):
				secretNr = self.secretNr(secretNr)
				if i == 2000 - 1:
					total += secretNr
				lastDigits.append(secretNr % 10)

			change = self.giveSeq(tuple(lastDigits))
			seen = set()
			
			# Checking every 4 consecutive changes and save the amount of appears
			for i in range(len(change) - 3):
				changeT = change[i:i+4]
				dAmount[changeT] += 1

				# Also save the first occuring number for each changing window
				if changeT not in seen:
					dTotal[changeT] += lastDigits[i + 4]
				seen.add(changeT)

		return total, max(dTotal.values())

def main():
	input = open("input/22.txt", "r").read()

	sol = Solution(input)
	print("Part 1 & 2:", sol.part())

if __name__ == "__main__":
	main()