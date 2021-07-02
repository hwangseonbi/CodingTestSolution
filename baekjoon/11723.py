"""
https://www.acmicpc.net/problem/11723
"""
import sys


M = int(sys.stdin.readline())
S = set()


def add(n):
    global S
    S.add(n)


def remove(n):
    global S
    if n in S:
        S.remove(n)


def check(n):
    global S

    if n in S:
        return 1
    else:
        return 0


def toggle(n):
    global S
    if n in S:
        S.remove(n)
    else:
        S.add(n)


def all(n=None):
    global S
    S = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])


def empty(n=None):
    global S
    S.clear()

OP = {
    "add": add,
    "remove": remove,
    "check": check,
    "toggle": toggle,
    "all": all,
    "empty": empty,
}

for _ in range(M):
    # op = int()
    op_info = sys.stdin.readline().split()

    operation = OP.get(op_info[0])
    n = None if len(op_info) < 2 else int(op_info[1])

    result = operation(n)
    if result != None: print(result)
    # print(f'[{operation.__name__} ({n})] -> {result} //   {S}')