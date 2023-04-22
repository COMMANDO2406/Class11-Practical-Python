# Aim: To Print the following series: x+x2/2-x3/3+x4/4-.....xn/n in python

x=float(input("Enter the value of x: "))
n = int(input("Enter the value of n: "))
s=x
sign=+1
for i in range(2,n+1):
    term=((x**i)*sign)/i
    s+=term
    sign*=-1
print("The sum of the series is:", s)

"""
Output:

Enter the value of x: 17
Enter the value of n: 23
The sum of the series is: -8.178646757399871e+26

"""