#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
POSITIVE = "POSITIVE"
NEGATIVE = "NEGATIVE"
ZERO = "ZERO"

def plusMinus(arr):
    # Write your code here
    table = {
        POSITIVE:0,
        NEGATIVE:0,
        ZERO:0
    }
    for a in arr:
        if a > 0:
            table[POSITIVE] += 1
        elif a == 0:
            table[ZERO] += 1
        elif a < 0:
            table[NEGATIVE] += 1
        else:
            raise Exception("Input Range Error")

    num_of_entity = table[POSITIVE] + table[NEGATIVE] + table[ZERO]
    positive_ratio = table[POSITIVE]/num_of_entity
    negative_ratio = table[NEGATIVE] / num_of_entity
    zero_ratio = table[ZERO] / num_of_entity
    print("{:.6f}".format(positive_ratio))
    print("{:.6f}".format(negative_ratio))
    print("{:.6f}".format(zero_ratio))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)



