import copy

with open("input/05.txt", "r") as f:
	rawInput = f.read()

rawCrates, instructions = rawInput.split('\n\n')

def getCrates(crates):
	crates.reverse()
	numbers = crates[0].split()
	stacks = [[] for _ in range(len(numbers))]

	for line in crates[1:]:
		i = 0
		for item in range(1, len(line), 4):
			if line[item] != ' ':
				stacks[i].append(line[item])
			i += 1
	return stacks

crates = getCrates(rawCrates.split('\n'))
crates2 = copy.deepcopy(crates)

instructions = instructions.split('\n')
for instruction in instructions:
	instr = instruction.split()
	fromStack = int(instr[3]) - 1
	toStack = int(instr[5]) - 1
	amount = int(instr[1])

	# part 1, one item per movement
	for i in range(amount):
		if crates[fromStack]:
			crate = crates[fromStack].pop()
			crates[toStack].append(crate)
	
	# part 2, all items in one
	amount = len(crates2[fromStack]) - amount
	saveBoxes = crates2[fromStack][amount::]
	del crates2[fromStack][amount::]
	crates2[toStack].extend(saveBoxes)

onTopStack = ""
onTopStack2 = ""

for item in crates:
	if len(item) > 0:
		onTopStack += item[-1]

for item in crates2:
	if len(item) > 0:
		onTopStack2 += item[-1]

print("Part 1:", onTopStack)
print("Part 2:", onTopStack2)

