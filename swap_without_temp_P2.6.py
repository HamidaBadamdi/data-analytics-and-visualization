'''
Program Name: Swapping two integer values

Description:
This Python program swaps two integer values without using
a temporary variable. It demonstrates Python's multiple
assignment feature for efficient value swapping.

Author: Hamida Badamdi
'''

a=int(input("Enter the first value: "))
b=int(input("Enter the second value: "))

print("\nBefore Swapping....\n")
print("Value of a = ", a)
print("Value of b = ", b)

a,b=b,a

print("\nAfter Swapping....\n")
print("Value of a = ", a)
print("Value of b = ", b)


