"""
Aim: To Create a dictionary with the roll number, name and marks of n students in a class and display the names of students who have scored marks above 75.

"""

no_of_std = int(input("Enter number of students: "))
result = {}
for i in range(no_of_std):
    print("Enter Details of student No.", i+1)
    roll_no = int(input("Roll No: "))
    std_name = input("Student Name: ")
    marks = int(input("Marks: "))
    result[roll_no] = [std_name, marks]
print(result)

for student in result:
    if result[student][1] > 75:
        print("Student's name who get more than 75 marks is/are",(result[student][0]))

"""
Output:

Enter number of students: 3
Enter Details of student No. 1
Roll No: 1
Student Name: john
Marks: 74
Enter Details of student No. 2
Roll No: 20
Student Name: Lebron             
Marks: 69
Enter Details of student No. 3
Roll No: 4
Student Name: Bob 
Marks: 17
{1: ['john', 74], 20: ['Lebron', 69], 4: ['Bob', 17]}

"""