from typing import List


def singleNumber(nums: List[int]) -> int:
    result = 0
    for num in nums:
        result ^= num
    return result


if __name__ == '__main__':
    nums = [4, 1, 2, 1, 2]
    print(singleNumber(nums))