def Knapsack(total, max_weight, weight, value):
    bag = [[0 for _ in range(max_weight + 1)] for _ in range(total + 1)]

    for i in range(1, total + 1):
        for j in range(1, max_weight + 1):
            if weight[i - 1] > j:
                bag[i][j] = bag[i - 1][j]
            else:
                bag[i][j] = max(bag[i - 1][j],
                                      value[i - 1] + bag[i - 1][j - weight[i - 1]])
    print(bag[-1][-1])


n, k = list(map(int, input().split()))
weight = [0] * n
value = [0] * n

for i in range(n):
    weight[i], value[i] = list(map(int, input().split()))

Knapsack(n, k, weight, value)
