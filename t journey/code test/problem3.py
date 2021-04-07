def charACount(s):
    freq = 0

    for ch in s:
        if 'a' == ch:
            freq += 1

    return freq


def solution(S):
    overAllCount = charACount(S)

    if overAllCount > 0 and overAllCount < 3:
        return 0

    count = 0

    for i in range(1, len(S)):
        for j in range(i + 1, len(S)):
            if charACount(S[:i]) == charACount(S[i:j]) == charACount(S[j:]):
                count += 1

    return count


# print(solution('babaa'))
# print(solution('ababa'))
# print(solution('aba'))
print(solution('bbbb'))
