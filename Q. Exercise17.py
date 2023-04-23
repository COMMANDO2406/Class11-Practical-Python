# To create a python program to input a list of numbers and swap elements at the even location with the elements at the odd location.

list1=eval(input("Enter the list: "))
print("Original list is: ",list1)
s=len(list1)
if (s%2!=0):
    s=s-1
    for i in range(0,s,2):
        print(i,i+1)
list1[i],list1[i+1]=list1[i+1], list1[i]
print("List after swapping: ", list1)

"""
Output:

Enter the list: [1,2,3,4,5,6,7] 
Original list is:  [1, 2, 3, 4, 5, 6, 7]
0 1
2 3
4 5
List after swapping:  [1, 2, 3, 4, 6, 5, 7]

"""