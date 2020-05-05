def getNumCount(n, k):
    num = n
    count = 0

    while num > 1:
        num = num // k
        count += num
    print(count)
    return count


def getZeroCount(n, m):
    return min(getNumCount(n, 5) - (getNumCount(m, 5) + getNumCount(n - m, 5)),
               getNumCount(n, 2) - (getNumCount(m, 2) + getNumCount(n - m, 2)))


n, m = map(int, input().split())
print(getZeroCount(n, m))
