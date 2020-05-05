def GreatestCommonDivisor(num1, num2):
    while num2 != 0:
        temp = num1 % num2
        num1 = num2
        num2 = temp
    return num1


def LeastCommonMultiple(num1, num2, gcd):
    return int(num1 * num2 / gcd)


a, b = map(int, input().split())
gcd = GreatestCommonDivisor(a, b)
lcm = LeastCommonMultiple(a, b, gcd)
print("{}\n{}".format(gcd, lcm))
