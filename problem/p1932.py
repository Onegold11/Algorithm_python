import sys


def Tirangle_cost(triangle):
    cost = triangle

    for i in range(len(cost)):
        if i != 0:
            for j in range(len(cost[i])):
                if j == 0:
                    cost[i][j] = cost[i][j] + cost[i - 1][j]
                elif j == (len(cost[i]) - 1):
                    cost[i][j] = cost[i][j] + cost[i - 1][j - 1]
                else:
                    cost[i][j] = cost[i][j] + max(cost[i - 1][j - 1], cost[i - 1][j])
    print(max(cost[-1]))


n = int(input())
triangle = []

for _ in range(n):
    triangle.append(list(map(int, sys.stdin.readline().split())))

Tirangle_cost(triangle)
