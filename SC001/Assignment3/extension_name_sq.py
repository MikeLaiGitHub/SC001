"""
File: name_sq.py (extension)
Name: Mike
----------------------------
This program is an extension of assignment3!
It will ask the user to provide a name, 
and the square pattern of the given name 
will be printed on the console.
"""


def main():
    print('This program prints a name in a square pattern!')
    name = input('Name: ')
    b = len(name)
    c = 1
    len_body = len(name)-2  # Body of the square pattern doesn't include first and last digit.
    print(name)             # Print the name as the upper 'line' of the square.
    print_square_body(name, c, len_body)    # Print the right and left 'line' with characters in the middle of the name.
    print_backward(name, b)                 # Lastly, print the name backward to complete the square pattern.


def print_square_body(name, c, len_body):  # Using the similar concept from rocket printing.
    while len_body != 0:   # Left side of the line like this JENNY, right side is inverted as example. From up to down.
        print(name[c], end='')              # Left side in the 'body' is not inverted from up then down.
        for i in range(len(name)-2):        # Print spaces needed to complete the square pattern.
            print(' ', end='')
        print(name[len_body], end='')       # Right side in the 'body' is inverted from up then down.
        print('')
        c += 1
        len_body -= 1               # Left side controls when the function stop. Meaning the whole body will be printed.


def print_backward(a, b):           # Print the name backward to complete the square pattern.
    while b != 0:
        print(a[b-1], end='')
        b -= 1


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
