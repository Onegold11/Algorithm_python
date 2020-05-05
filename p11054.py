def Bitonic(data):
    left = [1] * len(data)
    right = [1] * len(data)
    max_len = []

    for i in range(len(data)):
        for j in range(i):
            if data[j] < data[i]:
                if left[i] <= left[j]:
                    left[i] = left[j] + 1
    for i in range(len(data) - 1, 0, -1):
        for j in range(len(data) - 1, i, -1):
            if data[j] < data[i]:
                if right[i] <= right[j]:
                    right[i] = right[j] + 1

    for i in range(len(data)):
        max_len.append(left[i] + right[i] - 1)

    print(max(max_len))


n = int(input())
num = list(map(int, input().split()))
Bitonic(num)
