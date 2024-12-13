dirs = {"d": (1, 0), "u": (-1,0), "l": (0,-1), "r": (0,1)}
offsets = {"u": ((0,1), (0, -1)), "d": ((0,1), (0,-1)), "l": ((1,0),(-1,0)), "r": ((1,0), (-1, 0))}

pts = set()
grid = []
with open("input/12.txt", "r") as lines:
	x = 0
	for line in lines:
		grid.append(list(line.strip()))
		for y in range(len(line.strip())):
			pts.add((x,y))
		x += 1

pt1 = 0
pt2 = 0

while len(pts) > 0:
	start = pts.pop()
	polypts, tocheck = set(), {start}
	letter = grid[start[0]][start[1]]
	sided = set()
	while len(tocheck) > 0:
		curr = tocheck.pop()
		polypts.add(curr)
		for direc in dirs:
			i = dirs[direc]
			newcoords = (curr[0] + i[0], curr[1] + i[1])
			if newcoords in pts and grid[newcoords[0]][newcoords[1]] == letter:
				pts.discard(newcoords)
				tocheck.add(newcoords)
			elif newcoords not in polypts and newcoords not in tocheck:
				sided.add((newcoords, direc))
	pt1 += len(polypts) * len(sided)
	sides = 0
	while len(sided) > 0:
		curr = sided.pop()
		sides += 1
		for direc in offsets[curr[1]]:
			coord = [curr[0][0] + direc[0], curr[0][1] + direc[1]]
			while (tuple(coord), curr[1]) in sided:
				sided.discard((tuple(coord), curr[1]))
				coord[0] += direc[0]
				coord[1] += direc[1]
	pt2 += len(polypts) * sides
print(pt1, pt2)