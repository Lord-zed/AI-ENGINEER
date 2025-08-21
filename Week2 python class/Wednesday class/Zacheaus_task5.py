# # Task1
# #print("Enter your 3 favorite dish")
# #a= input( "1st dish : " )
# b= input("2nd dish   ")
# c=input("3rd dish   ")
# Dish= (a, b, c)
# Dishes=tuple(Dish)
# print(Dishes)
# print(f"{a}\n{b}\n{c}")

# # Task2
# print("Your 5 best friends names")
# a=input("1st friend :")
# b=input("2nd friend :")
# c=input("3rd friend :")
# d=input("4th friend :")
# e=input("5th friend :")
# friend=(a,b,c,d,e)
# tuple_friend=tuple(friend)
# print(tuple_friend)
# print(tuple_friend[::-1])

# #Task3
# print("Enter names of 5 Nigeria state")
# a=input("1st state :")
# b=input("2nd state :")
# c=input("3rd state :")
# d=input("4th state :")
# e=input("5th state :")
# tuple_state=(a,b,c,d,e)
# print(tuple_state[0:5])
# print( "Lagos" in tuple_state)
# print(len(tuple_state))

#Task4
# print( "Enter user info")

# a=input( "First name:"),
# b=input("       Age:"), 
# c=input("favr color:"), 
# d=input(" Home town:")
# user_info=(a,b,c,d)
# tuple_user_info=tuple(user_info)
# print(tuple_user_info)
# print(f"{a}\n{b}\n{c}\n{d}")

# Task5
print("Enter 3 items for your shopping list")
a=input("Item_1 :")
b=input("Item_2 :")
c=input("Item_3 :")
g=(a,b,c)
shopping_list=tuple(g)

ls_shopping_list=list(shopping_list)
d=input("Item_4 :")
e=input("Item_5 :")
f=(d,e)
ls_shopping_list.append(e)
ls_shopping_list.append(d)
print(ls_shopping_list)
convert=tuple(ls_shopping_list)
print(convert)




