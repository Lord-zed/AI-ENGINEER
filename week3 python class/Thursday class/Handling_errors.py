# Indentation error_ incorrect spacing
# for i in range(3):
# print(i) # wrong indentation
## correct spacing will be
# for i in range(3):
#     print(i)

# b) missing colon/ parenthesis error
# if 5<3
#    print("Hello")
## correct thing will be
# if 5>3:
#    print("Hello")

# Invalid syntax- general grammar mistake
#print "Hello"

# 2) Runtime error
# zero divisioon error
# x= 10/0 

# name error- using a variable before defining it
#print(age)

# tYpe error- wrong dataq type in an operation
#result= "10" + 5
# result = 10+5
# print(result)

# value error- invalid value for a function
#number= int("abc")

# indexerror - accessing list index out of range
# fruit= ["apple", "banana"]
# print(fruit[3])

# key error- accessing a dictionary with a missing key
# data= {"name": "Ada"}
# print(data["age"])

# File not found error- file does not exit
# f= open("missing,txt") 

## HANDLING RUNTIME ERRORS
# The try block
# try:
#     x=10/2
#     print("result", x)

# try:
#     x = 10 / 2
# print("Result:", x)

## The except block
# this is a specific exception
# try:
#     x=10/0
# except ZeroDivisionError:
#     print("cannot divide by zero")

# This is a case of multiple exception

# try:
#     number = int("abc")   # ValueError
#     result = 10 / 0       # ZeroDivisionError

# except ValueError:
#     print("Invalid conversion to integer.")

# except ZeroDivisionError:
#     print(" Cannot divide by zero.")


## The finally block
# IF you don't understand this line of code now, It's Ok. But make sure you come back to it once we are done the *File Handling**.

# try:
#     f = open("sample.txt", "r")
#     content = f.read()

# except FileNotFoundError:
#     print("File not found.")

# finally:
#     print("Closing file if it was opened.")

# LEts have more example on the application of try-except-finally, but try to read in between the line for better understanding.
# balance= 5000 # starting balance
# print("welcome to the ATM")
# amount= input("Enter amount to withdraw :")
# try:
#     amount=float(amount) # convert input to number
#     if amount > balance:
#         raise ValueError("Insufficient funds .")
#     balance -=amount 
#     print("withdrawal successful. New balance: ₦", balance)
# except ValueError as e:
#     print("Error:",e)
# except Exception as e:
#     print("Unexpected error:",e)
# finally:
#     print("Transaction session closed.")


## SEMANTIC ERRORS
# wrong condition in logic
# age=18
# if age >=18:
#     print("Eligible to vote")
# else: 
#     print("Not eligible to vote")

# Wrong Formula/Computation

# length = 10
# width = 5
# area = length + width   # should be multiplication
# print("Area:", area)

# # output: 15 (expected 50)


# # Wrong Variable Usage

# marks = [70, 80, 90]
# total = marks[0] * marks[1] * marks[2]   #  wrong, should be sum
# print("Total:", total)



