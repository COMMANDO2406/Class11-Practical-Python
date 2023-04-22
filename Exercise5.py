# Aim: To create a python program to input a number and check if the number is a prime number or composite number.

num = int(input("Enter a number: "))
if num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            print(num,"is a composite number")
            print(i,"times",num//i,"is",num)
            break
    else:
        print(num,"is a prime number")
else:
    print(num,"is a composite number")

"""
Output:

Enter a number: 88
88 is a composite number
2 times 44 is 88

"""