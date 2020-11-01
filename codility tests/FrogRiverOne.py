# 100% score achieved

import sys

def solution(X, A):
    path = set(A)

    if len(path) != X:
        return - 1
    
    destIndex = A.index(X) + 1
    mayBePath = set(A[:destIndex])
    
    if path == mayBePath:
        return destIndex - 1

    lenA = len(A)

    while destIndex < lenA:
        mayBePath.add(A[destIndex])

        if path == mayBePath:
            return destIndex
        
        destIndex += 1

print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4])) # 6
print(solution(1, [1])) # 0
print(solution(5, [1, 3, 1, 2, 3, 5, 4, 1, 3, 1, 2, 3, 5,])) # 12
print(solution(2, [1])) # -1
print(solution(5, [1, 3, 1, 2, 3, 5, 4, 1, 1, 2, 5,])) # 10