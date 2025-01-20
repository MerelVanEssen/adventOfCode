
with open("input/02.txt", "r") as f:
	rawInput = f.read()

rounds = rawInput.split('\n')

def calculate_score(other, played):
	points = {'X': 1, 'Y': 2, 'Z': 3}
	winning = {'Y': 'A', 'Z': 'B', 'X': 'C'}
	score = points[played]

	if played == chr(ord(other) + 23):
		score += 3
	elif winning[played] == other:
		score += 6

	return score

def getRightLetter(other, played):
	winning = {'A': 'Y', 'B': 'Z', 'C': 'X'}
	losing = {'A': 'Z', 'B': 'X', 'C': 'Y'}
	draw = {'A': 'X', 'B': 'Y', 'C': 'Z'}

	if played == 'X':
		return losing[other]
	elif played == 'Y':
		return draw[other]
	else:
		return winning[other]
	
total = 0
total2 = 0

for round in rounds:
	other, played = round.split()
	total += calculate_score(other, played)
	total2 += calculate_score(other, getRightLetter(other, played))

print("Part 1:", total)
print("Part 2:", total2)



