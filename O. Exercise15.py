# Aim: To create a python program to find the largest and smallest element of a given list 

list1 = eval(input("Enter your list: "))
len1 = len(list1)
maxelt = list1[0]
minelt = list1[0]

for i in range (0, len1):
    if (list1[i]> maxelt):
        maxelt = list1[i]
for a in range(0, len1):
    if (list1[a]<minelt):
        minelt = list1[a]
print("The list is: ", list1)
print("The maximum element is: ", maxelt)
print("The minimum element is: ", minelt)

"""
Output:

Enter your list: [1,2,3,4,5,6,7] 
The list is:  [1, 2, 3, 4, 5, 6, 7]
The maximum element is:  7
The minimum element is:  1
"""