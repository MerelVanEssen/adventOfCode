class Solution:
	def __init__(self, input):
		self.map = input.split('\n')
		self.grid = [[-1 for _ in range(len(self.map[0]))] for _ in range(len(self.map))]
		self.dir = [[0,1], [1,0], [0,-1], [-1,0]]
		self.visit = set()
		self.outsideVisited = set()

	def checkCorners2(self, listSides, saveCor):
		checks = [[0,1],[1,2],[2,3],[3,0]]
		corner = 0
		for check in checks:
			if check[0] in listSides and check[1] in listSides:
				# if a corner is double found it means that it is not a corner from outside but from the inside
				if (saveCor[check[0]], saveCor[check[1]]) in self.outsideVisited:
					corner -= 1
				else:
					self.outsideVisited.add((saveCor[check[0]], saveCor[check[1]]))
					self.outsideVisited.add((saveCor[check[1]], saveCor[check[0]]))
					corner += 1
		return corner

	def checkCorners1(self, listSides):
		checks = [[0,1],[1,2], [2,3],[3,0]]
		corner = 0
		for check in checks:
			if check[0] in listSides and check[1] in listSides:
				corner += 1
		return corner

	def checkCornersFromOutside(self, index, outside):
		total = 0
		outside = list(outside)
		wrongCornersOutside = []
		
		for y, x in outside:
			wrongCornersOutside.clear()
			saveCor = []
			for i, d in enumerate(self.dir):
				newY = y + d[0]
				newX = x + d[1]
				saveCor.append((newY, newX))
				if 0 <= newY < len(self.map) and 0 <= newX < len(self.map[0]) and self.grid[newY][newX] == index:
					wrongCornersOutside.append(i)
			total += self.checkCorners2(wrongCornersOutside, saveCor)
		return total

	def floating(self, index, char, y, x):
		deq = [(y, x)]
		self.grid[y][x] = index
		self.visit.add((y, x))
		amount = 1
		border = 0
		corner = 0
		outside = set()

		while deq:
			curr = deq.pop(0)
			wrongCornerInside = []
			for i, d in enumerate(self.dir):
				newY = d[0] + curr[0] 
				newX = d[1] + curr[1]
				insideMap = False

				if 0 <= newY < len(self.map) and 0 <= newX < len(self.map[0]):
					insideMap = True
				setNew = (newY, newX)

				if insideMap and self.map[newY][newX] == char and setNew not in self.visit:
					amount += 1
					self.grid[newY][newX] = index
					deq.append(setNew)
					self.visit.add(setNew)
				else:
					if not (insideMap and self.map[newY][newX] == char):
						border += 1
						wrongCornerInside.append(i)
					if insideMap and self.map[newY][newX] != char:
						outside.add((newY,newX))
			corner += self.checkCorners1(wrongCornerInside)

		corner += self.checkCornersFromOutside(index, outside)
		return amount, border, corner

	def part(self):
		index = 0
		corners = 0
		borders = 0
		for y in range(len(self.map)):
			for x in range(len(self.map[0])):
				char = self.map[y][x]
				self.outsideVisited.clear()
				if (y,x) not in self.visit:
					amount, border, corner = self.floating(index, char, y, x)
					corners += amount * corner
					borders += amount * border
					index += 1
		return borders, corners

def main():
	input = open("input/12.txt", "r").read()

	sol = Solution(input)
	print("Part 1:", sol.part())

if __name__ == "__main__":
	main()