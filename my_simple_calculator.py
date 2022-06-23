# python3 my_simple_calculator.py ADD 10 20
# python3 my_simple_calculator.py SUB 100 20
import sys
calculator_instruction= sys.argv[1]
num1 = int(sys.argv[2])
num2 = int(sys.argv[3])

# defining the function
def add(x, y):
	sum =  x + y
	return sum

def sub(x, y):
	minus =  x - y
	return minus

if calculator_instruction == "ADD":
	sum = add(num1, num2)
	print("Sum is " + str(sum))
elif calculator_instruction == "SUB":
	minus = sub(num1, num2)
	print("Minus is " + str(minus)) 	