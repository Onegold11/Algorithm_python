import sys
import io


def zip_video(start_x, start_y, n):
    global video
    global result
    color = video[start_y][start_x]

    for i in range(start_y, start_y + n):
        for j in range(start_x, start_x + n):
            if video[i][j] != color:
                length = n // 2
                result.write('(')
                zip_video(start_x, start_y, length)
                zip_video(start_x + length, start_y, length)
                zip_video(start_x, start_y + length, length)
                zip_video(start_x + length, start_y + length, length)
                result.write(')')
                return
    result.write(color)


global video
global result
N = int(input())
video = list()
result = io.StringIO()

for _ in range(N):
    video.append(list(sys.stdin.readline().strip()))
zip_video(0, 0, N)
print(result.getvalue())
