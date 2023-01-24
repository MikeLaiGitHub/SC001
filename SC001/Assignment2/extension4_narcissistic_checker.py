"""
File: extension4_narcissistic_checker.py
Name: Mike
------------------------
This program asks our user for input and checks if the input is a
narcissistic number or not.

A positive integer is called a narcissistic number if it
is equal to the sum of its own digits each raised to the
power of the number of digits.

Example: 153 is narcissistic because 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.
Note that by this definition all single digit numbers are narcissistic.

Students are recommended to use // and % to complete this program.

The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
    print('Welcome to the narcissistic checker.')
    while True:
        n = int(input('n: '))
        m = 1
        k = 0
        sum_data = 0
        if n == EXIT:
            print('Have a good one!')
            break
        elif n / 10 < 1:  # For number from 1 to 9.
            k += 1
        elif n / 10 == 1:  # For number 10.
            k += 2
        else:
            while n / 10 ** k > 1:  # For any number besides 1 to 10 and 10's multiples.
                n / 10 ** k
                k += 1
            if n % 10 == 0:  # 10's multiples need to add 1 to the value to get the right number of digits.
                k += 1
        while k - m >= 0:
            equation = (n / 10 ** (k - m)) // 1 % 10  # To get the value of each digit.
            sum_data += equation ** k
            m += 1
        if sum_data == n:  # If the calculated result is same as the number entered then it is a narcissistic number.
            print(int(sum_data), 'is a narcissistic number.')
        else:
            print(n, 'is not a narcissistic number.')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
