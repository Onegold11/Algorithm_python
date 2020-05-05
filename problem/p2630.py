import sys


def split_paper(start_x, start_y, n):
    global paper
    global white
    global blue
    color = paper[start_y][start_x]

    for i in range(start_y, start_y + n):
        for j in range(start_x, start_x + n):
            if paper[i][j] != color:
                length = n // 2
                split_paper(start_x, start_y, length)
                split_paper(start_x + length, start_y, length)
                split_paper(start_x, start_y + length, length)
                split_paper(start_x + length, start_y + length, length)
                return
    if color == 1:
        blue += 1
    else:
        white += 1


global white
global blue
white = 0
blue = 0

N = int(input())
paper = list()
for _ in range(N):
    paper.append(list(map(int, sys.stdin.readline().split())))
split_paper(0, 0, N)
print(white)
print(blue)
