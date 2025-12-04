# DAY 3: Removing rolls of paper 

def result(lines: list, remove: bool):
	total = 0
	search = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
	removed = True

	while removed:
		removed = False
		for i, line in enumerate(lines):
			for j, p in enumerate(line):
				if p != '@':
					continue
				pieces = 0
				for dir in search:
					check_i = i + dir[0]
					check_j = j + dir[1]
					if check_i >= 0 and check_i < len(lines) and check_j >= 0 and check_j < len(line):
						if lines[check_i][check_j] == '@':
							pieces += 1
				if pieces < 4:		
					total += 1
					if remove:
						lines[i][j] = '.'
						removed = True
	return total

filename = "input/04.txt"
print("Using input file:", filename)
f = open(filename, "r")
input = f.read()
lines  = input.split('\n')
lines = [list(line) for line in lines]
print("Part 1:", result(lines, False))
print("Part 2:", result(lines, True))
f.close() 