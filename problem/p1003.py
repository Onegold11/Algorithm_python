def Fibonacci(n):
    f_0 = [0] * (n + 1)
    f_1 = [0] * (n + 1)

    for i in range(0, n+1):
        if i == 0:
            f_0[i] = 1
            f_1[i] = 0
        elif i == 1:
            f_0[i] = 0
            f_1[i] = 1
        else:
            f_0[i] = f_0[i-1] + f_0[i-2]
            f_1[i] = f_1[i-1] + f_1[i-2]
    print("{} {}".format(f_0[n], f_1[n]))


n = int(input())
for _ in range(n):
    k = int(input())
    Fibonacci(k)
