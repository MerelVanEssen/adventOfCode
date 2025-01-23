from collections import defaultdict

with open("input/07.txt", "r") as f:
	rawInput = f.read()

commands = rawInput.split('\n')

folders = []
dic = defaultdict(int)

for command in commands:
	if command[:4] == "$ cd":
		name = command[5:]
		if name == "..":
			folders.pop()
		elif name == "/":
			folders = ["/"]
		else:
			folders.append(name)
	elif command[:4] == "$ ls":
		continue
	else:
		value, file = command.split()
		if value != "dir":
			size = int(value)
			for i, folder in enumerate(folders):
				path = "/".join(folders[:i + 1])
				dic[path] += int(value)

total = 0
removed_max = float('inf')
folder_size = 0
size_needed = 30000000 - (70000000 - dic["/"])

for name, value in dic.items():
	if value <= 100000:
		total += value
	if value > size_needed:
		if value - size_needed < removed_max:
			folder_size = value
			removed_max = value - size_needed
	
print("Part 1:", total)
print("Part 2:", folder_size)



<<<<<<< HEAD
=======


print("Part 1:", total, 1297683)

# 813094 too low
  1023738
>>>>>>> origin/main
