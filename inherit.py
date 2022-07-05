class Animal:
	def __init__(self, no_of_legs=4, color='white', age = 1, eye_color='black'):
		self.no_of_legs = no_of_legs
		self.color = color
		self.age = age
		self.eye_color = eye_color


	def run(self):
		print('Animal is running!')

	def walk(self):
		print('Animal is running!')

	def sleep(self):
		print('Animal is sleeping!')

# method override
# method overloading
# most important for Django because everything in django is class
class Cat(Animal):

	# this is 100% correct
	def __init__(self, no_of_legs=4, color='white', age = 1, eye_color='black', has_fur=False):
		# super() always referes to the parent class
		super().__init__(no_of_legs, color, age, eye_color)
		self.has_fur = has_fur

	def run(self):
		print('Cat is running!')

	
	def meow(self):
		print('cat is meowing!')


c1 = Cat(color='brown')

c1.walk() # MRO

print(c1.__dict__)
#
# Animal is running!

# inheritance is possible

print(help(Cat))