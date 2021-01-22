T = int(input())
A, B, C = 0, 0, 0

A = T // 300
T = T % 300

B = T // 60
T = T % 60

C = T // 10
T = T % 10

if T == 0:
    print("{} {} {}".format(A, B, C))
else:
    print("-1")
