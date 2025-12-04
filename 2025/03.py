# DAY 3: Largest Number Combination

def search_biggest_combination(line, keep):
	to_remove = len(line) - keep
	stack = []
	for n in line:
		while to_remove > 0 and stack and stack[-1] < n:
			stack.pop()
			to_remove -= 1
		stack.append(n)
	return int(''.join(stack[:keep]))

def result(lines):
	total1, total2 = 0, 0
	for line in lines:
		total1 += search_biggest_combination(line, 2)
		total2 += search_biggest_combination(line, 12)
	return total1, total2

filename = "input/03.txt"
print("Using input file:", filename)
f = open(filename, "r")
input = f.read()
lines  = input.split('\n')
print("Results:", result(lines))
f.close()