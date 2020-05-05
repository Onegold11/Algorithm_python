def backtracking(i, n, m, answer):
    #print("{} {}".format(i, answer))
    if promising(i, answer):
        #print("promising")
        if i == m:
            print_answer(answer)
        else:
            for j in range(1, n + 1):
                answer[i] = j
                backtracking(i + 1, n, m, answer)
            answer[i] = 0


def promising(i, answer):
    if i <= len(answer):
        return True
    else:
        return False


def print_answer(answer):
    for a in answer:
        print(a, end=" ")
    print()


n, m = map(int, input().split())
answer = [0] * m
backtracking(0, n, m, answer)
