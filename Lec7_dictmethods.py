
months = {
    'Jan':'January',
    'Feb':'Feburary',
    'Mar':'March',
}


print(f'THIS: {type(months)}')


# DONE
# .clear()
# .get()
# .pop()
# .popitem()
# .keys()
# .values()
# .items()
# .update()




# .fromkeys()
# .setdefault

# print(months['Jan'])
# print(months.get('Jan'))

# months.clear() # clears the dictionary

# months.pop('Jan') # returns the value it pop

# popped_item = months.pop('Jan')
# print(f'POPPED: {popped_item}')

# print(f'DIRECT PRINT {months.popitem()}')
#   'fromkeys', 'setdefault', 'update'

# keys
# print(months.keys()) # returns the keys of the dictionary

# # values
# print(months.values()) # returns the values of the dictrionary


# # items
# print(months.items()) # return the items as list of tuples (key, value)

# months['Apr'] = 'New Value' # this will update because 'Apr' key exists in the dictionary
# months['Jun'] = 'June' # this will be added because 'Jun' key does not exist in the dictionary


# months.update(
#     {
#         'Jan':'March',
#         'Feb':'o',
#         'Dec':'December',
#     }
# )

print(months.get('Sep')) # it returns the value of the specified key, else it returns none if key Does not exist

print(months)

