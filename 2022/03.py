
with open("input/03.txt", "r") as f:
	rawInput = f.read()

rucksacks = rawInput.split('\n')

def convertLetter(letter):
	ascii = ord(letter)
	if ascii >= 97:
		return ascii - 96
	else:
		return ascii - (65 - 27)

total = 0
for rucksack in rucksacks:
	middle = len(rucksack) // 2
	for letter in rucksack[:middle]:
		if letter in rucksack[middle:]:
			total += convertLetter(letter)
			break

print("Part 1:", total)
	
total2 = 0
for i in range(0, len(rucksacks), 3):
	for letter in rucksacks[i]:
		if letter in rucksacks[i + 1] and letter in rucksacks[i + 2]:
			total2 += convertLetter(letter)
			break

print("Part 2:", total2)