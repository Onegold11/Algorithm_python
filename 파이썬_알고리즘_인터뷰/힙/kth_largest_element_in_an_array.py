import heapq
from typing import List


def findKthLargest1(nums: List[int], k: int) -> int:
    heap = list()
    for n in nums:
        heapq.heappush(heap, -n)

    for _ in range(k):
        heapq.heappop(heap)

    return -heapq.heappop(heap)


def findKthLargest2(nums: List[int], k: int) -> int:
    heapq.heapify(nums)

    for _ in range(len(nums) - k):
        heapq.heappop(nums)

    return heapq.heappop(nums)


def findKthLargest3(nums: List[int], k: int) -> int:
    return heapq.nlargest(k, nums)[-1]


def findKthLargest4(nums: List[int], k: int) -> int:
    return sorted(nums, reverse=True)[k - 1]