"""
File: class_reviews.py
Name: Mike
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""


def main():
    num_data001 = 0
    num_data101 = 0
    max_data001 = 0
    min_data001 = 0
    max_data101 = 0
    min_data101 = 0
    total001 = 0
    total101 = 0
    while True:
        a = input('Which class? ')
        if a == '-1':
            exit_fill(max_data001, max_data101, min_data001, min_data101, total001, total101, num_data001, num_data101)
            break
        b = int(input('Score: '))
        if a.upper() == 'SC001':
            if num_data001 == 0:
                max_data001 = b
                min_data001 = b
                total001 = b
                num_data001 += 1
            else:
                if b > max_data001:
                    max_data001 = b
                elif b < min_data001:
                    min_data001 = b
                total001 += b
                num_data001 += 1
        if a.upper() == 'SC101':
            if num_data101 == 0:
                max_data101 = b
                min_data101 = b
                total101 = b
                num_data101 += 1
            else:
                if b > max_data101:
                    max_data101 = b
                elif b < min_data101:
                    min_data101 = b
                total101 += b
                num_data101 += 1


def exit_fill(max_data001, max_data101, min_data001, min_data101, total001, total101, num_data001, num_data101):
    if max_data001 == max_data101 == 0:
        print('No class scores were entered')
    else:
        print('============SC001============')
        if max_data001 == 0:
            print('No score for SC001')
        else:
            print('Max (001):', max_data001)
            print('Min (001):', min_data001)
            print('Avg (001):', total001 / num_data001)
        print('============SC101============')
        if max_data101 == 0:
            print('No score for SC101')
        else:
            print('Max (101):', max_data101)
            print('Min (101):', min_data101)
            print('Avg (101):', total101 / num_data101)


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
