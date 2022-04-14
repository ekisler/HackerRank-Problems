#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'whatFlavors' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY cost
#  2. INTEGER money
#

def whatFlavors(cost, money):
    # Write your code here
    cost_dict = {}
    for i,icost in enumerate(cost):
        if money-icost in cost_dict:
            print(str(cost_dict[money-icost]+1) + ' ' + str(i+1))
            return
        else:
            cost_dict[icost] = i

if __name__ == '__main__':
    t = int(raw_input().strip())

    for t_itr in xrange(t):
        money = int(raw_input().strip())

        n = int(raw_input().strip())

        cost = map(int, raw_input().rstrip().split())

        whatFlavors(cost, money)
