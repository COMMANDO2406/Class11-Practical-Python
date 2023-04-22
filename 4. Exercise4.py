# Aim: To create a python program to determine whether a number is a perfect number or an Armstrong number or a palindrome.

num1=int(input("Enter the number:"))
rev=0
temp1=num1
while(num1>0):
    dig=num1%10
    rev=rev*10+dig
    num1=num1//10
if(temp1==rev):
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")

num2=int(input("Enter the number:"))
sum1=0
temp2=num2
while(temp2>0):
    digit=temp2%10
    sum1+=digit**3
    temp2//=10

if(num2==sum1):
    print("It is an armstrong number")
else:
    print("It is not an armstrong number")

num3=int(input("Enter the number:"))
sum2=0
for x in range(1,num3):
    if(num3%x==0):
        sum2+=x

if(sum2==num3):
    print("It is a perfect number")
else:
    print("It is not a perfect number")

"""
Output:

Enter the number:1141
The number is not a palindrome
Enter the number:313
It is not an armstrong number
Enter the number:123
It is not a perfect number

"""