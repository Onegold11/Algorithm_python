from typing import List
import collections
import heapq


def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
    graph = collections.defaultdict(list)

    # u: 시작, v: 도착, w: 가격
    for u, v, w in flights:
        graph[u].append((v, w))

    # [(가격, 정점, 남은 경유지 수)]
    Q = [(0, src, K)]

    while Q:
        price, node, k = heapq.heappop(Q)
        if node == dst:
            return price
        if k >= 0:
            for v, w in graph[node]:
                alt = price + w
                heapq.heappush(Q, (alt, v, k - 1))
    return -1


if __name__ == '__main__':
    edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    print(findCheapestPrice(3, edges, 0, 2, 0))
