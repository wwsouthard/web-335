"""
Author: Will Southard
File Name: Southard_lemonadeStandSchedule.py
Description:
    This program manages a weekly schedule for a lemonade stand.
    It demonstrates the use of Python lists, for loops, and
    conditional (if/else) statements.
"""

# -------------------------------------
# List of lemonade stand tasks
# -------------------------------------

tasks = [
    "Buy fresh lemons and sugar",
    "Prepare lemonade mixture",
    "Set up lemonade stand",
    "Sell lemonade to customers",
    "Count earnings and restock supplies"
]

# -------------------------------------
# Print all tasks
# -------------------------------------

print("Weekly Lemonade Stand Tasks:\n")

for task in tasks:
    print(f"- {task}")

print("\n")

# -------------------------------------
# List of days of the week
# -------------------------------------

days = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
]

# -------------------------------------
# Assign tasks to days using loop and conditionals
# -------------------------------------

print("Weekly Schedule:\n")

task_index = 0  # Used to track which task to assign

for day in days:

    # If it is Saturday or Sunday, rest
    if day == "Saturday" or day == "Sunday":
        print(f"{day}: Day off! Time to rest and recharge.")
    else:
        # Assign tasks Monday through Friday
        print(f"{day}: {tasks[task_index]}")
        task_index += 1  # Move to next task