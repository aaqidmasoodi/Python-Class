# write a function to return the value that is passed to it

user_values = [1,6,4,2,3,7]



def get_coordinates(target_list):
    if len(target_list) != 6:
        return
    
    x = target_list[0] + target_list[1]
    y = target_list[2] + target_list[3]
    z = target_list[4] + target_list[5]


    return x, y, z



coordinates = get_coordinates(user_values)


print(coordinates)


# write a function to print numbers upto the given argument


gen_nums(10)



# print("waiting for payment...")
# i = 0

# while i < 10000:
#     i += 1
#     pass
# print("Success!")




pass # no operation


def add(num1, num2):
    pass # NA
    print("Hello")

def multiply(num1, num2):
    pass # NA







# for i in range(10):
#     pass # no Operator


# print("Hello")




# def my_func(param):
#     return param




# print(my_func("yo"))

# pass

# type hinting

# def just_a_func(my_val):
#     print("Hello 1")
#     print("Hello 2")
#     print("Hello 3")
#     print("Hello 4")
#     print("Hello 5")

#     return


# print(just_a_func(0)) # here




# names = ['Aaqid', 'Basit', 'Kaisar', 'Salman']


# def contains(string, target_list):
#     for name in target_list:
#         if name == string:
#             return True
#     return False



# print(contains('Inayat', names))


# def add(num1, num2):
#     print(num1 + num2)


# # BODMAS
# result = (add(7,8) + add(13, 54))/ add(5,6)


# print(result)


'''
    NEVER EVER, unless need, print from function.
'''