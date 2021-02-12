from typing import List


def arrayPairSum1(nums: List[int]) -> int:
    sum = 0
    pair = []
    nums.sort()

    for n in nums:
        pair.append(n)

        if len(pair) == 2:
            sum += min(pair)
            pair = []
    return sum


def arrayPairSum2(nums: List[int]) -> int:
    sum = 0
    pair = []
    nums.sort()

    for i, n in enumerate(nums):
        if i % 2 == 0:
            sum += n
    return sum


def arrayPairSum3(nums: List[int]) -> int:
    return sum(sorted(nums)[::2])


if __name__ == '__main__':
    nums = [1, 4, 3, 2]
    print(arrayPairSum1(nums))
    print(arrayPairSum2(nums))
    print(arrayPairSum3(nums))
