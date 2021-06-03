"""
https://programmers.co.kr/learn/courses/30/lessons/43163
"""
from collections import deque
from copy import deepcopy


def is_not_similar(a, b):
    diff_count = 0
    for _a, _b in zip(a, b):
        if _a != _b:
            diff_count += 1
    if diff_count > 1:
        return True
    return False


def solution(begin, target, words):
    answer = 0
    q = deque()
    q.append((begin, [True for _ in words]))

    while q:
        word, visited_info = q.popleft()

        if word == target:
            return len(list(filter(lambda x: not x, visited_info)))

        for i, allowed in enumerate(visited_info):
            if not allowed:
                continue
            if is_not_similar(word, words[i]):
                continue
            new_visited_info = deepcopy(visited_info)
            new_visited_info[i] = False
            q.append((words[i], new_visited_info))

    return answer
