def solution(A):
    allNums = set(A)

    if len(allNums) != len(A):
        return 0

    return 1


print(solution([4, 3, 2, 1, 5, 7, 3, 2, 5, 1, 8, 7, 4]))
