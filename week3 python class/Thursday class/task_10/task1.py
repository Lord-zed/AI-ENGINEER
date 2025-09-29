# Simulated USSD Menu Interaction

# 1. When the user runs the program, display a welcome screen with a Nigerian context greeting.
menu = "*737#"
data_balance = 1000
acc_balance = 10000

print("Welcome to Guaranty Trust Bank Mobile USSD Banking")

# 2. Ask the user to dial a USSD code (e.g., *123#) and store it in a variable.
options = input("Dial *737# for option menu: ")
try :
     options = str(options)
except:
     print("Please dial the right code for options")
finally :
     print("...")
if options != menu:
     print("Please dial the right code!")

while options == menu :
    print("1. Airtime-Self")
    print("2. Airtime-Others")
    print("3. Data")
    print("4. Trsf-GTB")
    print("5. Trsf-Others")
 

    choice = int(input("Enter an option: "))

    if choice == 1:
        amount = int(input("Please enter amount: "))
        if amount < 100 or amount > 100000:
            print("You have entered a wrong amount,please enter value between 100 to 100,000 ")
        else:
            print("Processing...., you will receive an sms details soon.")
            break
    elif choice == 2:
        number = int(input("Please enter 3rd party mobile number: "))
        amount = int(input("Please enter amount: "))
        
        if amount < 100 or amount > 100000:
            print("You have entered a wrong amount,please enter value between 100 to 100,000 ")
        else:
            print("Processing...., you will receive an sms details soon.")
            break
        
    elif choice == 3:
        data = input("Enter the number to purchase data for: ")
        data_amount = input("Enter the amount of data you wish to purchase: ")
        if len(data) != 11:
            print("Number must be 11 .") 
        else :
            print("Processing...., you will receive an sms details soon.")
            break
    elif choice == 4:
        account = input("Enter the account details: ")
        # if len(account) != 10:
        #     print("Account number has to be 10 in number")
        transfer_amount = int(input("Enter the amount you wish to transfer: "))
        if acc_balance >= transfer_amount:
                acc_balance -= transfer_amount
                print(f"Transfer successful, your account balance is now {acc_balance} naira")
                break
        else:
                print("Insufficient balance")
                break

    elif choice == 5:
        account = input("Enter the account details: ")
        # if len(account) != 10:
        #     print("Account number has to be 10 in number")
        bank = input("Enter the bank: ")
        transfer_amount = int(input("Enter the amount you wish to transfer: "))
        if acc_balance >= transfer_amount:
                acc_balance -= transfer_amount
                print(f"Transfer successful, your account balance is now {acc_balance} naira")
                break
        else:
                print("Insufficient balance")
                break
        




