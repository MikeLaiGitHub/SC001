"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	TODO:
	"""
	count = 0
	dictionary = []
	read_dictionary(dictionary)
	row_lst = []
	word_lst = []
	for i in range(4):
		row_words = input(f'{i+1} row of letters: ')
		lst = []
		if len(row_words) != 7:
			print('illegal input')
			break
		else:
			for j in range(4):
				lst += row_words[(2*j)].lower()
			row_lst.append(lst)

	for i in range(4):
		for j in range(4):
			character = row_lst[i][j]
			character_position = [(i, j)]
			find_word(row_lst, i, j, character, character_position, count, word_lst, dictionary)
			character_position.clear()

	print(f'there are {count} word(s) in total.')


def find_word(r, m, n, character, character_position, count, word_lst, dictionary):
	if character in dictionary and len(character) > 3 and character not in word_lst:
		print(f'Found: {character}')
		word_lst.append(character)
		count += 1
	else:
		if has_prefix(character, dictionary) is True:
			for i in range(-1, 2):
				for j in range(-1, 2):
					if 4 > m+i >= 0 and 4 > n+j >= 0 and (m+j, n+j) not in character_position:
						character += r[m+i][n+j]
						character_position.append((m+i, n+j))
						find_word(r, m+i, n+j, character, character_position, count, word_lst, dictionary)
						character_position.pop()
						character = character[:len(character)-1]


def read_dictionary(dictionary):
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, 'r') as f:
		for line in f:
			dictionary.append(line.strip())


def has_prefix(sub_s, dictionary):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dictionary:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
