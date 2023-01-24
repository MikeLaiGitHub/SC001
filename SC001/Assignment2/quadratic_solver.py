"""
File: quadratic_solver.py
Name: Mike
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	print('stanCode Quadratic Solver!')
	while True:
		a = int(input('Enter a: '))
		b = int(input('Enter b: '))
		c = int(input('Enter c: '))  # Enter a, b, c to make a quadratic equation.
		d = b*b - 4*a*c				 # Discriminant.
		if d > 0:					 # Discriminant > 0 => 2 roots.
			root1 = (-b + math.sqrt(d)) / (2 * a)
			root2 = (-b - math.sqrt(d)) / (2 * a)
			print('Two roots: '+str(root1), ',', str(root2))
			break
		elif d == 0:				 # Discriminant = 0 => 1 root.
			root1 = (-b + math.sqrt(d)) / (2 * a)
			print('One root: '+str(root1))
			break
		else:						 # In this case is discriminant < 0, no real roots.
			print('No real roots.')
			break


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
