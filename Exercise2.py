# Aim: To create a python program to input two numbers and display the larger or smaller number.
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))

if(num1>num2):
    print("The largest number is:",num1)
    print("The smallest number is:",num2)
else:
    print("The largest number is:",num2)
    print("The smallest number is:",num1)