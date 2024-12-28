import re
import sympy

class Solution:
	def __init__(self, input):
		input = input.split('\n')
		for i in range(len(input)):
			input[i] = input[i].replace(',', '')
			input[i] = input[i].split()
			x, y, z = input[i][0], input[i][1], input[i][2]
			vx, vy, vz = input[i][4], input[i][5], input[i][6]

			input[i] = ((int(x), int(y), int(z)), (int(vx), int(vy), int(vz)))

		self.input = input
		self.area = [200000000000000, 400000000000000]
		self.areaproef = [7,27]

	def calculateIntersection(self, p1, v1, p2, v2):
		try:
			u = ((p2[1] - p1[1]) * v2[0] - (p2[0] - p1[0]) * v2[1]) / (v2[0] * v1[1] - v2[1] * v1[0])
			v = ((p2[1] - p1[1]) * v1[0] - (p2[0] - p1[0]) * v1[1]) / (v2[0] * v1[1] - v2[1] * v1[0])

			if u < 0 or v < 0:
				return None
			xi = p2[0] + v2[0] * v
			yi = p2[1] + v2[1] * v
			return (xi, yi)
		except:
			return None

	def part1(self):
		total = 0
		for i in range(len(self.input)):
			xyz_one, vxyz_one = self.input[i]
			for j in range(i + 1, len(self.input)):
				xyz_two, vxyz_two = self.input[j]
				point = self.calculateIntersection(xyz_one, vxyz_one, xyz_two, vxyz_two)
				if point == None:
					continue
				if self.area[0] <= point[0] <= self.area[1]:
					if self.area[0] <= point[1] <= self.area[1]:
						total += 1
		return total
	
	def part2(self):

		eqs = []
		xr, yr, zr, dxr, dyr, dzr = sympy.symbols("xr, yr, zr, dxr, dyr, dzr")

		for point, dir in self.input[:10]:
			sx, sy, sz = point
			dx, dy, dz = dir
			eqs.append((sx - xr) * (dyr - dy) - (sy - yr) * (dxr - dx))
			eqs.append((sx - xr) * (dzr - dz) - (sz - zr) * (dxr - dx))

		solution = sympy.solve(eqs)

		assert len(solution) == 1
		part2 = solution[0][xr] + solution[0][yr] + solution[0][zr]
		return part2

	
def main():
	input = open("input/24.txt", "r").read()

	sol = Solution(input)
	print("Part 1:", sol.part1())
	print("Part 2:", sol.part2())

if __name__ == "__main__":
	main()