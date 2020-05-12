def init(node, start, end):
    global segment_tree
    global test_case

    print(node, start, end)
    if start == end:
        segment_tree[node] = start
    else:
        init(node * 2, start, (start + end) // 2)
        init(node * 2 + 1, (start + end) // 2 + 1, end)
        if test_case[segment_tree[node * 2]] <= test_case[segment_tree[node * 2 + 1]]:
            segment_tree[node] = segment_tree[node * 2]
        else:
            segment_tree[node] = segment_tree[node * 2 + 1]


def get_big_rect(n, s):
    global test_case

    if n == 1:
        return test_case[s]
    elif n % 2 == 0:
        temp1 = get_big_rect(n // 2, s)
        temp2 = get_big_rect(n // 2, s + n // 2)
    else:
        temp1 = get_big_rect(n - 1, s)
        temp2 = get_big_rect(1, s + n - 1)


while True:
    temp = list(map(int, input().split()))

    if temp[0] == 0:
        break
    n = temp[0]
    test_case = temp
    segment_tree = [0 for _ in range(2 * n - 1)]
    init(1, 0, n - 1)
    print(segment_tree)
