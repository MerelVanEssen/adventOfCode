class Solution:
	def __init__(self, input):
		self.maps = input.split('\n\n')
		for i in range(len(self.maps)):
			self.maps[i] = self.maps[i].split('\n')
		self.keys = []
		self.locks = []

	def part1(self):
		total = 0
		for map in self.maps:
			# makes a code for every key/lock with the highths
			code = [0,0,0,0,0]
			for y in range(len(map)):
				for x in range(len(map[0])):
					if map[y][x] == '#':
						code[x] += 1

			code = [x - 1 for x in code]

			# check if it is a key or a lock
			if map[0].count('#') == 5:
				self.locks.append(code)
			else:
				self.keys.append(code)

		# Checks for every lock and key if there is a match
		goodfits = 0
		for i, lock in enumerate(self.locks):
			for j, key in enumerate(self.keys):
				if i != j:

					fit = True
					for i in range(len(lock)):
						if lock[i] + key[i] > 5:
							fit = False
							break

					if fit:
						goodfits += 1

		return goodfits

def main():
	input = open("input.txt", "r").read()

	sol = Solution(input)
	print("Part 1:", sol.part1())

if __name__ == "__main__":
	main()