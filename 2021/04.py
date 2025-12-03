# Advent of Code 2021 - Day 4	

# check if a board has bingo
def checkBingo(board):
	for row in board:
		if all(nr == 'X' for nr in row):
			return True
	for col in range(len(board[0])):
		if all(row[col] == 'X' for row in board):
			return True
	return False

# count unmarked numbers on a board
def countUnmarked(board):
	total = 0
	for row in board:
		for nr in row:
			if nr != 'X':
				total += int(nr)
	return total

def result(balls, boards):
	first, last = None, None
	for ball in balls:
		for i, board in enumerate(boards):
			if board == '-1':
				continue
			for row in board:
				if ball in row:
					row[row.index(ball)] = 'X'
					break
			if checkBingo(board):
				if not first:
					first = countUnmarked(board) * int(ball)
				last = countUnmarked(board) * int(ball)
				boards[i] = '-1'
	return first, last

def createBingoBoards(boards):
	boards.pop(0)
	boards = [board.split('\n') for board in boards]
	for i, board in enumerate(boards):
		for j, row in enumerate(board):
			board[j] = row.split()
		boards[i] = board
	return boards
filename = "input/04.txt"
print("Using input file:", filename)
f = open(filename, "r")
input = f.read()
boards  = input.split('\n\n')
balls = boards[0].split(',')
boards = createBingoBoards(boards)
print("Results: ", result(balls, boards))
f.close() 