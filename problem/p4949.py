
def isBalanced(data):
    stack = []

    for i in range(len(data)):
        if data[i] == "(" or data[i] == "[":
            stack.append(data[i])

        if data[i] == ")" or data[i] == "]":
            if len(stack) == 0:
                return False
            else:
                temp = stack.pop()
                if data[i] == ")" and temp != "(":
                    return False
                if data[i] == "]" and temp != "[":
                    return False

    if len(stack) == 0:
        return True
    else:
        return False


while True:
    string = input()

    if len(string) == 1 and string[0] == '.':
        break
    else:
        if isBalanced(string):
            print("yes")
        else:
            print("no")
