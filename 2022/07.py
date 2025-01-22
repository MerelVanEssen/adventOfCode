from collections import Counter

with open("input/07.txt", "r") as f:
	rawInput = f.read()

commands = rawInput.split('\n')

class Folder:
	def __init__(self, name, childs, files, parent):
		self.name = name
		self.childs = childs
		self.files = files
		self.parent = parent

		def __lt__(self, other):
			return self.depth < other.depth

folders = []
all = []
start = False
for item in commands:
	if item[:4] == "$ cd":

		if start == True:
			if len(folders) > 1:
				all.append(Folder(folders[-1], childs, files, folders[-2]))
			else:
				all.append(Folder(folders[-1], childs, files, folders[-1]))

		name = item[5:]
		if name == "..":
			folders.pop()
		else:
			folders.append(name)
		start = False
	elif item[:4] == "$ ls":
		childs = []
		files = []
		start = True
	elif item[0].isdigit():
		size, file = item.split()
		files.append((file, int(size)))
	else:
		childs.append(item[4:])

if len(folders) > 1:
	all.append(Folder(folders[-1], childs, files, folders[-2]))
else:
	all.append(Folder(folders[-1], childs, files, folders[-1]))

def getSize(folder, all):

	size = 0

	for file, s in folder.files:
		size += s
	
	for dir in folder.childs:
		for searchFolder in all:
			if searchFolder.name == dir and searchFolder.parent == folder.name:
				size += getSize(searchFolder, all)

	return size


total = 0
for folder in all:
	print(folder.parent, folder.name, folder.childs, folder.files)
	size = getSize(folder, all)
	print(size)
	if size < 100000:
		total += size





print("Part 1:", total, 1297683)

# 813094 too low
  1023738