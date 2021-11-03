#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    table = {}

    for num in a:
        if num not in table:
            table[num] = 0
        table[num] += 1
    for k, v in table.items():
        if v == 1:
            return k

def test():
    print(lonelyinteger([1,2,3,4,3,2,1]))

if __name__ == '__main__':
    # test()

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
