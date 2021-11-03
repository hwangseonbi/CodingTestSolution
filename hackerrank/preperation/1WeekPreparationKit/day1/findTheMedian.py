#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
from math import floor
def findMedian(n, arr):
    # Write your code here
    arr.sort()
    i = floor(n/2)
    return arr[i]

if __name__ == '__main__':
    # test()
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
