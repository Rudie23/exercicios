def lonelyinteger(a):
    dic = {}

    for number in a:
        if number in dic.keys():
            dic[number] = dic[number] + 1
        else:
            dic[number] = 1

    for i in dic:
        if dic[i] == 1:
            print('Alone number ' + str(i))


arr = [2, 4, 4, 1, 1]
lonelyinteger(arr)


# same input - 0
# diff input - 1
# 1 ^ 0 = 1
# 1 ^ 1 = 0


def lonelyInteger(a):
    r = 0
    for num in a:
        r = r ^ num  # or r ^= num

    return r


arr2 = [5, 4, 3, 3]
print(lonelyInteger(arr2))
