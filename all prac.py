# Collecting unique visitors to an event
visitors = set()

# # Adding visitors
# visitors.add("Chinedu")
# visitors.add("Aisha")
# visitors.add("Chinedu") # Duplicate, ignored automatically
# print("Visitors:", visitors)


#dictionaries
# Task5
# print("Enter your 3 fav dishes")
# a=input("Enter first dish:")
# b=input("Enter 2nd dish: ")
# c=input("Enter 3rd dish: ")
# dish=(a,b,c)
# print(dish)
# print(f"{a}\n{b}\n{c}")

# question 2 & 3
# print("Enter your 5 best friends names")
# friend=[]
# a=input("Enter friend 1:")
# b=input("Enter friend 2:")
# c=input("Enter friend 3:")
# d=input("Enter friend 4:")
# e=input("friend 5:")
# friend.append(a)
# friend.append(b)
# friend.append(c)
# friend.append(d)
# friend.append(e)
# print(friend)
# ls_friend=tuple(friend)
# print(ls_friend)
# #print(ls_friend[::-1])
# print(ls_friend[::4])
# print(len(ls_friend))
# print("Lagos".upper() in ls_friend)

# question4
# 1. Unpacking Tuples
# person = ("John", 25, "Nigeria")
# name, age, country = person
# print(name)     # John
# print(age)      # 25
# print(country)  # Nigeria

# name=input("Enter your first name: ")
# age=input("Enter your age:")
# color=input("Enter your color:")
# town=input("Enter your home town:")


# question5
# print("Enter 3 items for your shopping list")
# a=input("Enter item 1: ")
# b=input("Enter item 2:")
# c=input("Enter item 3:")
# shoppin_list=(a,b,c)
# shopping_list=list(shoppin_list)
# d=input("Enter item 4:")
# e=input("Enter item 5:")
# shopping_list.append(d)
# shopping_list.append(e)
# print(shopping_list)
# print("|".join(shopping_list))

# question6
# 1. Using curly braces
# fruits = {"apple", "banana", "mango"}
# print(fruits)
# # 4. From a string (duplicates removed automatically)
# letters = set("mississippi")
# letters.add("green")
# print(letters)
# colors = {"red", "blue", "green"}
# removed = colors.pop()
# print("Removed:", removed)
# print("Remaining:", colors)

# Task6
# question1
# print("Enter your 5 fav names")
# #names=set()
# a=input("1st name:")
# b=input("2nd name:")
# c=input("3rd name:")
# d=input("4th name:")
# names.add(a)
# names.add(b)
# names.add(c)
# names.add(d)
# print(names)

# question2
# print("Enter your name")
# names=input("Enter your name: ")
# name_collector=set()
# while True:
#     i =range(5)
#     if i  names:
#         name_collector.add(names)
    
#     print(name_collector)
#     break




#question3
# seats=set(range(51))
# print(seats)
# for seat in seats:
#     seat=set()
#     B_seat=int(input("Enter seatnum bet 1-50:"))
#     seat.add(B_seat)
#     rem= seats - seat
#     print("Remaining seat numbers:",rem)


# question2
# names=set()
# print("Name collector")
# while True:
#     name=input("Enter your name:")
    
#     names.add(name)
#     name=input("Enter your name:")
#     names.add(name)
#     print(names)



# question4






# Dictionaries
# student= {"name": "Zack", "age": 39, "Track":"AI_Dev"}
# dim= student[]
# print(dim)

# squares= {x: x**2 for x in range(6)}
# print(squares)

# cube={x: x**3 for x in range(5) if x % 2 ==1}
# print(cube)


# students = {"Ada": 85, "John": 40, "Musa": 65}

# # Filter students who passed (score >= 50)

# passed_students = {name: score for name, score in students.items() if score >= 50}
# print(passed_students)

#details={"John": 35,"Golan":79, "Hope":80}
# #passed= {name: score for name, score in details.items() if score >= 50}

# #print(passed)
# print(details["Hope"])

#pased={x: b for x, b in details.items() if b >=50}
#print(pased)
# details["Golan"]=83
# print(details)

# Define a dictionary
#student = {"name": "Ada", "age": 20, "course": "Computer Science"}
# print(student.get("age"))
# student["age"]=32
# print(student)
# student["grade"]="A"
# print(student)

