def countingSort(arr):
    count = [0] * 100

    for num in arr:
        count[num] += 1

    return count


arr1 = [1, 1, 3, 2, 1, 1]
print(countingSort(arr1))
