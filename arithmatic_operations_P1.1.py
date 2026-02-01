"""
Program Name: Arithmetic Operations Calculator

Description:
A simple calculator that performs basic arithmetic operations
such as addition, subtraction, multiplication, division,
and modulo using functions and Python match-case statements.

Course: Data Analytics & Visualization (DAV)
Author: Hamida Badamdi
"""
print("----- Arithmetic Operations -----\n")

# Taking input from user
a = int(input("Enter 1st Number : "))
b = int(input("Enter 2nd Number : "))

op = input("Enter Operator (+, -, *, /, %) : ")


# Function definitions
def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def mod(a, b):
    return a % b


# Match-case to perform selected operation
match op:
    case '+':
        print("Addition:", add(a, b))

    case '-':
        print("Subtraction:", sub(a, b))

    case '*':
        print("Multiplication:", mul(a, b))

    case '/':
        if b == 0:
            print("Can't divide by zero!")
        else:
            print("Division:", div(a, b))

    case '%':
        print("Modulo:", mod(a, b))

    case _:
        print("Invalid operator!")


print("-----Arithmetic Operations-----\n")

a=int(input("Enter 1st Number : "))
b=int(input("Enter 2nd Number : "))

op=input("Enter Operator (+, -, *, /, %) : ")

def add(a , b):
    return  a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def mod(a, b):
    return a % b

match op:
    case '+':
        print("Addition: " ,add(a,b))
    case '-':
        print("Subtraction: " , sub(a,b))
    case '*':
        print("Multiplication: " , mul(a,b))
    case '/':
        if(b == 0):
            print("Can't be division by zero!")
        else:
            print("Division: " , div(a,b))
    case '%':
        print("Modulo division: " , mod(a,b))
    case _:
        print("Invalid operator!")
        

