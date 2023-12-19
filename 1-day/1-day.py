# Guess your music band name
# Author: Shalaka Deshan Silva
# Date created: 2023-12-19
# Date last modified: 2023-12-19
# Python Version: 3.9

import os

# Get user input
print("Welcome to the Music Band Name Generator.")
# Get the city name
city = input("What's the name of the city you grew up in?\n")
# Get the pet name
pet = input("What's your pet's name?\n")

# Print the band name
print("Your band name could be " + city + " " + pet)

# Clear the screen
print("\n\n\nDo you want to clear the screen?")
if input("Enter 'y' for yes and 'n' for no: ") == 'y':
    os.system('cls' if os.name == 'nt' else 'clear')
