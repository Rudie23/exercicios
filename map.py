
with_spaces = ['processing ', ' strings', 'with ', ' map']

lista = list(map(str.strip, with_spaces))
print(lista)

with_dots = ['processing..', '..strings', 'with..', '..map']

lista = list(map(lambda s: s.strip('.'), with_dots))
print(lista)

import re

def remove_ponctuation(word):
    return re.sub(r'[!?.:;,"()-]', '', word)

print(remove_ponctuation('...Python!'))

text = """Some people, when confronted with a problem, think
... "I know, I'll use regular expressions."
... Now they have two problems. Jamie Zawinski"""

words = text.split()
print(words)
