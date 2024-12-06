class Solution:
	# set with values time and distance and for part two one number
	def __init__(self, input):
		lines = input.split('\n')
		timeInput = lines[0].split()
		distInput = lines[1].split()
		self.time = [int(x) for x in timeInput[1:]]
		self.dist = [int(x) for x in distInput[1:]]
		
		self.time2 = int(lines[0][11:].replace(" ", ""))
		self.dist2 = distTwo = int(lines[1][11:].replace(" ", ""))
	
	# Part 1, looping through the races and when it is enough, total time minus 2 time "not enough"
	def function1(self):
		totalScore = 1
		for i, time in enumerate(self.time):
			j = 0
			raceScore = 0
			while True:
				if (self.time[i] - j) * j > self.dist[i]:
					raceScore = self.time[i] - (j * 2) + 1
					break
				j += 1
			totalScore *= raceScore
		return totalScore
	
	# Part 2
	def function2(self):
		totalScore = 1
		j = 0
		raceScore = 0
		while True:
			if (self.time2 - j) * j > self.dist2:
				raceScore = self.time2 - (j * 2) + 1
				break
			j += 1
		totalScore *= raceScore
		return totalScore

def main():
	with open("input/06.txt", "r") as f:
		input = f.read()

	sol = Solution(input)
	print("Part1:", sol.function1())
	print("Part2:", sol.function2())

if __name__ == "__main__":
	main()
