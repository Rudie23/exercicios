n = int(input('The score: '))
for _ in range(5):
    arr = list(map(int, input('Scores ').split()))

print(arr[(arr.index(max(arr))) - 1])
