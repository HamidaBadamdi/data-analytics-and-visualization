'''
Program Name: Number Sign Checker

Description:
Checks whether the given number is positive, negative,
or zero using conditional statements.

Author: Hamida Badamdi
Course: Data Analytics & Visualization (DAV)
'''

# Taking input from user
num = int(input("Enter the number: "))

# Checking number type
if num > 0:
    print(num, "is positive (+) number.")

elif num < 0:
    print(num, "is negative (-) number.")

else:
    print(num, "is zero.")
