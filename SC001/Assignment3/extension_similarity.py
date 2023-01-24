"""
File: similarity.py (extension)
Name: Mike
----------------------------
This program is an extension of assignment3!
It will compare short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    long_sequence = input('Please give me a DNA sequence to search: ')
    a = long_sequence.upper()   # Case-insensitive.
    short_sequence = input('What DNA sequence would you like to match? ')
    b = short_sequence.upper()  # Case-insensitive.
    c = 0
    best_match = ''
    for i in range(len(a)-len(b)+1):    # Calculate how many times of comparing needed.
        e = 0
        d = a[i:len(b)+i]               # Start from the first character of long sequence to reaching the last.
        for j in range(len(b)):         # If there is a match, add up for how many matches for later comparison.
            if d[j] == b[j]:
                e += 1
        if e > c:                     # Replace the previous data as best match, higher in number means more similarity.
            c = e
            best_match = d            # Best match will be found.
    print('The best match is', best_match)


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
