def soma(*x):
    return sum(x)


print(soma(5, 10, 15, 20))
print(soma(5, 58, 25, 14))

valores = [5, 7, 9, 11]

print(soma(*valores))
