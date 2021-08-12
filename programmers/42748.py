"""
https://programmers.co.kr/learn/courses/30/lessons/42748
"""


def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        sorted_list = sorted(array[i - 1:j])
        answer.append(sorted_list[k - 1])

    return answer
TEST_CASES = [
    {
        "array": [1, 5, 2, 6, 3, 7, 4],
        "commands":[[2, 5, 3], [4, 4, 1], [1, 7, 3]],
        "result": [5, 6, 3]
    }
]
