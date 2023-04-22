# Aim: To Print the following series: x+x2/2!-x3/3!+x4/4!-....xn/n!

x1=float(input("Enter the value of x: "))
n1= int(input("Enter the value of n: "))
s1=x1
sign=+1
for a in range(2,n1+1):
    fact=1
    for k in range(1,a+1):
        fact=fact*k
    term=((x1**a)*sign)/fact
    s1+=term
    sign*=-1
print("The sum of the series is:", s1)

"""
Output:

Enter the value of x: 21
Enter the value of n: 6
The sum of the series is: 91886.8125

"""