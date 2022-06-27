# Try and except hands on
import sys
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
try:
	division = num1 / num2
	print(division)
except:
	#retries
	print("Divisor should not be Zero", num1, num2)
finally:
	print("I am finally block ... ")

print("It is divsion program")

animail_name = "whale"
if "tiger" == animail_name:
	print("sound like hurrrrr")
elif "cat" == animail_name:	
	print("sound like miaaaooo")
elif "whale" ==	animail_name:
	pass
elif "spark" ==	animail_name:
	print("sound like miaaaooo")
	
