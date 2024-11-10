# The program's challenge is 5
"""
Reason: It was fun to learn new things.
"""
# 10-11. Favorite Number (Read)
# This program reads the stored favorite number from the file and prints a message.
import json

def read_favorite_number():
    try:
        # Read the favorite number from the JSON file
        with open('favorite_number.json', 'r') as f:
            favorite_number = json.load(f)
            print(f"I know your favorite number! It’s {favorite_number}.")
    
    except FileNotFoundError:
        print("I couldn't find your favorite number. Please run the first program to store it.")

# Call the function
read_favorite_number()