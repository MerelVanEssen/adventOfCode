# DAY 1: Arrow Movement

# Counts whenever the arrow points to 0 after each move.
def part1(lines):
	arrow = 50
	zeros = 0
	for line in lines:
		side = line[0]
		nr = int(line[1:]) % 100
		if (side == 'L'):
			arrow = arrow - nr
		else:
			arrow = arrow + nr
		arrow %= 100
		if (arrow == 0):
			zeros = zeros + 1
	return (zeros)

# Counts however many times the arrow points to 0 after each move.
def part2(lines):
	arrow = 50
	zeros = 0
	for line in lines:
		side = line[0]
		nr = int(line[1:])
		step = -1 if side == 'L' else 1
		for _ in range(nr):
			arrow = (arrow + step) % 100
			if arrow == 0:
				zeros += 1
	return zeros

def main():
	f = open("input/01.txt", "r")
	input = f.read()
	lines  = input.split('\n')
	print("Part 1:", part1(lines))
	print("Part 2:", part2(lines))
	f.close() 

if __name__ == "__main__":
	main()