def Spiral(n):
    p = [0] * (n+1)

    for i in range(1, n+1):
        if i <= 3:
            p[i] = 1
        else:
            p[i] = p[i-2] + p[i-3]
    print(p[n])


n = int(input())
for _ in range(n):
    t = int(input())
    Spiral(t)