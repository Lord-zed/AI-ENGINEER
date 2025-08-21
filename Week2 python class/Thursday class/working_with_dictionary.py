# # Creating dictionaries
# # using curly braces
# student= { 
#     "name":"Ada",
#     "age": 20,
#     "course":"computer science"
#     }
# print(student)

# # 2. Using the dict() constructor
# student_info= dict(name="john", age=25, course="Maaths")
# print(student_info)

# Empty dictionary
# empty_dict={}
# print(empty_dict)
## empty_dicty=dict()
## print(empty_dicty)

# 4. Dictionary Comprehension
# create a dictionary of numbers and their squares
# squares= {x:x**2 for x in range(1,6)}
# print(squares)
# square={y:y**2 for y in range(1,5)}
# print(square)
# add={x:x**3 for x in range(1,3)}
# print(add)

# With conditions
# Dictionary of even numbers and their cubes
# evens_cube = {x: x**3 for x in range(1, 10) if x % 2 == 0}
# print(evens_cube)

# #  From Existing Dictionary
# students = {"Ada": 85, "John": 40, "Musa": 65}
# # Filter students who passed (score >= 50)
# passed_students = {name: score for name, score in students.items() if score >= 50}
# print(passed_students)

# Using String Keys

# names = ["Ada", "John", "Musa"]
# lengths = {name: len(name) for name in names}
# print(lengths)

# Accessing Dictionary Items
# Define a dictionary
# student = {"name": "Ada", "age": 20, "course": "Computer Science"}

# Using key
#print(student["name"])
# print(student["age"])
# Using get() method (avoids error if key is missing)
# print(student.get("age"))
# print(student.get("grade", "Not Found"))

# # Modifying dictionaries
# student["age"] = 21  # Change value
# student["grade"] = "A"  # Add new key-value pair
# print(student)

#Removing Items from Dictionaries
# 1.  Using pop()
# student.pop("grade")
# print(student)

 # 2. Using popitem() - removes last inserted key-value
# student.popitem()
# print(student)

 # 3. Using del keyword
# del student["course"]
# print(student)

#  # 4. Using clear() - removes all items
# student.clear()

# print(student)

#Dictionary methods
# dot keys(), dot values(), dot items(), dot update()
# person = {"name": "Emeka", "age": 30}

# # 1. keys()
# print(person.keys())

# 2. values()
# print(person.values())

# 3. items()
# print(person.items())

# 4. update()
# person.update({"age": 31, "city": "Lagos"})
# print(person)

# NESTED DICTIONARIES
# students = { 
#     "student1": {"name": "Ada", "age": 20},
#     "student2": {"name": "John", "age": 22}
# }

# print(students["student1"]["name"])  # Access nested data
# print(students["student2"]["age"]) 
## students.update({"student3": {"name": "zack", "age": 13}})
# print(students)

# LOOPING THROUGH DICTIONARIES
# Define a dictionary
student = {"name": "Ada", "age": 20, "course": "Computer Science"}
# Loop through keys
# for key in student:
#     print(key)
##print(student.keys())
##print(student.values())  

# Loop through values
# for value in student.values():
#     print(value)

# Loop through key-value pairs
for key, value in student.items():
    print(f"{key}: {value}")

    # Storing a student's biodata
student = {
    "name": "Chinedu",
    "age": 19,
    "department": "Engineering",
    "subjects": ["Maths", "Physics", "Chemistry"],
    "is_full_time": True
}

print(f"Name: {student['name']}")
print(f"Subjects: {', '.join(student['subjects'])}")
