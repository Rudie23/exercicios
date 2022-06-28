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
            print("Values of pair are", arr[left], "&", arr[right],)
            right -= 1
            left += 1

arr = [5,7,4,3,9,8,19,21]
sumarray = 17
twosum(arr, sumarray)

n = int(input('Digite um numero inteiro: '))

if n % 2 != 0:
    print('Weird')
elif n % 2 == 0 and n in range(2, 5):
    print('Not Weird')
elif n % 2 == 0 and n in range(6, 20):
    print('Weird')
elif n % 2 == 0 and n >= 20:
    print('Not Weird')
