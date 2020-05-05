def pow_split(a, b, c):
    if b == 0:
        return 1
    elif b == 1:
        return a % c
    elif b % 2 == 0:
        t = pow_split(a, b // 2, c) % c
        return (t ** 2) % c
    else:
        return a * pow_split(a, b - 1, c) % c


A, B, C = map(int, input().split())
print(pow_split(A, B, C))
