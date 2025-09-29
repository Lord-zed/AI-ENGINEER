''' Nigerian Currency Converter
    Ask for:
        Amount in Naira (float)
        Exchange rate to US Dollars (float)
        Exchange rate to British Pounds (float)
    Convert and print results with thousands separators and currency symbols,
    neatly aligned in a table-like format using escape sequences.
'''
amount_in_naira = float(input("Enter amount in NGN: "))
exchange_rate = float(input("Input exhange rate in USD: "))
exchange_rate2 = float(input("Input exchange rate in GBP: "))

conv_to_dollar = float(amount_in_naira / exchange_rate)
conv_to_pounds = float(amount_in_naira / exchange_rate2)
print(f"Conversion of ₦{amount_in_naira:,} to USD is ${conv_to_dollar:,.2f} \nConversion of ₦{amount_in_naira:,} to GBP is £{conv_to_pounds:,.2f}")
