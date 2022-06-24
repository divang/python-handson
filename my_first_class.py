# Defining class 
class Car:
	# Color is property(nothing but a variable) of this class
	# Property
	color = None # no values

	#method
	def first_method(self):
		print("my first method in a class.")

# Creating/Instance FIRST object from above defined class
# car1 is first object
car1 = Car()
# Updating object's property
#car1.color is property of object
car1.color = "red"
# Access (get) property of a class
print(car1.color)
# calling class method -> first_method()
car1.first_method()

# Creating/Instance SECOND object from above defined class
car2 = Car()
car2.color = "blue"
print(car2.color)
car1.first_method()