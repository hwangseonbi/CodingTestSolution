import sys
A,B,C = map(int, sys.stdin.readline().split())

def solution():
    global A,B,C
    answers = []

    answer = (A+B)%C
    answers.append(answer)

    answer = ((A%C) + (B%C))%C
    answers.append(answer)

    answer = (A*B) % C
    answers.append(answer)

    answer = ((A % C) * (B % C)) % C
    answers.append(answer)

    for a in answers:
        print(a)

solution()