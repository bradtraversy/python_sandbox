# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Brad'
age = 37

# Concatenate
# print('Hello, my name is ' + name + ' and I am ' + str(age))

# String Formatting

# Arguments by Position
# print('My name is {name} and I am {age}'.format(name=name, age=age))

# F-Strings (3.6+)
# print(f'Hello, my name is {name} and I am {age}')

# String Methods

s = 'hello world'

# Capitalize string (capitalizes first letter (Hello))
print(s.capitalize())

# Make all uppercase
print(s.upper())

# Make all lowercase
print(s.lower())

# Swap case
print(s.swapcase())

# Get length
print(len(s))

# Replace
print(s.replace('world', 'everyone'))

# Count
sub = 'h'
print(s.count(sub))

# Starts with
print(s.startswith('hello'))  # returns True

# Ends with
print(s.endswith('e'))

# Split into a list
print(s.split())

# Find position
print(s.find('r'))

# Is all alphanumeric
print(s.isalnum())

# Is all numeric
print(s.isnumeric())

print(s.isalpha())
# 3 above return False because of the space
