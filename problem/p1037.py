def GetN(data):
    list = sorted(data)
    print(list[0] * list[-1])


count = int(input())
factor = list(map(int, input().split()))
GetN(factor)
