def Stair(num):
    score = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    for _ in range(1, num):
        temp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(10):
            if i == 0:
                # X0~: X = 1
                temp[i] = score[1]
            elif i == 9:
                # X9~: X = 8
                temp[i] = score[8]
            else:
                # Xn~: X = n-1, X = n+1
                temp[i] = score[i - 1] + score[i + 1]
        score = temp
    print(sum(score) % 1000000000)


n = int(input())
Stair(n)
