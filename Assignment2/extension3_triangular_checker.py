"""
File: extension3_triangular_checker.py
Name: Mike
--------------------------
This program asks our user for input and checks if the input is an
triangular number or not.

The triangular number (Tn) is a number that can be represented in the form of a triangular
grid of points where the first row contains a single element and each subsequent row contains 
one more element than the previous one.

We can just use the fact that the nth triangular number can be found by using a formula: Tn = n(n + 1) / 2.

The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
    print("Welcome to the triangular number checker.")
    while True:
        n = int(input('n: '))
        if n == EXIT:
            print('Have a good one!')
            break
        m = 1       # Base number for thr first triangular number.
        while m*(m+1)/2 <= n:       # Results can't go over number entered.
            if m*(m+1)/2 == n:
                print(n, 'is a triangular number.')
                break
            else:   # Add on 1 and go back to calculation if its not equal to n.
                m += 1
        if m*(m+1)/2 != n:      # If every possible m calculated aren't equal to n, not triangular number.
            print(n, 'is not a triangular number.')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
