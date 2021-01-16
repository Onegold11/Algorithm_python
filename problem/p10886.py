N = int(input())

result = 0
for _ in range(N):
    if input() == "1":
        result += 1

if result * 2 < N:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")