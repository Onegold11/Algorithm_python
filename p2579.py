def Layer_score(data):
    layer = []

    for i in range(len(data)):
        if i == 0:
            # first
            layer.append(data[0])
        elif i == 1:
            # second max : first + second
            layer.append(data[1] + data[0])
        elif i == 2:
            # third max : first + third(jump 2), second + third(jump 1)
            layer.append(data[2] + max(data[1], data[0]))
        else:
            # n max : n-3 + n-1(jump2) / + n(jump1),
            #         n-2 + / n(jump2)
            layer.append(data[i] + max(data[i - 1] + layer[i - 3], layer[i - 2]))
    print(layer[-1])


n = int(input())
layer = []

for _ in range(n):
    layer.append(int(input()))

Layer_score(layer)
