# # Comperison operators
# b = 20
# a = 10
# print(a == b)   # False
# print(a==b)
# print(a!=b)
# print(a>b)
# print(a<b)
# print(a >= 10)  # True
# print(b <= 25)  # True

# # Use case example - Student Exam Result
# Score=75
# print(Score>=50)
# print(Score<50)
# print(Score==100)

# ASSIGNMENT OPERATIONS

x= 10
# print("Initial value",x)
# x+=5
# print("After x += 5", x)
# x-=2
# print(x)
# x*=3
# print(x)
# x/=4
# print(x)
# x%=3
# print(x)
x=16
# x**=3
# # print(x)

# x//=3
# print(x)

# Use case example
# # define variables
# balance= 1000
# deposit=200
# withdraw=150

# balance+=deposit
# print(balance)
# balance-=deposit
# print(balance)

#Logical operators
x=10
y=20

# and operator
# print(x>5 and y>15)

# or operator
# print(x<5 or y>15)

# Not operator
# print(not(x==20))
 # Use case example1 - scholarship Eligibility
 #Define variables
age= 17
score= 85

# Must be younger than 18 and score above 80
eligible= (age<18) and (score>80)
print(eligible)

# `Use case example2 - Event Access
age = 22
has_ticket = False

can_enter = (age >= 18) and (has_ticket or age < 25)

print("Access Granted:", can_enter)  
# Output: Access Granted: True (because age < 25 even without ticket)
