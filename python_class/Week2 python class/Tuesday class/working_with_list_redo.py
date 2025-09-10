# lists=["apple", 24, True]
# print(lists)

# From a string (each character becomes an element)
# chars = ["Hello"]
# print(chars)
# charse=list("Hello")
# print(charse)

# tupulu=("apple","Mango","pawpaw")
# tupule=list(tupulu)
# print(tupule)
# print(tupule[0])

# num_range=list(range(5))
# print(num_range)

# Squares of numbers 0–4
# squares=[x**2 for x in range(5)]
# print(squares)

# cube=[x**3 for x in range(5)]
# print(cube)

# Matrix-like list
# matrix=[[1,2],[3,4],[5,6]]
# print(matrix)
# print(matrix[1])
# print(matrix[0][1])

# Characteristics of a list
# items=["rice","beans","yam","rice"]
# print(items)


# numbers=[1,2,3]
# numbers[1]=20
# print(numbers)
# numbers[2]=30
# print(numbers)

# nested_list = [[1, 2], ["a", "b"]]
# nested_list[0]=[20,30]
# print(nested_list)
# print(nested_list[1][0])
# nested_list.append([5,8])
# print(nested_list)

### LISTS METHOD
fruits=["apple","mango"]
# fruits.insert(0,"guava")
# print(fruits)

tropical=["banana","pawpaw"]
fruits.extend(tropical)
print(fruits)
fruits.remove("pawpaw")
# print(fruits)
# fruits.clear()
# print(fruits)
position=fruits.index("banana")
print(position)
print(fruits.count("mango"))
name="Ademide"
print(name.count("e"))
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)