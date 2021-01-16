points_x = []
points_y = []

for _ in range(3):
    x, y = map(int, input().split())

    # search x
    if x in points_x:
        points_x.remove(x)
    else:
        points_x.append(x)

    # search y
    if y in points_y:
        points_y.remove(y)
    else:
        points_y.append(y)

print(points_x[0], points_y[0])


