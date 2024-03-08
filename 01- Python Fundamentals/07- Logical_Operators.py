
# Logical Operators in Python:

# AND operator:
x = 10
y = 5

if x > 0 and y > 0:
    print('Both numers are postive ...')


# OR operator:
x = 7
y = -1

if x > 0 or y > 0:
    print('At least one of numers is postive ...')


# NOT operator:
password = ' '

if not password.strip():
    print('Password filed is empty')
else:
    print('Make your password strong..')


# These operators can also be combined to form more complex conditions.
x = 8
y = 7
z = -3

if (x > 0 and y > 0) or z < 0:
    print('Either x and y are positive or y is negative')

# Note:-  not has the highest precedence, followed by and, and then or.
# However, you can use parentheses to explicitly define the order of evaluation.
