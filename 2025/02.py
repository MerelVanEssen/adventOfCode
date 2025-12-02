# DAY 2: ID Validation

# Checks if the ID is made by repeating a substring.
def is_repeated_id_1(s: str, l: int) -> bool:
	if l % 2 != 0:
		return False
	half = l // 2
	return s[:half] == s[half:]

# Checks if the ID is made by repeating a substring n times (n >= 2).
def is_repeated_id_2(s: int, l: int) -> bool:
	k = 2
	for n in range(k, l + 1):
		if l % n == 0:
			temp_l = l // n
			part = s[:temp_l]
			if part * n == s:
				return True
	return False

# Computes the results for part 1 and part 2.
def result(lines):
	total1, total2 = 0, 0
	for id in lines:
		parts = id.split("-")
		a, b = int(parts[0]), int(parts[1])
		for n in range(a, b + 1):
			a_string = str(n)
			l = len(a_string)
			if is_repeated_id_1(a_string, l):
				total1 += n
			if is_repeated_id_2(a_string, l):
				total2 += n
	return total1, total2

def main():
	f = open("input/02.txt", "r")
	input = f.read()
	lines  = input.split(',')
	print("Results:", result(lines))
	f.close() 

if __name__ == "__main__":
	main()