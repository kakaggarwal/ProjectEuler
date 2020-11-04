def solution(A):
    allNums = set(A)
    maxNum = max(allNums)

    if maxNum < 1:
        return 1

    checkArr = [False] * (len(allNums) + 1)

    for num in allNums:
        if 0 < num <= (len(allNums)):
            checkArr[num - 1] = True

    for i in range(len(checkArr)):
        if checkArr[i] == False:
            return i + 1

    return len(checkArr) + 1


print(solution([-1000000, 1000000, 1, 4, 2, 3, 5]))
