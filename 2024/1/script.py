class Solution1:
	def function(self, lines):
		awnser = 0

		for line in lines:
			nrString = ""
			for letter in line:
				if letter >= '0' and letter <= '9':
					nrString += letter
					break
			for letter in reversed(line):
				if letter >= '0' and letter <= '9':
					nrString += letter
					break
			awnser += int(nrString)
		return (awnser)

class Solution2:
	def function(self, lines):
		digits = [".", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
		digits2 = [".","1", "2", "3", "4", "5", "6", "7", "8", "9"]
		awnser = 0

		def searchNr(line):
			firstIndex = len(line)
			lastIndex = -1
			lastNr = ""
			firstNr = ""
			for i in range(len(digits)):
				index = line.find(digits[i])
				index2 = line.find(digits2[i])
				index3 = line.rfind(digits[i])
				index4 = line.rfind(digits2[i])
				if index != -1:
					if index < firstIndex:
						firstIndex = index
						firstNr = str(i)
				if index2 != -1:
					if index2 < firstIndex:
						firstIndex = index2
						firstNr = str(i)
				if index3 != -1:
					if index3 > lastIndex:
						lastIndex = index3
						lastNr = str(i)
				if index4 != -1:
					if index4 > lastIndex:
						lastIndex = index4
						lastNr = str(i)
				
				i += 1
			return firstNr + lastNr
		
		for line in lines:
			nrString = ""
			nrString += searchNr(line)
			awnser += int(nrString)
		return (awnser)

def main():
	sol1 = Solution1()
	sol2 = Solution2()
	with open('input.txt', 'r') as file:
		input = file.read()
	lines = input.splitlines()
	print("2023 Day 1")
	print("Part 1:", sol1.function(lines))
	print("Part 2:", sol2.function(lines))

if __name__ == "__main__":
	main()
