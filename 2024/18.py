import heapq

class Solution:
	global SIZE

	def __init__(self, input, amount, size):
		self.bytes = input.split('\n')
		for i, line in enumerate(self.bytes):
			nrs = line.split(',')
			self.bytes[i] = [int(nrs[0]), int(nrs[1])]
		self.obstacles = set()
		self.size = size + 1
		self.amount = amount

	def dijkstra(self):
		dir = [[0,1], [1,0], [0,-1], [-1,0]]
		deq = [(0, 0, 0, 0, 0)]  # cost, y, x, dirY, dirX, path
		visited = set()
		shortest = float('inf')

		while deq:
			cost, y, x, dY, dX = heapq.heappop(deq)

			if y == self.size - 1 and x == self.size - 1:
				return cost

			if (y, x) in visited:
   				continue
			visited.add((y, x))

			for ndY, ndX in dir:
				newY, newX = y + ndY, x + ndX
				if not (0 <= newY < self.size and 0 <= newX < self.size):
					continue
				if (newY, newX) not in self.obstacles and (newY, newX) not in visited:
					heapq.heappush(deq, (cost + 1, newY, newX, ndY, ndX))
		return 0

	def part1(self):
		# Drop 2024 bytes and find the shortest way
		for i, byte in enumerate(self.bytes):
			if i == self.amount:
				break
			self.obstacles.add((byte[0], byte[1]))
		return self.dijkstra()

	def part2(self):
		# find the first byte that blocks your way towards the end
		for byte in self.bytes:
			self.obstacles.add((byte[0], byte[1]))
			total = self.dijkstra()
			if total == 0:
				coordinates = str(byte[0]) + "," + str(byte[1])
				return coordinates
		return []

def main():
	input = open("input/18.txt", "r").read()

	sol = Solution(input, 1024, 70)
	print("Part 1:", sol.part1())
	print("Part 2:", sol.part2())

if __name__ == "__main__":
	main()