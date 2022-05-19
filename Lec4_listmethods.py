from numpy import number


numbers = [1,2,3,4,5,6]

numbers.extend('HelloWorld')


print(numbers)
print(f'Len:  {len(numbers)}')