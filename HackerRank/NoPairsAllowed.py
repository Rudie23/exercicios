"""
For each word in a list of words, if any two adjacent characters are equal, change one of them. Determine the minimum
number of substitutions so the final string contains no adjcant equal characters.

Example
words = ['add', 'boook', 'break']
    1. 'add': change one d(1 change)
    2. 'boook': change the middle o(1 change)
    3. 'break': no changes are necessary(0 changes)

The return array is [1, 1, 0]

Function Description
Complete the function minimalOperations in the editor bellow.

minimalOperations has the following parameter(s):
    string words[n]: an array of strings

Returns:
    int[n]: each element i is the minimum substitutions for words[i]

Input Format for Custom Testing
Input from stdin will be processed as follows and passed to the function.

The first line contains an integer n, the size of the array words. Each of the next n lines contains a string words[i]


"""

def minimal_operations(words):
    words = []



