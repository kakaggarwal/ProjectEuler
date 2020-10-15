import sys

# findWord(["P>E","E>R","R>U"]) // PERU
# findWord(["I>N","P>A","A>I","S>P"]) // SPAIN


def findFirstChar(words):
    search = ''.join(words)

    for word in words:
        if search.count(word[0]) == 1:
            words.remove(word)
            return word[0] + word[2]


def assembleWord(ans, words):
    if len(words) == 1:
        return ans + words[0][2]

    for word in words:
        if ans[-1] == word[0]:
            ans += word[2]
            words.remove(word)
            break

    return assembleWord(ans, words)


def findWord(words):
    ans = findFirstChar(words)

    print(assembleWord(ans, words))


findWord(["I>N", "P>A", "A>I", "S>P"])
findWord(["P>E", "E>R", "R>U"])
