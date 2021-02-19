def solution(A):
    allNums = set(A)
    maxNum = max(allNums)

    if maxNum == len(A) == len(allNums):
        return 1

    return 0


print(solution([4, 3, 2, 1, 5, 7, 3, 2, 5, 1, 8, 7, 4]))
