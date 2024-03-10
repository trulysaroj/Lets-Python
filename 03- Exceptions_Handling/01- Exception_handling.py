
# * exception hadling:

try:
    age = int(input('Enter you age: '))
except ValueError as error:
    print('Plz enter a valid age value ... ')
    print(error)
    print(type(error))
else:
    print('No exception were thrown ..')


# handling multiple exeptions together:
try:
    age = int(input('Enter your age: '))
    xFactor = 20/age
except (ValueError, ZeroDivisionError):  # passing multiple exception
    print('Plz enter a valid age value ...')
else:
    print('No exception were thrown ..')


# Cleaning up
# finally block (optional): The finally block is always executed whether an exception occurred or not.
# It's typically used for cleanup code that should run regardless of whether an exception occurred.

try:
    file = open('app.py')
    age = int(input('Enter your age: '))
    xFactor = 20/age
except (ValueError, ZeroDivisionError):  # passing multiple exception
    print('Plz enter a valid age value ...')
else:
    print('No exception were thrown ..')
finally:
    file.close()


# with keyword:
# with keyword will automatically clean up for close the file while on the top without inplicitly write to close.
# We can also use with multiple resources

try:
    with open('app.py') as file:
        print('File opended successfully')

    age = int(input('Enter your age: '))
    xFactor = 20/age
except (ValueError, ZeroDivisionError):  # passing multiple exception
    print('Plz enter a valid age value ...')
else:
    print('No exception were thrown ..')
# finally:
#     file.close()
