# all rights reserved Radu Enachi
_wrong_wight = 0.0
_wrong_hight = 0.0


_height = float(input("Please enter your height: \n"))

if _height <_wrong_hight:
	print ("That's an invalid height.")
	exit()
_weight = float(input("Please enter your weight: \n"))

if _weight <_wrong_wight:
	print ("That's an invalid weight.")
	exit()
	
_devader = 703

_bmi =_weight* _devader /_height**2

if _bmi >= 18.5 and _bmi <= 25:
	print("BMI =", format(_bmi, ".2f"))
	print ("You are optimal.")
elif _bmi <18.5 and _bmi>=0:
	print("BMI =", format(_bmi, ".2f"))
	print ("You are underweight.")
elif _bmi >25:
	print("BMI =", format(_bmi, ".2f"))
	print ("You are overweight.")
else:
	exit()

