def mutate_string(string, position, character):
    return string[:position] + character + string[position + 1:]


s = 'casarado'
posit = 3
ch = 't'

print(mutate_string(s, posit, ch))
