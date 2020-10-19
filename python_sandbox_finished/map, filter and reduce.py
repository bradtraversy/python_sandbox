
from setuptools import reduce #importing reduce module for using reduce function

l1 = [2,3,4,5,6]

mapping_the_l1 = list(map(lambda x: x*2, l1)) # MAP FUNCTION APPLIES THE GIVEN COMMAND TO EVERY INDEX OF A LIST
# IN THIS CASE WE ARE MULTIPLYING EVERY CHARACTER IF LIST l1 TO 2 USING LAMBDA FUNCTION

print(mapping_the_l1)


filtering_the_l1 = list(filter(lambda x: x%2 ==0)) #FILTER FUNCTION FILTERS THE LIST ACCORDING TO OUR WISH
# IN THIS CASE WE ARE FILERING THE NUMBER WHICH IS DIVISIBLE BY 2 IN l1.

print(filtering_the_l1)

def add(x, y):
   return x+y
   
reducing_the_l1 = reduce(add, l1) # REDUCE FUNCTION IS USED FOR DOING MATHEMATICAL OPERATIONS IN A LIST
# HERE, WE ARE ADDING ALL THE CHARACTERS THE LIST l1 

print(reducing_the_l1)
