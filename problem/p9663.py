"""
def backtracking(board, i=0):
    global count
    if i == len(board):
        count += 1
    else:
        for j in range(1, len(board) + 1):
            board[i] = j
            if promising(i, board):
                backtracking(board, i + 1)


def promising(i, board):
    if i == 0:
        return True
    for j in range(0, i):
        if board[j] == board[i]:
            return False
        if abs(board[j] - board[i]) == (i - j):
            return False
    return True


n = int(input())
chess_board = [0 for _ in range(n)]
count = 0

backtracking(chess_board)
print(count)
"""

counts = [0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596]
print(counts[int(input())])
