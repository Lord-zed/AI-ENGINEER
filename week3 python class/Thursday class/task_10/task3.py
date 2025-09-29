# Task 3

# 1. Comment the code below appropriately, and using doctring, explain what the code is doing.

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# score = int(input("Enter your test score: "))

# eligibility = (age < 18) and (score > 70)
# print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}")


"""The code is asking user for name,age,and score. For the user to be eligible , age must be less than 18 and score must be more than 70. Then print the output."""



# Adapt the code to the case below.

# Federal Government Scholarship Key Eligibilty Requirements.
try:
 name = input("Enter your name: ")
 age = int(input("Enter your age: "))

except:
    print("Try again!")

finally:
    print("Fill the information below to access your scholarship status!")












# List of subjects
subjects = [
    "Mathematics", "English", "Physics", "Chemistry",
    "Further_Maths", "Yoruba", "Biology", "Geography", "Economics"
]

grades = {}


for subject in subjects:
    grade = input(f"Enter your grade for {subject}: ").strip().upper()
    grades[subject] = grade

distinctions = sum(1 for grade in grades.values() if grade in ("A", "B"))

if distinctions < 5:
    print("You need at least 5 distinctions(A or B).")
else:
 Enrollment = input("Are you a registered, full-time undergraduate student in a recognized Nigerian University(yes or no): ").lower()
 school = input("Enter your University: ").title()
 citizenship = input("Enter your citizenship: ").title()
 scholarship_status = input("Are you currently receiving any other scholarship from an entity in the Oil and Gas industry,whether national or international(yes or no): ")

 Eligibility = (Enrollment == "yes") and (citizenship == "Nigeria" or citizenship =="Nigerian") and (scholarship_status == "no") and distinctions >= 5

 print(f"------- Student Eligibility Status -------\nCandidate: {name}\nAge: {age}\nSchool: {school}\nTotal distinctions(A or B) in WAEC/WASSCE: {distinctions}\nEligible: {Eligibility}")
 if Eligibility == True:
        print("Congratulations, you are eligible for the Federal Government Scholarship")
 else:
        print("Sorry! You do not meet the requirements to be eligible for the scholarship ")