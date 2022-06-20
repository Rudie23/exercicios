
person = {'name': 'Diego', 'age': 25, 'city': 'Winter Garden'}
print(person)

print(person['name'])
print()

# Whether you want to add an element in dictionary
person['country'] = 'Brazil'
print(person)
print()

# To access the keys
print(person.keys())

# To access the values
print(person.values())
print()

# Only you can create keys using immutable data
dic = {(1, 2, 3): 'value'}
print(dic)

# You can also create a dictionary with the function <dict()>
a = dict(one=1, two=2, three=3)
print(a)
