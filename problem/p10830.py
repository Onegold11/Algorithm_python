def get_power_matrix(b):
    global A
    global N

    if b == 1:
        for i in range(N):
            for j in range(N):
                A[i][j] %= 1000
        return A
    elif b % 2 == 0:
        result = [[0 for _ in range(N)] for _ in range(N)]
        t1 = get_power_matrix(b // 2)
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    result[i][j] += t1[i][k] * t1[k][j]
                result[i][j] %= 1000
        return result
    else:
        result = [[0 for _ in range(N)] for _ in range(N)]
        t1 = get_power_matrix(b - 1)
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    result[i][j] += t1[i][k] * A[k][j]
                result[i][j] %= 1000
        return result


def print_matrix(t: list, n):
    for i in range(n):
        for j in range(n):
            print(t[i][j], end=' ')
        print()


N, B = map(int, input().split())
A = [[int(a) for a in input().split()] for _ in range(N)]
print_matrix(get_power_matrix(B), N)
