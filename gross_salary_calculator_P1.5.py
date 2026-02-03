"""
Program Name: Gross Salary Calculator

Description:
Calculates gross pay based on working hours and hourly rate.
If the employee works more than 30 hours, extra hours are paid
at 1.5 times the normal rate (overtime).

Author: Hamida Badamdi
Course: Data Analytics & Visualization (DAV)
"""

# Taking input from user
hours = float(input("Enter working hours: "))
rate = float(input("Enter rate per hour: "))

# Calculating pay with overtime logic
if hours > 30:
    # Normal pay for first 30 hours
    normal_pay = 30 * rate
    
    # Overtime pay for extra hours
    overtime_pay = (hours - 30) * rate * 1.5
    
    pay = normal_pay + overtime_pay
else:
    pay = hours * rate

# Display result
print("Pay:", pay)
