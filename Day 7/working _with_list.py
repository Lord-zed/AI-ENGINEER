# Method 1: Using square brackets
empty_list = []
print(empty_list)  # Output: []

# Method 2: Using the list() constructor
empty_list2 = list()
print(empty_list2)  # Output: []
# List of integers
numbers = [1, 2, 3, 4, 5]
print(numbers)  # Output: [1, 2, 3, 4, 5]
# List of strings
fruits = ["apple", "banana", "cherry"]
print(fruits)  # Output: ['apple', 'banana', 'cherry']
#fruit=[apple, mango]
#print(fruit)
# Mixed data types
mixed_list = ["Alice", 25, 5.8, True]
print(mixed_list)  # Output: ['Alice', 25, 5.8, True]
# From a string (each character becomes an element)
chars = list('hello')
print(chars)  # Output: ['h', 'e', 'l', 'l', 'o']

# Tuple
# From a tuple
my_tuple = (10, 20, 30)
list_from_tuple = list(my_tuple)
print(list_from_tuple)  # Output: [10, 20, 30]
# Range
numbers_range= list(range(5))
print(numbers_range) # output: [0, 1, 2, 3,4]

