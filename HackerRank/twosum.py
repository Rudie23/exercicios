def twosum(arr, sumarray):
    arr.sort()
    print(arr)
    left = 0
    right = len(arr) - 1
    while left <= right:
        if arr[left] + arr[right] > sumarray:
            right -= 1
        elif arr[left] + arr[right] < sumarray:
            left += 1
        elif arr[left] + arr[right] == sumarray:
            print("Values of pair are", arr[left], "&", arr[right], )
            right -= 1
            left += 1


arr = [5, 7, 4, 3, 9, 8, 19, 21]
sumarray = 28
twosum(arr, sumarray)
