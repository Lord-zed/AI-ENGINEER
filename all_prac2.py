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


def generate(age):
    while True:
        if age >= 59:
            print("youre trying")
        elif age ==50:
            print("Almost there")
        else:
            print("good work")
            break

generate(int(input("Enter your age:")))

        
    

