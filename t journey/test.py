
def solution(increment):
    # return number from 1 to 100

    for i in range(0, 101, increment):
        if i == 0:
            print(1)
        else:
            print(i)


# print(solution(5))

def numberOfCarryOperations(num1, num2):
    carryCount = 0
    carry = 0

    while num1 > 0 or num2 > 0:
        carry = (num1 % 10 + num2 % 10 + carry) // 10
        num1 = num1 // 10
        num2 = num2 // 10

        if carry > 0:
            carryCount += 1

    return carryCount


# print(numberOfCarryOperations(65, 55))
# print(numberOfCarryOperations(135, 955))
print(numberOfCarryOperations(123, 456))  # // 0
print(numberOfCarryOperations(555, 555))  # // 3
print(numberOfCarryOperations(900, 11))  # // 0
print(numberOfCarryOperations(145, 55))  # // 2
print(numberOfCarryOperations(0, 0))  # // 0
print(numberOfCarryOperations(1, 99999))  # // 5
print(numberOfCarryOperations(999045, 1055))  # // 5
print(numberOfCarryOperations(101, 809))  # // 1
print(numberOfCarryOperations(189, 209))  # // 1
