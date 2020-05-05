import sys


def getMaxCase(items):
    type_count = {}

    # sorting type
    for _ in range(len(items)):
        c_type = items.popitem()[1]

        if c_type in type_count:
            type_count[c_type] = type_count[c_type] + 1
        else:
            type_count[c_type] = 1

    # get case count
    if len(type_count) == 1:
        print(type_count.popitem()[1])
    else:
        case = 1
        for _ in range(len(type_count)):
            case = case * (type_count.popitem()[1] + 1)
        print(case - 1)


testcase = int(input())
for _ in range(testcase):
    items = {}

    n = int(input())
    for _ in range(n):
        item, c_type = sys.stdin.readline().split()
        items[item] = c_type
    getMaxCase(items)
