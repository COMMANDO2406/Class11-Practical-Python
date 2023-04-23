#To create a python program to input a list of elements, search for a given element in the list.

list1=eval(input("Enter a list: "))
length=len(list1)
elt=int(input("enter element to be searched for: "))
for i in range(0,length):
    if elt==list1[i]:
        print(elt, "found at index", i)
        break;
    elif elt not in list1:
        print(elt, "not found in given list")

"""
Output:

Enter a list: [1, 2, 3, 4, 5, 6, 7]   
enter element to be searched for: 5
5 found at index 4

"""