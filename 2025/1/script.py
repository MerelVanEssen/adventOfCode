import time
from collections import defaultdict

# left and right nr, give back a sum of the differences between the not used smallest in left and right
class Solution:
	def part1(self, lines):
		left = []
		right = []
		totalSum = 0
		for line in lines:
			lr = line.split()
			left.append(int(lr[0]))
			right.append(int(lr[1]))
		left.sort()
		right.sort()
		for i in range(len(left)):
			totalSum += abs(left[i] - right[i])
		return (totalSum)

# sum when you multiply the number in left by the amount of number in right
	def part2(self, lines):
		left = []
		right = defaultdict(int)
		totalSum = 0
		for line in lines:
			lr = line.split()
			left.append(int(lr[0]))
			right[(int(lr[1]))] += 1
		for i in range(len(left)):
			totalSum += left[i] * right[left[i]]
		return (totalSum)

def main():
	sol = Solution()
	f = open("input.txt", "r")
	input = f.read()
	lines  = input.split('\n')
	start = time.time()
	print("Part1", sol.part1(lines))
	end = time.time()
	print("Time cost:", end - start)
	start = time.time()
	print("Part2", sol.part2(lines))
	end = time.time()
	print("Time cost:", end - start)
	f.close() 

if __name__ == "__main__":
	main()
