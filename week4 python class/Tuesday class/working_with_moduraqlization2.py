# DIFFERENT WAYS TO IMPORT MODULES
#1. IMPORT THE WHOLE MODULE

# import math
# # lets put it to use
# print(math.sqrt(9))

# import an alias
# import math as m

# # lets make it to use
# print(m.sqrt(25))
# - This shortens the module name, this is common with libraries like numpy, pandas, etc

# 3. Import specific functions or variables
# from math import sqrt
# print(sqrt(36))
# print()
# - here you dont need the prefix 'math.' anymore

# 4. Import everything from the module
# from math import *
# print(sqrt(49))
# print(pi)
# - This is usually not recommended because it can cause name conflits if two modules have functions with the same name


# writing my own module
# my module/first.py
def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b != 0:
        return a/b
    else:
        return "cannot divide by zero"
    

# my_module/second.py

def greet(name):
    return f"Hello, {name}! I am creating my own module"


def reverse_string(string):
    return string[::-1]


def count_characters(string):
    return len(string)


def count_words(string):
    return len(string.split())

# my_module/main.py

import MY_MODULE.second as second
from MY_MODULE import first
# from MY_MODULE import second

# lets use the functions in the first.py file
import requests

print("=== Math Functions ===")
print("5 + 3 =", first.add(5, 3))
print("10 - 4 =", first.subtract(10, 4))
print("6 * 7 =", first.multiply(6, 7))
print("20 / 5 =", first.divide(20, 5))

# Lets us the functions in the second.py file
print("\n=== String Functions ===")
print(second.greet("Ridwan"))
print("Reverse of 'Python' =", second.reverse_string("Python"))
print("Character count in sentence =", second.count_characters("Python modules are powerful"))
print("Word count in sentence =", second.count_words("Python modules are powerful"))


# PYTHON PACKAGES
