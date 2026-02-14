'''
Program Name: Display Names from List Using Function

Description:
This program creates a list of student names based on user input.
A separate function is defined to display all the elements stored
in the list. The function is then called to execute and print
the names.

Author: Hamida Badamdi
Course: Data Analytics & Visualization (DAV)
'''

# Taking number of students
num = int(input("Enter the number of students names: "))

# Creating empty list
names = []

# Adding names to list
for i in range(num):
    stud = input("Enter the student name: ")
    names.append(stud)


# Function to display names
def print_names():
    print("\nAll Students Names....\n",names)

#Calling function...
print_names()

    
