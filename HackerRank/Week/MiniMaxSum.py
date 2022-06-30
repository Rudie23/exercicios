def miniMaxSum(arr):
    print(sum(arr) - max(arr), sum(arr) - min(arr))


arr1 = [1, 3, 5, 7, 9]
miniMaxSum(arr1)


def miniMax(arr2):
    s = 0
    mini = 9999999999999
    maxi = 0
    for i in range(len(arr2)):
        s += arr2[i]
        mini = min(mini, arr2[i])
        maxi = max(maxi, arr2[i])
    print(s - maxi, s - mini)


arra = [1, 3, 5, 7, 9]
miniMax(arra)
