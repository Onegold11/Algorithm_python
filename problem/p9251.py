import sys


def CommonLCS(f_data, s_data):
    total_max = [[0 for _ in range(len(f_data) + 1)] for _ in range(len(s_data) + 1)]

    for i in range(1, len(s_data) + 1):
        for j in range(1, len(f_data) + 1):
            if s_data[i - 1] == f_data[j - 1]:
                total_max[i][j] = total_max[i - 1][j - 1] + 1
            else:
                total_max[i][j] = max(total_max[i][j - 1], total_max[i - 1][j])

    print(total_max[-1][-1])


f_str = sys.stdin.readline()[:-1]
s_str = sys.stdin.readline()[:-1]

CommonLCS(f_str, s_str)
