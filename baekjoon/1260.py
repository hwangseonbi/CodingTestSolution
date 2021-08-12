import sys

#표준 입력
N, M, V = map(int, sys.stdin.readline().split())
GRAPH = []
for _ in range(M):
    GRAPH.append(tuple(map(int, sys.stdin.readline().split())))


def dictionarify(graph):
    result = {i: [] for i in range(1, N + 1)}
    for s, e in graph:
        result[s].append(e)
        result[e].append(s)

    return result


def bfs(graph, start_point):
    queue = [start_point]
    visited = []
    while queue:
        current_point = queue.pop(0)
        if current_point in visited:
            continue
        visited.append(current_point)

        # 다음 지점들이 여러개일 때 숫자가 작은 지점부터 큐에 넣어야한다.
        # 왜냐하면 While 루프에서 큐의 가장 앞쪽에 존재하는 숫자가 꺼내지기 때문이다.
        # 앞쪽의 숫자가 가장 적은 지점이어야한다.
        for next_point in sorted(graph[current_point]):
            if next_point in visited:
                continue
            queue.append(next_point)

    return visited


def dfs(graph, start_point):
    stack = [start_point]
    visited = []
    while stack:
        current_point = stack.pop()
        if current_point in visited:
            continue
        visited.append(current_point)

        # 다음 지점들이 여러개일 때 숫자가 큰 지점부터 스택에 넣어야한다.
        # 왜냐하면 While 루프에서 스택의 가장 마지막 쪽에 존재하는 숫자가 꺼내지기 때문이다.
        # 마지먹 쪽의 숫자가 가장 적은 지점이어야한다.
        for next_point in sorted(graph[current_point], reverse=True):
            if next_point in visited:
                continue
            stack.append(next_point)

    return visited


def solution():
    #Dictionary 형태의 그래프를 만들어준다.
    graph = dictionarify(GRAPH)


    dfs_route = dfs(graph, start_point=V)
    bfs_route = bfs(graph, start_point=V)
    return dfs_route, bfs_route


result_dfs, result_bfs = solution()
result = " ".join(map(str, result_dfs)) + "\n" + " ".join(map(str, result_bfs))
print(result)
