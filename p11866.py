from collections import deque


def josephus(n, k):
    queue = deque([i for i in range(1, n + 1)])
    count = 1
    result = "<"

    while len(queue) != 0:
        person = queue.popleft()

        if count != k:
            queue.append(person)
        else:
            result += str(person) + ', '
            count = 0
        count += 1

    result = result[:-2]
    result += '>'
    print(result)


N, K = map(int, input().split())

josephus(N, K)
