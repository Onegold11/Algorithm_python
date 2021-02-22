import collections
from typing import List


def findItinerary1(tickets: List[List[str]]) -> List[str]:
    graph = collections.defaultdict(list)

    for a, b in sorted(tickets):
        graph[a].append(b)

    route = []
    def dfs(a):
        while graph[a]:
            dfs(graph[a].pop(0))
        route.append(a)

    dfs('JFK')
    return route[::-1]


def findItinerary2(tickets: List[List[str]]) -> List[str]:
    graph = collections.defaultdict(list)

    for a, b in sorted(tickets, reverse=True):
        graph[a].append(b)

    route = []
    def dfs(a):
        while graph[a]:
            dfs(graph[a].pop())
        route.append(a)

    dfs('JFK')
    return route[::-1]


def findItinerary3(tickets: List[List[str]]) -> List[str]:
    graph = collections.defaultdict(list)

    for a, b in sorted(tickets):
        graph[a].append(b)

    route, stack = [], ['JFK']
    while stack:
        while graph[stack[-1]]:
            stack.append(graph[stack[-1]].pop(0))
        route.append(stack.pop())

    return route[::-1]


if __name__ == '__main__':
    tickets = [['MUC', 'LHR'], ['JFK', 'MUC'], ['SFO', 'SJC'], ['LHR', 'SFO']]
    print(findItinerary1(tickets))
    print(findItinerary2(tickets))
    print(findItinerary3(tickets))
