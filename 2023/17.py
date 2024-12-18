import heapq

class Solution:
	def __init__(self, input):
		self.map = input.split('\n')
		self.lY = len(self.map)
		self.lX = len(self.map[0])
		self.dir = [[0,1], [1,0], [0,-1], [-1,0]]

	def part1_dijkstra(self):
		visited = set()
		deq = []
		heapq.heappush(deq, (0, 0, 0, 1, 0, 0)) # cost, y, x, steps, dirY, dirX

		while deq:
			cost, y, x, s, dy, dx = heapq.heappop(deq)

			if s == 4:
				continue

			if (y, x, dy, dx, s) in visited:
				continue
			visited.add((y, x, dy, dx, s))
			
			# found end
			if y == self.lY - 1  and x == self.lX - 1:
				return cost
			
			for ndy, ndx in self.dir:
				if ndy == -dy and ndx == -dx:
					continue

				newY = y + ndy
				newX = x + ndx

				if 0 <= newY < self.lY and 0 <= newX < self.lX:
					newCost = cost + int(self.map[newY][newX])

					if [dy,dx] == [ndy,ndx]:
						heapq.heappush(deq, (newCost, newY, newX, s + 1, ndy, ndx))
					else:
						heapq.heappush(deq, (newCost, newY, newX, 1, ndy, ndx))
		return 0

	def part2_dijkstra(self):
		visited = set()
		deq = []
		heapq.heappush(deq, (0, 0, 0, 0, 0, 1)) # cost, y, x, steps, dirY, dirX
		heapq.heappush(deq, (0, 0, 0, 0, 1, 0))

		while deq:
			cost, y, x, s, dy, dx = heapq.heappop(deq)

			if (y, x, dy, dx, s) in visited:
				continue
			visited.add((y, x, dy, dx, s))

			# found end
			if y == self.lY - 1  and x == self.lX - 1:
				return cost
			
			for ndy, ndx in self.dir:	
				if ndy == -dy and ndx == -dx:
					continue

				newY = y + ndy
				newX = x + ndx

				if 0 <= newY < self.lY and 0 <= newX < self.lX:
					newCost = cost + int(self.map[newY][newX])
					if [dy,dx] == [ndy,ndx]:
						if s < 10:
							heapq.heappush(deq, (newCost, newY, newX, s + 1, ndy, ndx))
					elif s >= 4:
						heapq.heappush(deq, (newCost, newY, newX, 1, ndy, ndx))
		return 0
					
def main():
	input = open("input/17.txt", "r").read()

	sol = Solution(input)
	print("Part 1:", sol.part1_dijkstra())
	print("Part 2:", sol.part2_dijkstra())

if __name__ == "__main__":
	main()

# 1181 too high