import heapq

class Solution:
	def __init__(self, input):
		self.map = input.split('\n')
		self.start = self.end = 0
		self.costToEnd = [[float('inf') for _ in line] for line in self.map]
		self.shortest = float('inf')
		self.points = []
		for i, line in enumerate(self.map):
			if 'S' in line:
				j = line.index('S')
				self.start = (i, j)
			if 'E' in line:
				j = line.index('E')
				self.end = (i, j)

	def searchWays(self, cheatDistance):
		deq = [(0, self.start[0], self.start[1], -1, -1)]
		total = 0
		seen = set()

		while deq:
			cost, y, x, backY, backX = heapq.heappop(deq)

			if self.map[y][x] == 'E':
				continue

			seen.add((y,x))

			for dY, dX in [(0, 1), (1, 0), (0,-1), (-1,0)]:
				newY = dY + y
				newX = dX + x

				if newY == backY and newX == backX: # back
					continue

				if self.map[newY][newX] != '#':
					heapq.heappush(deq, (cost + 1, newY, newX, y, x))

			# Search in a area of the cheatDistance to places that are not visited and closer to the end
			for dy in range(-cheatDistance, cheatDistance + 1):
				for dx in range(-cheatDistance, cheatDistance + 1):
					checkY, checkX = y + dy, x + dx
					if (checkY, checkX) in seen:
						continue
					distance = abs(dy) + abs(dx)
					if (0 <= checkY < len(self.map) and 0 <= checkX < len(self.map[0]) 
						and self.map[checkY][checkX] != '#' and distance <= cheatDistance):
						remaining = self.shortest - (cost + distance + self.costToEnd[checkY][checkX])
						if remaining >= 100:
							total += 1
		return total

	def setCost(self): # end - > start, give the map the costs till the end
		deq = [(0, self.end[0], self.end[1], -1, -1)]

		while deq:
			cost, y, x, backY, backX = heapq.heappop(deq)

			self.costToEnd[y][x] = min(cost, self.costToEnd[y][x])

			if self.map[y][x] == 'S':
				if cost < self.shortest:
					self.shortest = cost
				continue

			for dY, dX in [(0, 1), (1, 0), (0,-1), (-1,0)]:
				newY = dY + y
				newX = dX + x
				if (newY == backY and newX == backX) or self.map[newY][newX] == '#':
					continue
				heapq.heappush(deq, (cost + 1, newY, newX, y, x))

	def part(self):
		self.setCost()
		total1 = self.searchWays(2)
		total2 = self.searchWays(20)
		return total1, total2

def main():
	input = open("input/20.txt", "r").read()

	sol = Solution(input)
	print("Part 1 & 2:", sol.part())

if __name__ == "__main__":
	main()