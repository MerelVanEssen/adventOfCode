from functools import cache

class Solution:
	def __init__(self, input):
		self.input = input.split(',')
		self.boxes = [[] for x in range(0, 256, 1)] 

	@cache
	def HASHalgorithm(self, hash: str) -> int:
		currNr = 0
		for char in hash:
			currNr += ord(char)
			currNr *= 17
			currNr %= 256
		return currNr
	
	def equalSign(self, hash: str) -> None:
		label, nr = hash.split('=')
		box = self.HASHalgorithm(label)
		for lens in self.boxes[box]:
			if lens[0] == label:
				lens[1] = nr
				return
		self.boxes[box].append([label, nr])

	def minSign(self, hash: str) -> None:
		label = hash[:len(hash) - 1]
		box = self.HASHalgorithm(label)
		for i, lens in enumerate(self.boxes[box]):
			if lens[0] == label:
				self.boxes[box].pop(i)
				break

	def calculateTotal(self) -> int:
		total = 0
		for b, box in enumerate(self.boxes):
			for l, lens in enumerate(box):
				total += (b + 1) * (l + 1) * int(lens[1])
		return total
	
	def part(self) -> tuple[int, int]:
		total = 0
		for hash in self.input:
			total += self.HASHalgorithm(hash)
			lastChar = hash[-1]
			if lastChar.isdigit():
				self.equalSign(hash)
			else:
				self.minSign(hash)
		return total, self.calculateTotal()

def main():
	input = open("input/15.txt", "r").read()

	sol = Solution(input)
	print("Part 1 & 2:", sol.part())

if __name__ == "__main__":
	main()