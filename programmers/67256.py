PHONE = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2),
    0: (3, 1)
}


def get_dist(src, dst):
    return abs(src[0] - dst[0]) + abs(src[1] - dst[1])


def solution(numbers, hand):
    answer = ''
    left = (3,0)
    right = (3,2)

    while numbers:

        number = numbers.pop(0)
        if number in [1,4,7]:
            left = PHONE[number]
            answer += "L"
        elif number in [3,6,9]:
            right = PHONE[number]
            answer += "R"
        else:
            left_dist = get_dist(left, PHONE[number])
            right_dist = get_dist(right, PHONE[number])

            if left_dist > right_dist:
                right = PHONE[number]
                answer += "R"
            elif left_dist < right_dist:
                left = PHONE[number]
                answer += "L"
            else:
                if hand == "right":
                    right = PHONE[number]
                    answer += "R"
                elif hand == "left":
                    left = PHONE[number]
                    answer += "L"
        # print(answer)
    return answer


assert solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right") == "LRLLLRLLRRL"
assert solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left") == "LRLLRRLLLRR"
assert solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right") == "LLRLLRLLRL"
