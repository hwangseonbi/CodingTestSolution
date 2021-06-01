"""
https://programmers.co.kr/learn/courses/30/lessons/72410
"""
import copy


def step1(input_str):
    output = [c.lower() for c in input_str]
    return output


def step2(input_str):
    alphabet_lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', \
                           'h', 'i', 'j', 'k', 'l', 'm', 'n', \
                           'o', 'p', 'q', 'r', 's', 't', 'u', \
                           'v', 'w', 'x', 'y', 'z']
    number_char = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    allowed_special_char = ['-', '_', '.']
    allowed_chars = alphabet_lower_case + number_char + allowed_special_char

    def is_allowed(char):
        if char in allowed_chars:
            return True
        else:
            return False

    output = list(filter(is_allowed, input_str))
    return output


def step3(input_str):
    output = copy.deepcopy(input_str)
    output = "".join(output)
    while ".." in output:
        output = output.replace("..", ".")
    return list(output)


def step4(input_str):
    output = copy.deepcopy(input_str)
    while len(output) != 0 and output[0] == '.':
        output.pop(0)

    while len(output) != 0 and output[-1] == '.':
        output.pop(-1)
    return output


def step5(input_str):
    output = copy.deepcopy(input_str)
    if len(output) == 0:
        output.append('a')
    return output


def step6(input_str):
    output = copy.deepcopy(input_str)
    if len(input_str) >= 16:
        output = input_str[0:15]
        if output[-1] == ".":
            output.pop(-1)
    return output


def step7(input_str):
    output = copy.deepcopy(input_str)
    while len(output) <= 2:
        output.append(input_str[-1])
    return output


def solution(new_id):
    answer = ''
    id_list = list(new_id)

    step1_output = step1(id_list)
    step2_output = step2(step1_output)
    step3_output = step3(step2_output)
    step4_output = step4(step3_output)
    step5_output = step5(step4_output)
    step6_output = step6(step5_output)
    step7_output = step7(step6_output)

    answer = ''.join(step7_output)
    return answer
