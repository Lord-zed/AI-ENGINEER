# Basic usage of print
print("Hello, world")

# using print with variables
name="Aisha"
age=25
print("Name :", name)
print("Age :", age)
print("My name is",name, "I am", age, "years old.")

# Using f-strings with print()
name= "Bola"
score=98
print(f"My name is {name} i scored {score} in my last math exam.")

# Using string concatenation
first_name="Ada"
last_name=" Beta"
print("my name is" +" "+ first_name + " "+ last_name)

# Comma vs concatenation
print("Hello", "World")      # With comma
print("Hello"+" "+"World")   # With concatenation

# Escape sequences in print - "\n", "\t"
print("line1\nline2")
print("line1\tline2")
print("He said, \"Hello\" today")
print("It\'s python!")

# Backslash
print("File path: c:\\users\\Aisha\\")

# Carriage return (\r)
print("123456\rABC")  # Output: ABC456 (replaces 123)

# Backspace (\b)
print("Helloo\b")  # Output: Hello

# Using sep and end in print
print("Python", "is", "fun", sep=" - ")
print("This is the first line.", end=" ")
print("This is the second line.")