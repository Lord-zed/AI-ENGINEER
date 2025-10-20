# def greet():
    
#     print('all will be well')

# greet()


# # Arguments and Parameter
# def greet(name):
#     print('all will be well',name)

# greet('Zacheaus')


# def greet(name,age):
#     print(f'my name is {name} i am {age+1} years old today ')

# greet('Zacheaus', 29)


# def greet(a, b):
#     print('The difference between ',a,'and',b,'is:\n', {a-b})
    

# greet(17,7)

# def greet(name):
#     print("Hello", name)

# # Function call
# result = greet("Esther")

# # You will notice that it did not store the name
# print("Result:", result)


# def greet(a,b):
    
#     return a+b

# result= greet(8,5)
# print('the sum of and is:',result)

# def greet(a,b):
#     return a+b

# result=greet(9,4)
# print(result)

# def count_up_to(n):
#     i=1
#     while i <=n:
#         yield i
#         i += 1

# using the generator
# for nummber in count_up_to(5):
#     print(nummber)

# def greet(name,age):
#     print(f'my name is {name} i am {age} yrs ')

# greet(age=29, name='zed')

# def introduce(name, track = "AI Engineering"):
#     print("My name is", name)
#     print("I am learning", track,".")

# introduce("Tunji Paul", track = "AI Development")

# def greet(name):
#     print('Hello',name,'welcome to growth')

# greet('zacheaus')

# def greet(name,age):
#     print(f'my name is {name} my age is {age}')

# result=greet('Zack', 27)

# def greet(a,b):
#     return a+b

# result=greet(3,6)
# print(result)

# def greet(n):
#     i=1
#     while i<n:
#         yield i
#         i +=1

# for number in greet(5):
#     print(number)

# positional argument
# def greet(name, age):
#     print(f'my age is {age} i am {name}')

# greet(27, 'Zacheaus')

# keyword argument
# def greet(name, age):
#     print(f'{name} is m name')
#     print(f'{age} is my age')

# greet(age=27, name='Zacheaus')

# default argument
# def greet(age,name='Zacheaus'):
#     print(f'{name} is m name')
#     print(f'{age} is my age')

# greet(27, name='Dayo')

# Varying length argument
def greet(*args):
    total=1
    for num in args:
        total +=num
    print( total)

greet(2,4,6)

