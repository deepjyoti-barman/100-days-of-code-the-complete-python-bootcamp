# Platform             : GitHub
# Course Name          : 100-days-of-code-the-complete-python-bootcamp
# Company              : Go Digit General Insurance Limited
# Author               : Deepjyoti Barman
# Designation          : QA Analyst
# Date                 : November 13 (Friday), 2020




""" Program to swap the values of two variables """

# Using a new variable
a = input('a: ')
b = input('b: ')

temp = a
a = b
b = temp

print("a = " + a)
print("b = " + b, '\n')

# -----------------------------------------------------------------------------

# Using comma operator
a = input('a: ')
b = input('b: ')

a, b = b, a

print("a = " + a)
print("b = " + b, '\n')

# -----------------------------------------------------------------------------

# The following algorithm applies only if the value stored inside the variable is a number (integer or float)
# Using arithmetic operator (+ and -)

a = int(input('a: '))
b = int(input('b: '))

a = a + b
b = a - b
a = a - b

print("a = ", a)
print("b = ", b, '\n')

# -----------------------------------------------------------------------------

# The following algorithm applies only if the value stored inside the variable is a number (integer or float)
# Using arithmetic operator (* and /)
a = float(input('a: '))
b = float(input('b: '))

a = a * b
b = a / b
a = a / b

print("a = ", a)
print("b = ", b, '\n')

# -----------------------------------------------------------------------------

# The following algorithm applies only if the value stored inside the variable is an integer number
# Using bitwise operator (^)
a = int(input('a: '))
b = int(input('b: '))

a = a ^ b
b = a ^ b
a = a ^ b

print("a = ", a)
print("b = ", b, '\n')