# question 1
# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract second number from first
def subtract(a, b):
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to divide first number by second
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
while True:
    try:
    # Display operation options to the user
      print("Select operation:")
      print("1. Add")
      print("2. Subtract")
      print("3. Multiply")
      print("4. Divide")
      print("5. exit")

# Take input from the user for operation choice
      choice = input("Enter choice (1/2/3/4/5): ")
      if choice == '5':
        print("Good bye")
        break

# Get two numbers as input from the user
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))

# Perform calculation based on user's choice
      if choice == '1':
        print("Result:", add(num1, num2))
       
      elif choice == '2':
        print("Result:", subtract(num1, num2))
      elif choice == '3':
        print("Result:", multiply(num1, num2))
      elif choice == '4':
        print("Result:", divide(num1, num2))
      
        
    except ValueError :
         print("Invalid choice")




# question 2
# while True:
#     user_input = input("Enter a number (or type 'exit' to quit): ")
#     if user_input == "exit":
#         print("Goodbye!")
#         break       # break out of loop
    
#     num = int(user_input)   # convert to integer
    
#     if num % 2 == 0:
#         print("The number is Even")
#     else:
#         print("The number is odd")
    
    
    


# # Question 3
# age = (input("Enter your age (or type exit to quit): "))
# while True:
#             try:
#                     if (age) == "exit":
            
#                       print("Goodbye!")
#                       break
#                     if int(age) >= 18:
#                       print("You can vote")
#                       break
#                     else:
#                       print("You cannot vote")
#                       break
#             except ValueError():
#                print("Invalid input")
#                break
            
    
        
    
        
            
            
                
            
                
        
            
             
           
    
    
    
        
            
        
            
    