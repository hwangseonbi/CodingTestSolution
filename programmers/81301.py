'''
https://programmers.co.kr/learn/courses/30/lessons/81301
'''

number_table = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


def solution(s):
    answer = 0
    for n_str, n in number_table.items():
        s = s.replace(n_str, n)

    answer = int(s)
    return answer


assert solution("one4seveneight") == 1478
assert solution("23four5six7") == 234567
assert solution("2three45sixseven") == 234567
assert solution("123") == 123
