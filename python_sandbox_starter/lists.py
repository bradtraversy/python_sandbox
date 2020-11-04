# A List is a collection which is ordered and changeable. Allows duplicate members.
 
#  create a list
numbers = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'grapes']

# use constructor
# numbers2 = list((1,2,3,4,5))

# print(numbers, numbers2)

# get a value
print(fruits[1])
# get length
print(len(fruits))
# append
fruits.append("mangos")
# remove
fruits.remove("apples")
# insert
fruits.insert(2, "papaya")
# Remove with pop
fruits.pop(2)
# reverse
fruits.reverse()
# sort
fruits.sort()
# reverse sort
fruits.sort(reverse=True)
# change value
fruits[0] = 'bananas'

print(fruits)