while True:
    n = int(input())
    if n == -1:
        break

    num = [1]
    x = int(n ** 0.5)
    for i in range(2, x + 1):
        if n % i == 0:
            num.extend([i, n // i])

    if sum(num) != n:
        print("%s is NOT perfect." % n)
    else:
        num.sort()
        print("{} = {}".format(n, " + ".join(map(str, num))))