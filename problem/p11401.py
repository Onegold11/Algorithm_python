def binomial(n, k):
    if n == k or k == 0:
        return 1
    else:
        return (binomial(n - 1, k) + binomial(n - 1, k - 1)) % 1000000007


N, K = map(int, input().split())
print(binomial(N, K))
