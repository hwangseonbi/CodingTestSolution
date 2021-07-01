import sys

N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))


def solution(N, M, A):
    answer = 0
    start = 0
    end = 0

    _sum = A[0]
    while True:
        if _sum < M:
            end+=1
            if end >= N:
                break
            _sum += A[end]
        elif _sum == M:
            answer+=1
            _sum -= A[start]
            start += 1

        elif _sum >M:
            _sum -= A[start]
            start +=1

    print(answer)




solution(N, M, A)
