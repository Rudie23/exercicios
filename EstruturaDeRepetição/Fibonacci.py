    """A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série
até o n−ésimo termo. """

f1 = 0
f2 = 1
f = 1


for _ in range(10):
    f = f2 + f1
    f1 = f2
    f2 = f

    print(f1, end=' ')