# student={}
# student["Name"]="Zacheaus"
# student["Age"]=70
# print(student)
# print(student.keys())
# print(student.values())
# print(student.items())
# student.update({"grade":"A"})
# print(student)
# student["Track"]="Dev"
# print(student)


# students = {
#     "student1": {"name": "Ada", "age": 20},
#     "student2": {"name": "John", "age": 22}
# }

# print(students["student1"]["name"])  # Access nested data

# Define a dictionary
#student = {"name": "Ada", "age": 20, "course": "Computer Science"}
# Loop through keys
# for key in student:
#     print(key)
# # Loop through values
# for value in student.values():
#     print(value)
# # Loop through key-value pairs
# for key, value in student.items():
#     print(f"{key}: {value}")
# for x in student.keys():
#     print(x)


    # Task 7
# question1
# student= {}
# a=input("Enter your name:")
# b=input("Enter your age")
# c1=input("Enter course 1:")
# c2=input("Enter course 2:")
# c3=input("Enter course 3:")
# c_total=[]
# c_total.append(c1)
# c_total.append(c2)
# c_total.append(c3)
# print(c_total)
# student["name"]=a
# student["Age"]=b
# student["Subject"]=c_total
# print(student)

# question 2

# working with control flow
# IF statement
# age = 20
# if age >= 18:
#     print("YOU ARE ELIGIBLE")
# x=10
# if x+1 >=9:
#     print("go for it")
# elif x+1 ==8:
#     print("not in it")
# else:
#     print("dont go ")
# price= 1000
# wallet=1000
# if price >wallet:
#     print("ojoro")
# elif price == wallet:
#     print("sure plug")
# else:
#     print("otilo")
# 
# Nested if
# age=19
# citizen=True
# passed= False
# if age >= 18:
#     if citizen:
#         if passed:
           
            
#            print("you can vote")
#         else:
#             print("you must pass to vote")
        
#     else:
#         print("You must be a citizen to vote")
# else:
#     print("Too young to vote")  
# # FOR loops
# fruits= ["apple", "banana", "orange"] 
# for fruit in fruits:
#     print(f"i like {fruit}") 

# word = "PYTHON"
# for x in word:
#     print(x)

# WHILE LOOP
# count=1
# while count <=5:
#     print(count)
#     count += 1

# num = 1
# while num <= 10:
#     print(num, end=" ")
    
#     num += 1

# Decrementing with `while`

# timer = 10
# while timer > 0:
#     print("Countdown:", timer)
#     timer -= 1

# While with User Input
## Keep asking until the user enters a correct password.

# password = ""
# while password != "python123":
#     password = input("Enter the password: ")

# print("Access Granted!")

# while True:
#     name =input("Enter your name or type done to exit:")
#     if name =="Done":
#         print("Good bye")
#         break
#     print("Hellow",name)
# task 5 question 3
# voter=set()
# while True:
#     print("Enter your name or type done to exit:")
#     name=input("Enter your name:")
#     if name == "done":
#         break
    
#     if name in voter:
#         print(f"{name}Already registered")
#     else:
#         voter.add(name)
#     print("succuesful registration")

# print("Number of successful registration :",len(voter))
# voters=list(voter)

# for names in voters:
#     print("weldone for completing your registration",voter)

# seat= set(range(50))
# print(seat)
# print("Book a seat number:")

# for x in seat:
#     seat_num=int(input("Enter seat number:"))
#     seat.discard(seat_num)
# print("remaing seats num",seat)
  
# for num in range(1, 10):
#     if num == 5:
#         break
#     print(num)  
# for num in range(1, 6):
#     if num == 3:
#         continue
#     print(num)   

# for num in range(6):
#     if num==3:
#         pass
#     print(num)

# for num in range(1, 6):
#     if num == 3:
#         pass   # do nothing for now
#     else:
#         print(num)

# while True:
#     age= input("Enter your age:")
#     if age.isdigit():
#         print("your age is", age)
#     else:
#         print("Inalid entry")
#         break
# for i in range(3):
#     print(i)
# try:
#     x=10%0
# except ZeroDivisionError:
#     print("Cannot divide by zero")

balance=5000
print("Welcome to atm")
amount=input("ENter amount to withdraw")
try:
    amount= float(amount)
    if amount > balance:
        raise ValueError("Insufficient funds")
    balance -= amount
    print("Withdrawal successful, new balance : N",balance)

#functions
def greet(name):
    print("Hello", name, "welcome to python")  
    