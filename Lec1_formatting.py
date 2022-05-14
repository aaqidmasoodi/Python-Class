name = 'Aaqid'
age = 22
marks = 2.1

'''
    How can we format our output in python.

    There are multiple ways of doing the same thing.
'''

# let's try to print thing from the about variables
# My name is Aaqid and i am 22 years old and i score 2.1%

# method 1
print("My name is", name, "and i am", age, "years old and i scored", marks, "%")

# method 2
print("My name is " + name + " and i am " + str(age) +" years old and i scored " + str(marks) + "%")

# method 3
print('My name is {} and i am {} years old and i scored {}%'.format(age, name, marks))

# method 4 
print(f'My name is {name} and i am {age} years old and i scored {marks}%')

'''
    using an f string is the best way. it is the most
    consize and clear method but only works in
    python3.6 and above.
'''