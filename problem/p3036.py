def GreatestCommonDivisor(num1, num2):
    while num2 != 0:
        temp = num1 % num2
        num1 = num2
        num2 = temp
    return num1


def GetTurn(ring):
    for i in range(1, len(ring)):
        
        if ring[0] % ring[i] == 0:
            print("{}/1".format(int(ring[0] / ring[i])))
        else:
            gcd = GreatestCommonDivisor(ring[0], ring[i])
            print("{}/{}".format(int(ring[0] / gcd), int(ring[i] / gcd)))


N = int(input())
ring = list(map(int, input().split()))
GetTurn(ring)
