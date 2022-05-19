my_list = [1,2,3,4,[1,5,6,7],5,7,8]

x = my_list.pop() # returns also the element it pops
x = my_list.pop() 
x = my_list.pop() 

print(len(my_list)) # 7
print(my_list) # 1234578
print(x) # [1, 5, 6 7]
print(type(x))