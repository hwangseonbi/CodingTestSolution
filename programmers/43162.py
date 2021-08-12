"""
https://programmers.co.kr/learn/courses/30/lessons/43162
"""
from collections import deque


def traverse(computers, networks, start_index):
    q = deque()
    q.append(start_index)
    while q:
        i = q.popleft()
        if computers[i][i] == 0:
            continue
        else:
            computers[i][i] = 0
            networks[i] = start_index
        for j, conn in enumerate(computers[i]):
            if conn == 1:
                q.append(j)


def solution(n, computers):
    answer = 0

    networks = [-1 for i in range(n)]

    for i in range(n):
        traverse(computers, networks, start_index=i)

    answer = len(set(networks))
    return answer



TEST_CASES = [
    {
        "n": 3,
        "computers": [[1, 1, 0], [1, 1, 0], [0, 0, 1]],
        "result": 2
    }, {
        "n": 3,
        "computers": [[1, 1, 0], [1, 1, 1], [0, 1, 1]],
        "result": 1
    }, {
        "n": 6,
        "computers": [
            [1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 0],
            [0, 0, 1, 1, 0, 0],
            [0, 0, 1, 1, 0, 0],
            [1, 1, 0, 0, 1, 1],
            [1, 0, 0, 0, 1, 1],
        ],
        "result": 2
    }, {
        "n": 5,
        "computers": [
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
        ],
        "result": 1
    }, {
        "n": 5,
        "computers": [
            [1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1],
        ],
        "result": 5
    }, {
        "n": 4,
        "computers": [
            [1, 0, 0, 1],
            [0, 1, 1, 1],
            [0, 1, 1, 0],
            [1, 1, 0, 1]
        ],
        "result": 1
    }
]
