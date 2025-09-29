''' Daily Market Report
    Market name
    Number of traders
    Daily revenue
    Display the result using f-string formatting with commas for thousands
    separator.
'''

market_name = input("Input market name: ")
no_of_traders = int(input("Number of traders: "))
daily_revenue = float(input("Input daily revenue: "))

print (f"Name of market is {market_name} and there are {no_of_traders} traders, and the daily revenue is {daily_revenue:,}")