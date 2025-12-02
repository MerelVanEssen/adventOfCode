# Advent of Code 2021 Day 2: Dive!

def result(lines):
	depth, pos, aim, depth2 = 0, 0, 0, 0
	for line in lines:
		dir, val = line.split()
		val = int(val)
		if dir == "forward":
			pos += val
			depth2 += aim * val
		elif dir == "down":
			depth += val
			aim += val
		elif dir == "up":
			depth -= val
			aim -= val
	return depth * pos, depth2 * pos

def main():
	filename = "input/02.txt"
	print("Using input file:", filename)
	f = open(filename, "r")
	input = f.read()
	lines  = input.split('\n')
	print("Results:", result(lines))
	f.close() 

if __name__ == "__main__":
	main()