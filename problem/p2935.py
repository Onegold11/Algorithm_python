A = input()
oper = input()
B = input()

if oper == '*':
    print('1' + '0' * (len(A) + len(B) - 2))
else:
    print(int(A) + int(B))