
# * List Data Structue in Python: []

# list of integers[
numbers = [1, 2, 3, 4, 5]

# string list
language = ['Python', 'Go', 'Rust']

# Mixed data tyles list
mixed_list = [0, 4.2, True, 'Hello']

# Nested list
matrix_list = [[1, 2], [1, 1], [0, 9]]

# combined two list
combined_list = numbers + language
print(combined_list)  # [ 1, 2, 3, 4, 5, 'Pytohn], 'Go', 'Rust]

# creating list of fix elements
twos_list = [2] * 10
print(twos_list)  # [2, 2, 2, 2, 2, 2 ,2 ,2 ,2, 2]


# list of number range
num_list = list(range(5))
print(num_list)  # [0, 1, 2, 3, 4 ]

# list of string literals
string_list = list('Python')
print(string_list)  # ['p', 'y', 't', 'h', 'o', 'n']


# -----------------------------------------------------------------------------------------------------

# * Some useyful List methods & Properties:

# Accessing list items
lang = ['python', 'Go', 'Rust', 'TypeScript']
print(lang[0])  # Python
print(lang[-2])  # Rust
print(lang[0:2])  # ['python', 'Go']
print(lang[0:])  # ['python', 'Go', 'Rust', 'TypeScript']
print(lang[:])  # ['python', 'Go', 'Rust', 'TypeScript']

# Slicing with a step
num = list(range(10))
print(num[::2])  # [0, 2, 4, 8]
print(num[::3])  # [0, 3, 6, 9]
print(num[::-2])  # [9, 7, 5, 3, 1]
print(num[::-1])  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


# -----------------------------------------------------------------------------------------------------

# * List Unpacking and Packing:
numbers = [1, 2, 3]

# Old ways:
# num1  = numbers[0]
# num2  = numbers[1]
# num3  = numbers[2]

# unpackng list syntax
num1, num2, num3 = numbers
print(num1, num2, num3)  # 1, 2 ,3


# Destructure like feature - unpacking, and packing list:
fav_lang = ['python', 'go', 'rust', 'c++']
first, second, *rest = fav_lang
print(first)  # python
print(second)  # go
print(rest)  # ['rust' 'c++']

first, *rest, last = fav_lang
print(rest)  # ['go', 'rust]


# -----------------------------------------------------------------------------------------------------

# * Looping through List:
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)  # 1, 2, 3, 4, 5


# with  enumerate()
# built-in Python function that  loop over an iterable (like a list) while also keeping track of the index of the current item.
# It returns pairs of index and value for each element in the iterable.

languages = ['Python', 'Go', 'Rust']

for index, language in enumerate(languages):
    # Index: 0, Value: Python ... Index:2, Value: Rust
    print(f"Index: {index}, Value: {language}")


# -----------------------------------------------------------------------------------------------------

# * Adding & Deleting items in List:
languages = ['Python', 'Go', 'Rust']

# Adding
languages.append('TypeScript')  # ['Python', 'Go', 'Rust', 'TypeScript']
# ['JavaScript', 'Python', 'Go', 'Rust', 'TypeScript']
languages.insert(0, 'JavaScript')


# Removing
languages.pop(2)  # Remove - Go
languages.remove('JavaScript')  # ['Python', 'Rust', 'TypeScript']

del languages[1: 3]  # ['Python'] -- Remove Rust and TypeScript

print(languages)


# -----------------------------------------------------------------------------------------------------

# * Finding items in list:

languages = ['Python', 'Go', 'Rust', 'Go']
print(languages.index('Go'))  # 1
print(languages.count('Go'))  # 2


# -----------------------------------------------------------------------------------------------------

# * Sorting List
num_list = [4, 9, 76, 2, 10, 55]
num_list.sort()
print(num_list)  # [2, 4, 9, 10, 55, 76]

# reverse sort
num_list.sort(reverse=True)
print(num_list)  # [76, 55, 10, 9, 4, 2]


# Sorted functionm
sorted_list = sorted(num_list)
print(sorted_list)  # [2, 4, 9, 10, 55, 76]


# -----------------------------------------------------------------------------------------------------

# sort & sorted difference:
# Sort:
# - modify the original list, doesn't return new list

# Sorted:
#  - doesn't modify the original list, creare and return a new sorted list

# -----------------------------------------------------------------------------------------------------

# * Lambda functions / expressions -a small anonymous function

# syntax:
# lambda arguments: expression


# sprting list of tuples
sales_list = [
    ("product1", 370),
    ("product2", 450),
    ("product3", 250)
]


# def sort_item(item):
#     return item[1]


sales_list.sort(key=lambda item: item[1])
print(sales_list)  # [('product3', 250), ('product1', 370), ('product2', 450)]


# -----------------------------------------------------------------------------------------------------

# * Lambda - Map functions

# syntax
# map(function, iterable)

numbers = [1, 2, 3, 4, 5]
result = map(lambda x: x * 2, numbers)
print(list(result))  # Output: [2, 4, 6, 8, 10]


books = [
    ('kite Runner', 650),
    ('Pagal Basti', 450),
    ('the archer', 100)
]

# With for loop ---
# prices = []
# for item in books:
#     prices.append(item[1])

# print(prices)  # [650, 450, 100]


# With Map function:
pages = list(map(lambda item: item[1], books))
print(pages)  # [650, 450, 100]


# -----------------------------------------------------------------------------------------------------

# * Lambda - Filter function:
books = [
    ('kite Runner', 650),
    ('Pagal Basti', 450),
    ('The Archer', 100)
]

filter_list = list(filter(lambda item: item[1] >= 400, books))
print(filter_list)  # [('kite Runner', 650), ('Pagal Basti', 450)]


# -----------------------------------------------------------------------------------------------------

# * List comprehensions
#  a concise way to create lists in Python. They are a more compact and readable alternative to using traditional loops (e.g., for loops) for generating lists.


# syntax:
# [expression for item in iterable if condition]
books = [
    ('kite Runner', 650),
    ('Pagal Basti', 450),
    ('The Archer', 100)
]

book_names = [item[0] for item in books]
print(book_names)  # ['kite Runner', 'Pagal Basti', 'The Archer']


# filtering it condition:
cheak_books = [item[1] for item in books if item[1] < 200]
print(cheak_books)  # 100


# -----------------------------------------------------------------------------------------------------

# * zip() function
#  combine multiple iterables (such as lists, tuples, or strings) element-wise into tuples.

# Syntax
# zip(iterable1, iterable2, ...)

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

zip_list = list(zip(list1, list2))
print(zip_list)  # [(1, 'a'), (2, 'b'), (3, 'c')]
