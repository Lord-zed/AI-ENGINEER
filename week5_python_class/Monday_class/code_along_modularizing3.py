# class student:
#     def __init__(self,name,course,level): # This runs authomtically
#         print('creating a new student...')
#         self.name=name
#         self.course=course
#         self.level=level
#         print(f'student {name} has been created!')
#         print(f'Kemis {course} has been noted')

# Kemi=student('Kemi Adebayo', 'Comp_science', 300)


# HOW INIT AND SELF WORKS TOGETHER
# class Nigerianstudent:
#     def __init__(self,name,state, course):
#         print(f"Step 1: Creating student object...")
#         self.name=name                              # Step 2: Assign name to THIS object
#         self.state_of_origin=state                  # Step 3: Assign state to THIS object
#         self.course=course                          # Step 4: Assign course to THIS object
#         self.student_id= self.generate_id() 
#         print(f"Step 6: {self.name} from {self.state_of_origin} is ready!")        # Step 5: Generate ID for THIS object

#     def generate_id(self):
#         import random
#         return f'UNISAIL{random.randint(1000,9999)}'
    
# bio=Nigerianstudent('Zacheaus','Ogun state','AI-Engineering')
# print(bio.name)
# print(bio.generate_id())

# MORE EXAMPLE
# class phoneuser:
#     def __init__(self,name,network):
#         self.name =name
#         self.network =network
#         self.airtime =0
#         print(f'{self.name} joined {self.network} network')

#     def buy_airtie(self,amount):
#         self.airtime += amount      # self ensures it goes to the RIGHT person
#         return f'{self.name} now has ₦{self.airtime} airtime'
    

# # creating multiple users
# abeeb=phoneuser('Abeeb Bakare','MTN')
# Zacheaus =phoneuser('Zacheaus','Airtel')

# print(Zacheaus.buy_airtie(1000))
# print(abeeb.airtime)       


# Defining Attributes of a student
class Student:
    def __init__(self,name,course,level,state_of_origin):
        self.name=name
        self.course=course
        self.level=level
        self.state_of_origin=state_of_origin
        self.cgpa=self.result()

    def result(self):
        import numpy as np
        import random
        return f'cgpa is {random.randint(0, 5)}'
        #print(f'{self.name} has a cgpa of {self.cgpa}')
        
    
Zacheaus=Student('Zcheaus','AI-Engineer',300,'Ogun state')
        
print(Zacheaus.level)
print(Zacheaus.result())       
        

## TYPES OF ATTRIBUTE
#1) Instance attribute
student1 = Student("Anthony Johnson", "Engineering", 200, "Ogun")
student2 = Student("Fadilat Hassan", "Medicine", 400, "Lagos")

print(student1.name)  
print(student2.name)  

# 2) Class attribute
class student:
    university=  "Federal University of Technology Akure"  
    
    def __init__(self, name, course):
        self.name = name         
        self.course = course

print(Student.university)     
print(student1.university)   
print(student2.university) 
