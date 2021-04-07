def solution(A):
    s = set(A.sort())
    i = 1

    if max(s) < 1:
        return i

    for val in s:
        if i != val:
            break

        i += 1

    return i


print(solution([1, 3, 6, 4, 1, 2]))

print(solution([1, 2, 3]))
