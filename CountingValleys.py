#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    a = 0
    count = 0
    for i in range(0, len(s)):
        if (s[i]=='U'):
            a+=1
            if(a == 0):
                count+=1
        else:
            a-=1
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
