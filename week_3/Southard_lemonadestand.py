"""
Author: Will Southard
Date: January 30, 2026
File Name: Southard_lemonadeStand.py
Description: This program simulates a lemonade stand by calculating
the cost of making lemonade and the profit from selling it using functions.
"""

# Function to calculate the total cost of making lemonade
def calculate_cost(lemons_cost, sugar_cost):
    # Adding the cost of lemons and sugar
    total_cost = lemons_cost + sugar_cost
    return total_cost

# Function to calculate the profit from selling lemonade
def calculate_profit(lemons_cost, sugar_cost, selling_price):
    # Calculating total cost
    total_cost = calculate_cost(lemons_cost, sugar_cost)
    # Calculating profit
    profit = selling_price - total_cost
    return profit

# Test variables
lemons_cost = 5
sugar_cost = 3
selling_price = 12

# Building output strings using string concatenation
cost_output = str(lemons_cost) + " + " + str(sugar_cost) + " = " + str(calculate_cost(lemons_cost, sugar_cost))
profit_output = "Selling Price: " + str(selling_price) + " - Total Cost = " + str(calculate_profit(lemons_cost, sugar_cost, selling_price))

# Printing results to the console
print("Total Cost Calculation:")
print(cost_output)

print("\nProfit Calculation:")
print(profit_output)
