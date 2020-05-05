def Fibonacci(n):
    f = [0] * (n + 1)

    for i in range(0, len(f)):
        if i <= 1:
            f[i] = i
        else:
            f[i] = f[i-1] + f[i-2]
    print(f[n])


n = int(input())
Fibonacci(n)
