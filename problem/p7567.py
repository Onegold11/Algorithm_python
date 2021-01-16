bowl = list(input())

front = bowl[0]
height = 10

for i in range(1, len(bowl)):
    if front == bowl[i]:
        height += 5
    else:
        height += 10

    front = bowl[i]

print(height)