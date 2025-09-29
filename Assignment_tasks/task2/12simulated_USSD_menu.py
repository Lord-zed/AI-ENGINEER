''' Simulated USSD Menu Interaction
    You are to design a mock USSD interface for a mobile services.
    Requirements:
        1. when the user runs the program, display a welcome screen with
        a Nigerian context greeting.
        2. ask the user to "dial" a USSD code (e.g., *123#) and store it in 
        a variable.
        3. print a menu with at least 3 options (e.g., "Check Balance", 
        "Buy Airtime", "Buy Data") using newline escape squences (\n) for
        formatting.
        4. ask the user to choose an option (1, 2, or 3) and store their 
        choice in a variable.
        5. use f-strings and/or concatenation to display a confirmation
        message showing the selected option.
        6. ask for an amount (if applicable) and store it as a 
        number using type casting.
        7. display a final message summarizing the transaction.
'''
print ("Welcome to Airmon USSD Service")
code = input("Dial USSD code (e.g., *123#): ")
print ("Please choose an option:\n1. Buy Airtime \n2. Buy Data \n3. Check Data \n4. Manage Services")
option = int(input("Enter choice 1-4: "))
print (f"You selected option {option}")
amount = float(input("Enter amount: "))
print (f"\nYou dialled {code} for service {option} and the amount N{amount}")
print ("Thank you for using our service.")
