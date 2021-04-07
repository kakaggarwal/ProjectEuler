# 100% score achieved

import sys

def getProd(nums):
    prod = 1

    for num in nums:
        prod *= num
    
    return prod

def euler(n):
    ans = -1

    for num in range(3, n - 2):
        if num % 2 == 0:
            if (num / 2) * (num + 2) > n:
                break
            elif (num / 2) * (num + 2) == n:
                prod = num * ((num / 2)** 2 + 1) * ((num / 2)** 2 - 1)
                
                ans = int(max(ans, prod))
        else:
            if num * (num + 1) > n:
                break
            elif num * (num + 1) == n:
                prod = num * ((num ** 2 / 2) + 0.5) * ((num ** 2 / 2) - 0.5)

                ans = int(max(ans, prod))

    return ans

t = int(input().strip())

for a0 in range(t):
    n = int(input().strip())
    
    print(euler(n))