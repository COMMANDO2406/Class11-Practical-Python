num1 = int(input("Enter the number: "))
if (str(num1) == str(num1)[::-1]):
    print("The number ", num1, " is a palindorme")
else:
    print("Not a palindrome")