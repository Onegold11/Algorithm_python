def Max_sum(data):
    sum = [0] * len(data)

    for i in range(len(data)):
        sum[i] = data[i] + max(sum[i-1], 0)
    print(max(sum))

n = int(input())
list = list(map(int, input().split()))

Max_sum(list)
