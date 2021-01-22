T = int(input())
for _ in range(T):
    N = int(input())

    rs, rl = 0, 0
    for _ in range(N):
        S, L = input().split()

        if int(L) > rl:
            rs = S
            rl = int(L)
    print(rs)
