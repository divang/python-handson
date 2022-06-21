import sys
# List examples
l=[11,22,33,44,55]
#  0 ,1 ,2 ,3 ,4

print(l)
# Update list value
l[0]=15
print(l)
# Add one more element in list at end position
l.append(66)
print(l)
l.insert(3,40)
print(l)
#[15, 22, 33, 40, 44, 55, 66]
# 0   1    2   3   4  5   6
#Remove element
l.remove(40)
print(l)
# Delete all elements 
l.clear()
print(l)

print("Output: sys.argv")
print(sys.argv)

arg_num = int(sys.argv[1])
print("Num: ", arg_num)

if arg_num in l:
	print("Your number is present")
else:
	print("Your value does not belong to list")


# Range of List indexes
print(l[1:2])
print(l[1:])
print(l[:3])

print(l)
#To get First element in List
print(l[0])
# To access second elements
print(l[1])
# To access third elements
print(l[2])
# To access Fourth elements
print(l[3])
# To access fifthe elements
print(l[4])
# Range of List indexes
print(l[1:6])
