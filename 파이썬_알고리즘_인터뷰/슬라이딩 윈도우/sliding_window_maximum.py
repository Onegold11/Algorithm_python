from typing import List
import collections


def maxSlidingWindow1(nums: List[int], k: int) -> List[int]:
    if not nums:
        return nums

    r = []
    for i in range(len(nums) - k + 1):
        r.append(max(nums[i:i + k]))
    return r


def maxSlidingWindow2(nums: List[int], k: int) -> List[int]:
    results = []
    window = collections.deque()
    current_max = float('-inf')
    for i, v in enumerate(nums):
        window.append(v)
        if i < k - 1:
            continue

        # push
        if current_max == float('-inf'):
            current_max = max(window)
        elif v > current_max:
            current_max = v

        results.append(current_max)

        # pop
        if current_max == window.popleft():
            current_max = float('-inf')
    return results


if __name__ == '__main__':
    print(maxSlidingWindow1([1, 3, -1, -3, 5, 3, 6, 7], 3))
    print(maxSlidingWindow2([1, 3, -1, -3, 5, 3, 6, 7], 3))