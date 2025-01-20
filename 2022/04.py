
with open("input/04.txt", "r") as f:
	rawInput = f.read()

couples = rawInput.split('\n')

total = 0
total2 = 0
for couple in couples:
	first, second = couple.split(',')
	first = [int(x) for x in first.split('-')]
	second = [int(x) for x in second.split('-')]
	
	if first[0] >= second[0] and first[1] <= second[1]:
		total += 1
	elif second[0] >= first[0] and second[1] <= first[1]:
		total += 1
	
	if max(first[0], second[0]) <= min(first[1], second[1]):
		total2 += 1

print("Part 1:", total)
print("Part 2:", total2)
