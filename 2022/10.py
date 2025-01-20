with open("input/10.txt", "r") as f:
	rawInput = f.read()

instructions = rawInput.split('\n')

cycle = 0
x = 1
values = []
save_last_value = 0
check = 20

for line in instructions:
	if " " in line:
		add, value = line.split()
		cycle += 2
		if cycle == check or cycle - 1 == check:
			values.append(x)
			check += 40
		x += int(value)
		save_last_value = x
	else:
		cycle += 1
		if cycle == check:
			values.append(x)
			check += 40

check = 20
total = 0
for xvalue in values:
	total += xvalue * check
	check += 40

print(total)


	