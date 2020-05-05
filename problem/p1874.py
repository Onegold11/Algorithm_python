import sys


def get_stack_oper_asc(data):
    stack = []
    print_buf = ''
    num_asc = 1

    for target in data:
        while num_asc <= target:
            stack.append(num_asc)
            print_buf += "+\n"
            num_asc += 1

        top = stack.pop()
        if top == target:
            print_buf += "-\n"
        else:
            print("NO")
            return

    print(print_buf)


n = int(sys.stdin.readline())
num = [int(sys.stdin.readline()) for _ in range(n)]
get_stack_oper_asc(num)
