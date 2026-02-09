'''
Program Name: Leap Year Checker

Description:
This program prompts the user to enter a year and checks
whether it is a leap year or not using standard leap year rules.

Author: Hamida Badamdi

'''

print("----------- Find Leap Year -----------")

year = int(input("Enter the year: "))

if year % 400 == 0:
    print(f"{year} is a leap year.")
elif year % 100 == 0:
    print(f"{year} is not a leap year.")
elif year % 4 == 0:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
