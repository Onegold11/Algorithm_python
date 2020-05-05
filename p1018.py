import sys

row_chess, column_chess = 8, 8
row, column = map(int, sys.stdin.readline().split())
board_chess_W = ["WBWBWBWB",
                 "BWBWBWBW",
                 "WBWBWBWB",
                 "BWBWBWBW",
                 "WBWBWBWB",
                 "BWBWBWBW",
                 "WBWBWBWB",
                 "BWBWBWBW"]

board_chess_B = ["BWBWBWBW",
                 "WBWBWBWB",
                 "BWBWBWBW",
                 "WBWBWBWB",
                 "BWBWBWBW",
                 "WBWBWBWB",
                 "BWBWBWBW",
                 "WBWBWBWB"]
board = []

for i in range(row):
    board.append(sys.stdin.readline()[:-1])


def check_board(_board, _board_chess, _x, _y):
    change = 0
    for _row in range(8):
        for _column in range(8):
            if _board[_row+_x][_column+_y] != _board_chess[_row][_column]:
                change += 1
    return change


min_change = 64
for x in range(row - row_chess+1):
    for y in range(column - column_chess+1):
        min_change_step = min([
            check_board(board, board_chess_B, x, y),
            check_board(board, board_chess_W, x, y)]
        )
        if min_change_step < min_change:
            min_change = min_change_step
print(min_change)
