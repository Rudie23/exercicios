"""
You are given s string S and width w.
Your task is to wrap the string into a paragraph of width w.

Constraints

0 < len(string) < 1000
0 < max_width < len(string)

Sample Input

    ABCDEFGHIJKLIMNOQRSTUVWXYZ
    4

Sample Output

    ABCD
    EFGH
    IJKL
    IMNO
    QRST
    UVWX
    YZ

"""
import textwrap


def wrap(string, max_width):
    return textwrap.fill(string, max_width)


string = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
maxi = 3


print(wrap(string, maxi))

