"""
Program Name: Odd and Even Number Checker

Description:
Determines whether a given number is odd or even
using the modulus (%) operator and conditional statements.

Author: Hamida Badamdi
Course: Data Analytics & Visualization (DAV)
"""

# Taking input from user
num = int(input("Enter the number: "))

# Checking odd or even
if num % 2 == 0:
    print(num, "is even number.")

else:
    print(num, "is odd number.")
