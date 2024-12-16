from collections import deque, defaultdict

INCREASE = 1
DECREASE = 0

class Solution:
	# checks difference between the numbers and returns false is they are incorrect
	def checkDifference(self, rapport, inc_dec):
		for i in range(len(rapport) - 1):
			if inc_dec == DECREASE:
				diff = rapport[i] - rapport[i + 1]
			else:
				diff = rapport[i + 1] - rapport[i]
			if diff < 1 or diff > 3:
				return False
		return True
	
	# part 1
	def checkLine1(self, rapport):
		# checks if sequence is increasing or decreasing
		inc_dec = INCREASE if rapport[0] < rapport[1] else DECREASE
		return self.checkDifference(rapport, inc_dec)

	def checkLine2(self, rapport, check):
		save = True

		inc_dec = INCREASE if rapport[0] < rapport[1] else DECREASE
		if self.checkDifference(rapport, inc_dec):
			return True
		if check == 0:
			for i in range(len(rapport)):
				if i == 1:	# checks when we remove the first element
					newLine = rapport[1:]
					if self.checkLine2(newLine, 1):
						return True
				# removes the next element and checks the line again
				newLine = rapport[:i + 1] + rapport[i + 2:]
				if self.checkLine2(newLine, 1):
					return True

				# removes the curr ellement and checks the line again
				newLine = rapport[:i] + rapport[i + 1:]
				if self.checkLine2(newLine, 1):
					return True
				
		return False
		
	def collectRapports(self, lines):
		validRapports2 = 0
		validRapports1 = 0

		for line in lines:
			rapport = [int(x) for x in line.split()]
			save1 = self.checkLine1(rapport)
			if save1:
				validRapports1 +=1
			save2 = self.checkLine2(rapport, 0)
			if save2:
				validRapports2 += 1
		return (validRapports1, validRapports2)

def main():
	sol = Solution()
	with open("input/02.txt", "r") as f:
		lines = f.read().split('\n')
	print(sol.collectRapports(lines))

if __name__ == "__main__":
	main()
