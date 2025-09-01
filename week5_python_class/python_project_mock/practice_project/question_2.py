

# To do list application
    
tasks=[]
print("Enter five activities for the day")

a=input("Activitie 1:")
b=input("Activitie 2:")
c=input("Activitie 3:")
d=input("Activitie 4:")
e=input("Activitie 5:")
tasks.append(a)
tasks.append(b)
tasks.append(c)
tasks.append(d)
tasks.append(e)

print(tasks)
print("activity is added into tasks")
f=input("activity to remove:")
if f in tasks:
    tasks.remove(f)
    print(f, "removed in activities")
else:
    print("activities not found")
print("activity left:",tasks)


# def email_slicer():
#     print(" Email Slicer Tool ")
#     email_slicer()
#      # Accepting user inp
#     email = input("Enter your email address: ")
#     # Validate email format
#     if "@" not in email or email.count("@") != 1:
#         print("Invalid email format. Please include exactly one '@' symbol.")
#         return
#     # Split into username and domain
#     username, domain = email.split("@")
#     # 
#     if not username or not domain:
#         print("Invalid email format. Username or domain missing.")
#         return
#     # Display results (formatted output)
#     print("\n Result ")
#     print(f"Username: {username}")
#     print(f"Domain: {domain}")