
'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""
# x = 1           #int
# y = 2.5         #float
# name = "John"   #string
# is_cool = True  #bool

#multi assigment

x, y, name, is_cool = (1, 2.5, "john", True)

print("Hello")

# basic math
a = x + y

# Casting

x = str(x)
y = int(y)
z = float(y)

print(type(z), z)
