def getCompressedCount(n):
    i = 0
    compressed = ''

    while i < len(n):
        count = 0

        for j in range(i, len(n)):
            if n[i] != n[j]:
                break
            else:
                count += 1

        if count > 1:
            compressed = compressed + str(count) + n[i]
        else:
            compressed = compressed + n[i]

        i += count

    return len(compressed)

def solution(S, K):
    lengths = []

    for i in range(len(S) - K + 1):
        lengths.append(getCompressedCount(S[0:i] + S[i + K:]))

    return min(lengths)