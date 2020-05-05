def Tile(n):
    # ex) t[3] = (00 + □) + (1 + □□)
    t = [0] * (n+1)

    for i in range(1, n+1):
        if i <= 2:
            t[i] = i
        else:
            t[i] = (t[i-1] + t[i-2]) % 15746
    print(t[n])


n = int(input())
Tile(n)