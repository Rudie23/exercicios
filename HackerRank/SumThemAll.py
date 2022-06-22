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


def arraySum(n: int):
    # Write your code here
    numbers = []

    for _ in range(n):
        numbers_item = int(input('Enter the number to add to the list: '))
        numbers.append(numbers_item)

    result = sum(numbers)
    print(result)


arraySum(5)
