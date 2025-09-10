# collecting data of a user to determine their eligibility
name = input("Enter your name: ")
age = int(input("Enter your age: "))
score = int(input("Enter your test score: "))

eligibility = (age < 18) and (score > 70)
print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}")

# The code is used to determine the eligibility of a candidate, the condition is for the candidate to be less than 18yrs and score above 70 but for the available data, the candidate is above 18 and score less than 70, since both conditions are not met the output will be false.

eligibility= (name== "Nigerian citizen") 
