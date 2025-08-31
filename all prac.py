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

squares= {x: x**2 for x in range(6)}
print(squares)

cube={x: x**3 for x in range(5) if x % 2 ==0}
print(cube)