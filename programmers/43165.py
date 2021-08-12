import itertools

# def solution(numbers, target):
#     answer = 0
#
#     numbers_index = [i for i in range(len(numbers))]
#     _sum = sum(numbers)
#     for i in range(len(numbers)):
#         for minus_index in itertools.combinations(numbers_index, i):
#             minus_sum = 0
#             for j in minus_index:
#                 minus_sum += numbers[j]
#             if (_sum - minus_sum * 2) == target:
#                 answer += 1
#
#     return answer


answer = 0


def DFS(depth, numbers, target, result):
    global answer

    if depth >= len(numbers):
        if result == target:
            answer += 1
            print(result)
    else:
        DFS(depth + 1, numbers, target, result - numbers[depth])
        DFS(depth + 1, numbers, target, result + numbers[depth])


def solution(numbers, target):
    global answer
    DFS(0, numbers, target, 0)
    return answer


TEST_CASES = [
    {
        "numbers": [1, 1, 1, 1, 1],
        "target": 3,
        "result": 5
    }
]
