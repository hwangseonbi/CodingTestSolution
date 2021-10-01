import math

def solution(n, times):
    answer = 0

    right = max(times) * n
    left = 1
    mid = math.floor((right + left) / 2)
    while True:
        done = sum(map(lambda x: math.floor(mid / x), times))

        if done >= n:
            right = mid
        else:
            left = mid
        mid = math.floor((right + left) / 2)

        if left == mid:
            answer = right
            break

    return answer


assert solution(6, [7, 10]) == 6
