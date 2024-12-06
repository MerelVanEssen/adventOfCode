from collections import deque

class Solution:
	def __init__(self):
		self.DIR = [[-1,-1],[0,-1],[1,-1]]
		
	def part1and2(self, input):
		lines = input.split('\n')
		i = 0
		sumNrs = 0
		sumGears = 0
		while i < len(lines):
			j = 0
			while j < len(lines[i]):
				if lines[i][j] != '.' and lines[i][j].isdigit() == False:
					gears = []
					for d in self.DIR:
						newI, newJ = i + d[0], j + d[1]
						newI = max(newI, 0)
						newJ = max(newJ, 0)
						newI = min(newI, len(lines))
						newI = min(newI, len(lines[i]))
						maxIt = j + 2
						while newJ < len(lines[newI]) and newJ < maxIt:
							if lines[newI][newJ].isdigit():
								while newJ > 0 and lines[newI][newJ - 1].isdigit():
									newJ -= 1
								nr = ""
								while newJ < len(lines[newI]) and lines[newI][newJ].isdigit():
									nr += lines[newI][newJ]
									newJ += 1
								sumNrs += int(nr)
								if lines[i][j] == '*':
									gears.append(int(nr))
							else:
								newJ += 1
					if len(gears) > 1:
						sumGear = 1
						for gear in gears:
							sumGear *= gear
						sumGears += sumGear

				j += 1
			i +=1
		return (sumNrs, sumGears)

def main():
	sol = Solution()
	with open("input/03.txt", "r") as f:
	input = f.read()
	print(sol.part1and2(input))

if __name__ == "__main__":
	main()
