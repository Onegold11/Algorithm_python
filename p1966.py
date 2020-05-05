from collections import deque
import sys


def printer(n, m, queue):
    count = 1

    while True:
        document = queue.popleft()

        i = 0
        p = True
        while i != len(queue):
            compare = queue.popleft()
            if compare[0] > document[0]:
                p = False
            queue.append(compare)
            i += 1

        if not p:
            queue.append(document)
        elif document[1] == m:
            print(count)
            break
        else:
            count += 1


test_case = int(input())
for _ in range(test_case):
    N, M = map(int, sys.stdin.readline().split())
    priority = list(map(int, sys.stdin.readline().split()))

    priority_queue = deque([priority[i], i] for i in range(N))
    printer(N, M, priority_queue)
