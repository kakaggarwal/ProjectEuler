#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findSubstring' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#
vowels = ['a', 'e', 'i', 'o', 'u']


def getVowelCount(s):
    count = 0

    for v in vowels:
        count += s.count(v)

    return count


def findSubstring(s, k):
    max = 0
    res = ''

    for i in range(len(s) - k + 1):
        vCount = getVowelCount(s[i: i + k])

        if vCount > max:
            max = vCount
            res = s[i: i + k]
        elif vCount == max and s[i: i + k] < res:
            res = s[i: i + k]

    return res


findSubstring('azerdii', 5)
