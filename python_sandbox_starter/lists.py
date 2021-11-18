# A List is a collection which is ordered and changeable. Allows duplicate members.

# create list
numbers = [1, 2, 3, 4, 5, 6]
fruits = ['apples', 'oranges', 'grapes', 'pears']

#use constructor
numbers2 = list((9, 8, 7, 6, 5, 4, 3))

print(numbers, numbers2)
print(len(fruits))
print(fruits[2])

#append item to list
fruits.append('mangoes')

#insert into position of list
fruits.insert(0, 'strawberries')

# remove item from list
fruits.remove(fruits[2])
print(fruits)