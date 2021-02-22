from typing import List
import itertools


def permute1(nums: List[int]) -> List[List[int]]:
    results = []
    prev_elements = []

    def dfs(elements):
        # leaf
        if len(elements) == 0:
            results.append(prev_elements[:])

        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)

            prev_elements.append(e)
            dfs(next_elements)
            prev_elements.pop()

    dfs(nums)
    return results


def permute2(nums: List[int]) -> List[List[int]]:
    return list(map(list, itertools.permutations(nums)))


if __name__ == '__main__':
    nums = [1, 2, 3]
    print(permute1(nums))
    print(permute2(nums))
