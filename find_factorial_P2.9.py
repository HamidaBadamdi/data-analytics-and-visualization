'''
Program Name: Factorial of a Number

Description:
This Python program calculates the factorial of a user-entered number
using a normal (non-recursive) function.
The factorial of a number is the product of all positive integers
less than or equal to that number.

Author: Hamida Badamdi
'''

# Function to calculate factorial
def find_fact(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    return fact

num=int(input("Enter the number: "))

# Calling function
res=find_fact(num)
print(f"Factorial of {num} = {res}")


    

