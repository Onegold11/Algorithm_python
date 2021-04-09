from typing import List


def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    # 해결 가능
    if sum(gas) < sum(cost):
        return -1

    start, fuel = 0, 0
    for i in range(len(gas)):
        # 출발점 안됨, 초기화
        if gas[i] + fuel < cost[i]:
            start = i + 1
            fuel = 0
        else:
            fuel += gas[i] - cost[i]
    return start