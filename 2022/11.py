import re
import copy

with open("input/11.txt", "r") as f:
	input = f.read()

monkeys = input.split('\n\n')

regex_items = R"Starting items: ([\d, ]+)"
regex_operation = R"Operation: new = ((\w+) (\W) (\w+|\d+))"
regex_test = R"Test: divisible by (\d+)"
regex_true = R"true: throw to monkey (\d+)"
regex_false = R"false: throw to monkey (\d+)"

for i, monkey in enumerate(monkeys):
	lines = monkey.splitlines()
	items_string = re.search(regex_items, monkey).group(1)
	items_string = items_string.replace(" ", "")
	items_str = items_string.split(',')
	start_items = []
	for item in items_str:
		start_items.append(int(item))
	op = re.search(regex_operation, monkey).group(1)
	op = op.split()
	test = re.search(regex_test, monkey).group(1)
	true = re.search(regex_true, monkey).group(1)
	false = re.search(regex_false, monkey).group(1)
	monkeys[i] = [start_items, op, test, true, false, 0]

def calculate(old, statement):
	first, sign, second = statement
	if first == "old":
		first = old
	else:
		first = int(first)
	if second == "old":
		second = old
	else:
		second = int(second)
	if sign == "+":
		return first + second
	elif sign == "-":
		return first - second
	elif sign == "/":
		return first / second
	else:
		return first * second

def go_through_rounds(monkeys, devide, rounds):
	for x in range(rounds):
		for i, monkey in enumerate(monkeys):
			if monkey[0] == []:
				continue
			items = monkey[0]
			monkeys[i][0] = []
			for item in items:
				monkeys[i][5] += 1
				newItem = calculate(item, monkey[1])
				if devide:
					newItem //= 3
				# if newItem > 10000000000:
				# 	newItem %= 10000000000
				if newItem % int(monkey[2]) == 0:
					monkeys[int(monkey[3])][0].append(newItem % 100000000)
				else:
					monkeys[int(monkey[4])][0].append(newItem % 100000000)
			print(newItem)
		print(x)
	highest = []
	for monkey in monkeys:
		highest.append(monkey[5])
	print(highest)
	highest.sort()
	return highest

highest = go_through_rounds(copy.deepcopy(monkeys), True, 20)

print("Total part 1:",highest[-1] * highest[-2])

highest = go_through_rounds(copy.deepcopy(monkeys), true, 1000)

print("Total part 2:",highest[-1] * highest[-2])
print("Total part 2:",2713310158)


# 149401725 low
# 2713310158 low






