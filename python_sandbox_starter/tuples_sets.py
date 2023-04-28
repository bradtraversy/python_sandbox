# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
#  create a tuple
fruits = ('Apples', 'Oranges', 'Grapes')
fruits2 = 'Mango'

# delete
# del fruits2

print(fruits)
print(fruits2)


# A Set is a collection which is unordered and unindexed. No duplicate members.

# create a set
fruits_set = {'Apples', 'Orange', 'Mango'}
# check if in set
print('Apples' in fruits_set)
# Add to set
fruits_set.add('papaya')
print(fruits_set)
# remove
fruits_set.remove('papaya')
print(fruits_set)
# clear set
fruits_set.clear()
print(fruits_set)
