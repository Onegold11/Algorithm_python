import sys
import math


# a = M * (a/M) + n
# b = M * (b/M) + n
# a - M * (a/M) = b - M * (b/M)
# a - b = ((b/M) - (a/M)) * M

def GetMs(data):
    num = sorted(data, reverse=True)
    diff = []
    divisor = []

    for i in range(len(num) - 1):
        diff.append(num[i] - num[i + 1])

    if len(diff) != 1:
        for _ in range(len(diff) - 1):
            num1 = diff.pop()
            num2 = diff.pop()
            diff.append(math.gcd(num1, num2))

    max = diff.pop()
    for i in range(2, int(math.sqrt(max)) + 1):
        if max % i == 0:
            if i * i == max:
                divisor.append(i)
            else:
                divisor.append(i)
                divisor.append(int(max / i))
    divisor.append(max)

    divisor = sorted(divisor)
    print(*divisor, sep=" ")


N = int(input())
num = []
for _ in range(N):
    num.append(int(sys.stdin.readline()))
GetMs(num)
