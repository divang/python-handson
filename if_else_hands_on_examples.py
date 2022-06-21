# Supply three arguments, we have to print in sorted ascending order.
# 1 2 3
#<py file> <arg1> <arg2> <arg3>
import sys
num1= int(sys.argv[1])
num2= int(sys.argv[2])
num3= int(sys.argv[3])

print("num1:", num1)
print("num2:", num2)
print("num3:", num3)

#  300 < 200 => False
if num1 < num2:
	#  300 < 100 => False
	if num1 < num3:
		print(num1)
		#  200 < 100 => False
		if num2 < num3:
			print(num2)
			print(num3)
		else:
			print(num3)
			print(num2)
	else:
		#  200 < 100 => False
		if num2 < num3:
			print(num2)
			print(num1)
			print(num3)
		else:
			print(num3)
			print(num1)
			print(num2)

#  300 > 200 => True [This block will execute]
elif num1 > num2:
	# 200 < 100 => False
	if num2 < num3:
		print(num2) #200
		# 300 < 100 => False
		if num1 < num3:
			print(num1)
			print(num3)
		# 300 < 100 => False	
		else:
			print(num3)  #100
			print(num1)  #300
	else:
		if num1 < num3:
			print(num1)
			print(num2)
			print(num3)
		# 300 < 100 => False	
		else:
			print(num3)  #100
			print(num2)
			print(num1)  #300 		

