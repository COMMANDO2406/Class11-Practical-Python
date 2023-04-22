# Aim: To input a string and determine whether it is a palindrome or not and convert the case of characters in a string.

string = input("Enter the string:")
if(string == string[::-1]):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
str1=string.upper()
print("The string after converting the case:")
print(str1)

"""
Output:

The string is not a palindrome
The string after converting the case:
THIS IS NOT A PALINDROME
"""