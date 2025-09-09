# # Using string concatenation
# first_name = "Ada"
# last_name = "Lovelace"
# print("full name:",first_name+" "+last_name )
# print("hello"+" "+"world")
# print("line 1\nline 2\tline 3")
# # Backspace (\b)
# print("Helloo\b")

# Task2 question2
# price=input("Enter the price of garriper paint in naira:")
# print("The price of garri is:",float(price))

# question 3
# a=input("Enter your name:")
# b=input("Enter your state of origin:")
# c=input("Enter your class:")
# print("my name is"+" "+ a +" "+"i am from"+" "+ b+" "+ "i am in"+ " "+c + "")

#question 6
# a=input("Enter your name:")
# b=int(input("Enter unit consumed:"))
# c=float(input("Cost per unit:"))
# print("     ====RECEIPT====\nCustomer's name   ||\t",a,"\nUnit consumed(KWh)||\t",b,"\nCost per unit     ||\t",c,"\nTotal bill in ngn ||\t",b*c)

# question 12
# print("====Welcome to Nigeria ussd services====")

# def ussd_code():
#     a="*123#"
#     inputs=input("Dial the ussd code:")
#     if inputs==a:
#      print("1. Check Balance\n2. Buy Airtime\n3. Buy Data")
#      choices=float(input("Enter your choice:"))
#      if choices==1:
#         choices=b="check balance"
#         print("Thank you for choosing the "+" "+b+" "+"services")
#      if choices==2:
#         choices=c="Buy Airtime"
#         print("Thank you for choosing the "+" "+c+" "+"services")
#      if choices==3:
#         choices=d="Buy Data"
#         print("Thank you for choosing the "+" "+d+" "+"services")
#     else:
#      print("Invalid code")

# while True:
#    ussd_code()

# WEEK2

# text = "Hello World"
# print(text.find("o"))   # 4
# print(text.rfind("o"))  # 7

# text = "Hello World"
# print(text.replace("World", "Me")) 
# print(text.count("o"))

# fruits = ("mango", "orange","banana")
# print(" ".join(fruits))
# print(fruits.split())
# print(fruits)
# fruits=[]
# print(fruits)

# words = ["I", "love", "Python"]
# print(" ".join(words))

# fruits="apple,banana,orange"
# print(fruits.split())

#even=[x for x in range(13) if x % 2 ==0]
#print(even)
# square=[x**2 for x in range(10)]
# print(square)

# fruits = ["apple", "banana"]
# fruits.insert(1,"Mango")
# print(fruits)
# print(fruits.count())

# names=[]
# a=input("Enter your name:")
# b=input("Enter your name:")
# c=input("Enter your name:")
# d=input("Enter your name:")
# e=input("Enter your name:")

# names=[a.lower(),b.lower(),c.lower(),d.lower(),e.lower()]
# names.sort()
# for name in names:
#     print(name)

# name=[]
# score=[]
# a=input("Enter your name:")
# b=input("Enter your name:")
# c=input("Enter your name:").
# name=[a,b,c]
# d=input("Enter youe score:")
# e=input("Enter your score:")
# f=input("Enter your score:")
# score=[d,e,f]
# for n,s in zip(name, score):
#    print(f"{n} scored {s}")

# fruits = ("apple", "banana", "cherry")
# fruits=list(fruits)
# print(fruits)

# set
# letters = set("mississippi")
# print(letters)

# numbers = set([1, 2, 3, 4])
# print(numbers)

# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# print(set1 ^ set2)
# print(set1.symmetric_difference(set2)) 

# print(set1 - set2)
# print(set1.difference(set2))

# Dictionary

# student = {
#     "name": "Ada",
#     "age": 20,
#     "course": "Computer Science"
# }
# print(student)

# student["name"]="Tobet"
# print(student)
# student.update("track","AI Dev")
# print(student)
        
# squares={x:x**2 for x in range(6) if x%2 ==0}  
# print(squares) 

#students = {"Ada": 85, "John": 40, "Musa": 65}

# Filter students who passed (score >= 50)

# passed={name:score for name,score in students.items() if score >= 50}
# print(passed)
    
student = {"name": "Ada", "age": 20, "course": "Computer Science"}    
# names = ["Ada", "John", "Musa"]
# lengths = {name: len(name) for name in names}
# print(lengths)
    
# print(student["name"])

# Using get() method (avoids error if key is missing)
# print(student["age"])
# print(student.get("age","not found"))
# print(student.get("grade"))
# print(student.get("grade", "Not Found"))
# student["Grade"]="A"
# print(student)
# print(student.keys())
# print(student.items())
# student.pop("Grade")
# print(student)

# students = {
#     "student1": {"name": "Ada", "age": 20},
#     "student2": {"name": "John", "age": 22}
# }

# print(students["student1"]["name"])

# studentt={
#     "student1":{"name":"Tada", "age":23,"Track":"AI Dev"},
#     "student2":{"name":"Tayo","age":20,"track":"AI Engr"}
# }  
# print(studentt["student2"]["age"]) 
# for value in studentt["student2"].values():
#     print(value)

# Storing a student's biodata
student = {
    "name": "Chinedu",
    "age": 19,
    "department": "Engineering",
    "subjects": ["Maths", "Physics", "Chemistry"],
    "is_full_time": True
}

print(f"Name: {student['name']}")
print(f"Subjects: {' '.join(student['subjects'])}")

