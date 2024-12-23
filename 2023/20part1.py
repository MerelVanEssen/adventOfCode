import re
from collections import deque
from math import gcd
from functools import reduce
from collections import Counter, defaultdict
import heapq
from functools import cache

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
		self.sendToNC = defaultdict(int)
		for item, value in self.conj['nc']:
			self.sendToNC[item] = 0
	
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
		if allHigh and receiver in self.sendToNC and self.sendToNC[receiver] == 0:
			self.sendToNC[sender] = i
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
					if receiver == 'rx' and newSignal == 'high' and searchRX == None:
						print(sender, receivers, newSignal)
						searchRX = i
					deq.append([receiver, newSignal])

		return self.amount['high'] * self.amount['low'], searchRX

	def part2(self):
		searchRX = None

		for i in range(100000):
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
		print(self.sendToNC)
		return self.amount['high'] * self.amount['low'], searchRX

def main():
	# CHANGE INPUTFILE
	input = open("21.txt", "r").read()

	sol = Solution(input)
	# print("Part 1:", sol.part1(), 1020211150)
	print("Part 2:", sol.part2())

if __name__ == "__main__":
	main()

	# 999 too low