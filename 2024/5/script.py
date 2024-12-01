from collections import deque

class Solution:
	def	calculator(self, seed, sdr):
		dest = int(sdr[0])
		source = int(sdr[1])
		range = int(sdr[2])
		# print ("before", seed)
		if seed >= source and seed < source + range:
			seed = seed - source + dest
		else:
			return seed, False
		# print("after", seed)
		return seed, True

	def plantSeeds(self, seeds, lines):
		validSeeds = [1] * len(seeds)
		for line in lines:
			if line and line[0] and line[0].isdigit():
				sdr = line.split()
				for i in range(len(seeds)):
					if (validSeeds[i] == 1):
						seeds[i], change = self.calculator(int(seeds[i]), sdr)
						if change:
							validSeeds[i] = 0
			else:
				validSeeds = [1] * len(seeds)
		lowestNr = float('inf')
		for seed in seeds:
			lowestNr = min(lowestNr, seed)
		return (lowestNr)

	def function(self, input):
		lines = input.split('\n')
		name, data = lines[0].split(':')
		seeds = data.split()
		return self.plantSeeds(seeds, lines)
	
	def function2(self, input):
		lines = input.split('\n')
		name, data = lines[0].split(':')
		seeds = data.split()
		buckets = []
		allsBuckets = []
		i = 0
		for line in lines:
			if line and line[0] and line[0].isdigit():
				dsr = line.split()
				buckets.append([int(dsr[1]), int(dsr[2]), int(dsr[0])])
			else:
				if len(buckets) > 0:
					buckets.sort()
					allsBuckets.append(buckets)
				buckets = []
		print (allsBuckets)
		# for group in allsBuckets:




def main():
	sol = Solution()
	f = open("input.txt", "r")
	input = f.read()
	# print(sol.function(input))
	# print(sol.function2(input))
	f.close() 

if __name__ == "__main__":
	main()
