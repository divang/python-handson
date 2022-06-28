import json

person_detail_response_http_api = '{"name":"John","age":"30", "cars": {"tata":"neno","maruti":"800"}}'

json_object = json.loads(person_detail_response_http_api)

print(json_object)
print(json_object["cars"])
print(json_object["cars"]["tata"])


import random as rd
import sys

list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(list)
lottary_num=rd.choice(list)
print(lottary_num)
rd.shuffle(list)	
print(list)

# Lottary Game: Predict a number and won the game
while True:
	your_lucky_num = input("Enter your lucy number:")
	print(type(your_lucky_num), int(your_lucky_num))
	lottary_num=rd.choice(list)
	print(lottary_num)
	if int(your_lucky_num) == lottary_num:
		print("You won the lottary")
		break
	else:
		print("Try next time...")
		print("You have infinite chance to play and win ... :)")	

print("Game is over")


import math
response_times = [100,300,400,500]
min_res_time = min(response_times)
print(min_res_time)

max_res_time = max(response_times)
print(max_res_time)

abolute_value = abs(-10.998)
print(abolute_value)

power_of_10=pow(10,3)
print(power_of_10)

value_ceil = math.ceil(1.4)
print(value_ceil)

value_floor = math.floor(9.901)
print(value_floor)

import os

current_working_directory=os.getcwd()
new_folder="temp01"
folder_path=os.path.join(current_working_directory, new_folder)
print(os.path.exists(folder_path))
# Folder creation
os.mkdir(folder_path)
print(os.path.exists(folder_path))
# List of files inside above folder
print(os.listdir(folder_path)) # Empty file list

# Creating a file inside above new folder
file_absolute_path=os.path.join(folder_path, "new_file01.txt")

# Create a file and write some data
file_object=open(file_absolute_path, "a")
file_object.write("Writing to file....")
file_object.close()
print("File is created.", file_absolute_path)
print(os.listdir(folder_path)) # one file should be present
