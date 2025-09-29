# Admission Process

name = input("Enter your name: ")
age = int(input("Enter your age: "))










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
 school = input("Enter your school: ").title()
 UTME = int(input("Enter your UTME score: "))
 Post_Utme = int(input("Enter your post utme score: "))

 Eligibility =  (distinctions >= 5) and (UTME > 200) and (Post_Utme > 200) and (age >= 16)

 print(f"------- Student Eligibility Status -------\nCandidate: {name}\nAge: {age}\nSchool: {school}\nTotal distinctions(A or B) in WAEC/WASSCE: {distinctions}\nEligible: {Eligibility}")
 if Eligibility == True:
        print("Congratulations, you are eligible for admission")
 else:
        print("Sorry! You do not meet the requirements to be eligible for admission ")