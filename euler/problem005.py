# 100% score achieved

import sys

def euler(n):
    ans = 1

    if n == 1:
        return ans

    nums = list(range(2, n + 1))

    while len(nums) > 0:
        ans *= nums[0]
        nums = [num // nums[0] if num % nums[0] == 0 else num for num in nums]
        nums = [num for num in nums if num > 1]

    return ans

t = int(input().strip())

for a0 in range(t):
    n = int(input().strip())

    print(euler(n))