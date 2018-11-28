# If/ Else conditions are used to decide to do something based on something being true or false

x = 21
y = 20

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

# Simple if
if x > y:
  print(f'{x} is greater than {y}')

# If/else
if x > y:
  print(f'{x} is greater than {y}')
else:
  print(f'{y} is greater than {x}')  

# elif
if x > y:
  print(f'{x} is greater than {y}')
elif x == y:
  print(f'{x} is equal to {y}')  
else:
  print(f'{y} is greater than {x}')  

# Nested if
if x > 2:
  if x <= 10:
    print(f'{x} is greater than 2 and less than or equal to 10')
    

# Logical operators (and, or, not) - Used to combine conditional statements

# and
if x > 2 and x <= 10:
    print(f'{x} is greater than 2 and less than or equal to 10')

# or
if x > 2 or x <= 10:
    print(f'{x} is greater than 2 or less than or equal to 10')

# not
if not(x == y):
  print(f'{x} is not equal to {y}')


# Membership Operators (not, not in) - Membership operators are used to test if a sequence is presented in an object

numbers = [1,2,3,4,5]

#  in
if x in numbers:
  print(x in numbers)

# not in
if x not in numbers:
  print(x not in numbers)

# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# is
if x is y:
  print(x is y)

# is not
if x is not y:
  print(x is not y)