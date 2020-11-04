 # A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# 
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

print(person, type(person))
# get vlaue
print(person['first_name'])
print(person.get('last_name'))

# add key value
person['phone'] = '34343434'

# get dict key
print(person.keys())

# remove item

del person['age']
person.pop('phone')

# clear
# person.clear()

# legnth
print(len(person))

# list of dict
people = [
    {'name': 'niko', 'age': 5},
    {'name': 'yan', 'age': 54},
]

print(people[0]['name'])



