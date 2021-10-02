def solution(brown, yellow):
    answer = []

    for y in range(1, yellow+1):
        x, rest = divmod(yellow, y)
        if rest != 0:
            continue
        elif 2 * x + 2 * y + 4 == brown:
            answer = [x+2, y+2]
            break

    return answer


assert solution(10, 2) == [4, 3]
assert solution(8, 1) == [3, 3]
assert solution(24, 24) == [8, 6]
