"""
URL : https://www.acmicpc.net/problem/2178
"""
from collections import deque

N = None
M = None
BOARD = None



def input_from_str(input):
    global n, m, board

    input_list = input.splitlines()
    n, m = map(int, input_list.pop(0).split())
    board = []
    for i in range(n):
        board.append(list(map(int, input_list[i])))

    solution()


def input_from_std():
    global N, M, BOARD
    N, M = map(int, input().split())
    BOARD = []
    for _ in range(N):
        BOARD.append(list(map(int, input())))
    solution()


def BFS(start_point):
    global N, M, BOARD

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    q = deque()
    q.append(start_point)

    while q:
        i, j = q.popleft()

        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < N and 0 <= nj < M and BOARD[ni][nj] == 1:
                q.append((ni, nj))
                BOARD[ni][nj] = BOARD[i][j] + 1
                if ni == N - 1 and nj == M - 1:
                    return


def solution():
    start_point = (0, 0)
    BFS(start_point)
    print(BOARD[N - 1][M - 1])

input_from_std()



