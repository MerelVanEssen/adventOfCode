from collections import defaultdict

class Solution:
	def calculate(self, nr):
		if nr <= 2:
			return nr
		total = 1
		nr -= 1
		while nr:
			total *= 2
			nr -= 1
		return total
	
	def function(self, input):
		lines = input.split('\n')
		totalSum = 0
		amountLines = 0
		for line in lines:
			amountLines += 1
			card, numbers = line.split(':')
			winning, hand = numbers.split('|')
			winCards = winning.split()
			handCards = hand.split()
			winningCards = 0
			for card in handCards:
				if card in winCards:
					winningCards += 1
			totalSum += self.calculate(winningCards)
		return (totalSum, amountLines)

	def function2(self, input, amountLines):
		lines = input.split('\n')
		totalSum = 0
		d = [1] * (amountLines + 1)
		amountCards = 0
		for line in lines:
			card, numbers = line.split(':')
			name, cardNr = card.split()
			winning, hand = numbers.split('|')
			winCards = winning.split()
			handCards = hand.split()
			winningCards = 0
			amountCards += d[int(cardNr)]
			for card in handCards:
				if card in winCards:
					winningCards += 1
			for i in range(winningCards):
				d[int(cardNr) + 1 + i] += d[int(cardNr)]
		return (amountCards)



def main():
	sol = Solution()
	with open("input/04.txt", "r") as f:
		input = f.read()
	awsner, lines = sol.function(input)
	print("Part 1", awsner)
	print("Part 2", sol.function2(input, lines))
	f.close() 

if __name__ == "__main__":
	main()
