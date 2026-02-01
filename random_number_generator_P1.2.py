'''
Program Name: Random Number Generator(between given range)

Description:
Write a Python script to prompt users to enter
the first and last values and generate some random
values between the two entered values.

Subject: Data Analytic & Visualization

Author: Hamida Badamdi
'''
import random

start=int(input("Enter the starting value: "))
end=int(input("Enter ending value: "))

cnt=int(input("\nHow many values want to generate? "))

print(f"\n-------Random Number Between {start} to {end}-------")
for i in range(cnt):
    val=random.randint(start,end)
    print(val)
    
    
