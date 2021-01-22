T = int(input())

for _ in range(T):
    Y, K = 0, 0
    for _ in range(9):
        y, k = map(int, input().split())
        Y += y
        K += k
    if Y == K:
        print("Draw")
    elif Y > K:
        print("Yonsei")
    else:
        print("Korea")