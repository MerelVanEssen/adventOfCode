import re
import heapq

class Solution:
	def __init__(self, input):
		self.map = input.split('\n')
		self.dir = [[0,1], [1,0], [0,-1], [-1,0]]
		self.way = [[ x for x in line] for line in self.map]
		self.grid = [[float('inf') for _ in range(len(self.map[0]))] for _ in range(len(self.map))]
		self.steps = 0
		self.turn = 0
		for i, line in enumerate(self.map):
			if 'S' in line:
				index = line.index("S")
				self.start = [i, index]
			if 'E' in line:
				index = line.index("E")
				self.end = [i, index]
		self.path = set()
		self.visited = set()


	def get_cost(self, curr_dir, next_dir):
		if curr_dir == next_dir:
			return(1)
		return(1001)

	def part1(self):
		deq = []
		visited = set()
		heapq.heappush(deq, (1, self.start[0], self.start[1], 0, set())) # cost, y, x, dir down
		foundEnd = False
		part1 = 0
		self.grid[self.start[0]][self.start[1]] = 1

		while deq:
			cost, y, x, direction, path = heapq.heappop(deq)

			path.add((y, x))

			if [y,x] == self.end and foundEnd == False:
				foundEnd = True
				part1 = cost - 1
				continue
			
			for i, d in enumerate(self.dir):
				newY = y + d[0]
				newX = x + d[1]

				if not (0 <= newY < len(self.map) and 0 <= newX < len(self.map[0])) or self.map[newY][newX] == '#':
					continue

				if (newY, newX) in path:
					continue
				
				Newcost = cost + self.get_cost(i, direction)
				
				copyPath = path.copy()

				if Newcost <= self.grid[newY][newX] or self.grid[newY + d[0]][newX + d[1]] == Newcost + 1:
					self.grid[newY][newX] = Newcost
					heapq.heappush(deq, (Newcost, newY, newX, i, copyPath))


		max_col_widths = [0] * max(len(row) for row in self.grid)
		for row in self.grid:
			for i, cell in enumerate(row):
				max_col_widths[i] = max(max_col_widths[i], len(str(cell)))

		# Print rijen met uitlijning
		for row in self.grid:
			formatted_row = [
				str(row[i]).ljust(max_col_widths[i]) if i < len(row) else " " * max_col_widths[i]
				for i in range(len(max_col_widths))
			]
			print(" | ".join(formatted_row))
		return (part1)

	def recursive(self, y, x, oldY, oldX):

		if oldY == y and oldX == x:
			return

		if [y,x] == self.start:
			print("start found")
			return

		for d in self.dir:
			newY = y + d[0]
			newX = x + d[1]

			if self.grid[newY][newX] <= self.grid[y][x]:
				self.way[newY][newX] = '$'
				self.recursive(newY, newX, y, x)


	def part2(self):
		total = 0
		y, x = self.end
		self.visited.clear()
		self.recursive(y, x, -1, -1)
		for line in self.way:
			print(line)
			total += line.count('$')
		return total + 2

def main():
	input = open("input/16.txt", "r").read()

	sol = Solution(input)
	print("Part 1:", sol.part1(), 95444)
	print("Part 2:", sol.part2(), 513)

if __name__ == "__main__":
	main()