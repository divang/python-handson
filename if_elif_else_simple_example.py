import sys
num1= int(sys.argv[1])
num2= int(sys.argv[2])

#  300 < 200 => False
if num1 == 0 or num2 == 0:
	print("Ohh! either one of the argument is zero")
elif num1 < 0 or num2 < 0:	
	print("Ohh! negative number is not allowed")
elif num1 < num2:
	print(num1)
	print(num2)
elif num1 == num2:
	print("Hey! you are supplied same numbers. Please try again!!!")
else:
	print(num2)
	print(num1)


