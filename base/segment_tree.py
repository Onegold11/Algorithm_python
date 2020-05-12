def init(node, start, end):
    global tree
    global a

    if start == end:
        tree[node] = a[start]
    else:
        tree[node] = init(node * 2, start, (start + end) // 2) + \
                     init(node * 2 + 1, (start + end) // 2 + 1, end)
        return tree[node]