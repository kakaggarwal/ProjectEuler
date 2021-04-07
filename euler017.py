import sys

suffixes = ['Trillion',
            'Hundred', 'ty', 'Billion',
            'Hundred', 'ty', 'Million',
            'Hundred', 'ty', 'Thousand',
            'Hundred', 'ty', '']


def getSpecialWords(num):
    if num == '1':
        return 'Eleven'
    elif num == '2':
        return 'Twelve'
    elif num == '3':
        return 'Thirteen'
    elif num == '4':
        return 'Fourteen'
    elif num == '5':
        return 'Fifteen'
    elif num == '6':
        return 'Sixteen'
    elif num == '7':
        return 'Seventeen'
    elif num == '8':
        return 'Eighteen'
    elif num == '9':
        return 'Nineteen'
    elif num == '0':
        return 'Ten'


def euler(n):
    if n == '0':
        return 'zero'

    res = [''] * 13
    n = '0' * (13 - len(n)) + n

    for i in range(13):
        if n[i] == '0':
            if (i == 3 or i == 6 or i == 9) and (n[i - 2] != '0' or n[i - 1] != '0'):
                res[i] = suffixes[i]
        elif n[i] == '1':
            if i == 2 or i == 5 or i == 8 or i == 11:
                res[i + 1] = suffixes[i + 1]
                res[i] = getSpecialWords(n[i + 1])
                n = n[: i + 1] + ' ' + n[i + 2:]
            else:
                res[i] = 'One ' + suffixes[i]
        elif n[i] == '2':
            if i == 2 or i == 5 or i == 8 or i == 11:
                res[i] = 'Twen' + suffixes[i]
            else:
                res[i] = 'Two ' + suffixes[i]
        elif n[i] == '3':
            if i == 2 or i == 5 or i == 8 or i == 11:
                res[i] = 'Thir' + suffixes[i]
            else:
                res[i] = 'Three ' + suffixes[i]
        elif n[i] == '4':
            if i == 2 or i == 5 or i == 8 or i == 11:
                res[i] = 'For' + suffixes[i]
            else:
                res[i] = 'Four ' + suffixes[i]
        elif n[i] == '5':
            if i == 2 or i == 5 or i == 8 or i == 11:
                res[i] = 'Fif' + suffixes[i]
            else:
                res[i] = 'Five ' + suffixes[i]
        elif n[i] == '6':
            if i == 2 or i == 5 or i == 8 or i == 11:
                res[i] = 'Six' + suffixes[i]
            else:
                res[i] = 'Six ' + suffixes[i]
        elif n[i] == '7':
            if i == 2 or i == 5 or i == 8 or i == 11:
                res[i] = 'Seven' + suffixes[i]
            else:
                res[i] = 'Seven ' + suffixes[i]
        elif n[i] == '8':
            if i == 2 or i == 5 or i == 8 or i == 11:
                res[i] = 'Eigh' + suffixes[i]
            else:
                res[i] = 'Eight ' + suffixes[i]
        elif n[i] == '9':
            if i == 2 or i == 5 or i == 8 or i == 11:
                res[i] = 'Nine' + suffixes[i]
            else:
                res[i] = 'Nine ' + suffixes[i]

        i += 1

    return ''.join(list(map(lambda x: x + ' ' if len(x.strip()) > 0 else '', res))).strip()


t = int(input().strip())

for a0 in range(t):
    n = input().strip()

    print(euler(n))
