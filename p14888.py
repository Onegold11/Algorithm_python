

def backtracking(i=0):
    global n
    global operator
    global operator_list
    global min_result
    global max_result

    if i == n - 1:
        answer = calc()

        if answer < min_result:
            min_result = answer
        if answer > max_result:
            max_result = answer
    else:
        for op in range(4):
            operator_list[i] = op
            operator[op] = operator[op] - 1

            if promising(op):
                backtracking(i + 1)

            operator[op] = operator[op] + 1
            operator_list[i] = -1


def promising(i):
    global operator

    if operator[i] < 0:
        return False

    return True


def calc():
    global operator_list
    global num

    result = num[0]
    for i in range(len(num)-1):
        if operator_list[i] == 0:
            result = result + num[i+1]
        elif operator_list[i] == 1:
            result = result - num[i+1]
        elif operator_list[i] == 2:
            result = result * num[i+1]
        else:
            result = int(result / num[i+1])
    return result


n = int(input())
num = list(map(int, input().split()))
operator = list(map(int, input().split()))
operator_list = [-1] * (n-1)
min_result = 1000000000
max_result = -1000000000

backtracking()
print(max_result)
print(min_result)
