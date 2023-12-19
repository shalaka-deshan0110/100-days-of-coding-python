# Tip Calculator
# Author: shalaka deshan silva
# Date created: 2023-12-19
# Date last modified: 2023-12-19
# Python Version: 3.9
import os

print("Welcome to the tip calculator.")
# Get the bill amount
print("What was the total bill?")
total_bill = input("Rs. ")

# Get percentage of tip
print("What percentage tip would you like to give? 10, 12, or 15?")
tip_percentage = input("% ")

# Get number of people to split the bill
print("How many people to split the bill?")
num_people = input(" ")

# Calculate the bill amount per person
bill_per_person = (float(total_bill) + (float(total_bill) * float(tip_percentage) / 100)) / float(num_people)

# Print the bill amount per person
print("Each person should pay: Rs. " + str(round(bill_per_person, 2)))

# Clear the screen
print("\n\n\nDo you want to clear the screen?")
if input("Enter 'y' for yes and 'n' for no or enter: ") == 'y':
    os.system('cls' if os.name == 'nt' else 'clear')