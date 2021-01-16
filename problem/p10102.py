V = int(input())
ticket = input()

# count ticket
result = 0
for t in ticket:
    if t == 'A':
        result += 1
    else:
        result -= 1

# calc result
if result == 0:
    print("Tie")
elif result > 0:
    print("A")
else:
    print("B")