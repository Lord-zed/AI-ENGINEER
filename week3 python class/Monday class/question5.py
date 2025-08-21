store={"Book": 15, "Pen": 9, "Bags": 10}
print(store)
item=input(" item to be purchase :").title()
Quantity=int(input("quantuty to be purchased:"))
store[item]-= Quantity
print("Before purchase", store)
print("After purchase",store)





