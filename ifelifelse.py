


_monday = 1
_tuesday = 2
_wednsday = 3
_thursday = 4
_friday = 5
_saturday = 6
_sunday = 7

day_week =int(input("Please enter the number of the day (1..7): "))

if day_week == _monday:
	print("Monday")
elif day_week == _tuesday:
	print("Tuesday")
elif day_week == _wednsday:
	print("Wednsday")
elif day_week == _thursday:
	print("Thursday")
elif day_week == _friday:
	print("Friday")
elif day_week == _saturday:
	print("Saturday")
elif day_week == _sunday:
	print("Sunday")
elif day_week >7 or day_week <= 0:
	print(day_week,"is not in the range 1..7.")
	print("Please re-run the program and enter a valid value.")
else:
	exit()
