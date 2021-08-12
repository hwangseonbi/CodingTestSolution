'''
https://programmers.co.kr/learn/courses/30/lessons/81302
'''
from collections import deque


def BFS(place, start_point):
    visited = []
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    q = deque()
    q.append(start_point)

    while q:
        i, j = q.popleft()
        visited.append((i, j))
        for d in range(4):
            new_i = i + di[d]
            new_j = j + dj[d]
            manhattan_distance = abs(start_point[0] - new_i) + abs(start_point[1] - new_j)

            if (new_i, new_j) not in visited:
                if 0 <= new_i < 5 and 0 <= new_j < 5 and place[new_i][new_j] != 'X' and manhattan_distance <= 2:
                    q.append((new_i, new_j))
    visited.pop(0)
    return list(map(lambda x: place[x[0]][x[1]], visited))

def is_legal(place, p_list):
    for p in p_list:
        visited = BFS(place, p)
        if "P" in visited:
            return 0
    return 1
def solution(places):
    answers = []
    for place in places:
        p_list = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    p_list.append((i, j))

        answers.append(is_legal(place, p_list))
    return answers

assert solution([
    ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
    ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
]) == [1, 0, 1, 1, 1]
