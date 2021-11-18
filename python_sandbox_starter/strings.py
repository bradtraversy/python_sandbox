# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Askhat'
age = 37

# Concatenate
print('Hello my name is '+ name + ' i`am ' + str(age) +'.')

# String Formatting

# arguments by position
print('my name is {name} i am {age}'.format(name = name, age = age))

#F-Strings
print(f'hello, my name is {name} and i am {age}')

# String Methods
s = 'hello, world!'
print(s.capitalize())
