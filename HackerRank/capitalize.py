def solve(s):
    words = s.split()
    separator = ' '
    return separator.join([word.capitalize() for word in words])


strin = 'hello world'

print(solve(strin))
