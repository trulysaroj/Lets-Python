

# * Dictionery in Python
# In Python, a dictionary is a built-in data type that stores a collection of key-value pairs.
# It is also known as an associative array or a hash map in other programming languages.
# Dictionaries are unordered, mutable, and dynamic.


# crating disctionery
values = {"a": 10, "b": 20}

# with dict() function
values = dict(a=20, b=40)
print(values)  # {'a': 20, 'b': 40}


# Some useful operations
values['a'] = 10  # {'a': 10, 'b': 40}
values['c'] = 70  # {'a': 10, 'b': 40, 'c': 70}
del values['a']  # {'b': 40, 'c': 70}
print(values)


# Dictionary methods
books = dict(book1=200, book2=400, book3=750)

print(books.keys())  # dict_keys(['book1', 'book2', 'book3'])
print(books.values())  # dict_values([200, 400, 750])
# dict_items([('book1', 200), ('book2', 400), ('book3', 750)])
print(books.items())


# iterating through dictionery
for key in books:
    print(key)  # book1 book2


# Alternatively, you can use the items() method for key-value pairs
for book, price in books.items():
    print(book, - price)  # book1 -200 book2 -400 book3 -750


# dictionery comprehension
# Syntax:
# {key_expression: value_expression for element in iterable}

even_num = {num * 2 for num in range(5)}
print(even_num)  # {0, 2, 4, 6, 8}

dict_number = {num: num * 3 for num in range(5)}
print(dict_number)  # {0: 0, 1: 3, 2: 6, 3: 9, 4: 12}
