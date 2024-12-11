from collections import Counter, defaultdict

class Solution:
	def __init__(self, input):
		self.stones = [int(s) for s in input.split()]

	# return a list with the new stoneNrs
	def applyRules(self, nr):
		if nr == 0:
			return [1]
		string = str(nr)
		if len(string) % 2 == 0:
			middle = len(string) // 2
			return [int(string[:middle]), int(string[middle:])]
		return [nr * 2024]

	# goes through all the current stones, apply the rules and increase the nr of stones
	def blink(self, counterStones):
		d = defaultdict(int)
		for stone, amount in counterStones.items():
			stones = self.applyRules(stone)
			for stone2 in stones:
				d[stone2] += amount
		return d
	
	# Making a dictonary with Counter to keep track how many stones have the same nr
	def part(self, amount):
		stones = Counter(self.stones)
		for _ in range(amount):
			stones = self.blink(stones)
		return sum(stones.values())

def main():
	input = open("input/11.txt", "r").read()

	sol = Solution(input)
	print("Part 1:", sol.part(25))
	print("Part 2:", sol.part(75))

if __name__ == "__main__":
	main()



