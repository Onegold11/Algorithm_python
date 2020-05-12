def get_fibo(n):
    if n == 0:
        return [[1, 0], [0, 1]]
    elif n == 1:
        return F
    elif n % 2 == 0:
        result = [[0 for _ in range(2)] for _ in range(2)]
        t1 = get_fibo(n // 2)
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    result[i][j] += t1[i][k] * t1[k][j]
                result[i][j] %= 1000000
        return result
    else:
        result = [[0 for _ in range(2)] for _ in range(2)]
        t1 = get_fibo(n - 1)
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    result[i][j] += t1[i][k] * F[k][j]
                result[i][j] %= 1000000
        return result


n = int(input())
F = [[0, 1], [1, 1]]
print(get_fibo(n)[1][0])
