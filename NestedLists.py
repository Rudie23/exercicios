numbers = [5, 2, 5, 2, 2]

for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)


numbers2 = [5, 2, 5, 2, 2]

print("\nIn another way")
for x in numbers2:
    print("x" * x)