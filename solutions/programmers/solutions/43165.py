import itertools

def solution(numbers, target):
    answer = 0

    numbers_index = [i for i in range(len(numbers))]
    _sum = sum(numbers)
    for i in range(len(numbers)):
        for minus_index in itertools.combinations(numbers_index, i):
            minus_sum = 0
            for j in minus_index:
                minus_sum += numbers[j]
            if (_sum - minus_sum * 2) == target:
                answer += 1

    return answer
