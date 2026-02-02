'''
Program Name: Kilometer to Miles Converter

Description:
Converts distance from kilometers to miles using the
conversion factor (1 km = 0.62 miles).
Demonstrates basic arithmetic operations and user input.

Author: Hamida Badamdi
Course: Data Analytics & Visualization (DAV)
'''

# Conversion constant
KM_TO_MILES = 0.62


# Taking input from user
dist = float(input("Enter distance (in km): "))

# Converting distance
miles = dist * KM_TO_MILES

# Displaying result
print("Distance", dist, "km in miles is:", miles)
