i=1
num=1
while 10:
	print(num)
	num = num + 1
	if num == 10:
		break
print("We come out from loop 1")	

num=1
while num <= 10:
	print(num)
	num = num + 1
	#i = i + 1
print("We come out from loop 2")	

# Only Even number
print("Only even numbers")	
num=0
while num <= 10:
	num = num + 1
	if num % 2 == 0:
		print(num)	

# Only Odd number
print("Only edd numbers")	
num=0
while num < 10:
	num = num + 1
	if num % 2 == 0:
		continue
	print(num)	


# List
# Dictoinary
print("List:---")	
countries_list = ["India", "USA", "UK"]

for x in countries_list:
	if "India" == x:
		print("India is my country")
	else:	
		print("Other Country is "+x)

# Dictoinary
print("Dictionary:---")	
country_code_dict = {"India": 91, "USA":1, "UK":4}

# print dictionary keys
for k in country_code_dict:
	print(k)

# print dictionary keys
for v in country_code_dict.values():
	print(v)

# print dictionary keys
for k,v in country_code_dict.items():
	print(k,v)

