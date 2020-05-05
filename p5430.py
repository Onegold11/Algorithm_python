def ac_language(p, n, arr):
    is_reverse = False
    left = 0
    right = 0

    for o in p:
        if o == "R":
            is_reverse = not is_reverse
        elif o == "D":
            if is_reverse:
                right += 1
            else:
                left += 1

    if left + right <= n:
        result = arr[left: n - right]
        if is_reverse:
            result.reverse()

        print('[' + ','.join(result) + ']')
    else:
        print("error")


T = int(input())
for _ in range(T):
    p = input()
    n = int(input())
    if n == 0:
        input()
        arr = []
    else:
        arr = input()[1:-1].split(',')
    ac_language(p, n, arr)
