"""
Author: Riley Bird
Date: 6/13/2025
File Name: bird_lemonadeStand.py
Description: Lemonade Stand cost vs. profit generator.
"""

def calculate_cost(lemons_cost, sugar_cost):
    total_cost = lemons_cost + sugar_cost
    return total_cost

def calculate_profit(lemons_cost, sugar_cost, selling_price):
    profit_result = selling_price - (lemons_cost + sugar_cost)
    return profit_result

lemons_cost = 3
sugar_cost = 4
selling_price = 9

cost = calculate_cost(lemons_cost, sugar_cost)

profit = calculate_profit(lemons_cost, sugar_cost, selling_price)

print(cost)

print(profit)
