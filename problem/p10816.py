def get_card_count(target: int):
    global N
    global card_num

    first, last = 0, N - 1
    count = 0

    while first <= last:
        center = (first + last) // 2
        print(card_num)
        if card_num[center] == target:
            count += 1
            last -= 1
            card_num.remove(target)
        if card_num[center] >= target:
            last -= 1
        else:
            first += 1
    return count


N = int(input())
card_num = list(map(int, input().split()))
M = int(input())
target_num = list(map(int, input().split()))

card_num.sort()

for i in range(M):
    print(get_card_count(target_num[i]))
    print('---')
