#!/bin/python3
#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pos = 0
    neg = 0
    zero = 0
    lenght = len(arr)
    for i in range(lenght):
        if arr[i] > 0:
            pos = pos + 1
        elif arr[i] < 0:
            neg = neg + 1
        elif arr[i] == 0:
            zero = zero + 1

    ratio_pos = pos / len(arr)
    ratio_neg = neg / len(arr)
    ratio_zero = zero / len(arr)
    print(ratio_pos)
    print(ratio_neg)
    print(ratio_zero)


# if __name__ == '__main__':
#    n = int(input().strip())
#
#   arr = list(map(int, input().rstrip().split()))
# #   plusMinus(arr)

arr1 = [1, 2, 0, -1, 0]
plusMinus(arr1)
