# Importing reduce module for using reduce function
from functools import reduce 

# Higher order methods takes functions as parameters

# Create a list
l = [1,2,3,4,5]

# Map function runs a command for every index in the list
# In this case every index in the list is multiplied by 2
l_map = list(map(lambda x: x*2, l)) 

print("Showing mapped value of list, all values multiplied by 2")
print(l_map)

# filter function, filters the list based on the condition provided
# In this case only numbers divisible by 2 would remain
l_filter = list(filter(lambda x: x%2 == 0, l)) 

print("Showing filtered value of list, all values divisible by 2")
print(l_filter)

# Reduce function is used for doing mathematical operations ina list
# In this case we are adding all the numbers in the list
def add(x, y):
   return x+y

l_reduce = reduce(add, l) 
print("Showing the values of list after it has been reduced using add method")
print(l_reduce)
