# 10-1. Favorite Number (Store)
# This program prompts the user for their favorite number and stores it in a JSON file.
import json

def store_favorite_number():
    # Prompt user for their favorite number
    favorite_number = input("What's your favorite number? ")
    
    # Store the favorite number in a JSON file
    with open('favorite_number.json', 'w') as f:
        json.dump(favorite_number, f)
        print("Your favorite number has been saved!")

# Call the function
store_favorite_number()
