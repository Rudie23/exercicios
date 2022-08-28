"""
In Python, transposing is usually implemented using a nested list (list inside a list) treating each element as a
row of the matrix. However, with the zip function, it can be achieved in a few lines.
"""

mat = [[8, 9, 10], [11, 12, 13]]
new_mat = zip(*mat)

for row in new_mat:
    print(row)
