from collections import deque
import sys


class Deque:
    def __init__(self):
        self.queue = deque()

    def push_front(self, x):
        self.queue.appendleft(x)

    def push_back(self, x):
        self.queue.append(x)

    def pop_front(self):
        if len(self.queue) == 0:
            return -1
        else:
            return self.queue.popleft()

    def pop_back(self):
        if len(self.queue) == 0:
            return -1
        else:
            return self.queue.pop()

    def size(self):
        return len(self.queue)

    def empty(self):
        if len(self.queue) == 0:
            return 1
        else:
            return 0

    def front(self):
        if len(self.queue) == 0:
            return -1
        else:
            num = self.queue.popleft()
            self.queue.appendleft(num)
            return num

    def back(self):
        if len(self.queue) == 0:
            return -1
        else:
            num = self.queue.pop()
            self.queue.append(num)
            return num


N = int(input())
dque = Deque()

for _ in range(N):
    order_list = sys.stdin.readline().split()
    order = order_list[0]

    if order == 'push_front':
        dque.push_front(order_list[1])
    elif order == 'push_back':
        dque.push_back(order_list[1])
    elif order == 'pop_front':
        print(dque.pop_front())
    elif order == 'pop_back':
        print(dque.pop_back())
    elif order == 'size':
        print(dque.size())
    elif order == 'empty':
        print(dque.empty())
    elif order == 'front':
        print(dque.front())
    elif order == 'back':
        print(dque.back())
    else:
        continue
