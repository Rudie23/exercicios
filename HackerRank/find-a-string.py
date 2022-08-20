

def count_substring(string, sub_string):

    ml = len(string)
    sl = len(sub_string)
    c = 0

    for i in range(ml - sl + 1):
        if string[i:i+sl] == sub_string:
            c += 1

    return c

s1 = 'ABCDCDC'
s2 = 'CDC'

print(count_substring(s1,s2))