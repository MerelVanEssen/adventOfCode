from collections import Counter

class Solution:
	# set with values time and distance and for part two one number
	def __init__(self, input):
		self.lines = input.split('\n')
		self.amountHands = len(self.lines)
		transform = str.maketrans("AKQT98765432J", "abcdefghijklm")
		for i in range(len(self.lines)):
			hand, value = self.lines[i].split()
			self.lines[i] = [hand.translate(transform), int(value)]
		self.hands = [[] for _ in range(7)]

	def calculateHands(self):
		rank = self.amountHands
		total = 0
		i = 0
		for hand in self.hands:
			hand.sort()
			if len(hand) == 0:
				continue
			for cards, value in hand:
				print(hand, value, total, rank, "i", i)
				total += value * rank
				rank -= 1
			i += 1
		return total
    # 0 Five of a kind, where all five cards have the same label: AAAAA
    # 1 Four of a kind, where four cards have the same label and one card has a different label: AA8AA
    # 2 Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
    # 3 Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
    # 4 Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
    # 5 One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
    # 6 High card, where all cards' labels are distinct: 23456
	
	# Part 1, looping through the races and when it is enough, total time minus 2 time "not enough"
	def function(self, part):
		for hand, value in self.lines:
			counter = Counter(hand)
			jokers = 0
			if part == 2:
				jokers = counter['m'] # search for jokers
			counter['m'] = 0
			if any(count == 5 for count in counter.values()) or (jokers > 0 and any(count == 5 - jokers for count in counter.values())): # Five of a Kind
				print("add five", hand, value)
				self.hands[0].append([hand, value])
			elif any(count == 4 for count in counter.values()) or (jokers > 0 and any(count == 4 - jokers for count in counter.values())): # Four of a Kind
				print("add four", hand, value)
				self.hands[1].append([hand, value])
			else:
				found_3 = any(key for key, count in counter.items() if count == 3)
				found_2 = any(key for key, count in counter.items() if count == 2)
				if found_3 and found_2:
					print("add full", hand, value)
					self.hands[2].append([hand, value])
				elif found_3 or (jokers > 0 and found_2):
					print("add three", hand, value)
					self.hands[3].append([hand, value])
				elif found_2:
					amountPairs = 0
					for key, count in counter.items():
						if count == 2:
							amountPairs += 1
					print("amount pairs", amountPairs)
					if amountPairs == 2 and jokers > 0:
						self.hands[2].append([hand, value])
						print("add full", hand, value)
					elif amountPairs == 2 or (jokers > 0):
						self.hands[4].append([hand, value])
						print("add 2 pairs", hand, value)
					else:
						self.hands[5].append([hand, value])
						print("add pair", hand, value)
				else:
					if jokers == 1:
						print("add pair", hand, value)
						self.hands[5].append([hand, value])
					elif jokers == 2:
						self.hands[3].append([hand, value])
						print("add three", hand, value)
					else:
						print("add lonley", hand, value)
						self.hands[6].append([hand, value])
		return (self.calculateHands())
		

	# Part 2
	def function2(self):
		print("part2")

def main():
	f = open("input.txt", "r")
	input = f.read()

	sol = Solution(input)
	# print("Part1:", sol.function(1))
	print("Part2:", sol.function(2), 250665248)
	f.close() 

if __name__ == "__main__":
	main()
