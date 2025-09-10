# class Student:
#     def __init__(self,name, course, level):
#         print("creating a new student...:")
#         self.name=name
#         self.course=course
#         self.level=level
#         print(f"student{name} has been created")

# kemi= Student("kemi Adebayo", "computer science", 300) 
#         print(f"Step 1: Creating student object...")
#         self.name = name           # Step 2: Assign name to THIS object
#         self.state_of_origin = state    # Step 3: Assign state to THIS object
#         self.course = course       # Step 4: Assign course to THIS object
#         self.student_id = self.generate_id()  # Step 5: Generate ID for THIS object
#         print(f"Step 6: {self.name} from {self.state_of_origin} is ready!")
    
#     def generate_id(self):
#         import random
#         return f"UNISAIL{random.randint(1000, 9999)}"
    
class PhoneUser:
    def __init__(self, name, network):
        self.name = name
        self.network = network
        self.airtime = 0
        print(f"{self.name} joined {self.network} network")
    
    def buy_airtime(self, amount):
        self.airtime += amount  # self ensures it goes to the RIGHT person
        return f"{self.name} now has ₦{self.airtime} airtime"