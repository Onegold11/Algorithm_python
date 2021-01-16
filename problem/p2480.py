dice = sorted(list(map(int, input().split())), reverse=True)
set_dice = set(dice)
count, same = 0, 0

# check same
for num in set_dice:
    temp = dice.count(num)

    if temp > count and temp > 1:
        count = temp
        same = num

# calc result
if count == 3:
    print(10000 + dice[0] * 1000)
elif count == 2:
    print(1000 + same * 100)
else:
    print(dice[0] * 100)
