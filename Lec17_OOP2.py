class Employee:

	no_of_employees = 0
	raise_amt = 9.5

	def __init__(self, name='', age=0, salary=0):
		self.name = name
		self.age = age
		self.salary = salary
		Employee.no_of_employees += 1


	def get_salary(self):
		return self.salary


	def apply_raise(self):

		self.salary = self.salary * self.raise_amt

	# string representation of an object
	def __str__(self):

		return self.name


emp1 = Employee('Salman', 20, 10000)
emp2 = Employee('Basit', 20, 10000)

emp1.raise_amt = 12.0

emp1.apply_raise()
emp2.apply_raise()

print(emp1.get_salary())
print(emp2.get_salary())


print(emp1.__dict__)
print(emp2.__dict__)

# x = [1,2,3] # we can change the string representation of an object
# print(x)