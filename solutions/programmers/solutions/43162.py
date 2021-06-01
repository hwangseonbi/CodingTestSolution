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
