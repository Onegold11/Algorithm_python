import sys


def split_paper(start_x, start_y, n):
    global paper
    global one
    global zero
    global m_one
    color = paper[start_y][start_x]

    for i in range(start_y, start_y + n):
        for j in range(start_x, start_x + n):
            if paper[i][j] != color:
                length = n // 3
                split_paper(start_x, start_y, length)
                split_paper(start_x + length, start_y, length)
                split_paper(start_x + length * 2, start_y, length)
                split_paper(start_x, start_y + length, length)
                split_paper(start_x + length, start_y + length, length)
                split_paper(start_x + length * 2, start_y + length, length)
                split_paper(start_x, start_y + length * 2, length)
                split_paper(start_x + length, start_y + length * 2, length)
                split_paper(start_x + length * 2, start_y + length * 2, length)
                return
    if color == 1:
        one += 1
    elif color == -1:
        m_one += 1
    else:
        zero += 1


one = 0
zero = 0
m_one = 0

N = int(input())
paper = list()
for _ in range(N):
    paper.append(list(map(int, sys.stdin.readline().split())))
split_paper(0, 0, N)
print(m_one)
print(zero)
print(one)
