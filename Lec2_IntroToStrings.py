'''
    String in python
'''

# how to make a string
# use a single qoutes or double qoutes to make a string literal

# example
my_str = str() # string constructor
my_str = '' # len() -> 0
my_str = 'Hello World'


# type hinting
# type annonating

name: str = 'Hello World' # valid syntax


# hello world is a string

'''
    String objects have many methods associated with them
    Methods:
        capitalize() - Converts the first character to upper case
        casefold() - Converts string into lower case
        center() - Returns a centered string
        count() - Returns the number of times a specified value occurs in a string
        encode() - Returns an encoded version of the string
        endswith() - Returns true if the string ends with the specified value
        expandtabs() - Sets the tab size of the string
        find() - Searches the string for a specified value and returns the position of where it was found
        format() - Formats specified values in a string
        format_map() - Formats specified values in a string
        index() - Searches the string for a specified value and returns the position of where it was found
        isalnum() - Returns True if all characters in the string are alphanumeric
        isalpha() - Returns True if all characters in the string are in the alphabet
        isascii() - Returns True if all characters in the string are ascii characters
        isdecimal() - Returns True if all characters in the string are decimals
        isdigit() - Returns True if all characters in the string are digits
        isidentifier() - Returns True if the string is an identifier
        islower() - Returns True if all characters in the string are lower case
        isnumeric() - Returns True if all characters in the string are numeric
        isprintable() - Returns True if all characters in the string are printable
        isspace() - Returns True if all characters in the string are whitespaces
        istitle() - Returns True if the string follows the rules of a title 
        isupper() - Returns True if all characters in the string are upper case
        join() - Converts the elements of an iterable into a string
        ljust() - Returns a left justified version of the string
        lower() - Converts a string into lower case
        lstrip() - Returns a left trim version of the string
        maketrans() - Returns a translation table to be used in translations
        partition() - Returns a tuple where the string is parted into three parts
        replace() - Returns a string where a specified value is replaced with a specified value
        rfind() - Searches the string for a specified value and returns the last position of where it was found
        rindex() - Searches the string for a specified value and returns the last position of where it was found
        rjust() - Returns a right justified version of the string
        rpartition() - Returns a tuple where the string is parted into three parts
        rsplit() - Splits the string at the specified separator, and returns a list
        rstrip() - Returns a right trim version of the string
        split() - Splits the string at the specified separator, and returns a list
        splitlines() - Splits the string at line breaks and returns a list
        startswith() - Returns true if the string starts with the specified value
        strip() - Returns a trimmed version of the string
        swapcase() - Swaps cases, lower case becomes upper case and vice versa
        title() - Converts the first character of each word to upper case
        translate() - Returns a translated string
        upper() - Converts a string into upper case
        zfill() - Fills the string with a specified number of 0 values at the beginning

        # 52 total

'''

# Examples on how to use them


name = 'Aaqid'
name = 5
print(name.count('A'))
# output: AAQID

'''
    we use the dot syntax to access a method in python.
    most STRING methods return a new string back.
'''

# other examples

first_name = 'aaqid'
print(first_name.capitalize())
# output: Aaqid

first_name = 'Aaqid'
print(first_name.lower())
# output: aaqid

print(first_name.index('q'))
# output: 2


print('Hello {}'.format('World'))
# output: Hello World


'''
    Strings in python are indexed collections,
    therefore we can use an indexer with them
'''


# STRING: 'Hello'
# INDEX:   01234

# Example
first_name = 'Aaqid'
last_name = 'Masoodi'


print(first_name[0])
# output: A
# because 'A' is at index 0 in the first_name

print(first_name[2])
print(first_name[-1])
print(first_name[-3])

'''
output:
    q
    d
    q
'''

'''
    not only can we specify one number in the indexer
    but we can also specify a range

    1) start:end
    2) start:end:step
'''

print(first_name[0:3])
# this will start from index 0 and go all the way upto
# but no including the index 3
# output: Aaq

print(last_name[0:]) # starts from 0 to end

print(last_name[:2]) # start from beginning upto but not including 2

print(last_name[:]) # print everything

'''
    nagative indicies can also be specified
'''

print(last_name[-4:-1])
print(last_name[1:-1])


'''
    you can optionally also pass a step
'''

print(last_name[0:6:2]) # this will move forward 2 units each time

'''
    A positive step indicate forward movement
    >>>>>>>>

    A negative step indicates backward movement
    <<<<<<<<

    the default value of step is 1
'''

last_name = 'Helloworld'
print(last_name[-1:-4:-1])
# start from -1 and go back upto by not including -4.


'''
    string objects do not need to be in a variable to use
    the indexer. you can use the indexer directly on a string
    literal.
'''

# Example
print('Salman'[0:2]) 

last_letter = 'Salman'[-1] # what is only obj[-1]?
print(last_letter)


'''
    String objects can also be concatenated using '+'
'''

full_name = first_name + last_name
print(full_name)

print(f'reverse: {full_name[-1::-1]}')


# guess the output
str_1 = 'DXVK'
str_2 = 'VULCAN'

print(f'HELLO {str_1[:]} - {str_2[:4]}')

new_str = str_1[0] + str_2[:2] + '!'

print(new_str)

