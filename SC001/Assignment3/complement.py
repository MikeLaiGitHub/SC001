"""
File: complement.py
Name: Mike
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program provides different DNA sequence as
a python string that is case-sensitive.
Your job is to output the complement of them.
"""


def main():
    print(build_complement('ATC'))
    print(build_complement(''))
    print(build_complement('ATGCAT'))
    print(build_complement('GCTATAC'))


def build_complement(dna):
    ans = ""
    if dna == '':
        return 'DNA strand is missing.'
    else:
        for i in range(len(dna)):   # Replace the requested DNA string to the requested DNA.
            complement = dna[i]
            if complement == 'A':
                ans = ans+'T'
            if complement == 'T':
                ans = ans+'A'
            if complement == 'G':
                ans = ans+'C'
            if complement == 'C':
                ans = ans + 'G'
        return ans


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
