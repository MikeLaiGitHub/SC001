"""
File: prime_checker.py
Name: Mike
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
	print('Welcome to the prime checker!')
	while True:
		n = int(input('n: '))
		number = 2
		if n == EXIT:
			print('Have a good one!')
			break
		elif n == 1:
			print('1 is not a prime number.')
		else:
			while number < n:
				if n % number == 0:			# If n has any factors besides itself, it's not a prime number.
					print(str(n), 'is not a prime number.')
					break
				number += 1					# Keep looking for if there is any factor to make n % number = 0.
			if n == number:					# If n has no factors besides itself and 1, it's a prime number.
				print(str(n), 'is a prime number.')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
