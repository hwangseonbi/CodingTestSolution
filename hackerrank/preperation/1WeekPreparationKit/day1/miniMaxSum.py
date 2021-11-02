#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    min_sum = 0
    for i in range(0,4):
        min_sum += arr[i]
        # print(arr[i])


    # print()
    max_sum = 0
    for i in reversed(range(1,5)):
        max_sum += arr[i]
        # print(arr[i])

    print(f'{min_sum} {max_sum}')


def test():
    # miniMaxSum([1, 2, 3, 4, 5])
    miniMaxSum([7, 69, 2, 221, 8974])

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
    # test()
