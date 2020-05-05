import sys


def HousePaint(n, cost):
    house_cost = cost

    for i in range(n):
        if i != 0:
            house_cost[i][0] = house_cost[i][0] + min(house_cost[i - 1][1], house_cost[i - 1][2])
            house_cost[i][1] = house_cost[i][1] + min(house_cost[i - 1][0], house_cost[i - 1][2])
            house_cost[i][2] = house_cost[i][2] + min(house_cost[i - 1][0], house_cost[i - 1][1])
    print(min(house_cost[n-1]))


n = int(input())
cost = []

for _ in range(n):
    cost.append(list(map(int, sys.stdin.readline().split())))

HousePaint(n, cost)
