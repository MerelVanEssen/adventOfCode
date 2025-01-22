from collections import defaultdict

with open("input/07.txt", "r") as f:
	rawInput = f.read()

commands = rawInput.split('\n')
dic = defaultdict(int)
folders = {}
currentDir = []
inLs = False

for line in commands:
	if line[0:7] == "$ cd ..":
		currentDir.pop()
	elif line[0:4] == "$ cd":
		currentDir.append(line[5:])
	elif line[0:4] != "$ ls":
		nr, file = line.split()
		if nr != "dir":
			for dir in currentDir:
				dic[dir] += int(nr)

total = 0
for parent, child in dic.items():
	print(parent, child)
	if child < 100000:
		total += child
	
print("Part 1:", total, 1297683)