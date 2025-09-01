# # TYR AND EXCEPT

# balance = 5000  # starting balance

# print("Welcome to the ATM")
# amount = input("Enter amount to withdraw: ")

# try:
#     amount = float(amount)  # convert input to number
    
#     if amount > balance:
#         raise ValueError("Insufficient funds.")
    
#     balance -= amount
#     print("Withdrawal successful. New balance: ₦", balance)

# except ValueError as e:
#     print("Error:", e)

# except Exception as e:
#     print("Unexpected error:", e)

# finally:
#     print("Transaction session closed.")

# # USSD
# def ussd_menu():
#     while True:
#         print("\n--- Welcome to My Airtime Service ---")
#         print("1. Airtime Recharge")
#         print("2. Check Balance")
#         print("3. Exit")
        
#         choice = input("Select an option: ")

#         if choice == "1":
#             recharge_airtime()
#         elif choice == "2":
#             check_balance()
#         elif choice == "3":
#             print("Thank you for using My Airtime Service. Goodbye!")
#             break
#         else:
#             print("Invalid option. Please try again.")


# # CALCULATOR
# # Simple Calculator Program

# # Function to add two numbers
# def add(a, b):
#     return a + b

# # Function to subtract second number from first
# def subtract(a, b):
#     return a - b

# # Function to multiply two numbers
# def multiply(a, b):
#     return a * b

# # Function to divide first number by second
# def divide(a, b):
#     if b != 0:
#         return a / b
#     else:
#         return "Error: Division by zero"

# # Display operation options to the user
# print("Select operation:")
# print("1. Add")
# print("2. Subtract")
# print("3. Multiply")
# print("4. Divide")

# # Take input from the user for operation choice
# choice = input("Enter choice (1/2/3/4): ")

# # Get two numbers as input from the user
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# # Perform calculation based on user's choice
# if choice == '1':
#     print("Result:", add(num1, num2))
# elif choice == '2':
#     print("Result:", subtract(num1, num2))
# elif choice == '3':
#     print("Result:", multiply(num1, num2))
# elif choice == '4':
#     print("Result:", divide(num1, num2))
# else:
#     print("Invalid choice")

# zip()
# names = ["Esther", "Precious", "Kennie"]
# scores = [85, 90, 75]
# for n, s in zip(names, scores):
#     print(n, "scored", s)

# Function with an argument - the placeholder
# def greet(name):
#     print("Hello", name, "welcome to Python learning!")

# # Calling with parameter- the actual name
# greet("Class rep")
# greet("Ridwan")

# def add(a, b):
#     return a + b

# # Function call

# result = add(4, 6)
# print("The sum is:", result)

def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    print("Sum:", total)

# function call 
# Take note of the output
add_numbers(2, 4, 6)
add_numbers(10, 20, 30, 40, 50)

def student_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)


# function call - Take note of the output
student_details(name="Peter", track = "AI Engineering", interest="Block Chain")