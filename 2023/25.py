import networkx as nx

input = open("input/25.txt", "r").read()

dic = {}
input = input.split('\n')
allConnections = set()
for line in input:
	wires = line.split()
	headwire = wires[0].replace(":", "")
	dic[headwire] = wires[1:]
	for wire in wires[1:]:
		if (headwire, wire) in allConnections:
			continue
		allConnections.add((wire, headwire))

G = nx.Graph()

for connection in allConnections:
	G.add_node(connection[0] + connection[1])
print(allConnections)

print(list(G.edges))