
import sys
user_citizenship_country = sys.argv[1]
# List
# Dictoinary
countries_list = ["India", "USA", "UK"]

for country in countries_list:
	if user_citizenship_country == country:
		print(country + " is my country")
	elif user_citizenship_country == "XYZ":
		print("XYZ is blacklist country")
		break
	else:
		print(country + " is not my country")

	
# Dictoinary
print("Dictionary:---")	
country_code_dict = {"India": 91, "USA":1, "UK":4}
print("India country code:")
print(country_code_dict["USA"])
# print dictionary keys

for k in country_code_dict:
	print("key:" + k)

	# fetch the value from current key
	value = country_code_dict[k]
	print(value)

for k,v in country_code_dict.items():
	print("key:" + k)
	# fetch the value from current key
	print(v)

