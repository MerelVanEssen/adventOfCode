from math import gcd
import re

class Solution:
	def __init__(self, input):
		self.input = input
		self.results = []
		self.res = []

	def searchInput(self):
		# Gebruik regex om de input correct te parsen
		pattern = r"(Button [AB]|Prize): X[+=]?(\d+), Y[+=]?(\d+)"
		matches = re.findall(pattern, self.input)
		for match in matches:
			if match:
				label = match[0]  # Button A, Button B of Prize
				x_value = int(match[1])  # X-waarde als een integer
				y_value = int(match[2])  # Y-waarde als een integer
				self.results.append((label, x_value, y_value))

	def ex_gcd(self, a, b):
		# Initialiseer de x, y waarden van de eerste recursie
		x0, y0, x1, y1 = 1, 0, 0, 1

		while b != 0:
			# Bereken de quotiënt en het restant
			q = a // b
			a, b = b, a % b

			# Update de x en y waarden
			x0, x1 = x1, x0 - q * x1
			y0, y1 = y1, y0 - q * y1

		return a, x0, y0


	def min_tokens(self, a_x, a_y, b_x, b_y, p_x, p_y):
		# Bereken de GCD van de bewegingen
		gcd_x, x, y = self.ex_gcd(a_x, b_x)
		gcd_y, x, y = self.ex_gcd(a_y, b_y)
		print(gcd_x, gcd_y)
		
		# Controleer of een oplossing mogelijk is
		if p_x % gcd_x != 0 or p_y % gcd_y != 0:
			return None  # Geen oplossing mogelijk
		
		# Schaal alles terug met GCD
		a_x //= gcd_x
		b_x //= gcd_x
		p_x //= gcd_x
		a_y //= gcd_y
		b_y //= gcd_y
		p_y //= gcd_y

		# Zoeken naar minimale kosten
		min_cost = float('inf')
		best_n_a, best_n_b = None, None

		# Itereer over mogelijke waarden van n_a
		for n_a in range(0, p_x // a_x + 1):  # Beperk op basis van het x-doel
			# Bereken n_b op basis van x-verplaatsing
			remaining_x = p_x - n_a * a_x
			if remaining_x % b_x != 0:
				continue
			n_b_x = remaining_x // b_x

			# Controleer ook de y-verplaatsing
			if n_a * a_y + n_b_x * b_y == p_y:
				cost = 3 * n_a + 1 * n_b_x
				if cost < min_cost:
					min_cost = cost
					best_n_a, best_n_b = n_a, n_b_x
		print(best_n_a, best_n_b)
		if best_n_a is not None and best_n_b is not None:
			return min_cost, best_n_a, best_n_b
		else:
			return None  # Geen oplossing gevonden

	def part(self, part):
		total = 0
		self.searchInput()
		extra = 0

		if part == 2:
			extra = 10000000000000  # Alleen voor part 2

		while len(self.results) >= 3:  # Zorg ervoor dat er voldoende gegevens zijn
			buttonA = self.results.pop(0)
			buttonB = self.results.pop(0)
			prize = self.results.pop(0)

			# Roep de min_tokens functie aan met de geschaalde prijswaarden
			saveResult = self.min_tokens(buttonA[1], buttonA[2], buttonB[1], buttonB[2], prize[1] + extra, prize[2] + extra)
			if part == 1 and saveResult:
				total += saveResult[0]
			if part == 2 and saveResult:
				print(saveResult)
				total += saveResult

		return total

def main():
	# CHANGE INPUTFILE
	input = open("input/13.txt", "r").read()

	sol = Solution(input)
	print("Part 1:", sol.part(1))
	print("Part 2:", sol.part(2))

if __name__ == "__main__":
	main()