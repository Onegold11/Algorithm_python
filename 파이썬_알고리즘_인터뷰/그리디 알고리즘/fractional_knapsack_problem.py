

def fractional_knapsack(cargo: list):
    capacity = 15
    pack = []
    for c in cargo:
        pack.append((c[0] / c[1], c[0], c[1]))
    pack.sort(reverse=True)

    # 그리디 계산
    total_value: float = 0
    for p in pack:
        if capacity - p[2] >= 0:
            capacity -= p[2]
            total_value += p[1]
        else:
            fraction = capacity / p[2]
            total_value += p[1] * fraction
            break
    return total_value


if __name__ == '__main__':
    cargo = [
        (4, 12),
        (2, 1),
        (10, 4),
        (1, 1),
        (2, 2)
    ]
    r = fractional_knapsack(cargo)
    print(r)