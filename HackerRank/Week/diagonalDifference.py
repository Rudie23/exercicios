"""
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix  is shown below:

1 2 3
4 5 6
9 8 9
The left-to-right diagonal = 1 + 5 + 9 = 15 . The right to left diagonal = 3 + 5 + 9 = 17 .
Their absolute difference is |15 - 17| = 2.
"""
lista = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(lista[0][2])

i, j = 0, 0

print()
print('Diagonal')
while i < len(lista):
    print(lista[i][j])
    i = i + 1
    j = j + 1

print()
print('Diagonal reversa')

while i < len(lista):
    print(lista[i][j])
    i = i + 1
    j = j - 1

print()
print("The difference between the diagonals")


def diagonalDifference(arr):
    leftSum, rightSum = 0, 0

    i, j = 0, 0

    while i < len(arr):
        leftSum += arr[i][j]
        i += 1
        j += 1

    i, j = 0, len(arr) - 1

    while i < len(arr):
        rightSum += arr[i][j]
        i += 1
        j -= 1

    print(leftSum, rightSum)
    print()
    print("The absolute value between diagonal difference")
    return abs(leftSum - rightSum)


print(diagonalDifference(lista))
print()


def diagonal(arr):
    left, right = 0, 0
    for i in range(len(arr)):
        left += arr[i][i]
        right += arr[i][len(arr) - 1 - i]

    print(left, right)


diagonal(lista)
