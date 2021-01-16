N = int(input())

result = 0
for _ in range(N):
    A, B, C = map(int, input().split())

    if A == B and A == C:
        result = max(result, 10000 + A * 1000)
    elif A == B or A == C:
        result = max(result, 1000 + A * 100)
    elif B == C:
        result = max(result, 1000 + B * 100)
    else:
        result = max(result, max(A, B, C) * 100)
print(result)