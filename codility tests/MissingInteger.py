def solution(A):
    allNums = set(A)
    maxNum = max(allNums)

    if maxNum < 1:
        return 1
    elif maxNum == len(allNums):
        return maxNum + 1

    allNumsArr = list(allNums)
    allNumsArr.sort()

    first = 0
    end = len(allNumsArr)
    inc = int(end / 10)

    while inc > 0:
        while first < end:
            if first + 1 != allNumsArr[first]:
                end = first
                first -= inc
                break
            else:
                first += inc

        inc = int(end / 10)

    while first < end:
        if first + 1 != allNumsArr[first]:
            return first + 1
        else:
            first += 1


print(solution([-1000000, 1000000, 1, 4, 2, 3, 5]))
