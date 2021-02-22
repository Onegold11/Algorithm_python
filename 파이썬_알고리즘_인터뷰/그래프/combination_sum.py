from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    results = []

    def dfs(csum, index, path):
        if csum < 0:
            return
        if csum == 0:
            results.append(path)
            return

        for i in range(index, len(candidates)):
            dfs(csum - candidates[i], i, path + [candidates[i]])

    dfs(target, 0, [])
    return results


if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7

    print(combinationSum(candidates, target))
