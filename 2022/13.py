

with open("input/13.txt", "r") as f:
	input = f.read()

input = input.split('\n\n')

def getNextNrInList(lst: str):
    i = 0
    while i < len(lst) and lst[i].isdigit():
        i += 1
    return int(lst[:i]), lst[i:]

index = 1
for lists in input:
    l1, l2 = lists.split('\n')
    i, j = 0, 0
    goodPair = True

    while l1:
        if l1[0] == '[' and l2[0] == '[':
            l1 = l1[1:]
            l2 = l2[1:]
        elif l1[0] == ']' and l2[0] == ']':
            l1 = l1[1:]
            l2 = l2[1:]
        elif l1[0] == '[':
            l1 = l1[1:]
        elif l2[0] == '[':
            l2 = l2[1:]

        if l1 and l1[0].isdigit() and l2 and l2[0].isdigit():
            n1, l1 = getNextNrInList(l1)
            n2, l2 = getNextNrInList(l2)
            if n1 < n2:
                print(n1, n2, "Left is smaller", l1, l2)
            elif n1 > n2:
                print(n1, n2, "Right is smaller", l1, l2)
                goodPair = False
                break

        if l1 and l1[0] == ',':
            l1 = l1[1:]
        if l2 and l2[0] == ',':
            l2 = l2[1:]
    if goodPair:
        print("Good pair:", index)
        index += 1