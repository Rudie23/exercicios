

def is_odd(n):
    if n % 2 != 0:
        return True
    else:
        return False


n = int(input('Digite um número: '))
print(is_odd(n))

if is_odd(n):
    print(n, 'is an odd number')

else:
    print(n, 'is an even number')
