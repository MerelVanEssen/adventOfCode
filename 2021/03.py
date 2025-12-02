from aoc import createMap, turnMapBackwardsList, bitsToDecimal

# Return multiplication of most common bits and least common bits
def part1(map: map):
	bits, epsilon = '', ''
	for line in map:
		if line.count('1') > line.count('0'):
			bits += '1'
			epsilon += '0'
		else:
			bits += '0'
			epsilon += '1'
	return bitsToDecimal(bits) * bitsToDecimal(epsilon)

# Return first most common bits and least common bits at position pos
def getCommonBitLines(bits, pos, most = True):
	ones = []
	zeros = []
	for bit in bits:
		if bit[pos] == '1':
			ones.append(bit)
		else:
			zeros.append(bit)
	if most:
		return ones if len(ones) >= len(zeros) else zeros
	else:
		return zeros if len(ones) >= len(zeros) else ones

# Return multiplication of oxygen generator rating and CO2 scrubber rating
def part2(lines):
	OXILines = lines[:]
	CO2Lines = lines[:]
	l = len(lines[0])
	for bitPos in range(l):
		OXILines = getCommonBitLines(OXILines, bitPos)
		if len(OXILines) == 1:
			break
	for bitPos in range(l):
		CO2Lines = getCommonBitLines(CO2Lines, bitPos, False)
		if len(CO2Lines) == 1:
			break
	return bitsToDecimal(OXILines[0]) * bitsToDecimal(CO2Lines[0])

def main():
	filename = "input/03.txt"
	print("Using input file:", filename)
	f = open(filename, "r")
	input = f.read()
	lines  = input.split('\n')
	print("Part 1:", part1(turnMapBackwardsList(createMap(lines))))
	print("Part 2:", part2(lines))
	f.close() 

if __name__ == "__main__":
	main()