#
# Complete the 'arraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY numbers as parameter.
#

"""
def arraySum(numbers):
    # Write your code here


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    numbers_count = int(input().strip())

    numbers = []

    for _ in range(numbers_count):
        numbers_item = int(input().strip())
        numbers.append(numbers_item)

    result = arraySum(numbers)

    fptr.write(str(result) + '\n')

    fptr.close()

"""


def arraySum(numbers):
    # Write your code here
    sumarray = 0
    for element in numbers:
        sumarray += element
    result = sumarray

    return result


# Lembre-se que é uma soma dos elementos de uma lista.
numbers = [5, 7, 9, 12, 15]
print(arraySum(numbers))
