def getZeroIndex(n):
    count = 0
    num = n

    while num > 9:
        remainder = num % 10
        if remainder != 0:
            break
        else:
            count += 1
            num = num // 10
    print(count)


def factorial(n):
    fac = 1

    for i in range(2, n + 1):
        fac = fac * i
    return fac


n = int(input())
getZeroIndex(factorial(n))
