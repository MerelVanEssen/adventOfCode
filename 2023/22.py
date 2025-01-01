from collections import deque

class Block:
	def __init__(self, input, nr):
		self.blockNr = str(nr)
		ends = input.split("~")
		self.x1, self.y1, self.z1 = map(int, ends[0].split(','))
		self.x2, self.y2, self.z2 = map(int, ends[1].split(','))
		self.supported = set()
		self.support = set()
		self.amount = 0

	def __repr__(self):
		return self.blockNr
		
	def overlap(self, other):
		if max(self.x1, other.x1) <= min(self.x2, other.x2) and max(self.y1, other.y1) <= min(self.y2, other.y2):
			return True
		else: 
			return False

input = open("input/22.txt", "r").read()

rawinput = input.split()
blocks = []
for i, item in enumerate(rawinput):
	blocks.append(Block(item, i))
	
blocks.sort(key=lambda b: b.z1)


for i, block in enumerate(blocks):
	floor = 1
	for other in blocks[:i]:
		if block.overlap(other):
			floor = max(floor, other.z2 + 1)
	difference = block.z1 - floor
	block.z1 -= difference
	block.z2 -= difference

blocks.sort(key=lambda b: b.z1)

for i, block in enumerate(blocks):
	for other in blocks[:i]:
		if block.overlap(other) and block.z1 - 1 == other.z2:
			block.supported.add(other)
			other.support.add(block)
			
total1 = 0
notMove = set()
for block in blocks:
	remove = True
	for supports in block.support:
		if len(supports.supported) == 1:
			remove = False
			break
	if remove:
		total1 += 1
	else:
		notMove.add(block)

print("Part 1:", total1)

total2 = 0

for block in blocks:
	q = deque([block])
	fallen = set()
	while q:
		b = q.popleft()
		if b in fallen:
			continue
		fallen.add(b)
		for subblock in b.support:
			if subblock.supported.issubset(fallen):
				q.append(subblock)
	total2 += len(fallen) - 1

print("Part 2:", total2)