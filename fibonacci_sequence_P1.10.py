'''
Program Name: Fibonacci Sequence Generator

Description:
This program generates the Fibonacci sequence up to
a user-defined number of terms.

The Fibonacci sequence starts with 0 and 1, and each
next number is the sum of the previous two numbers.

Author: Hamida Badamdi

'''

seq=int(input("Enter the no. of terms: "))
a=0
b=1

print(f"\nFebonacci Sequence of {seq}....")
print(a,b,end=" ")

for i in range(3,seq+1):
    c=a+b
    print(c,end = " ")
    a=b
    b=c


