def Stack(data):
    stack = []
    for i in range(len(data)):
        if data[i][0] == 'push':
            stack.append(data[i][1])
        elif data[i][0] == 'pop':
            if len(stack) != 0:
                num = stack.pop()
                print(num)
            else:
                print(-1)
        elif data[i][0] == 'size':
            print(len(stack))
        elif data[i][0] == 'empty':
            if len(stack) != 0:
                print(0)
            else:
                print(1)
        elif data[i][0] == 'top':
            if len(stack) != 0:
                print(stack[-1])
            else:
                print(-1)
        else:
            continue


N = int(input())
command = []
for _ in range(N):
    command.append(input().split())
Stack(command)
