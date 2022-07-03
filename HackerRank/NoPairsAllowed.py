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
    # n stores the length of the string s
    n = len(words)

    # ans will store the required ans
    ans = 0

    # i is the current index in the string
    i = 0

    while i < n:
        j = i

        # Move j until characters s[i] & s[j]
        # are equal or the end of the
        # string is reached
        while j < n and (words[j] == words[i]):
            j += 1

        # diff stores the length of the
        # substring such that all the
        # characters are equal in it
        diff = j - i

        # We need at least diff/2 operations
        # for this substring
        ans += diff // 2
        i = j

        print(ans)


words = 'caaab'
minimal_operations(words)

print('Programa melhorado')
