# Triple quotes (for multi-line strings)
story = '''Once upon a time,there was a coder named Ada.'''
print(story)

# slicing
word = "Python"
print(word[0:4])   # Pyth
print(word[2:])    # thon
print(word[:3])    # Pyt
print(word[::2])   # Pto
print(word[::-1])
print(word[::3])
print(word[::1])

word = "Hi! "
print(word * 3)  # Hi! Hi! Hi!
name="tems "
print(name * 3)

#membership
text="the patient dog is dead"
print("patient" in text)
print("hope" in text)


text = "Hello World"
print(text.find("H"))   # 4

# creating and manupulating string
name= "  ada balogun  "
# print(name.upper())
# print(name.lower())
# print(name.title())
# print(name.strip())
# print(name.rstrip())
# print(name.lstrip())
print(name.replace("ada", "Taiwo"))

message = "I love Java"
print(message.replace("Java", "Python"))  
# Output: I love Python

text = "Hello ABEOKUTA"
print(text.swapcase())  
# Output: hELLO abeokuta

fruits= "mango,pawpaw, apple"
print(fruits.split())

lines = "Line 1\nLine 2\nLine 3"
print(lines.splitlines())  
# Output: ['Line 1', 'Line 2', 'Line 3']

# join
word= ["I", "love","python"]
print(" ".join(word))
