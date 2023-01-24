"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    TODO:
    """
    print("Welcome to stanCode \"Anagram Generator (or -1 to quit)")
    while True:
        word = str(input("Find anagrams for: ")).lower()
        start = time.time()
        if word == EXIT:
            break
        print("Searching...")
        lst = read_dictionary(word)
        find_anagrams(word, lst)
        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary(word):
    same_len = []
    with open(FILE, 'r') as f:
        for line in f:
            if len(word)+1 == len(line):
                same_len.append(line.strip())   # 把和輸入的字相同長度的放在一個list
    return same_len


def find_anagrams(word, same_len):
    d = {}
    for ch in word:     # 字母出現次數 eg.{(r: 2), ...}
        if ch in d:
            d[ch] += 1
        else:
            d[ch] = 1
    final_result = find_anagrams_helper(word, '', [], same_len, d)
    if len(final_result) >= 1:
        print(len(final_result), 'anagrams:', final_result)
    else:
        print(word, 'is not in the dictionary!')


def find_anagrams_helper(user_input, current_s, result_lst, same_len, d):
    if len(current_s) == len(user_input):
        if current_s in same_len:
            print('Found:', current_s)
            print('Searching...')
            result_lst.append(current_s)
    else:
        for ch in d:
            if d[ch] >= 1:

                current_s += ch
                d[ch] -= 1

                if has_prefix(current_s, same_len) is True:
                    find_anagrams_helper(user_input, current_s, result_lst, same_len, d)

                current_s = current_s[:len(current_s)-1]
                d[ch] += 1

    return result_lst


def has_prefix(sub_s, same_len):
    for word in same_len:
        if word.startswith(sub_s) is True:
            return True


if __name__ == '__main__':
    main()
