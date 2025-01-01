import re
from collections import deque
from math import gcd
from functools import reduce
from collections import Counter, defaultdict
import heapq
from functools import cache
from math import gcd
from functools import reduce

# self.hands = [[] for _ in range(7)]
# inte = [int(x) for x in line]
# self.field = [['.' for _ in row] for row in self.map]

class Solution:
	def __init__(self, input):
		pattern = r"broadcaster -> ([\w, ]+)\n"
		bc = re.findall(pattern, input)
		bc = bc[0].split(',')
		self.bc = [name.strip() for name in bc]

		pattern2 = r"([%&])(\w+) -> ([\w, ]+)"
		matches = re.findall(pattern2, input)
		self.ff = {}
		self.conj = {}
		self.receivers = {}
		for m in matches:
			sort, name, sendTo = m
			receiver = sendTo.replace(",", "")
			if sort == '%':
				self.ff[name] = "off"
			else:
				self.conj[name] = []
			self.receivers[name] = receiver.split()
		for name, inputs in self.conj.items():
			for key, value in self.receivers.items():
				if name in value:
					inputs.append([key, 'low'])
					self.conj[name] = inputs
		self.amount = {'high': 0, 'low': 0}
		self.sendToNC = {}
		for item, value in self.conj['nc']:
			self.sendToNC[item] = []
	
	def flipflow(self, name, signal):
		if signal == 'high':
			return None
		if self.ff[name] == 'off':
			self.ff[name] = 'on'
			return  'high'
		else:
			self.ff[name] = 'off'
			return 'low'
	
	def conjunction(self, sender, receiver, signal, i):
		incoming = self.conj[receiver]
		allHigh = True
		for i, check in enumerate(incoming):
			checkName, checkSignal = check
			if checkName == sender:
				incoming[i][1] = signal
			if incoming[i][1] == 'low':
				allHigh = False

		if allHigh:
			return 'low'
		else:
			return 'high'

	def part1(self):
		searchRX = None

		for i in range(1000):
			deq = deque()
			start = True

			while deq or start == True:
				if start == True:
					receivers = self.bc
					sender = "broadcast"
					signal = 'low'
					self.amount[signal] += 1
				else:
					sender, signal = deq.popleft()
					if sender not in self.receivers:
						continue
					receivers = self.receivers[sender]

				self.amount[signal] += len(receivers)
				start = False

				for receiver in receivers:
					if receiver in self.ff:
						newSignal = self.flipflow(receiver, signal)
						if newSignal == None:
							continue
					elif receiver in self.conj:
						newSignal = self.conjunction(sender, receiver, signal, i)
					deq.append([receiver, newSignal])

		return self.amount['high'] * self.amount['low']

	def part2(self):
		for i in range(10000):
			deq = deque()
			start = True

			while deq or start == True:
				if start == True:
					receivers = self.bc
					sender = "broadcast"
					signal = 'low'
					self.amount[signal] += 1
				else:
					sender, signal = deq.popleft()
					if sender not in self.receivers:
						continue
					receivers = self.receivers[sender]

				# saves first and second moment that the receiver is nc
				if 'nc' in receivers and signal == 'high':
						if len(self.sendToNC[sender]) < 3:
							values = self.sendToNC[sender]
							values.append(i)
							self.sendToNC[sender] = values

				self.amount[signal] += len(receivers)
				start = False

				for receiver in receivers:
					if receiver in self.ff:
						newSignal = self.flipflow(receiver, signal)
						if newSignal == None:
							continue
					elif receiver in self.conj:
						newSignal = self.conjunction(sender, receiver, signal, i)
					deq.append([receiver, newSignal])
		
		# calculate the moment when all the signals are high towards nc
		deq = []
		for key, values in self.sendToNC.items():
			first, second = values
			deq.append(second - first)
		
		def lcm(a, b):
			return abs(a * b) // gcd(a, b)

		def lcm_of_lists(numbers):
			return reduce(lcm, numbers)
		
		return lcm_of_lists(deq)

def main():
	input = open("input/20.txt", "r").read()

	sol = Solution(input)
	print("Part 1:", sol.part1())
	print("Part 2:", sol.part2())

if __name__ == "__main__":
	main()

	# 999 too low
	# 246206750905905 too high