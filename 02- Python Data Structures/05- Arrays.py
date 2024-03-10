
# * Arrays:

# In Python, arrays can refer to various types of data structures.
# The built-in array module provides support for arrays,
# but it's more commonly used for numeric arrays with homogeneous  data types.
# For more general-purpose arrays with mixed data types or dynamic resizing, the list type is typically used.

# importin array module
from array import array


# creating array of integers
num_array = array('i', [1, 2, 3, 4, 5])  # 'i' denotes integer

# accessing elements
print(num_array[0])  # 1

# adding element
num_array.append(6)
print(num_array)  # array('i', [1, 2, 3, 4, 5, 6])

# removing element
num_array.pop()
print(num_array)  # array('i', [1, 2, 3, 4, 5])


# NOTE: Since arrays are much more faster than list, use Array data structure only if you encounter performance issues, otherwise List is fine ... :)
