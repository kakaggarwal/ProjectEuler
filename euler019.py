import sys


def checkLeapYear(y):
    if (y % 100 == 0):
        if (y % 400 == 0):
            return True
    elif y % 4 == 0:
        return True

    return False


def getMonthDays(y, m):
    days = 0

    if (m == 1):
        return days
    else:
        days += 31

    if (m == 2):
        return days
    else:
        if checkLeapYear(y) == True:
            days += 29
        else:
            days += 28

    if (m == 3):
        return days
    else:
        days += 31

    if (m == 4):
        return days
    else:
        days += 30

    if (m == 5):
        return days
    else:
        days += 31

    if (m == 6):
        return days
    else:
        days += 30

    if (m == 7):
        return days
    else:
        days += 31

    if (m == 8):
        return days
    else:
        days += 31

    if (m == 9):
        return days
    else:
        days += 30

    if (m == 10):
        return days
    else:
        days += 31

    if (m == 11):
        return days
    else:
        days += 30

    return days


def getDay(y, m, d):
    m = getMonthDays(y, m)

    y = (y - 1) % 400
    ty = y % 100
    y = y - ty

    if (y == 100):
        y = 5
    elif (y == 200):
        y = 3
    elif (y == 300):
        y = 1

    y += ty + int(ty / 4)

    day = (d + m + y) % 7

    return day


def getSundayCount(y1, m1, d1, y2, m2, d2):
    sundayCount = 0

    if d1 != 1:
        d1 = 1

        if m1 < 12:
            m1 += 1
        else:
            m1 = 1
            y1 += 1

    if d2 != 1:
        d2 = 1

    if y2 >= y1 and m2 >= m1 and d2 >= d1:
        while True:
            if y1 >= y2:
                if m1 > m2:
                    return sundayCount

            if getDay(y1, m1 % 12, d1) == 0:
                sundayCount += 1

            if m1 == 12:
                m1 = 1
                y1 += 1
            else:
                m1 += 1

    return sundayCount


t = int(input().strip())

for a0 in range(t):
    date1 = [int(n_temp) for n_temp in input().strip().split(' ')]
    y1 = date1[0]
    m1 = date1[1]
    d1 = date1[2]

    date2 = [int(n_temp) for n_temp in input().strip().split(' ')]
    y2 = date2[0]
    m2 = date2[1]
    d2 = date2[2]

    print(getSundayCount(y1, m1, d1, y2, m2, d2))
