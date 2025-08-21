# Tuples using parentheses()
#fruits = ("apple", "banana", "cherry")
#print(fruits)  # ('apple', 'banana', 'cherry')

# Tuples without parenthesis()
#numbers = 1, 2, 3
#print(numbers)  # (1, 2, 3)
#fruits = "apple", "banana", "cherry"
#print(fruits)

# Single-item tuple (must include a comma)
#$single_item = ("apple",)
#print(single_item)       # ('apple',)
#print(type(single_item)) # <class 'tuple'>

# Using the tuple() constructor
#fruits_list = ["apple", "banana", "cherry"]
#fruits_tuple = tuple(fruits_list)
#print(fruits_tuple)  # ('apple', 'banana', 'cherry')

##fruits_list = ["apple", "banana", "cherry"]
##print(fruits_list)
##fruits_tuple = tuple(fruits_list)
##print(fruits_tuple)

# characteristics of Tuples
# Ordered
#colors = ("red", "green", "blue")
#print(colors[0])  # red

# Immutable
#colors[1]= "yellow"


# Allow duplicates
numbers = (1, 2, 2, 3)
print(numbers)  # (1, 2, 2, 3)

# Mixed data types
mixed = ("apple", 3, True, 5.6)
print(mixed)  # ('apple', 3, True, 5.6)

# Nested tuples
nested = (("a", "b"), (1, 2))
print(nested)  # (('a', 'b'), (1, 2))

# TUPLE OPERATION
#  Indexing

fruits = ("apple", "banana", "cherry" "grape")
print(fruits[1])   # banana
print(fruits[-1])  # cherry 

# 2. Slicing

print(fruits[0:2])   # ('apple', 'banana')
print(fruits[::-1])  # ('cherry', 'banana', 'apple')

# 3. Concatenation
tuple1 = (1, 2)
tuple2 = (3, 4)
#result = tuple1 + tuple2
#print(result)  # (1, 2, 3, 4)
##print( tuple2+   tuple2)

# 4. Repetition
nums = (1, 2)
print(nums * 3)  # (1, 2, 1, 2, 1, 2)

# 5. Membership

fruits = ("apple", "banana", "cherry", "mango")
print("banana" in fruits)  # True
print("grape" not in fruits)  # True

# 6. Iteration
for fruit in fruits:
    print(fruit)

# TUPLES METHOD
# dot count() and dot index()

numbers = (1, 2, 2, 3, 4)

print(numbers.count(2))  # 2  (counts occurrences of 2)
print(numbers.index(3))  # 3  (position of first occurrence of 3)

# Converting Between List and Tuple
# Tuple to List
t = (1, 2, 3)
lst = list(t)
lst.append(6)
print(lst)  # [1, 2, 3, 4]

# List back to Tuple
t = tuple(lst)
print(t)  # (1, 2, 3, 4

# Built in function with tuple
nums = (4, 1, 7, 3)

print(len(nums))   # 4
print(max(nums))   # 7
print(min(nums))   # 1
print(sum(nums))   # 15

