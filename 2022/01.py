
with open("input/01.txt", "r") as f:
	rawInput = f.read()

carriedFood = rawInput.split("\n\n")

def findMostCalories(carriedFood):
	highest = 0

	for elf in carriedFood:
		calories = elf.split('\n')
		totalElf = 0
		for calorie in calories:
			totalElf += int(calorie)
		highest = max(highest, totalElf)

	return highest

def findTopThree(carriedFood):
	total = []

	for elf in carriedFood:
		calories = elf.split('\n')
		totalElf = 0
		for calorie in calories:
			totalElf += int(calorie)
		total.append(totalElf)

	amount = 0
	for i in range(3):
		top = max(total)
		total.remove(top)
		amount += top

	return amount

print("Part 1:", findMostCalories(carriedFood))
print("Part 2:", findTopThree(carriedFood))