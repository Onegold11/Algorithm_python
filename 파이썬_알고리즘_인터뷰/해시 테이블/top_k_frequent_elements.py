import collections
import heapq
from typing import List


def topKFrequent1(nums: List[int], k: int) -> List[int]:
    freqs = collections.Counter(nums)
    freqs_heap = []

    for f in freqs:
        heapq.heappush(freqs_heap, (-freqs[f], f))

    topk = list()
    for _ in range(k):
        topk.append(heapq.heappop(freqs_heap)[1])
    return topk


def topKFrequent2(nums: List[int], k: int):
    return list(zip(*collections.Counter(nums).most_common(k)))[0]


if __name__ == '__main__':
    nums, k = [1, 1, 1, 2, 2, 3], 2

    print(topKFrequent1(nums, k))
    print(topKFrequent2(nums, k))
