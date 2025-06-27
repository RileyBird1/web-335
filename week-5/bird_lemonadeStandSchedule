"""
Author: Riley Bird
Date: 6/27/2025
File name: bird_lemonadeStandSchedule.py
Description: Assignment to create, iterate, and assign list to iterated loop.
"""

#Create list of tasks and print to console
lemonadeTasks = ["squeeze lemons", "mix lemonade", "setup table", "clean cups", "sell lemonade"]
for item in lemonadeTasks:
    print(item)

#Create list of days and iterate through weekday tasks in accordance with which day it is
weekDays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
for i in range(len(weekDays)):
    day = weekDays[i]
    if day == "Sunday" or day == "Saturday":
        print(f"{day}: Today is a day off, do something fun!")
    else:
        lemonadeTasks_index = i % len(lemonadeTasks)
        print(f"{day}: {lemonadeTasks[lemonadeTasks_index]}")
