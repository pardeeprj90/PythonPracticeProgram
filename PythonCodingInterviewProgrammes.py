# P-1:- Swap two numbers
# Ist approach by using temp variable
def swapTwoNumbersWithTemp():
    number1 = input(f'Please enter 1st Number:- ')
    number2 = input(f'Please enter 2nd Number:- ')
    print(f'Value of Number1 before swap {number1}')
    print(f'Value of Number2 before swap {number2}')
    temp = number1
    number1 = number2
    number2 = temp
    print(f'Value of Number1 After swap {number1}')
    print(f'Value of Number2 After swap {number2}')


# swapTwoNumbersWithTemp()

# 2nd approach by using temp variable
def swapTwoNumbersWithoutTemp():
    number1 = input(f'Please enter 1st Number:- ')
    number2 = input(f'Please enter 2nd Number:- ')
    print(f'Value of Number1 before swap {number1}')
    print(f'Value of Number2 before swap {number2}')
    number1, number2 = number2, number1
    print(f'Value of Number1 After swap {number1}')
    print(f'Value of Number2 After swap {number2}')


# swapTwoNumbersWithoutTemp()

# 3rd approach by using list
def swapTwoNumbersUsingList(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    print(list)


number = [34, 67, 56, 87, 90]
_swap_pos1 = 1
_swap_pos2 = 4


# swapTwoNumbersUsingList(number, _swap_pos1 - 1, _swap_pos2 - 1)


# P-2:- Check entered number is prime or not?
def isPrime():
    num1 = int(input("Please enter a number to check whether it is prime or not? "))
    count = 0
    if num1 > 1:
        for i in range(1, num1 + 1):
            if (num1 % i) == 0:
                count += 1
        if count == 2:
            print(f'Entered number {num1} is a prime number')
        else:
            print(f'Entered number {num1} is not a prime number')


# isPrime()

# P-3:- Find the factorial of a number
# Factorial of a number is the product of all the integers from 1 to that number. For example, the factorial of 7 is 1*2*3*4*5*6*7 = 5040

# Facts
# factorial of -ve doesn't exist
# factorial of 0 is 1

def findFactorial():
    number1 = int(input("Please enter the number whose factorial needs to be identified:- "))
    factorial = 1
    if number1 < 0:
        print(f'entered number {number1} is -ve so factorial can not be calculated')
    elif number1 == 0:
        print(f'Factorial of entered number {number1} is 1')
    elif number1 > 0:
        for i in range(1, number1 + 1):
            factorial = factorial * i
        print(f'Calculated factorial of entered number {number1} is {factorial}')


# findFactorial()

# Print Fibonacci series
# Desc:-Fibonacci Sequence is the series of numbers, where each number in the series is the sum of two preceding numbers.0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ..

def printFibonacciSeries():
    num1 = int(input(f'Please enter the starting Range from where Fibonacci Series needs to be started:- '))
    num2 = int(input(f'Please enter the starting Range from where Fibonacci Series needs to be Ended:- '))
    for i in range(num1, num2):
        addition = num1 + num2
        print(addition)
        num1 = num2
        num2 = addition


# printFibonacciSeries()

# Swap 1st and last element of a list
def swapList():
    listNums = [1, 2, 3, 4]
    print(f'Before swap list {listNums}')
    size = len(listNums)
    temp = listNums[0]
    listNums[0] = listNums[size - 1]
    listNums[size - 1] = temp
    print(f'After swapping ist and last values of list {listNums}')


# swapList()

# Remove the occurrence of a word from a list

def removeSpecificWordFromList():
    value = list(map(str, input("Please enter multiple String values separated by a space:- ").split()))
    print(value)
    valueToBeRemoved = input(f'Please enter a string value from above list which needs to be removed:- ')
    listElementCount = len(value)
    if listElementCount > 0:
        for i in range(0, listElementCount):
            if value[i] == valueToBeRemoved:
                del value[i]
        print(value)
    else:
        print(f'Empty list {listElementCount}')


# removeSpecificWordFromList()


# Remove the occurrence of a word from a list

def removeRepetitiveWordFromList():
    value = list(map(str, input("Please enter multiple String values separated by a space:- ").split()))
    _new_list = list(set(value))
    # updated_list = [*_new_list]
    print(_new_list)


removeRepetitiveWordFromList()
