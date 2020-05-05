import sys
from collections import deque


class Queue:
    def __init__(self):
        self.__queue = deque()
        self.__size = 0

    def push(self, num):
        self.__queue.append(num)
        self.__size += 1

    def pop(self):
        if self.__size == 0:
            return -1
        else:
            num = self.__queue.popleft()
            self.__size -= 1
            return num

    def size(self):
        return self.__size

    def empty(self):
        return 1 if self.__size == 0 else 0

    def front(self):
        if self.__size == 0:
            return -1
        else:
            num = self.__queue.popleft()
            self.__queue.appendleft(num)
            return num

    def back(self):
        if self.__size == 0:
            return -1
        else:
            num = self.__queue.pop()
            self.__queue.append(num)
            return num


N = int(input())
queue = Queue()

for _ in range(N):
    order = sys.stdin.readline().split()

    if order[0] == 'push':
        queue.push(int(order[1]))
    elif order[0] == 'pop':
        print(queue.pop())
    elif order[0] == 'size':
        print(queue.size())
    elif order[0] == 'empty':
        print(queue.empty())
    elif order[0] == 'front':
        print(queue.front())
    elif order[0] == 'back':
        print(queue.back())
    else:
        continue
