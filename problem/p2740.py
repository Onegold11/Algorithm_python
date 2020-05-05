def mul_matrix(a: list, b: list, N, M, K):
    for i in range(N):
        for j in range(K):
            t = 0
            for k in range(M):
                t += a[i][k] * b[k][j]
            print(t, end=' ')
        print()


N, M = map(int, input().split())
A = [[i for i in map(int, input().split())] for j in range(N)]
M, K = map(int, input().split())
B = [[i for i in map(int, input().split())] for j in range(M)]
mul_matrix(A, B, N, M, K)
