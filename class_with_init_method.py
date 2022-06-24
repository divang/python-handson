# Defnition of class
class Animal:
	# property
	name = None
	food = None
	
	# Constructor
	# --- self -> first argument and it ref to this object itself 
	def __init__(self, name_of_animal, my_food):
		self.name = name_of_animal
		self.food = my_food
		print("I am constructor. I am always be called while OBJECT CREATION.")

	# FIRST ARGUMENT is ALWAYS be "SELF". name_of_animal -> self 
	def do_action(self_different_name, my_food):
		self_different_name.food = my_food

	# Method of this class
	def sound(self):
		if self.name == "cat":
			print("I sound like miyaaooo ...")
		elif self.name == "dog":
			print("I sound like bhoobhooouuu ...")
		else:
			print("I sound like ????????????? ")
			
# Create a object
i_am_cat = Animal("cat", "fish")  # self -> cat object
print(type(i_am_cat))
i_am_cat.sound()
i_am_cat.do_action("food1")
print(i_am_cat.food)

i_am_dog = Animal("dog", "bones") # self -> dog object
print(i_am_dog.name)
i_am_dog.sound()
