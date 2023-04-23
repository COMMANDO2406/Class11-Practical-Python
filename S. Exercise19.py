"""
Aim: To create a python program input a list of numbers and test if a number is
equal to the sum of the cubes of its digits. Find the smallest and largest such
number from the given list of numbers.

"""

list1=eval(input("Enter a list: "))
list2=[]
s=len(list1)
for i in range(s):
    num=list1[i]
    csum=0
    while num:
        dig=num%10
        csum+=(dig*dig*dig)
        num=num//10
    if csum==list1[i]:
        list2.append(list1[i])
print("The largest number which equals sum of its digits' cubes is: ", max(list2))
print("The smallest number which equals sum of its digits' cubes is: ", min(list2))

"""
Output:

Enter a list:  [1, 2, 3, 4, 5, 6, 7]   
The largest number which equals sum of its digits' cubes is:  1
The smallest number which equals sum of its digits' cubes is:  1

"""