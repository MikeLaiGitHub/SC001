"""
File: weather_master.py
Name: Mike
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""
# This constant controls when to stop
EXIT = -100


def main():
	print("stanCode \"Weather Master 4.0!")
	data = int(input("Next Temperature: (or -100 to quit)? "))
	if data == EXIT:
		print("No temperatures were entered.")
	else:
		highest = data
		lowest = data
		sum_data = data
		count = 1				# First data entered count as 1 data collected.
		average = sum_data/count
		if data < 16:
			cold_days = 1		# Cold days will be counted under 16 degrees Celsius.
		else:
			cold_days = 0
		while True:
			data = int(input("Next Temperature: (or -100 to quit)? "))
			if data == EXIT:
				break
			elif data < lowest:
				lowest = data
			elif data > highest:
				highest = data
			if data < 16:
				cold_days += 1
			sum_data += data		# Number entered will be add up once finished the discriminating from above.
			count += 1				# Return to enter the next data make count +1.
			average = sum_data/count
		print('Highest temperature = ' + str(highest))
		print('Lowest temperature = ' + str(lowest))
		print('Average = ' + str(average))
		print(str(cold_days), 'cold day(s)')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
