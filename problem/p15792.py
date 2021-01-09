A, B = map(int, input().split())

under_nums = [(str(A // B) + ".")]

for _ in range(1000):
    A = (A % B) * 10

    if A == 0:
        break
    under_nums.append(str(A // B))

print(''.join(under_nums))
