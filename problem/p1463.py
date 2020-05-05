def MakeOne(num):
    case = [0] * (num + 1)

    for i in range(num + 1):
        if i == 0 or i == 1:
            case[i] = 0
        elif i == 2 or i == 3:
            case[i] = 1
        else:
            if i % 3 == 0:
                case[i] = min(case[i - 1], case[int(i / 3)]) + 1
            elif i % 2 == 0:
                case[i] = min(case[i - 1], case[int(i / 2)]) + 1
            else:
                case[i] = case[i - 1] + 1
    print(case[-1])


n = int(input())
MakeOne(n)
