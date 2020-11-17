# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 20:31:16 2020

@author: pavdemesh
"""


def calc_months(starting_salary):
    left = 1
    right = 10000

    counter_steps = 0

    while left <= right:

        # Increase the counter of bisection searches by 1
        counter_steps += 1

        # Define the mid point for bisection search
        mid = left + (right - left) // 2
        # print(f"left: {left}, right: {right}, mid: {mid}")

        # Calculate the amount of the down payment
        # By multiplying total_cost by the percentage of the down payment
        total_cost = 1_000_000
        portion_down_payment = 0.25
        amount_down_payment = total_cost * portion_down_payment
        # print(amount_down_payment)

        # Calculate the monthly return rate given the annual return rate
        annual_return_rate = 0.04
        monthly_return_rate = annual_return_rate / 12
        # print(monthly_return_rate)

        # Define the semi_annual_raise
        semi_annual_raise = 0.07

        # Reset all values to rheir initial state
        current_savings = 0
        monthly_salary_saved = 0
        annual_salary = starting_salary

        # Define the required number of months
        num_of_months = 36

        # Calculate the savings amount after 36 months
        # The savings rate is the (mid) of (left and right)
        for month in range(1, num_of_months + 1):

            # Calculate the monthly salary savings:
            # Divide the annual by 12 to get monhly salary
            # Multiply the monthly salary with the mid == percent to be saved
            monthly_salary_saved = annual_salary / 12 * mid / 10000

            # Increase current savings by monthly return (revenue) from existing savings
            # Plus monthly salary
            current_savings += current_savings * monthly_return_rate + monthly_salary_saved

            # If month divisible by 6 - increase annual salary by semi_annual_raise
            if month % 6 == 0:
                annual_salary += annual_salary * semi_annual_raise

        # Check resulting savings against the amount of down payment
        # If the savings amount lies within USD 100 of required downpayment
        # Print appropriate message and return the savings rate as deciaml
        if -100 <= (current_savings - amount_down_payment) <= 100:
            best_savings_rate = round(mid / 10_000, 4)
            print("Best savings rate: ", best_savings_rate)
            print("Steps in bisection search: ", counter_steps)
            return

        # If savings amount too big: search the left half: lesser values
        elif (current_savings - amount_down_payment) > 100:
            right = mid - 1

        # Else search the right half
        else:
            left = mid + 1

    # If no savings rate found - print appropriate message
    print("It is not possible to pay the down payment in three years.")
    return


calc_months(int(input("Enter the starting salary: ")))
