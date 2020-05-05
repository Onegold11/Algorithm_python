def ATM(data):
    wait_time = sorted(data)
    total_time = []

    for i in range(len(wait_time)):
        if i == 0:
            total_time.append(wait_time[i])
        else:
            total_time.append(wait_time[i] + total_time[i - 1])
    print(sum(total_time))


N = int(input())
P = list(map(int, input().split()))
ATM(P)