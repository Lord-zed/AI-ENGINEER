#name orgniser
name=input("Enter 5 names seperated by commas:")
name_lower=name.lower()
print(name_lower)
name_split=name_lower.split()
print(name_split)
name_split.sort()
print(name_split)
print(f"\n{name_split}")



