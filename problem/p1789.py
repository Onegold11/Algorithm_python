S = int(input())
N = 0
sum = 0

while True:
    N += 1
    sum += N

    if sum > S:
        break
print(N-1)