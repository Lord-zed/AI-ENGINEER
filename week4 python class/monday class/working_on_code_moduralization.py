# working on built-in functions
# range
# for i in range(3):
#     print(i)

#zip()
names=["esther","precious","kennie"]
scores=[85,90,75]
for names, scores in zip(names, scores):
    print(names,"scored", scores)

# It's Ok, if don't know what lambda is  or how to use it. I will touch on it later. Just focus on  the outputs
# map()
# nums=[1,2,3,4]
# squared=list(map(lambda x: x**2, nums))
# print(squared)

# filter()
# even_nums= list(filter(lambda x: x% 2 ==0, nums))
# print(even_nums)


# Student Performance & Feedback System
# # Step 1: Input student data
# name1= input("Enter first student name: ")
# score1= int(input("Enter score for" + name1 + " : "))
# name2= input("Enter second student name: ")
# score2= int(input("Enter score for" + name2 + " : "))
# name3= input("Enter third student name:")
# score3= int(input("Enter score for"+ name3+ " : "))

# # step2: store in a list
# names= [name1,name2,name3]
# scores=[score1,score2,score3]
 
#  # step3: Display data
# print("\nstudent data:")
# for index, (n,s) in enumerate(zip(names,scores)):
#     print(f"{index + 1}. {n} - {s}")

# # step 4: Summary using built-ins
# total= sum(scores)
# average= round(total / len(scores), 2)
# highest=max(scores)
# lowest= min(scores)

# print("\nperformance Summary:")
# print("Total Score:", total)
# print("Average Score:", average)
# print("Highest Score:", highest)
# print("Lowest Score:", lowest)

# # step 5: Ranking(using sorted and zip)
# ranked = sorted(zip(scores,names), reverse=True)
# print("\nRanking:")
# for rank, (score,name) in enumerate(ranked,1):
#     print(f"{rank}.{name} - {score}")

# # step6: check data types
# print("\nData Type Checks:")
# print("Types of names:", type(names))
# print("Type of scores:", type(scores))
# print("ID of names list:", id(names))
# print("ID of scores list:", id(scores))

# # step7: filter passing students(>=50)
# passing= list(filter(lambda s: s>=50, scores))
# print("\npassing scores:", passing)

# # step8: map names to uppercase
# upper_name= list(map(lambda n: n.upper(), names))
# print("Uppercase Names:", upper_name)

# # step9: Use help() to show documentation of len
# print("\nHelp on len():")
# help(len)



# USER DEFINE----------------------------------
# Defining a function
# def greet():
#     print("Hello, welcome to AI Fellowship!")

# When you want to use a function, this is how to call it.
# And you can call it as many times as possible.
# greet()
# greet()
# greet()

#def my_sake():
#     name=input("Enter your name: ")
#     print(f"I {name} can do all thing's through christ")

# my_sake()

# Function with an argument - the placeholder
# def greet(name):
#     print("Hello", name, "welcome to Python learning!")

# # Calling with parameter- the actual name
# greet("Class rep")
# greet("Ridwan")

# def my_sake(name):    
#      print(f"I {name} can do all thing's through christ")

# my_sake("Zacheaus")
# my_sake("Taiwo")

# RETURN
#def add(a, b):
#     return a + b

# # Function call

# result = add(4, 6)
# print("The sum is:", result)

# Note the output and compare it with that of print()

# def add(a, b):
#     return a + b

# # Function call

# result=add(4, 6)
# print("The sum is:", result)

# Note the output and compare it with that of print()

# YIELD
# def count_up_to(n):
#     i = 1
#     while i <= n:
#         yield i   # pause and return i
#         i += 1

# # Using the generator
# for number in count_up_to(5):
#     print(number)

# # Note the output: Instead of giving all numbers at once, the function yields them one at a time. 

# # my practise
# def range(n):
#     i =1
#     while i <= 5:
#         yield i
#         i += 1
# # using the generator
# for num in range(5):
#     print(num)

# # POSITIONAL ARGUMENTS
# def introduce(name, track):
#     print("My name is", name)
#     print("I am learning", track, ".")

# # function call
# introduce("Ngozi", "AI Engineering")   # Correct order

# # Change the arrangment and watch the output

# introduce("AI Engineering","Ngozi")   # Incorrect order, this will throw a semantic error

# kEYWORD ARGUMENTS
# def introduce(name,track):
#     print("My name is", name)
#     print("I am learning", track)

# # function call
# introduce(name="Ngozi",track="AI Engineer")

# # change the arrangement and watch the output
# introduce(track = "AI Engineering",name = "Ngozi")

#DEFAULT ARGUMENTS
# def introduce(name, track = "AI Engineering"):
#     print("My name is", name)
#     print("I am learning", track)

#function call
#Without specifying the default argument, but watch the ouput
#introduce("Paul") 

#Specify the default argument and watch the output

#introduce("Tunji Paul", track = "AI Development")

## My practice
# def introduce(name, track):
#     print("My name is", name)
#     print("I study", track)

# introduce("Zacheaus","AI-Engineering")

# Another practice
# def introduce(name="Zacheaus", track="AI_Engineering"):
#     print("my name is", name,"i study",track)

# introduce()
# introduce("Taiwo")

## Another practice
# def add(a,b):
#     return a + b
# result= add(5, 9)
# print("My result is:", result)

# def add(a=20,d=30):
#     result= a + d
#     print("my answer is:", result)


# add()
# add(20,10)

# VARYING LENGTH
# Non keyword(tuple)
# def add_number(*args):
#     total=0
#     for num in args:
#         total += num
#     print("sum", total)

# # function call
# # Take note of the output
# add_number(2,4,6)
# add_number(10, 20, 30, 40, 50)

# ## MY PRACTICE
# def add(*args):
#     total=2
#     for num in args:
#         total += num
#     print("sum is:", total)
# add(4,6,8)

# ## PRACTISE
# def lists(*args):
    
#     for names in args:
#         print("my name is:", names)
# lists(input("Enter your name:"))

## PRACTICE
# def adds(*args):
#     std_score=int(input("Enter your standard score:"))
#     for cats in args:
#         (std_score) += cats
#     print("my total score is:", std_score)
# adds(10,20,30)


# KEYWORDS ARGUMENTS
# def student_details(**kwargs):
#     for key, value in kwargs.items():
#         print(key, ":", value)

# student_details(name="Zcheaus", track="AI_Engineer", interest="Data scientist")

def square(x):
    return x ** 2

# Lambda function
square_lambda = lambda x: x ** 2

print(square(5))         
print(square_lambda(5))  