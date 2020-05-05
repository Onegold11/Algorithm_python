import sys


def backtracking(board, i=0):
    global blank_pos
    if i == len(blank_pos):
        print_board(board)
        sys.exit()
    else:
        for value in range(1, 10):
            board[blank_pos[i][1]][blank_pos[i][0]] = value
            if promising(board, i):
                backtracking(board, i + 1)
            board[blank_pos[i][1]][blank_pos[i][0]] = 0


def promising(board, i):
    global blank_pos
    x = blank_pos[i][0]
    y = blank_pos[i][1]

    for j in range(0, len(board)):
        if board[y][j] != 0 and j != x and board[y][j] == board[y][x]:
            return False
    for j in range(0, len(board)):
        if board[j][x] != 0 and j != y and board[j][x] == board[y][x]:
            return False

    start_x = (x // 3) * 3
    start_y = (y // 3) * 3

    for i in range(start_x, start_x+3):
        for j in range(start_y, start_y+3):
            if board[j][i] == board[y][x] and i != x and j != y:
                return False
    return True


def print_board(board):
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            print("{}".format(board[i][j]), end=" ")
        if i != len(board)-1:
            print()


def get_blank_pos(board):
    lst = []
    for y in range(0, len(board)):
        for x in range(0, len(board)):
            if board[y][x] == 0:
                lst.append([x, y])
    return lst


board = []
for _ in range(0, 9):
    line = list(map(int, input().split()))
    board.append(line)

blank_pos = get_blank_pos(board)
backtracking(board)
