def isVPS(data):
    stack = []

    for i in range(len(data)):
        if data[i] == "(":
            stack.append(data[i])
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False


T = int(input())
string = []

for _ in range(T):
    string = input()

    if isVPS(string):
        print("YES")
    else:
        print("NO")
