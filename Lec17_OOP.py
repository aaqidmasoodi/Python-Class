# OOP
class Dog:
	# this idea is fundamental
	def __init__(self, name, age): # constructor
		self.name = name
		self.age = age
		

	def bark(self):
		print(f'{self.name} is barking')

	# make a method that returns a string name-age
	# get_info

#      create an object
dog1 = Dog('Bruno', 4) # constructor

dog2 = Dog('Carl', 0)

dog3 = Dog('Jones', 3)


dog1.bark()

dog2.bark()

dog3.bark()

# create the objects
# passes the addres of the newly created object to __init__
# also returns the address of the newly created object


# Make a class Employee:
	# initialze the class with 
	name
	age
	emp_code

	# methods
		get_name - gets the name of the Employee
		set_name - set new name for the employee

		get_age - gets the age of the Employee
		set_age - set new age for the employee

		get_emp_code - gets the emp_code of the Employee
		set_emp_code - set new emp_code for the employee


		can_drink
			returns age > 18


