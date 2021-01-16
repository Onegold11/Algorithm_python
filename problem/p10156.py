K, N, M = map(int, input().split())

result = K * N

if M >= result:
    print("0")
else:
    print(result - M)