#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    global x,y
    x = 1
    y = 1
    for x in range(1,n+1):
        y = x*y

    print(y)

if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)
