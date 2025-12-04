# Advent of Code 2021 Day 7: Align whales

def getFuel(numbers, align):
	fuel = 0
	for nr in numbers:
		fuel += abs(nr - align)
	return fuel

def getFuel2(numbers, align):
	fuel = 0
	for nr in numbers:
		n = abs((nr - align))
		fuel += n * (n + 1) // 2
	return fuel

def searchFromAlignPoint(numbers, align, alignDir, fuel, part):
	newFuel = 0
	while True:
		align += alignDir
		newFuel = getFuel(numbers, align) if part == 1 else getFuel2(numbers, align)
		if newFuel < fuel:
			fuel = newFuel
		else:
			break
	return fuel

def result(numbers: list, part: int):
	align = int(sum(numbers) / len(numbers))
	fuel = getFuel(numbers, align) if part == 1 else getFuel2(numbers, align)
	newFuel = searchFromAlignPoint(numbers, align, 1, fuel, part)
	fuel = newFuel if newFuel < fuel else fuel
	newFuel = searchFromAlignPoint(numbers, align, -1, fuel, part)
	fuel = newFuel if newFuel < fuel else fuel
	return fuel

filename = "input/07.txt"
print("Using input file:", filename)
f = open(filename, "r")
input = f.read()
lines  = input.split(',')
numbers = [int(nr) for nr in lines]
print("Part 1:", result(numbers, 1))
print("Part 2:", result(numbers, 2))
f.close() 
