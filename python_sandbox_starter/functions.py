# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

# Create a function
def sayHello(name):
    print(f'Hello {name} !')

def sayHelloSam(name='Sam'):
    print(f'Hello to you to {name}')

sayHello('Nikolas')
sayHelloSam()

# return values 
def getSum(num1, num2):
    total = num1 + num2
    return total

print(getSum(3,5))


# A lambda function is a small anonymous function.  
value = lambda n1, n2: n1 + n2
print(value(2,3))
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

