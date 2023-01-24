"""
File: coin_flip_runs.py
Name: Mike
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random as r


def main():
	print("Let's flip a coin!")
	num_run = int(input('Number of runs: '))
	run = 0
	is_in_a_row = False
	roll1 = r.randint(1, 2)
	convert_roll1(roll1)
	while True:
		if run != num_run:
			roll2 = r.randint(1, 2)
			convert_roll2(roll2)
			if roll1 == roll2:
				if not is_in_a_row:
					run += 1
					is_in_a_row = True
			else:
				is_in_a_row = False
			roll1 = roll2
		else:
			break


def convert_roll1(roll1):
	if roll1 == 1:
		print('H', end='')
	else:
		print('T', end='')


def convert_roll2(roll2):
	if roll2 == 1:
		print('H', end='')
	else:
		print('T', end='')


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
