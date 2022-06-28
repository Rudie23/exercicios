#
# Complete the 'reverseArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
"""
def reverseArray(arr):
    # Write your code here
    ar

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = reverseArray(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

"""
from typing import List


def reverseArray(arr: List):
    # Write your code here

    lenght = len(arr) - 1
    return print(arr[lenght::-1])


arr = [5, 4, 3, 2, 1, 6]
reverseArray(arr)
