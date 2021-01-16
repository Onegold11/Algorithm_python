T = int(input())


def GCD(A, B):
    if B == 0:
        return A
    else:
        return GCD(B, A % B) if A >= B else GCD(A, B % A)


for _ in range(T):
    A, B = map(int, input().split())
    print(int(A * B / GCD(A, B)))

