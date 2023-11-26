"""
Converting a 2D list into a 1D list, called flattening the list usually requires nested loops, list comprehensions,
recursion, built-in functions, or importing libraries in Python depending on the regularity and depth of the nested
lists, the easiest of all being using imported libraries. Here is how it can be done.
"""

import itertools

a = [[1, 2], [3, 4], [5, 6]]
b = list(itertools.chain.from_iterable(a))
print(b)
