# Aim: To create a python program to display the terms of a Fibonacci series.

nterms = int(input("How many terms? "))
n1, n2 = 0, 1
count = 0
print("Fibonacci sequence:")
while count < nterms:
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1

"""
Output:

How many terms? 10
Fibonacci sequence:
0
1
1
2
3
5
8
13
21
34

"""