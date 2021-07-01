"""
https://programmers.co.kr/learn/courses/30/lessons/77484
"""
def solution(lottos, win_nums):
    answer = []
    rank_table = {
        6: 1,
        5: 2,
        4: 3,
        3: 4,
        2: 5,
        1: 6,
        0: 6
    }
    lottos_set = set(lottos)
    win_nums_set = set(win_nums)
    unknown_num_len = sum([1 for l in lottos if l == 0])

    if 0 in lottos_set:
        lottos_set.remove(0)

    equal_num_len = len(lottos_set & win_nums_set)

    min_equal_num_len = equal_num_len
    max_equal_num_len = equal_num_len + unknown_num_len

    answer = [rank_table.get(max_equal_num_len), rank_table.get(min_equal_num_len)]
    return answer
