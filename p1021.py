from collections import deque


def revolving_queue(N, M, pos):
    queue = deque()
    count = 0

    for i in range(1, N + 1):
        queue.append(i)

    for target in pos:
        index = queue.index(target)
        left_dis = index
        right_dis = len(queue) - index

        if left_dis <= right_dis:
            for _ in range(left_dis):
                temp = queue.popleft()
                queue.append(temp)
                count += 1
        else:
            for _ in range(right_dis):
                temp = queue.pop()
                queue.appendleft(temp)
                count += 1
        queue.popleft()
    print(count)


N, M = map(int, input().split())
pos = list(map(int, input().split()))
revolving_queue(N, M, pos)
