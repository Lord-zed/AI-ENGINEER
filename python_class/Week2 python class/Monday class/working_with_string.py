# Single quotes
name = 'Ada'
# Double quotes
greeting = "Hello"
# Triple quotes (for multi-line strings)
story = '''Once upon a time,
there was a coder named Ada.'''
# String with numbers and symbols
password = "p@ssw0rd123"
# String operation
# Indexing
word= "python"
print(word[0])
print(word[-1])
print(word[1])
print(word[2])
print(word[4])
print(word[5])
print(word[-2])
words= " that which i am "
print(words[1])
# Slicing
word = "Python"
print(word[0:4])
print(word[:5])
print(word[::2]) 
print(word[::3])
print(word[::-1])
print(word[::-2])
print(word[::1])
# string concatenation & repition
# concatenation
a = "Hello"
b = "World"
c= "It's a new day"
d= "Here"
print(a + " " + b)  # Hello World
print(a+ " " +c) 
print(a,b)
print(f" {b} {c}")
print(a+ " "+b +" "  +c+" " + d)
# Repetetion
wordy = "Hi! "
print(wordy*3)
text = "Python programming"
print("Python" in text)  
print("Java" not in text) 
print( "Hope" in text)
text1= " The choice is mine"
print("mine" in text1 )
text = "Hello World"
print(text.find("o"))   
print(text.rfind("o")) 
text = "Hello World"
print(text.index("World"))   # 6 
filename= "data.csv"
print(filename.startswith("data"))
print(filename.startswith(".csv"))  
print(filename.endswith(".csv")) 
# upper
# convert all characters in yhr tring to upper case
name= "Ade Balogun"
print(name.upper())
# Lower
# # convert all characters in yhr tring to lower case
name= "ADE BALOGUN"
print(name.lower())
# Strip
#**strip()**
# Removes whitespace (or specified characters) from both ends of the string.
text= "   Abuja "
print(text.strip())
print(text)
#**replace()**
# Replaces occurrences of a substring with another substring.
message= "I love java"
print(message.replace("java", "python"))
#**swapcase()**
#  Switches lowercase to uppercase and vice versa.
text = "Hello ABEOKUTA"
print(text.swapcase())  
# Output: hELLO abeokuta

#**lstrip()**
# Removes whitespace (or specified characters) from the left side only
text = "   Nigeria"
print(text.lstrip())  
# Output: Nigeria 

#**rstrip()**
# Removes whitespace (or specified characters) from the right side only.
text = " Nigeria   "
print(text.rstrip())  
# Output: Nigeria




