class Dog:


	def __init__(self, name, age, color, breed):
		self.name = name
		self.age = age
		self.color = color
		self.breed =breed 

	def bark(self):
		return 'Woof!'

d1 = Dog('Bruno', 2, 'white', 'german shepherd')

print(d1.bark())