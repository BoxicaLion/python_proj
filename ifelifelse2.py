# all rights reserved Radu Enachi


_one = 1
_two = 2
_three = 3
_four = 4
_five = 5
_six = 6
_seven = 7
_eight = 8
_nine = 9
_ten = 10

roman_number =int(input("Please enter a number 1..10: "))

if roman_number == _one:
	print("\nThe roman numeral for", _one, "is I.")
elif roman_number == _two:
	print("\nThe roman numeral for", _two, "is II.")
elif roman_number == _three:
	print("\nThe roman numeral for", _three, "is III.")
elif roman_number == _four:
	print("\nThe roman numeral for", _four, "is IV.")
elif roman_number == _five:
	print("\nThe roman numeral for", _five, "is V.")
elif roman_number == _six:
	print("\nThe roman numeral for", _six, "is VI.")
elif roman_number == _seven:
	print("\nThe roman numeral for", _seven, "is VII.")
elif roman_number == _eight:
	print("\nThe roman numeral for", _eight, "is VIII.")
elif roman_number == _nine:
	print("\nThe roman numeral for", _nine, "is IX.")
elif roman_number == _ten:
	print("\nThe roman numeral for", _ten, "is X.")
elif roman_number >10 or roman_number <= 0:
	print("\nThat's not a valid number.")
else:
	exit()