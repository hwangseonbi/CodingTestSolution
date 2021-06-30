import sys
from heapq import heappush, heappop

INF = float('inf')
V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
GRAPH = [[] for _ in range(V + 1)]
SHORTEST_DISTANCES = [INF] * (V + 1)

heap = []


def dijkstra(start):
    SHORTEST_DISTANCES[start] = 0
    heappush(heap, (SHORTEST_DISTANCES[start], start))
    while heap:
        current_distance, current_node = heappop(heap)
        for adj_node, d in GRAPH[current_node]:
            new_distance = current_distance + d
            if new_distance < SHORTEST_DISTANCES[adj_node]:
                SHORTEST_DISTANCES[adj_node] = new_distance
                heappush(heap, (new_distance, adj_node))


for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    GRAPH[u].append((v, w))

dijkstra(K)
for d in SHORTEST_DISTANCES[1:]:
    print(d if d != INF else "INF")
