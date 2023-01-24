"""
File: extension1_factorial.py
Name: Mike
-------------------
This program will continually ask our user to give a number
and will calculate the factorial result of the number and print it on the console.

The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
	print('Welcome to stanCode factorial master!')
	while True:
		n = int(input('Give me a number, and I will list the answer of the factorial: '))
		if n == EXIT:
			print('------See ya!------')
			break
		else:
			print(factorial(n))
		# m = 1			# Base value for calculating the factorial.
		# if n == EXIT:
		# 	print('------See ya!------')
		# 	break
		# while n < 0:
		# 	n = int(input('Enter the value again, it must be bigger than or equal to 0: '))
		# for i in range(1, n+1):		# Factorial equation to multiply from 1 to the number entered.
		# 	m = m*i
		# print('Answer:', m)


def factorial(n):
	if n == 0:
		return 1
	else:
		return n*factorial(n-1)


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
	main()