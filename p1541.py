import re

expr = input()
num = list(map(int, re.split('\D', expr)))
oper = re.findall('\D', expr)

sum = num[0]
find_minus = False
for i in range(len(oper)):
    if find_minus:
        sum -= num[i + 1]
    else:
        if oper[i] == '+':
            sum += num[i + 1]
        else:
            sum -= num[i + 1]
            find_minus = True
print(sum)
