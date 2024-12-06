from collections import deque

class Solution:
	def __init__(self, lines):
		# init Seeds
		self.seeds = []
		lineSeeds = lines[0].split()
		i = 1
		while i < len(lineSeeds):
			self.seeds.append([int(lineSeeds[i]), int(lineSeeds[i]) + int(lineSeeds[i + 1]) - 1])
			i += 2

		# init lines
		self.maps = []
		lines = lines[3::]
		save_map = []
		for line in lines:
			if line and line[0] and line[0].isdigit():
				dsr = line.split()
				dest = int(dsr[0])
				source = int(dsr[1])
				range = int(dsr[2])
				save_map.append([source, source + range - 1, dest, dest + range - 1]) # source, endSource, dest, endDest
			else:
				if not line:
					self.maps.append(save_map)
					save_map = []

	def function(self):
		minumumNr = float('inf')
		i = 0
		# go through diffent maps
		lenSeeds = len(self.seeds)
		for map in self.maps:
			i = 0
			while i < lenSeeds:
				seed, seedEnd = self.seeds[i]
				for src, srcEnd, des, desEnd in map:
					diff = des - src
					# in the bucket
					if seed >= src and seedEnd <= srcEnd:
						self.seeds[i] = [seed + diff, seedEnd + diff]
						break
					# over the bucket, both sides
					elif seed < src and seedEnd > srcEnd:
						self.seeds.append([seed, src - 1])
						self.seeds.append([srcEnd + 1, seedEnd])
						self.seeds[i] = [des, desEnd]
						break
					# before and in bucket
					elif seed < src and seedEnd >= src:
						self.seeds.append([seed, src - 1])
						self.seeds[i] = [des, seedEnd + diff]
						break
					# after and in bucket
					elif seed >= src and seed <= srcEnd and seedEnd > srcEnd:
						self.seeds.append([srcEnd + 1, seedEnd])
						self.seeds[i] = [seed + diff, desEnd]
						break
				lenSeeds = len(self.seeds)
				i += 1
		for seed, end in self.seeds:
			minumumNr = min(seed, minumumNr)
		return (minumumNr)

def main():
	with open("input/05.txt", "r") as f:
		input = f.read()

	lines = input.split('\n')
	sol = Solution(lines)
	print(sol.function(), 69323688)


if __name__ == "__main__":
	main()
