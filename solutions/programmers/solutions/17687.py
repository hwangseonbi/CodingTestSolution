"""
https://programmers.co.kr/learn/courses/30/lessons/17687
"""
def num_to_str(x, n):
    num_str = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

    y = ""
    while True:
        y = num_str[x % n] + y
        x = x // n
        if x == 0:
            break
    return y


def solution(n, t, m, p):
    answer = []
    order = 0
    binary_number = 0

    while True:
        num_str = num_to_str(binary_number, n)

        for a in num_str:
            if order % m + 1 == p:
                answer.append(a)
                if len(answer) == t:
                    return ''.join(answer)
            order += 1
        binary_number += 1

