def binary_search(N: int, A: list, M: int, X: list):
    A.sort()

    for i in range(M):
        first, last = 0, N - 1
        exist = False
        while first <= last:
            center = (first + last) // 2
            if A[center] == X[i]:
                exist = True
                break
            if A[center] > X[i]:
                last = center - 1
            else:
                first = center + 1
        if exist:
            print(1)
        else:
            print(0)


N = int(input())
A = [a for a in map(int, input().split())]
M = int(input())
X = [x for x in map(int, input().split())]
binary_search(N, A, M, X)
