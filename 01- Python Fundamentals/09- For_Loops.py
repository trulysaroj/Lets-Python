
# For Loops:
# is used to iterate over a sequence (such as a list, tuple, string, or range) or any iterable object


# Syntax:
# for item in sequence:
# code block to be executed for each item


# example:
for x in 'Python':
    print(x)  # P y t h o n


# with list
for fruit in ['Apple', 'Banana', 'Avocado']:
    print(fruit)  # Apple Banana Avocado


# wiht range() function
for a in range(5):
    print(a)  # 0 1 2 3 4


# printing from specified range
for x in range(10, 15):
    print(x)  # 10 11 12 13 14


# iterating only speficid vlaue
for s in range(0, 10, 2):
    print(s)  # 0 2 4 6 8


# --------------------------------------------------------------------------------------------

# For..Else Blck:

# Syntax:
# for item in sequence:
    # code block to be executed for each item
# else:
    # code block to be executed after the loop completes normally


# simple example:
names = ['Hari', 'Ram', 'Sita']

for name in names:
    if name.startswith('R'):
        print('Name start with word R exist')
        break
else:
    print('Name start with R does not exist')
