"""
To create a program to input the value of x and n and print the sum of
the following series:
 1+x+x^2+x^3+x^4+.......x^n
 1-x+x^2-x^3+x^4+...... x^n
"""
#series: 1+x+x2+x3+.....+xn
x = float(input("Enter value of x :"))
n = int(input("Enter value of n :"))
s = 0
for a in range (n + 1) :
    s+=x**a
print("Sum of series", s)

#series: 1-x+x2-x3+x4+....xn
import math
x1 = float(input("Enter value of x :"))
n1 = int(input("Enter value of n :"))
s1 = 0
for i in range (n1 + 1) :
    s1+=pow(-x1,i)
print("Sum of series", s1)

"""
Output:

Enter value of x :21
Enter value of n :3
Sum of series 9724.0
Enter value of x :21
Enter value of n :5
Sum of series -3898460.0

"""