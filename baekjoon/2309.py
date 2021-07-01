import sys
from itertools import permutations
NUMBERS = []
for _ in range(9):
    NUMBERS.append(int(sys.stdin.readline()))


def solution():
    global NUMBERS
    for c in permutations(NUMBERS,7):
        if sum(c) == 100:
            for answer in sorted(c):
                print(answer)
            return
solution()