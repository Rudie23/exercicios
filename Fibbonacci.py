
a, b = 0, 1
while a < 10000000:
    print(a, end=' ')
    a, b = b, a+b
print('\n')
def fib(n):
    '''Return a list containing the Fibonacci series up to on'''
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
        print(a, end=' ')
    return result

fib(100)