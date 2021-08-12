"""
분류 : 코딩테스트 연습 /2021 KAKAO BLIND RECRUITMENT
문제명 : 메뉴 리뉴얼
URL : https://programmers.co.kr/learn/courses/30/lessons/72411
"""


from itertools import combinations
import collections


def solution(orders, course):
    answer = []
    for course_len in course:
        order_combination = []
        for order in orders:
            order_combination += map(lambda x: ''.join(x),
                                     combinations(sorted(order), course_len))

        most_orderd = collections.Counter(order_combination).most_common()

        result = [subset for subset, num in most_orderd if num > 1
                  and num == most_orderd[0][1]]
        answer += result
    answer = sorted(answer)
    return answer


TEST_CASES = [
    {
        "orders": ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],
        "course": [2, 3, 4],
        "result": ["AC", "ACDE", "BCFG", "CDE"]
    },
    {
        "orders": ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],
        "course": [2, 3, 5],
        "result": ["ACD", "AD", "ADE", "CD", "XYZ"]
    },
    {
        "orders": ["XYZ", "XWY", "WXA"],
        "course": [2, 3, 4],
        "result": ["WX", "XY"]
    }
]
