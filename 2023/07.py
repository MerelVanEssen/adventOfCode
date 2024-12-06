from collections import Counter
from icecream import ic # source myenv/bin/activate

class Solution:
	# set with values time and distance and for part two one number
	def __init__(self, input, part):
		self.lines = input.split('\n')
		self.amountHands = len(self.lines)
		if part == 1:
			transform = str.maketrans("AKQJT98765432", "abcdefghijklm")
		else:
			transform = str.maketrans("AKQT98765432J", "abcdefghijklm")
		for i in range(len(self.lines)):
			hand, value = self.lines[i].split()
			self.lines[i] = [hand.translate(transform), int(value)]
		self.hands = [[] for _ in range(7)]

	# sort the cards from the same groups and give them a rank
	def calculateHands(self):
		rank = self.amountHands
		total = 0
		i = 0
		for hand in self.hands:
			hand.sort()
			if len(hand) == 0:
				continue
			for cards, value in hand:
				total += value * rank
				rank -= 1
			i += 1
		return total
	
	# adding the cards to the possible groups
	def addingHands(self, amount, hand, value):
		if amount[4] == 1: 						# Five of a Kind
			self.hands[0].append([hand, value])
		elif amount[3] == 1: 					# Four of a Kind
			self.hands[1].append([hand, value])
		elif amount[2] >= 1 and amount[1] >= 1:	# Full house
			self.hands[2].append([hand, value])
		elif amount[2]:							# Three of a Kind
			self.hands[3].append([hand, value])
		elif amount[1] == 2:					# Two Pairs
			self.hands[4].append([hand, value])
		elif amount[1] == 1:					# Pair
			self.hands[5].append([hand, value])
		else:									# Highest card
			self.hands[6].append([hand, value])

	# Part 1, looping through the races and when it is enough, total time minus 2 time "not enough"
	def part1(self):
		for hand, value in self.lines:
			counter = Counter(hand)
			amount = [0,0,0,0,0]
			for count in counter.values():
				amount[count - 1] += 1
			self.addingHands(amount, hand, value)
		return (self.calculateHands())

	# adding the jokers to the highest handcombi, except for the full house case
	def addJokerValues(self, hand):
		counter = Counter(hand)
		amount = [0,0,0,0,0]
		jokers = counter['m']
		counter['m'] = 0
		for count in counter.values():
			if count != 0:
				amount[count - 1] += 1
		if jokers == 0:
			return amount
		if jokers == 5:
			amount[4] = 1
		elif amount[1] == 2: # full house (special)
			amount[1] -= 1
			amount[2] += 1
		else:
			index = max((i for i, num in enumerate(amount) if num > 0), default=-1)
			amount[index + jokers] = 1
			amount[index] -= 1
		return (amount)

	# Part 2
	def part2(self):
		# reset hands from part 1
		self.hands = [[] for _ in range(7)]
		for hand, value in self.lines:
			amount = self.addJokerValues(hand)
			self.addingHands(amount, hand, value)
		return (self.calculateHands())

def main():
	with open("input/07.txt", "r") as f:
		input = f.read()

	sol = Solution(input, 1)
	print("Part1:", sol.part1())
	sol2 = Solution(input, 2)
	print("Part2:", sol2.part2())

if __name__ == "__main__":
	main()
