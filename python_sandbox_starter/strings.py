# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = "Nikolas"
age = 32

#concatenate
# print('Hello i am ' + name + 'I am ' + str(age))

# String Formatting

# arguments by position
# print('Mt name is {name} and i am {age}'.format(name=name, age=age))

#F-Strings (3.6+)
# print(f'Hello, my name is {name} and i am {age}')

# String Methods

s = 'hello kitty'

# capitalizy
print(s.find("e"))
