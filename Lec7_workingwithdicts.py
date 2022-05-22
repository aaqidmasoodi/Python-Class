months = {
    (1,2,3):'January',
    'Feb':'January',
    'Mar':'March',
    'mar':'Mar1ch', # latest value
}


# Keys must be hasable or immutable python types

# print(months['Jan'])
# months['Jan'] = 'April' # modify values


# dict keys are unique

months[(1,2,3)] = 'April'



print(months[(1,2,3)])