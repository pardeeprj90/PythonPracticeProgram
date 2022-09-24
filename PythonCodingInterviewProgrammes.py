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
