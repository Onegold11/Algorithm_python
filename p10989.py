import sys

n = int(sys.stdin.readline())

# input list
numbers = [0] * 10000
for i in range(n):
    num = int(sys.stdin.readline())
    numbers[num-1] += 1

# print
for i in range(len(numbers)):
    if numbers[i] == 0:
        continue
    for j in range(numbers[i]):
        print(i+1)