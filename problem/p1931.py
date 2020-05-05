from operator import itemgetter

def GreedyCase(data):
    time_schedule = sorted(data, key=itemgetter(1, 0))
    last_end_time, count = 0, 0

    for i in range(len(data)):
        start_time = time_schedule[i][0]
        end_time = time_schedule[i][1]

        if start_time < last_end_time:
            continue
        else:
            count += 1
            last_end_time = end_time

        if last_end_time == time_schedule[-1][1]:
            break

    print(count)


N = int(input())
room_time = []

for _ in range(N):
    room_time.append(list(map(int, input().split())))

GreedyCase(room_time)
