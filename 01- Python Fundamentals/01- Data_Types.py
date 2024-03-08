
# * FUNDAMENTALS OF PYTHON LANGAUGE

# Primitive Data Types:
fav_language = 'Python'  # string
multiline_string = ''' 
Python is 
the beautiful programming 
language out there
'''
net_profit = 699  # integer
GDP = 67.7  # float
is_married = False  # boolean


# type() ---> Check the data types:
print(type(GDP))  # float
print(type(is_married))  # bool
print(type(multiline_string))  # str


# Type annottion in python:
product: str = 'Book'
price: int = 690
