def myfunc1(n):
    return len(n)


x = map(myfunc1, ('apple', 'banana', 'cherry'))
# To show the length of each item in a tuple
print(list(x))


def function(a, b):
    return a + b


y = map(function, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
# To show the sum of each item
print(list(y))


# Python program to demonstrate working
# of map.

# Return double of n
def addition(n):
    return n + n


# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

# Double all numbers using map and lambda

numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))

# Add two lists using map and lambda

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))

# List of strings
l = ['sat', 'bat', 'cat', 'mat']

# map() can listify the list of strings individually
test = list(map(list, l))
print(test)


def powers(x):
    return x ** 2, x ** 3


numbers = [1, 2, 3, 4]

show = list(map(powers, numbers))
print(show)

import math

numbers = [1, 2, 3, 4, 5, 6, 7]

show_factorial = list(map(math.factorial, numbers))
print(show_factorial)
