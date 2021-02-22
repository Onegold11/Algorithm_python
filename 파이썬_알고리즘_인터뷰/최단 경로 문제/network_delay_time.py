from typing import List
import collections
import heapq

def networkDelayTime(times: List[List[int]], N: int, K: int) -> int:
    graph = collections.defaultdict(list)

    # 그래프 구성
    # v: 도착지, w: 소요 시간
    for u, v, w in times:
        graph[u].append((v, w))
    print(graph)

    # 큐: [(소요 시간, 정점)]
    Q = [(0, K)]
    dist = collections.defaultdict(int)

    while Q:
        time, node = heapq.heappop(Q)
        if node not in dist:
            dist[node] = time
            for v, w in graph[node]:
                alt = time + w
                heapq.heappush(Q, (alt, v))
        print(Q)

    print(dist)
    if len(dist) == N:
        return max(dist.values())
    return -1


if __name__ == '__main__':
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    print(networkDelayTime(times, 4, 2))