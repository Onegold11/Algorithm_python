K = int(input())
cog = []

for _ in range(K):
    write = int(input())

    if write == 0:
        cog.pop()
    else:
        cog.append(write)

print(sum(cog))