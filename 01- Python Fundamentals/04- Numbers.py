
# * Numbers in Python:

# Integers
import math
x = 10
y = -2

#  Float
a = 3.2
b = 99.99

# Complex number
p = 2 + 6j
q = -1 + 9j


# Binery Number system:
num = 0b10
print(num)  # 2

# convert to binery
print(bin(10))  # 0b1010


# Hex-deicimol numer
hex_num = 0x10a
print(hex_num)  # 266

# convert to hex-decimol
print(hex(10))  # 0xa


# ----------------------------------------------------------------------------------------------------------

# * Arithmetic operations

s = 10 + 10
s = 10 - 4
s = 10 * 10
s = 10 / 3  # 3.33
s = 10 // 3  # 3
s = 10 % 3  # 1
s = 10 ** 3  # 1000

x = x + 1
x += 1

print(s)


# ----------------------------------------------------------------------------------------------------------

# * Working wiht Numbers in python:

PI = -3.14  # Use UPPERCASE convection for constant value

# Some useful methods
print(abs(PI))  # 3.14
print(round(PI, 1))  # -3.1

num = [1, 2, 4, 7, 8]
print(max(num))  # 8
print(min(num))  # 1
print(sum(num))  # 22

print(pow(2, 5))  # 32
print(divmod(10, 3))  # Output: (3, 1) - Quotient is 3, remainder is 1
print(int(3.14))  # Output: 3
print(float("3.14"))  # Output: 3.14
print(bin(10))  # Output: '0b1010'


# Working with Math modules in Python:

# Square root
print(math.sqrt(25))  # Output: 5.0

# Trigonometric functions
print(math.sin(math.pi/2))  # Output: 1.0
print(math.cos(math.pi))    # Output: -1.0
print(math.tan(math.pi/4))  # Output: 1.0

# Exponential and logarithmic functions
print(math.exp(2))      # Output: 7.38905609893065 (e^2)
print(math.log(10))     # Output: 2.302585092994046 (natural logarithm of 10)
print(math.log10(100))  # Output: 2.0 (base-10 logarithm of 100)

# Constants
print(math.pi)    # Output: 3.141592653589793
print(math.e)     # Output: 2.718281828459045
print(math.inf)   # Output: inf (positive infinity)
print(-math.inf)  # Output: -inf (negative infinity)
