lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = []

# variable to 0
index = 0

# interating over the sub_list length (3) times

for i in range(len(lists[0])):
    # appending an empty sub_list
    result.append([])
    # interating lists length (3) times
    for j in range(len(lists)):
        # adding the element to the result
        result[index].append(lists[j][index])

# moving to the next index

index += 1

# printing the result
print(result)
