import re
import heapq

class Solution:
	def __init__(self, input):
		self.map = input.split('\n')

		for i, line in enumerate(self.map):
			if 'S' in line:
				index = line.index("S")
				self.start = (i, index)

	def part(self):	
		deq = [(0, *self.start, 0, 1, [self.start])] # cost, y, x, dirY, dirX, path
		p1 = None
		visited = {(*self.start, 0, 1)}
		shortest = float('inf')
		savePaths = set()

		while deq:
			cost, y, x, dY, dX, path = heapq.heappop(deq)

			visited.add((y, x, dY, dX))

			# Saves the first shortest way and keep track of other routes with the same cost
			if self.map[y][x] == 'E':
				if p1 == None:
					p1 = cost
				if cost <= shortest:
					shortest = cost
					for p in path:
						savePaths.add(p)
				else:
					break

			# Step in the same direction
			if self.map[y + dY][x + dX] != '#' and (y + dY, x + dX, dY, dX) not in visited:
				heapq.heappush(deq, (cost + 1, y + dY, x + dX, dY, dX, path + [(y + dY, x + dX)]))

			# Turn 90 degrees
			for ndY, ndX in [(-dX, dY), (dX, -dY)]:
				if self.map[y + ndY][x + ndX] != '#' and (y, x, ndY, ndX) not in visited:
					heapq.heappush(deq, (cost + 1000, y, x, ndY, ndX, list(path)))

		return (p1, len(savePaths))

def main():
	input = open("input/16.txt", "r").read()

	sol = Solution(input)
	print("Part 1 & 2:", sol.part())

if __name__ == "__main__":
	main()