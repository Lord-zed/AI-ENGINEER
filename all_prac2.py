# import math
# from math import sqrt
# print(sqrt(36))
# print()
# from math import *
# print(pi)

# how to make use of zip
# names=["Esthere","Zion","Sade"]
# score=[75,30,90]
# for n,s in zip(names, score):
#  print(n, "scored", s)

# names=["Zacheaus","Joy","YK"]
# score=[70,78,90]
# subject=["Math","ENG","PYTHON"]
# for n,s, su in zip(names, score, subject):
#     print(f"{n} scored{s} in {su}")

# def name(name):
#     print("I can be all i want to be ",name)

# name(input("Enter your name:"))

# def add(a, b):
#     return a+b
# result= add(4,6)
# print("The result gives: ",result)


# def generate(age):
#     while True:
#         if age >= 59:
#             print("youre trying")
#         elif age ==50:
#             print("Almost there")
#         else:
#             print("good work")
#             break

# generate(int(input("Enter your age:")))

# practicing nested if statement
# def prac(name,age,citizen,pas):
#     if age >=18:
#         if citizen == "Yes":
#             if pas=="Yes":
#                  print("you are eligible to vote")
#             else:
#                 print("You are not eligible to vote ")
#         else:
#             print("You have to be a citizen")
#     else:
#         print("Too young to vote")
#         name

# name=input("Enter your name:")    
# age=int(input("Enter you age:"))
# citizen=[input("Are you a citizen(Answer: Yes or No ):")]
# pas=[input("Did you 200 above in your jamb(Answer: Yes or No ):")]
# prac(name,age,citizen,pas)
# a=[str(age)]
# c=list(citizen)
# p=list(pas)
# n=[name]

# for n,a,c,p in zip(n,a,c,p):
#     print(f"{n} aged {a} in {c} but {p}")

# Understanding while
# count=""
# while count!="Safe":
#     count=input("Enter the missing word:",).title()
# print("Access granted")
    
# Understanding while True
while True:
    name=input("Enter your name:")
    if name=="exit":
        print("Done")
        break
    print(f"Hello, {name}")

  
