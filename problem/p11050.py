def BinomialCoefficient(N, K):
    up = 1
    down = 1

    for i in range(N, N - K, -1):
        up = up * i
    for i in range(1, K + 1, 1):
        down = down * i
    print(int(up / down))


N, K = map(int, input().split())
BinomialCoefficient(N, K)
