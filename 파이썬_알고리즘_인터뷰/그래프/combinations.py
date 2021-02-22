from typing import List
import itertools

def combine1(n: int, k: int) -> List[List[int]]:
    results = []

    def dfs(elements, start: int, k: int):
        if k == 0:
            results.append(elements[:])

        for i in range(start, n + 1):
            elements.append(i)
            dfs(elements, i + 1, k - 1)
            elements.pop()

    dfs([], 1, k)
    return results


def combine2(n: int, k: int) -> List[List[int]]:
    return list(itertools.combinations(range(1, n + 1), k))


if __name__ == '__main__':
    print(combine1(4, 2))
    print(combine1(5, 3))

    print(combine2(4, 2))
    print(combine2(5, 3))