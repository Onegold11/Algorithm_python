# Number of crossed wires = Total wire - Number of uncrossed wire
# Number of uncrossed = Ascending destination(pre: ascending starting point)


def RemoveWire(n, data):
    max_uncrossed = [1] * n

    for i in range(n):
        for j in range(i):
            if data[i][1] > data[j][1] and max_uncrossed[i] <= max_uncrossed[j]:
                max_uncrossed[i] = max_uncrossed[j] + 1
    print(len(data) - max(max_uncrossed))


n = int(input())
wire_pair = []

for _ in range(n):
    wire_pair.append(list(map(int, input().split())))

wire_pair = sorted(wire_pair, key=lambda wire: wire[0])
RemoveWire(n, wire_pair)
