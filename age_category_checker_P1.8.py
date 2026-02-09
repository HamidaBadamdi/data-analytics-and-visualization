"""
Program Name: Age Category Checker

Description:
This program takes the age of a person as input and 
classifies them into one of the categories:
Child, Teenager, Adult, or Senior Citizen using conditional statements.

Author: Hamida Badamdi

"""

age = int(input("Enter person age: "))

if age > 0:
    if age < 13:
        print("Age:", age, "(Child)")
    elif age < 20:
        print("Age:", age, "(Teenager)")
    elif age < 60:
        print("Age:", age, "(Adult)")
    else:
        print("Age:", age, "(Senior Citizen)")
else:
    print("Invalid Age!")
