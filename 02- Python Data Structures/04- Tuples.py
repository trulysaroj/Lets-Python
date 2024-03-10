

# * Tuple :
# tuple is an immutable sequence of elements.
# This means that once a tuple is created, its contents cannot be changed.
# Tuples are defined by enclosing comma-separated values within parentheses ().

num_tuple = (1, 2, 3, 4)

# accessing item from tuple
print(num_tuple[1])  # 2
print(num_tuple[-1])  # 4

# slicing tuple
print(num_tuple[1: 3])  # (2, 3)

# mixed tuple
mix_tuple = (True, 1, 'python', 3, 4)

# nested tuple
nested_tuple = ((1, 2), (3, 4), (True, False))

# concatinating tuple
combine_tuple = (1, 2) + (3, 4)
print(combine_tuple)  # (1, 2, 3, 4)


# convert any iterable to tuple
print(tuple([1, 2, 3]))  # (1, 2, 3)
print(tuple("Python"))  # ('P', 'y', 't', 'h', 'o', 'n')

# unpacking with tuple
first, second, third = (1, 2, 3)
print(first, second, third)  # 1 2 3
