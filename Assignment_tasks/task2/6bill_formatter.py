''' Electricity Bill Formatter
    Ask for:
        customer's full name
        units consumed (kWh) - integer
        cost per unit - float
    calculate the total bill and print it in a neatly formatted receipt
    using escape sequences for line breaks.
'''

full_name = input("Enter full name: ")
units_consumed = int(input("Enter units consumed(kWh): "))
cost_per_unit = float(input("Cost per unit: "))

total_bill = units_consumed * cost_per_unit

print ("\nCustomer Receipt")
print (f"Customer Name: \t{full_name} \nUnits consumed: {units_consumed} \nCost/Unit: \t{cost_per_unit} \nTotal bill:\t{total_bill:,}")