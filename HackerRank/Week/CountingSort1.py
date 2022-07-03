def countingSort(arr):
    n = len(arr)
    count = [0] * n

    for num in arr:
        count[num] += 1

    return count


arr1 = [1, 1, 3, 2, 1, 1]
print(countingSort(arr1))
