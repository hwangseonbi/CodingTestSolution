"""
미로찾기
https://programmers.co.kr/learn/courses/30/lessons/81304
"""

START = "START"
DESTINATION = "DESTINATION"
COST = "COST"


def get_min_node(current_node, graph,cost, visited):
    min_node = None
    min_distance = float('inf')
    for node in graph[current_node]:
        if visited[node]:
            continue
        if min_distance > cost[(current_node, node)]:
            min_distance = cost[(current_node, node)]
            min_node = node

    if min_node == None:
        for node, is_visited in visited.items():
            if not is_visited:
                min_node = node
    return min_node


def solution(n, start, end, roads, traps):
    answer = 0
    graph = {}
    cost = {}
    distances = {}
    visited = {}
    for i in range(1, n+1):
        distances[i] = float("inf")
        visited[i] = False
        graph[i] = []

    for s, e, c in roads:
        graph[s].append(e)

        if (s, e) not in cost:
            cost[(s, e)] = None
            cost[(e, s)] = None
        cost[(s, e)] = c
        cost[(e, s)] = c


    print(graph)
    print(cost)
    for e in graph[start]:
        distances[e] = cost[(start, e)]
    visited[start] = True

    current_node = start
    while False in visited.values():
        current_node = get_min_node(current_node, graph,cost, visited)
        for next_node in graph[current_node]:
            new_distance = distances[current_node] + cost[(current_node, next_node)]
            if cost[(current_node, next_node)] > new_distance:
                cost[(current_node, next_node)] = new_distance

        visited[current_node] = True

        if current_node in traps:
            targets = graph[current_node]
            for i, next_node in enumerate(targets):
                graph[current_node].pop(i)
                graph[next_node].append(current_node)
    return answer


# assert solution(
#     n=3,
#     start=1,
#     end=3,
#     roads=[[1, 2, 2], [3, 2, 3]],
#     traps=[2]) == 5
assert solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]) == 4
