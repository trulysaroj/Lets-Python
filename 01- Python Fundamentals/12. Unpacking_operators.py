
# * Unpacking operators:
# Unpacking operators in Python, also known as iterable unpacking or sequence unpacking, allow you
# to unpack the elements of an iterable (such as a list, tuple, or dictionary) into individual variables or elements.
# Same as JS spread(...) operators


# tuple unpack
my_tuple = (1, 2, 3)
a, *b = my_tuple
print(b)  # [2, 3]

# list unpacking
number = [*range(7)]
print(number)  # [0, 1, 2, 3, 4, 5, 6]
print([*'PYTHON'])  # ['P', 'Y', 'T', 'H', 'O', 'N']


# combining two list
list1 = [1, 2, 3,]
list2 = [2, 4, 3]

combined_list = [*list1, *list2]
print(combined_list)  # [1, 2, 3, 2, 4, 3]


# Unpacking dictionary: (**)
user1 = {"name": 'Ramesh'}
user2 = {"name": 'Ram', "ID": 2}

combined_dict = {**user1, **user2, "passion": 'Archery'}
print(combined_dict)  # {'name': 'Ram', 'ID': 2, 'passion': 'Archery'}
