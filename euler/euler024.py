import sys

_word = 'abcdefghijklm'


def getFactorial(n):
    if n == 1:
        return 1
    else:
        return int(n * getFactorial(n - 1))


def euler(n):
    word = _word
    ans = ''
    leng = len(_word)

    while leng > 1:
        fact = getFactorial(leng - 1)
        i = int(n / fact)

        if n % fact == 0:
            i -= 1

        ans += word[i]
        word = word.replace(word[i], '')
        n = n % fact

        if n == 0:
            n = fact

        leng -= 1

    return ans + word


t = int(input().strip())

for a0 in range(t):
    n = int(input().strip())
    print(euler(n))
