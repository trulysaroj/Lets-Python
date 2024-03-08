
# Functions in python

# defining function
def greet():
    print('Namaste, How are you ? ')


greet()


# with parameters
def greet_guest(first_name, last_name):
    print(f"Namaste, {first_name} {last_name}")


greet_guest('Hari', 'Bahadur')  # Namaste, Hari Bahadur


# with return values:
def add_num(a, b):
    return a + b


result = add_num(4, 7)
print(result)  # 11


# Python, keyword arguments (also known as named arguments)
def increment_num(number, by):
    return number + by


cals = increment_num(number=19, by=19)
print(cals)  #


# default values for arguments:
def incrment_num_by_two(num, by=2):
    return num + by


print(incrment_num_by_two(5))  # 7


# -----------------------------------------------------------------------------------------------------------------


# * Multiple arguments :
# (*args)  allows the my_function to accept any number of positional arguments.
# Inside the function, args is treated as a tuple containing all the positional arguments passed to the function.


# example:
def addition(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total


print(addition(2, 5, 7, 5, 4))  # 23


# (**kwargs) to accept an arbitrary number of keyword arguments:
def save_user(**data):
    print(data['name'])


save_user(name='Alice', age=19, id=2)  # Alice


# Scope of the Function
globale_var = "I am global.."  # avaid using gloabl as much as possible


def my_function():
    local_var = 'I am local variable ...'
    print(local_var)


# -----------------------------------------------------------------------------------------------------------------


# Simple FizzBuzz Exercie:

# Rules --->
# 1) if num devisible by 3 = Fizz
# 2) if num devisible by 5 = Buzz
# 3) If num devisible by both 3 & b = FizzBuzz
# 4) Else if num itself

def fizz_buzz(num):
    if (num % 3 == 0) and (num % 5 == 0):
        return 'FizzBuzz ...'
    if num % 3 == 0:
        return 'Fizz'
    if num % 5 == 0:
        return 'Buzz'

    return num


print(fizz_buzz(60))
