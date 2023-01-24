"""
File: hailstone.py
Name: Mike
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    print("This program computes Hailstone sequence")
    n = int(input("Enter a number: "))
    hailstone(n)


def hailstone(n):
    a = 0                       # Before the function start, 0 step is counted.
    while n != 1:
        if n % 2 == 0:          # If even number divide in half. Keep calculating till reach 1.
            print(int(n), "is even so I take half: ", end='')
            n = n/2
            print(int(n))
        else:                   # If odd number make 3n+1. Keep calculating till reach 1.
            print(int(n), "is odd so I make 3n+1: ", end='')
            n = 3*n + 1
            print(int(n))
        a += 1                  # After discriminating a will +1 means 1 step.
    print('It took', a, 'steps to reach 1.')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
