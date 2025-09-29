''' School Fees Breakdown
    Ask for:
        school name
        tuition fee (float)
        hostel fee (float)
        feeding fee (float)
    Calculate the total and print it in receipt format with each fee on
    a new line.
'''
school_name = input("Enter school name: ")
tuition_fee = float(input("Enter tuition fee: NGN"))
hostel_fee = float(input("Enter hostel fee: NGN"))
feeding_fee = float(input("Enter feeding fee: NGN"))

total_fee = tuition_fee + hostel_fee + feeding_fee

print ("\nSchool Fees Receipt")
print (school_name)
print (f"Tuition fee: \t{tuition_fee:,} \nHostel fee: \t{hostel_fee:,} \nFeeding Fee: \t{feeding_fee:,} \nTotal Fee: \t{total_fee:,}")