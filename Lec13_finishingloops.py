# 1 - 100

# fizz - odd
# buzz - even

# 0 1 2 3 4
# unintended result

for i in range(5):
    if i % 2:
        print("odd", end=' ')
    else:
        print("even", end=' ')

print()

# for i in range(5):
#     if i % 2 == 0:
#         print("even",  end=' ')
#     else:
#         print("odd", end=' ')