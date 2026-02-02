'''
Program Name: Celsius to Fahrenheit Converter

Description:
Converts temperature from Celsius to Fahrenheit using the
formula: F = (C × 1.8) + 32.
Demonstrates user input, arithmetic operations, and unit conversion.

Author: Hamida Badamdi
Course: Data Analytics & Visualization (DAV)
'''

# Taking temperature input from user
temp_c = float(input("Enter temperature (in Celsius): "))

# Conversion formula
temp_f = (temp_c * 1.8) + 32

# Display results
print("\n--> Temperature (in Celsius):", temp_c)
print("--> Temperature (in Fahrenheit):", temp_f)
