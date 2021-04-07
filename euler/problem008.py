# 100% score achieved

import sys

def getProd(nums):
    prod = 1

    for num in nums:
        prod *= num
    
    return prod

def euler(n, k, num):
    maxProd = 0
    nums = list(map(int, str(num)))

    for i in range(n - k + 1):
        prod = getProd(nums[i: i + k])
        maxProd = max(maxProd, prod)
    
    return maxProd

t = int(input().strip())

for a0 in range(t):
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]

    num = int(input().strip())
    
    print(euler(n, k, num))