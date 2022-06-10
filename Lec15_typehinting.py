# type hinting
# for python it does not mean anything

# list 
# tuple
# dict
# set

import typing

print(dir(typing))


name: str = 'Basit'


def check_even(number: int) -> bool:

    if number % 2: # 0 when number is even
        return False
    else:
        return True

# (0°C × 9/5) + 32 = 32°F


check_even(15) # False / True

# x: str = 'Hello'

# def greet(name: str) -> str:

#     return f'Hello {name}' # string

