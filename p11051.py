def BinomialCoefficient(N, K):
    pascal_tri = [1 for _ in range(N + 2)]

    for i in range(2, N + 1):
        temp = pascal_tri.copy()
        for j in range(1, i):
            pascal_tri[j] = temp[j - 1] + temp[j]

    print(pascal_tri[K] % 10007)


N, K = map(int, input().split())
BinomialCoefficient(N, K)