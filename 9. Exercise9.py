""" Aim: To print the following pattern:
A
AB
ABC
ABCD
ABCDE
"""
n = 5
for i in range(n):
    for j in range(i+1):
        print(chr(j + 65), end="")
    print()

"""
Output:

A
AB
ABC
ABCD
ABCDE

"""