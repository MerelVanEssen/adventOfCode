with open("input/08.txt", "r") as f:
	rawInput = f.read()

map = rawInput.split('\n')

seen = [[False for x in line] for line in map]


for y, wood in enumerate(map):
	prev = -1
	for x, tree in enumerate(wood):
		if int(tree) > prev:
			seen[y][x] = True
		prev = max(prev, int(tree))
	prev = -1
	for x, tree in enumerate(wood[::-1]):
		if int(tree) > prev:
			seen[y][len(map[0]) - 1 - x] = True
		prev = max(prev, int(tree))

x = 0
while x < len(map[0]):
	y = 0
	prev = -1
	while y < len(map):
		if int(map[y][x]) > prev:
			seen[y][x] = True
			prev = int(map[y][x])
		y += 1
	y = len(map) - 1
	prev = -1
	while y >= 0:
		if int(map[y][x]) > prev:
			seen[y][x] = True
			prev = int(map[y][x])
		y -= 1
	x += 1

total = 0
for line in seen:
	total += sum(line)

print("Part 1:", total)

highest = 0
dir = ((0,1), (0,-1), (1,0), (-1,0))
for y, wood in enumerate(map):
	if y == 0 or y == len(map) - 1:
		continue
	for x, tree in enumerate(wood):
		if x == 0 or x == len(map[0]) - 1:
			continue
		total = 1
		treehigh = int(map[y][x])
		for d in dir:
			newY = y
			newX = x
			amount = 0
			while True:
				newY = newY + d[0]
				newX = newX + d[1]
				if not (0 <= newY < len(map) and 0 <= newX < len(map[0])):
					break
				if int(map[newY][newX]) < treehigh:
					amount += 1
				else:
					amount += 1
					break
			total *= amount
		highest = max(highest, total)
				
print("Part 2:", highest)




def move_head_tail(head, tail, d):
	print(head, tail)
	if (abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1):
		return tail
	elif tail[0] + d[0] + d[0] == head[0] and tail[1] + d[1] + d[1] == head[1]:
		return [tail[0] + d[0], tail[1] + d[1]]
	else:
		return (find_diagonal_movement(head, tail, direction))


dir = {"U": [-1,0], "D": [1,0], "L": [0,-1], "R": [0,1]}
head = [15,10]
tail = [15,10]
longtail = [[15,10] for _ in range(9)]
print(longtail)
visit = set()
visit.add((0,0))
visit2 = set()
visit2.add((0,0))
for line in instructions:
	direction, steps = line.split()
	for _ in range(int(steps)):
		d = dir[direction]
		head[0] = head[0] + d[0]
		head[1] = head[1] + d[1]
		tail = move_head_tail(head, tail, d)
		visit.add((tail[0], tail[1]))
		for i, l_tail in enumerate(longtail):
			if i == 0:
				longtail[i] = move_head_tail(head, l_tail, d)
			else:
				longtail[i] = move_head_tail(longtail[i - 1], l_tail, d)
	for l_tail in longtail:
		visit2.add((l_tail[0], l_tail[1]))

map_2d = [[" " for _ in range(30)] for _ in range(30)]
for y, x in visit:
	map_2d[y + 1][x + 1] = "X"

for line in map_2d:
	print(line)