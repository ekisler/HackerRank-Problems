#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#
def findMedian(cntarr, d):
    cnt = 0
    rslt = 0

    if d%2 is not 0:
        for i in range(len(cntarr)):
            cnt += cntarr[i]

            if cnt > d//2:
                rslt = i
                break
    else:
        first = 0
        second = 0

        for i, _ in enumerate(cntarr):
            cnt += cntarr[i]
            if first == 0 and cnt >= d//2:
                first = i
            if second == 0 and cnt >= d//2 + 1:
                second = i
                break
        rslt = (first+second) / 2
    return rslt
def activityNotifications(expenditure, d):
    # Write your code here
    noti = 0
    cntarr = [0 for _ in range(201)]
    for i in range(d):
        cntarr[expenditure[i]] += 1

    for i in range(d, len(expenditure)):
        median = findMedian(cntarr, d)

        if 2*median <= expenditure[i]:
            noti += 1

        cntarr[expenditure[i-d]] -= 1
        cntarr[expenditure[i]] += 1

    return noti

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
