my_list = [1,2,3]

print(id(my_list))

my_list2 = my_list # there are no "TWO" lists. it is single pointed at by two difference referencess

xyz = my_list

print(f'ID list1: {id(my_list)}')
print(f'ID list2: {id(my_list2)}')

xyz.clear()


print(my_list)
print(my_list2)


# # nested lists
# # lists can have multiple types at the same time in a single list

# mylist = [['yo',2,3], [4,'yo',6], [7,8,'yo']]


# # write three print statement to extract the three yos outta the list

# # Syntax Error


# print(mylist)

