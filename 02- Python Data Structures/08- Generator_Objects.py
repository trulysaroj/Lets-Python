
# * Generator Expression:
# Generator expressions are similar to list comprehensions, but instead of creating a list,
# they create a generator object. Generator expressions are particularly useful
# when you want to iterate over large datasets and do not need to store the entire sequence in memory.

# sytanxc:
# (generator_expression for element in iterable)

from sys import getsizeof
num_generator = (num for num in range(10))
for value in num_generator:
    print(value)  # 0, 1, 2, 3, 4, 5, 6, 7, 8 ,9

print(num_generator)

huge_list = list(range(100))


# for getting the size of an object
print(getsizeof(num_generator))  # 192 (byte)
print(getsizeof(huge_list))  # 856 (byte)


# NOTE:- Generator expressions are more memory-efficient than list comprehensions
# because they generate values on-the-fly as needed,
# rather than creating the entire sequence in memory.


# -------------------------------------------------------------------------------
# Simple Exercise:
# Find the most repeating charact in this string
sentence = 'These unpacking operators are powerful tools in Python'
removedSpace_str = "".join(sentence.split())

repeated_char = {}

for char in removedSpace_str:
    if char in repeated_char:
        repeated_char[char] += 1
    else:
        repeated_char[char] = 1

# sroting items
sorted_repeated_char = sorted(repeated_char.items(),
                              key=lambda value: value[1],
                              reverse=True)

most_repeated_char = sorted_repeated_char[0]
print(most_repeated_char)  # ('o', 6)
