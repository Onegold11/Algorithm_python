def MostWineAmount(data):
    amount = []

    for i in range(len(data)):
        if i == 0:
            amount.append(data[i])
        elif i == 1:
            amount.append(data[1] + data[0])
        elif i == 2:
            amount.append(data[2] + max(data[1], data[0]))
            amount[i] = max(amount[2], amount[1])
        else:
            amount.append(data[i] + max(data[i - 1] + amount[i - 3],
                                        amount[i - 2]))
            amount[i] = max(amount[i], max(amount[:i]))
    print(max(amount))


n = int(input())
wine_amount = []

for _ in range(n):
    wine_amount.append(int(input()))
MostWineAmount(wine_amount)
