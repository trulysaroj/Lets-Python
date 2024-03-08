
# * String in Details

lang = "Python Programming"

print(len(lang))  # 18
print(lang[0])  # p
print(lang[-1])  # g
print(lang[0:6])  # python
print(lang[:6])  # python
print(lang[0:])  # Python Programming
print(lang[:])  # Python Programming


# String is immutable:
print(id(lang))  # 1865751934576
print(id(lang[5]))  # 140718370603848


# -------------------------------------------------------------------------------------------------------

# * Escape sequences:
#  Python are special character combinations that are used to represent characters that are difficult or impossible to represent directly in a string.
# These escape sequences begin with a backslash \ followed by a specific character or sequence of characters.

# Here are some common escape sequences in Python:

# \n: Newline character
# \t: Tab character
# \\: Backslash character
# \': Single quote character
# \": Double quote character
# \b: Backspace character
# \r: Carriage return character


# Examples:
print('Lets learn \nPython Language')  # Lets learn
# Python Languag
print('JavaScript \\ TypeScript')  # JavaScript \ TypeScript
print("Let\'s learn Python")  # Let's learn Python
print("""Lets learn 
Python Programming 
Language""")  # Lets learn
#   Python Programming
#   Language


# -------------------------------------------------------------------------------------------------------

# Formatted strings in Python allow you to embed expressions and variables within strings,
# making it easy to create dynamic output. Formatted strings are created using f-strings,
# which begin with the letter 'f' or 'F' before the opening quote of the string.
# Within an f-string, you can include Python expressions and variables by enclosing them in curly braces {}.


# String concatenation:
first_name = 'Elon'
last_name = 'Musk'

full_name = first_name + ' ' + last_name
print(full_name)  # Elon Musk


# Here's a simple example of a formatted string:
print(f"{first_name} {last_name} {10 * 10}")  # Elon Musk 100


# -------------------------------------------------------------------------------------------------------

# * Some useful String Methods:
greet = 'Good morning '

print(greet.upper())  # GOOD MORNING
print(greet.lower())  # good morning
print(greet.title())  # GOOD
# Good Morning (Remove white sppace also right - rstrip  left - lstrip)
print(greet.strip())
print(greet.find('Good'))  # 0
print(greet.replace('morning ', 'night'))  # Good night
print('Good' in greet)  # True
print('Good' not in greet)  # False
print(greet.split())  # ['Good' 'Morning']

arr = ['Siya', 'Ram']
print("".join(arr))  # SiyaRam
