T = int(input())

for _ in range(T):
    stack = input().split()
    result = 0

    for top in stack:
        if top == '@':
            result *= 3
        elif top == '%':
            result += 5
        elif top == '#':
            result -= 7
        else:
            result += float(top)
    print('%.2f' % result)