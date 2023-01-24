"""
File: largest_digit.py
Name: Mike
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""
biggest = 0


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n:
	:return:
	"""
	global biggest
	if n < 0:
		n = -n
	if int(n % 10) == 0:
		result = biggest
		biggest = 0
		return result
	else:
		num = n % 10
		if biggest < num:
			biggest = num
		return find_largest_digit(n//10)


if __name__ == '__main__':
	main()
