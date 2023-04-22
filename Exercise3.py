# Aim: To create a python program to input three numbers and display the largest or smallest number.

num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
num3=int(input("Enter the third number:"))

if(num1>num2)&(num1>num3):
    print("The largest number is:",num1)
elif(num2>num3):
    print("The largest number is:",num2)
else:
    print("The largest number is:",num3)

"""
Output:

Enter the first number:100
Enter the second number:20
Enter the third number:257
The largest number is: 257

"""