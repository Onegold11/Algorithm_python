import sys

n = int(sys.stdin.readline())

def is_doom_num(_num):
    num = _num
    while(True):
        if num % 1000 == 666:
            return True
        num = int(num / 10)
        if num == 0:
            return False

count = 0
name = 0
i = 0
while(True):
    if is_doom_num(i):
        count += 1
    if count == n:
        name = i
        break;
    i += 1
print(name)