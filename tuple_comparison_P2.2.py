'''
Program Name: Tuple Comparison (Integers and Strings)

Description:
This program compares tuples of integers and tuples of strings
using relational and equality operators. It demonstrates how
Python performs lexicographical comparison between tuple elements.

Author: Hamida Badamdi

'''

#Tuple of integers
int_tup1 =(10,20,13)
int_tup2 = (19,15,46)

#Tuple of strings
str_tup1 = ('red' ,'pink' , 'black')
str_tup2 = ('apple' , 'rose' ,'banana')


print("Integer Tuple-1 : " , int_tup1)
print("Integer Tuple-2 : " , int_tup2)

print("\nComparing integer tuples.....\n")
print("int_tup1 == int_tup2 : " , int_tup1 == int_tup2)
print("int_tup1 > int_tup2 : " , int_tup1 > int_tup2)
print("int_tup1 < int_tup2 : " , int_tup1 < int_tup2)

print("\n---------------------------------------------------\n")
print("String Tuple-1 : ", str_tup1)
print("String Tuple-2 : ", str_tup2)

print("\nComparing string tuples.....\n")
print("str_tup1 == str_tup2 : " , str_tup1 == str_tup2)
print("str_tup1 > str_tup2 : " , str_tup1 > str_tup2)
print("str_tup1 < str_tup2 : " , str_tup1 < str_tup2)
