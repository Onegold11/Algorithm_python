def IncreaseNum(data):
    max_len = [1] * len(data)

    for i in range(len(data)):
        for j in range(i):
            if data[j] < data[i]:
                if max_len[i] <= max_len[j]:
                    max_len[i] = max_len[j] + 1
    print(max(max_len))


n = int(input())
num = list(map(int, input().split()))
IncreaseNum(num)
