with open("input/09.txt", "r") as f:
	rawInput = f.read()

instructions = rawInput.split('\n')

def move_head_tail(head, tail, d):
	if (abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1):
		return tail
	elif tail[0] == head[0] and tail[1] < head[1]:
		return [tail[0], tail[1] + 1]
	elif tail[0] == head[0] and tail[1] > head[1]:
		return [tail[0], tail[1] - 1]
	elif tail[0] < head[0] and tail[1] == head[1]:
		return [tail[0] + 1, tail[1]]
	elif tail[0] > head[0] and tail[1] == head[1]:
		return [tail[0] - 1, tail[1]]
	elif head[0] < tail[0] and head[1] < tail[1]:
		return [tail[0] - 1, tail[1] - 1]
	elif head[0] < tail[0] and head[1] > tail[1]:
		return [tail[0] - 1, tail[1] + 1]
	elif head[0] > tail[0] and head[1] > tail[1]:
		return [tail[0] + 1, tail[1] + 1]
	elif head[0] > tail[0] and head[1] < tail[1]:
		return [tail[0] + 1, tail[1] - 1]
	else:
		return tail

dir = {"U": [-1,0], "D": [1,0], "L": [0,-1], "R": [0,1]}

# Part 1
head = [0,0]
tail = [0,0]
visit = set()
visit.add((0,0))

# Part 2
longtail = [[0,0] for _ in range(9)]
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
		visit2.add((longtail[-1][0], longtail[-1][1]))

print("Total part 1:", len(visit))
print("Total part 2:", len(visit2))




