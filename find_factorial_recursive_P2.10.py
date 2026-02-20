'''
Unit-2

10.Write a program  in python to find factorial of  user entered 
number using recursion. 

Date: 15-Feb-2026
'''

#Using Recursive function...
def find_fact_rec(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * find_fact_rec(num-1)


num=int(input("Enter the number: "))
print("\nUisng recursive function.....\n")
res=find_fact_rec(num)
print(f"Factorial of {num} = {res}")
