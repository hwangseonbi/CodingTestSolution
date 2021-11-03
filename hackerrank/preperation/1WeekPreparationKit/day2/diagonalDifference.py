#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
import math



def diagonalDifference(arr):
    # Write your code here

    n = len(arr)

    left_to_right_diagonal = 0
    right_to_left_diagonal = 0
    for i in range(n):
        left_to_right_diagonal += arr[i][i]
    for i in range(n):
        right_to_left_diagonal += arr[i][n-i-1]


    return abs(left_to_right_diagonal - right_to_left_diagonal)

def test():
    print(diagonalDifference([
        [11, 2, 4],
        [4, 5, 6],
        [10, 8, -12]
    ]))
if __name__ == '__main__':
    # test()
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
