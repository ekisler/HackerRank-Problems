#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'commonChild' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def commonChild(s1, s2):
    # Write your code here
    m = len(s1)
    n = len(s2)
    prev = [0 for x in range(n + 1)]
    for i in range(1, m + 1):
        curr = [0 for x in range(n + 1)]
        for j in range(1, n + 1):
            curr[j] = max(prev[j], curr[j - 1])
            if s1[i - 1] == s2[j - 1]:
                curr[j] = max(curr[j], prev[j - 1] + 1)
        prev = curr
    return curr[n]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = raw_input()

    s2 = raw_input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
