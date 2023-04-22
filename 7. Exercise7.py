# Aim: To create a python program to compute the greatest common divisor and least common multiple of two integers.

num1 = int(input("Enter the first value: "))
num2 = int(input("Enter the first value: "))

if num1 > num2:
    num1,num2=num2,num1

for i in range(1,num1+1):
    if num1%i == 0 and num2%i == 0:
        gcd = i
lcm = (num1 * num2)/gcd

print("Greatest Common Divisor is: ", gcd)
print("Lowest Common Multiple is: ", lcm)

"""
Output:

Enter the first value: 69
Enter the first value: 36
Greatest Common Divisor is:  3
Lowest Common Multiple is:  828.0

"""