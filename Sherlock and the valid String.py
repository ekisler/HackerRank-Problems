#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    
    arr=[0 for i in range(26)]
    
    for i in s:
        arr[ord(i)-97]+=1
    
    xset=set(arr)
    xset.discard(0)
    
    if len(xset)==1:    
        return "YES"
    
    elif len(xset)==2:  
        a,b=xset.pop(),xset.pop()   
        if (abs(b-a)==1 or a==1) and arr.count(a)==1:
            return "YES"
        
        elif (abs(b-a)==1 or b==1) and arr.count(b)==1:
            return "YES"
        
        else:
            return "NO"
        
    else:               
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
