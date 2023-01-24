"""
File: extension2_number_checker.py
Name: Mike
------------------------
This program asks our user for input and checks if the input is a
perfect number、deficient number or an abundant number.

A number is said to be perfect if it is equal to the sum of all its
factors (for obvious reasons the list of factors being considered does
not include the number itself).

A number is considered to be abundant if the sum of its factors
(aside from the number) is greater than the number itself.

And a number is said to be deficient if it is bigger than the sum of all its
factors(aside from the number itself).

The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
    print('Welcome to the number checker!')
    while True:
        n = int(input('n: '))
        m = 1
        sum_data = 0
        if n == EXIT:
            print('Have a good one.')
            break
        while m < n:
            if n % m == 0:      # Find all the factors besides number entered and add up.
                sum_data += m
                m += 1
            elif n % m != 0:    # m is not a factor, add 1 and go back to calculate again.
                m += 1
        if sum_data == n:
            print(n, 'is a perfect number.')
        elif sum_data > n:
            print(n, 'is an abundant number.')
        else:
            print(n, 'is a deficient number.')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
