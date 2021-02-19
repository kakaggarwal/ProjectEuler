import sys

def solution(A):
    nums = set(A)
    maxNum = max(nums)

    if maxNum = len(nums):
        return maxNum + 1
    elif maxNum < 1:
        return 1
    
    

    return A

print(solution([1, 3, 6, 4, 1, 2]))
print(solution([1, 2, 3]))
print(solution([-1, -3]))