"""
File: caesar.py
Name: Mike
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""
# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    k = int(input('The Secret number: '))
    new_alphabet = ALPHABET[26-k:26] + ALPHABET[0:26-k]     # Set the new alphabet base on how user want to change it.
    m = str(input("What's the ciphered string? "))
    m = m.upper()   # Case-insensitive.
    ans = ''
    for i in range(len(m)):
        for j in range(26):
            if m[i] == new_alphabet[j]:
                ans += ALPHABET[j]  # Decipher the ciphered string by using the new alphabet.W
            elif m[i] == ' ':   # Print space if the input string has it.
                ans += ' '
                break
            elif not m[i].isalpha():    # For anything like symbols or anything not in the alphabet.
                ans += m[i]
                break
    print(ans)


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
