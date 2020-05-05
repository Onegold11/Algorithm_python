import sys

n = int(sys.stdin.readline())

num = [0] * n
for i in range(n):
    num[i] = int(sys.stdin.readline())

num.sort()


def mean(num):
    return round(sum(num) / len(num))


def center(num):
    return num[int(len(num) / 2)]


def freq(num):
    if len(num) == 1:
        return num[0]

    map = {}
    for i in num:
        if not map.get(i):
            map[i] = 1
        else:
            map[i] += 1
    print(map)
    value = 0
    freq_key = 0
    is_not_second = True
    for key in map:
        if map[key] > value:
            value = map[key]
            freq_key = key
    for key in map:
        if is_not_second and map[key] == value and key > freq_key:
            freq_key = key
            is_not_second = False
    return freq_key


def diff(num):
    return num[-1] - num[0]


print(mean(num))
print(center(num))
print(freq(num))
print(diff(num))
