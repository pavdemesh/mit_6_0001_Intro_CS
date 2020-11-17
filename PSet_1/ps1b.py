# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 07:21:08 2020

@author: pavdemesh
"""

annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semiannual raise, as a decimal: "))

# Calculate the amount of the down payment
# By multiplying total_cost by the percentage of the down payment
portion_down_payment = 0.25
amount_down_payment = total_cost * portion_down_payment

# Calculate the monthly return rate given the annual return rate
annual_return_rate = 0.04
monthly_return_rate = annual_return_rate / 12

current_savings = 0

num_of_months = 0

# Repeat the cycle until current savings are smaller than down payment
while current_savings < amount_down_payment:
    # Calculate the monthly salary savings:
    # Divide the annual by 12 to get monhly salary
    # Multiply the monthly salary with the percent to be saved
    monthly_salary_saved = annual_salary / 12 * portion_saved
    # Increase current savings by monthly return (revenue) from existing savings
    # Plus monthly salary
    current_savings += current_savings * monthly_return_rate + monthly_salary_saved
    # Increase the number of months by 1
    num_of_months += 1
    if num_of_months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise
    
print("Number of months:", num_of_months)